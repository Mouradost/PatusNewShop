# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SellHistoryBrowser.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateTimeEdit, QDialog, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QSizePolicy, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1376, 800)
        Dialog.setMinimumSize(QSize(1200, 800))
        icon = QIcon()
        icon.addFile(u":/Simple icons/simple_icons/fi-rr-incognito.svg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"*\n"
"{\n"
"	\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	\n"
"	color: rgb(79, 79, 79);\n"
"	background-color:  rgba(223, 223, 223, 200);\n"
"}\n"
"\n"
"\n"
"QToolButton\n"
"{ \n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background-color: rgb(185, 185, 185);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	position: center;\n"
" }\n"
"\n"
"QToolButton:hover\n"
"{\n"
"	background: rgba(225, 225, 225, 180);\n"
"	border-style: dashed;\n"
"}\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"	\n"
"	background-color: rgb(136, 136, 136, 180);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(121, 121, 121);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.l_title = QLabel(self.frame)
        self.l_title.setObjectName(u"l_title")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.l_title.setFont(font)
        self.l_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.l_title)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cb_sellHistory_DateTime = QCheckBox(self.frame_3)
        self.cb_sellHistory_DateTime.setObjectName(u"cb_sellHistory_DateTime")

        self.verticalLayout_3.addWidget(self.cb_sellHistory_DateTime)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dte_sellHistory_dateStart = QDateTimeEdit(self.frame_5)
        self.dte_sellHistory_dateStart.setObjectName(u"dte_sellHistory_dateStart")
        self.dte_sellHistory_dateStart.setEnabled(False)
        self.dte_sellHistory_dateStart.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.dte_sellHistory_dateStart)

        self.dte_sellHistory_dateEnd = QDateTimeEdit(self.frame_5)
        self.dte_sellHistory_dateEnd.setObjectName(u"dte_sellHistory_dateEnd")
        self.dte_sellHistory_dateEnd.setEnabled(False)
        self.dte_sellHistory_dateEnd.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.dte_sellHistory_dateEnd)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cb_sellHistory_worker = QCheckBox(self.frame_4)
        self.cb_sellHistory_worker.setObjectName(u"cb_sellHistory_worker")

        self.verticalLayout_4.addWidget(self.cb_sellHistory_worker)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cb_sellHistory_workerName = QComboBox(self.frame_6)
        self.cb_sellHistory_workerName.setObjectName(u"cb_sellHistory_workerName")
        self.cb_sellHistory_workerName.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.cb_sellHistory_workerName)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.tb_search = QToolButton(self.frame_2)
        self.tb_search.setObjectName(u"tb_search")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_search.sizePolicy().hasHeightForWidth())
        self.tb_search.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/Simple icons/simple_icons/fi-rr-search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_search.setIcon(icon1)
        self.tb_search.setIconSize(QSize(32, 32))
        self.tb_search.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.tb_search)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.tw_sellHistory = QTableWidget(self.frame)
        self.tw_sellHistory.setObjectName(u"tw_sellHistory")
        self.tw_sellHistory.setFont(font)
        self.tw_sellHistory.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_sellHistory.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_sellHistory.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.tw_sellHistory)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)
        self.cb_sellHistory_DateTime.toggled.connect(self.dte_sellHistory_dateStart.setEnabled)
        self.cb_sellHistory_DateTime.toggled.connect(self.dte_sellHistory_dateEnd.setEnabled)
        self.cb_sellHistory_worker.toggled.connect(self.cb_sellHistory_workerName.setEnabled)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Ticket History", None))
        self.l_title.setText(QCoreApplication.translate("Dialog", u"Ticket History Browser", None))
        self.cb_sellHistory_DateTime.setText(QCoreApplication.translate("Dialog", u"Filter by date and time", None))
        self.cb_sellHistory_worker.setText(QCoreApplication.translate("Dialog", u"Filter by worker", None))
        self.tb_search.setText(QCoreApplication.translate("Dialog", u"Search", None))
    # retranslateUi

