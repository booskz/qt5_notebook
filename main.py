import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ui_box import Ui_Win
import json
import os
from PyQt5.QtGui import QIcon
import time


class MWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MWin, self).__init__(parent)
        self.ui = Ui_Win()
        self.ui.setupUi(self)
        self.wset_icon()
        self.list_widget_visible = True  # 用于跟踪listWidget的当前状态
        self.data = {}  # 用于存储listWidget的内容和对应的文本框内容
        self.load_data()
        # 安装事件过滤器来捕捉Enter键
        self.ui.tcon.installEventFilter(self)

        # 创建系统托盘图标
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('static/img/notebook.png'))

        # 创建托盘菜单
        tray_menu = QtWidgets.QMenu(self)
        show_action = QtWidgets.QAction("显示", self)
        quit_action = QtWidgets.QAction("退出", self)

        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)

        # 信号槽连接
        show_action.triggered.connect(self.show_window)
        quit_action.triggered.connect(QtWidgets.qApp.quit)
        self.tray_icon.activated.connect(self.on_tray_icon_activated)

        # 显示托盘图标
        self.tray_icon.show()

    def wset_icon(self):
        self.setWindowIcon(QIcon('static/img/notebook.png'))
        self.ui.addp.setIcon(QIcon('static/img/add.png'))
        self.ui.delp.setIcon(QIcon('static/img/delete.png'))
        self.ui.bsz.setIcon(QIcon('static/img/app-drawer.png'))
        self.ui.tbredo.setIcon(QIcon('static/img/redo.png'))
        self.ui.tbundo.setIcon(QIcon('static/img/undo.png'))

        self.ui.tbh2.setIcon(QIcon('static/img/h2.png'))
        self.ui.tbh4.setIcon(QIcon('static/img/h4.png'))
        self.ui.tbh6.setIcon(QIcon('static/img/h6.png'))

        self.ui.tbleft.setIcon(QIcon('static/img/align-left.png'))
        self.ui.tbcenter.setIcon(QIcon('static/img/align-center.png'))
        self.ui.tbright.setIcon(QIcon('static/img/align-right.png'))
        self.ui.tblink.setIcon(QIcon('static/img/link.png'))
        self.ui.tbcut.setIcon(QIcon('static/img/scissors.png'))
        self.ui.tbsall.setIcon(QIcon('static/img/check.png'))
        self.ui.tbcopy.setIcon(QIcon('static/img/copy.png'))
        self.ui.tbpaste.setIcon(QIcon('static/img/paste.png'))

    def closeEvent(self, event):
        # 在窗口关闭时最小化到系统托盘，而不是退出程序
        event.ignore()
        self.hide()

    def show_window(self):
        # 显示窗口
        self.showNormal()
        self.activateWindow()

    def on_tray_icon_activated(self, reason):
        # 响应托盘图标的双击事件
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.show_window()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress and source is self.ui.tcon:
            if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
                cursor = self.ui.tcon.textCursor()
                cursor.insertBlock()  # 插入新的块（相当于新的一行）

                # 创建默认格式
                default_format = QtGui.QTextCharFormat()
                default_format.setFontPointSize(12)  # 设置默认字体大小为12
                default_format.setForeground(QtGui.QBrush(
                    QtGui.QColor("#000000")))  # 设置默认字体颜色为黑色

                # 应用默认格式到新段落
                cursor.setBlockCharFormat(default_format)

                return True
        return super(MWin, self).eventFilter(source, event)

    def load_data(self):
        if os.path.exists('data.json'):
            with open('data.json', 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            self.populate_list()

    def save_data(self):
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def populate_list(self):
        self.ui.listWidget.clear()
        for key in self.data.keys():
            item = QtWidgets.QListWidgetItem(key)
            self.ui.listWidget.addItem(item)

    def new_lst_item(self):
        # 在self.listWidget里增加一个item，并激活它
        new_item_name = "doc_" + str(time.time()).replace(".", "")[9:15]
        item = QtWidgets.QListWidgetItem(new_item_name)
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setCurrentItem(item)
        self.data[new_item_name] = {"title": new_item_name, "content": ""}
        self.ui.itt.setText(new_item_name)
        self.ui.tcon.clear()  # 清空QTextEdit的内容
        self.save_data()

    def del_lst_item(self):
        # 删除self.listWidget激活的item，之前弹出确认对话框
        selected_item = self.ui.listWidget.currentItem()
        if selected_item:
            reply = QtWidgets.QMessageBox.question(
                self,
                '确认删除',
                f'确定要删除 "{selected_item.text()}" 吗？',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No
            )
            if reply == QtWidgets.QMessageBox.Yes:
                del self.data[selected_item.text()]
                self.ui.listWidget.takeItem(
                    self.ui.listWidget.row(selected_item))
                self.save_data()

    def title_change(self, text):
        # 更新当前选中项的内容并保存到JSON文件
        selected_item = self.ui.listWidget.currentItem()
        if selected_item:
            old_key = selected_item.text()
            self.data[text] = self.data.pop(old_key)
            self.data[text]["title"] = text
            selected_item.setText(text)
            self.save_data()

    def content_change(self):
        # 获取当前QTextEdit的内容（HTML格式）并更新到JSON文件
        selected_item = self.ui.listWidget.currentItem()
        if selected_item:
            content = self.ui.tcon.toHtml()
            self.data[selected_item.text()]["content"] = content
            self.save_data()

    def act_doc(self, list_item):
        # 切换item时更新单行文本框和多行文本框内容
        item_text = list_item.text()
        self.ui.itt.setText(self.data[item_text]["title"])
        self.ui.tcon.setHtml(self.data[item_text]["content"])

    def tool_h2(self):
        # QTextEdit 工具按钮 点击 设置/取消选中文字大小为H2
        current_size = self.ui.tcon.fontPointSize()
        if current_size == 18:
            self.ui.tcon.setFontPointSize(12)  # 恢复到默认大小
        else:
            self.ui.tcon.setFontPointSize(18)

    def tool_h4(self):
        # QTextEdit 工具按钮 点击 设置/取消选中文字大小为H4
        current_size = self.ui.tcon.fontPointSize()
        if current_size == 14:
            self.ui.tcon.setFontPointSize(12)  # 恢复到默认大小
        else:
            self.ui.tcon.setFontPointSize(14)

    def tool_h6(self):
        # QTextEdit 工具按钮 点击 设置/取消选中文字大小为H6
        current_size = self.ui.tcon.fontPointSize()
        if current_size == 12:
            self.ui.tcon.setFontPointSize(12)  # 恢复到默认大小（保持为12）
        else:
            self.ui.tcon.setFontPointSize(12)

    def tool_red(self):
        # QTextEdit 工具按钮 点击 设置/取消选中文字颜色 #e4007f
        current_color = self.ui.tcon.textColor()
        if current_color == QtGui.QColor("#e4007f"):
            self.ui.tcon.setTextColor(QtGui.QColor("#000000"))  # 恢复到默认颜色（黑色）
        else:
            self.ui.tcon.setTextColor(QtGui.QColor("#e4007f"))

    def tool_green(self):
        # QTextEdit 工具按钮 点击 设置/取消选中文字颜色 #32b16c
        current_color = self.ui.tcon.textColor()
        if current_color == QtGui.QColor("#32b16c"):
            self.ui.tcon.setTextColor(QtGui.QColor("#000000"))  # 恢复到默认颜色（黑色）
        else:
            self.ui.tcon.setTextColor(QtGui.QColor("#32b16c"))

    def tool_blue(self):
        # QTextEdit 工具按钮 点击 设置/取消选中文字颜色 #00a0e9
        current_color = self.ui.tcon.textColor()
        if current_color == QtGui.QColor("#00a0e9"):
            self.ui.tcon.setTextColor(QtGui.QColor("#000000"))  # 恢复到默认颜色（黑色）
        else:
            self.ui.tcon.setTextColor(QtGui.QColor("#00a0e9"))

    def tool_left(self):
        # QTextEdit 工具按钮 点击 设置选中文字左对齐
        self.ui.tcon.setAlignment(QtCore.Qt.AlignLeft)

    def tool_center(self):
        # QTextEdit 工具按钮 点击 设置选中文字居中
        self.ui.tcon.setAlignment(QtCore.Qt.AlignCenter)

    def tool_right(self):
        # QTextEdit 工具按钮 点击 设置选中文字右对齐
        self.ui.tcon.setAlignment(QtCore.Qt.AlignRight)

    def tool_link(self):
        # QTextEdit 工具按钮 点击 设置/取消选中文本的下划线
        fmt = self.ui.tcon.currentCharFormat()
        if fmt.fontUnderline():
            fmt.setFontUnderline(False)  # 取消下划线
        else:
            fmt.setFontUnderline(True)  # 设置下划线
        self.ui.tcon.setCurrentCharFormat(fmt)

    def mbsz(self):
        # 收起和展开listWidget
        self.list_widget_visible = not self.list_widget_visible
        self.ui.listWidget.setVisible(self.list_widget_visible)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Win = MWin()
    Win.show()
    sys.exit(app.exec_())
