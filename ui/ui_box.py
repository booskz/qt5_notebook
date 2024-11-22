# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'box.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Win(object):
    def setupUi(self, Win):
        Win.setObjectName("Win")
        Win.setEnabled(True)
        Win.resize(1100, 700)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setUnderline(False)
        Win.setFont(font)
        Win.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Win.setAutoFillBackground(False)
        Win.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(Win)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tbredo = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbredo.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.tbredo.setFont(font)
        self.tbredo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbredo.setStyleSheet("border:none;")
        self.tbredo.setObjectName("tbredo")
        self.horizontalLayout.addWidget(self.tbredo)
        self.addp = QtWidgets.QToolButton(self.centralwidget)
        self.addp.setMinimumSize(QtCore.QSize(0, 0))
        self.addp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.addp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.addp.setFont(font)
        self.addp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addp.setStyleSheet("border:none;")
        self.addp.setObjectName("addp")
        self.horizontalLayout.addWidget(self.addp)
        self.delp = QtWidgets.QToolButton(self.centralwidget)
        self.delp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.delp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.delp.setFont(font)
        self.delp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delp.setStyleSheet("border:none;")
        self.delp.setObjectName("delp")
        self.horizontalLayout.addWidget(self.delp)
        self.bsz = QtWidgets.QToolButton(self.centralwidget)
        self.bsz.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.bsz.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.bsz.setFont(font)
        self.bsz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bsz.setStyleSheet("border:none;")
        self.bsz.setObjectName("bsz")
        self.horizontalLayout.addWidget(self.bsz)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.listWidget.setStyleSheet("border:none;\n"
"background-color:rgba(255, 255, 255, 0)")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.itt = QtWidgets.QLineEdit(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(224, 255, 235, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 255, 235, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 255, 235, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 255, 235, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 255, 235, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 255, 235, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 255, 235, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 255, 235, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 255, 235, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.itt.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.itt.setFont(font)
        self.itt.setWhatsThis("")
        self.itt.setStyleSheet("border-width:0 0 2px 0;\n"
"border-style:solid;\n"
"border-color:rgb(0, 0, 0);\n"
"background-color:rgba(224, 255, 235, 0);\n"
"font-weight: bold;")
        self.itt.setText("")
        self.itt.setObjectName("itt")
        self.verticalLayout.addWidget(self.itt)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tbundo = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbundo.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setUnderline(True)
        self.tbundo.setFont(font)
        self.tbundo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbundo.setStyleSheet("border:none;")
        self.tbundo.setObjectName("tbundo")
        self.horizontalLayout_2.addWidget(self.tbundo)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.tbh2 = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbh2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        font.setUnderline(True)
        self.tbh2.setFont(font)
        self.tbh2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbh2.setStyleSheet("border:none;")
        self.tbh2.setObjectName("tbh2")
        self.horizontalLayout_2.addWidget(self.tbh2)
        self.tbh4 = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbh4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        font.setUnderline(True)
        self.tbh4.setFont(font)
        self.tbh4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbh4.setStyleSheet("border:none;")
        self.tbh4.setObjectName("tbh4")
        self.horizontalLayout_2.addWidget(self.tbh4)
        self.tbh6 = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbh6.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setUnderline(True)
        self.tbh6.setFont(font)
        self.tbh6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbh6.setStyleSheet("border:none;")
        self.tbh6.setObjectName("tbh6")
        self.horizontalLayout_2.addWidget(self.tbh6)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_2.addWidget(self.line_6)
        self.tbred = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbred.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.tbred.setFont(font)
        self.tbred.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbred.setStyleSheet("border:none;")
        self.tbred.setObjectName("tbred")
        self.horizontalLayout_2.addWidget(self.tbred)
        self.tbgreen = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbgreen.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.tbgreen.setFont(font)
        self.tbgreen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbgreen.setStyleSheet("border:none;")
        self.tbgreen.setObjectName("tbgreen")
        self.horizontalLayout_2.addWidget(self.tbgreen)
        self.tbblue = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbblue.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.tbblue.setFont(font)
        self.tbblue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbblue.setStyleSheet("border:none;")
        self.tbblue.setObjectName("tbblue")
        self.horizontalLayout_2.addWidget(self.tbblue)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_2.addWidget(self.line_7)
        self.tbleft = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbleft.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setUnderline(True)
        self.tbleft.setFont(font)
        self.tbleft.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbleft.setStyleSheet("border:none;")
        self.tbleft.setObjectName("tbleft")
        self.horizontalLayout_2.addWidget(self.tbleft)
        self.tbcenter = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbcenter.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setUnderline(True)
        self.tbcenter.setFont(font)
        self.tbcenter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbcenter.setStyleSheet("border:none;")
        self.tbcenter.setObjectName("tbcenter")
        self.horizontalLayout_2.addWidget(self.tbcenter)
        self.tbright = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbright.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setUnderline(True)
        self.tbright.setFont(font)
        self.tbright.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbright.setStyleSheet("border:none;")
        self.tbright.setObjectName("tbright")
        self.horizontalLayout_2.addWidget(self.tbright)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_2.addWidget(self.line_8)
        self.tblink = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tblink.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setUnderline(True)
        self.tblink.setFont(font)
        self.tblink.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tblink.setStyleSheet("border:none;")
        self.tblink.setObjectName("tblink")
        self.horizontalLayout_2.addWidget(self.tblink)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.tbcut = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbcut.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setUnderline(True)
        self.tbcut.setFont(font)
        self.tbcut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbcut.setStyleSheet("border:none;")
        self.tbcut.setObjectName("tbcut")
        self.horizontalLayout_2.addWidget(self.tbcut)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_2.addWidget(self.line_10)
        self.tbsall = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbsall.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setUnderline(True)
        self.tbsall.setFont(font)
        self.tbsall.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbsall.setStyleSheet("border:none;")
        self.tbsall.setObjectName("tbsall")
        self.horizontalLayout_2.addWidget(self.tbsall)
        self.tbcopy = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbcopy.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setUnderline(True)
        self.tbcopy.setFont(font)
        self.tbcopy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbcopy.setStyleSheet("border:none;")
        self.tbcopy.setObjectName("tbcopy")
        self.horizontalLayout_2.addWidget(self.tbcopy)
        self.tbpaste = QtWidgets.QToolButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.tbpaste.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setUnderline(True)
        self.tbpaste.setFont(font)
        self.tbpaste.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tbpaste.setStyleSheet("border:none;")
        self.tbpaste.setObjectName("tbpaste")
        self.horizontalLayout_2.addWidget(self.tbpaste)
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.horizontalLayout_2.addWidget(self.line_11)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_3.addWidget(self.line_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tcon = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setUnderline(False)
        self.tcon.setFont(font)
        self.tcon.setStyleSheet("")
        self.tcon.setObjectName("tcon")
        self.verticalLayout.addWidget(self.tcon)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        Win.setCentralWidget(self.centralwidget)

        self.retranslateUi(Win)
        self.tbundo.clicked.connect(self.tcon.undo) # type: ignore
        self.tbredo.clicked.connect(self.tcon.redo) # type: ignore
        self.tbsall.clicked.connect(self.tcon.selectAll) # type: ignore
        self.tbcopy.clicked.connect(self.tcon.copy) # type: ignore
        self.tbcut.clicked.connect(self.tcon.cut) # type: ignore
        self.tbpaste.clicked.connect(self.tcon.paste) # type: ignore
        self.tbh2.clicked.connect(Win.tool_h2) # type: ignore
        self.tbh4.clicked.connect(Win.tool_h4) # type: ignore
        self.tbh6.clicked.connect(Win.tool_h6) # type: ignore
        self.tbred.clicked.connect(Win.tool_red) # type: ignore
        self.tbgreen.clicked.connect(Win.tool_green) # type: ignore
        self.tbblue.clicked.connect(Win.tool_blue) # type: ignore
        self.tbleft.clicked.connect(Win.tool_left) # type: ignore
        self.tbcenter.clicked.connect(Win.tool_center) # type: ignore
        self.tbright.clicked.connect(Win.tool_right) # type: ignore
        self.tblink.clicked.connect(Win.tool_link) # type: ignore
        self.itt.textChanged['QString'].connect(Win.title_change) # type: ignore
        self.tcon.textChanged.connect(Win.content_change) # type: ignore
        self.listWidget.itemClicked['QListWidgetItem*'].connect(Win.act_doc) # type: ignore
        self.addp.clicked.connect(Win.new_lst_item) # type: ignore
        self.delp.clicked.connect(Win.del_lst_item) # type: ignore
        self.bsz.clicked.connect(Win.mbsz) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Win)
        Win.setTabOrder(self.addp, self.delp)

    def retranslateUi(self, Win):
        _translate = QtCore.QCoreApplication.translate
        Win.setWindowTitle(_translate("Win", "备忘录"))
        self.tbredo.setToolTip(_translate("Win", "<html><head/><body><p>还原</p></body></html>"))
        self.tbredo.setText(_translate("Win", "还原"))
        self.addp.setToolTip(_translate("Win", "<html><head/><body><p>新建</p></body></html>"))
        self.addp.setText(_translate("Win", "新建"))
        self.delp.setToolTip(_translate("Win", "<html><head/><body><p>删除</p></body></html>"))
        self.delp.setText(_translate("Win", "删除"))
        self.bsz.setToolTip(_translate("Win", "<html><head/><body><p>展开收起</p></body></html>"))
        self.bsz.setText(_translate("Win", "收放"))
        self.itt.setToolTip(_translate("Win", "<html><head/><body><p>标题</p></body></html>"))
        self.tbundo.setToolTip(_translate("Win", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">撤销</span></p></body></html>"))
        self.tbundo.setText(_translate("Win", "撤销"))
        self.tbh2.setToolTip(_translate("Win", "<html><head/><body><p>H2</p></body></html>"))
        self.tbh2.setText(_translate("Win", "H"))
        self.tbh4.setToolTip(_translate("Win", "<html><head/><body><p>H4</p></body></html>"))
        self.tbh4.setText(_translate("Win", "H"))
        self.tbh6.setToolTip(_translate("Win", "<html><head/><body><p>H6</p></body></html>"))
        self.tbh6.setText(_translate("Win", "H"))
        self.tbred.setToolTip(_translate("Win", "<html><head/><body><p>R</p></body></html>"))
        self.tbred.setText(_translate("Win", "R"))
        self.tbgreen.setToolTip(_translate("Win", "<html><head/><body><p>G</p></body></html>"))
        self.tbgreen.setText(_translate("Win", "G"))
        self.tbblue.setToolTip(_translate("Win", "<html><head/><body><p>B</p></body></html>"))
        self.tbblue.setText(_translate("Win", "B"))
        self.tbleft.setToolTip(_translate("Win", "<html><head/><body><p>左对齐</p></body></html>"))
        self.tbleft.setText(_translate("Win", "左"))
        self.tbcenter.setToolTip(_translate("Win", "<html><head/><body><p>居中对齐</p></body></html>"))
        self.tbcenter.setText(_translate("Win", "中"))
        self.tbright.setToolTip(_translate("Win", "<html><head/><body><p>右对齐</p></body></html>"))
        self.tbright.setText(_translate("Win", "右"))
        self.tblink.setToolTip(_translate("Win", "<html><head/><body><p>下划线</p></body></html>"))
        self.tblink.setText(_translate("Win", "链接"))
        self.tbcut.setToolTip(_translate("Win", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">剪切</span></p></body></html>"))
        self.tbcut.setText(_translate("Win", "剪切"))
        self.tbsall.setToolTip(_translate("Win", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">全选</span></p></body></html>"))
        self.tbsall.setText(_translate("Win", "全选"))
        self.tbcopy.setToolTip(_translate("Win", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">复制</span></p></body></html>"))
        self.tbcopy.setText(_translate("Win", "复制"))
        self.tbpaste.setToolTip(_translate("Win", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">粘贴</span></p></body></html>"))
        self.tbpaste.setText(_translate("Win", "粘贴"))
        self.tcon.setHtml(_translate("Win", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'微软雅黑\'; font-size:12pt;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Win = QtWidgets.QMainWindow()
    ui = Ui_Win()
    ui.setupUi(Win)
    Win.show()
    sys.exit(app.exec_())