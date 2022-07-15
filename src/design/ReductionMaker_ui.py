# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReductionMaker.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QSizePolicy, QToolButton, QWidget)
import resource_rc

class Ui_DialogReduce(object):
    def setupUi(self, DialogReduce):
        if not DialogReduce.objectName():
            DialogReduce.setObjectName(u"DialogReduce")
        DialogReduce.resize(890, 587)
        DialogReduce.setStyleSheet(u"*\n"
"{\n"
"	\n"
"	font: 26pt \"MS Shell Dlg 2\";\n"
"	\n"
"	color: rgb(79, 79, 79);\n"
"	background-color:  rgba(223, 223, 223, 200);\n"
"}\n"
"\n"
"\n"
"QPushButton\n"
"{ \n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(185, 185, 185);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	position: center;\n"
" }\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background: rgba(225, 225, 225, 180);\n"
"	border-style: dashed;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	\n"
"	background-color: rgb(136, 136, 136);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QToolButton\n"
"{ \n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	\n"
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
"	background-color: rgb(136, 136, 136);\n"
"	bor"
                        "der-width: 2px;\n"
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
"")
        self.horizontalLayout = QHBoxLayout(DialogReduce)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.f_content = QFrame(DialogReduce)
        self.f_content.setObjectName(u"f_content")
        self.f_content.setFrameShape(QFrame.StyledPanel)
        self.f_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.f_content)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tb_coupon_reduce = QToolButton(self.f_content)
        self.tb_coupon_reduce.setObjectName(u"tb_coupon_reduce")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_coupon_reduce.sizePolicy().hasHeightForWidth())
        self.tb_coupon_reduce.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/Simple icons/simple_icons/fi-rr-ticket.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_coupon_reduce.setIcon(icon)
        self.tb_coupon_reduce.setIconSize(QSize(48, 48))
        self.tb_coupon_reduce.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.tb_coupon_reduce)

        self.tb_manual_reduce = QToolButton(self.f_content)
        self.tb_manual_reduce.setObjectName(u"tb_manual_reduce")
        sizePolicy.setHeightForWidth(self.tb_manual_reduce.sizePolicy().hasHeightForWidth())
        self.tb_manual_reduce.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/Simple icons/simple_icons/fi-rr-smile-wink.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_manual_reduce.setIcon(icon1)
        self.tb_manual_reduce.setIconSize(QSize(48, 48))
        self.tb_manual_reduce.setPopupMode(QToolButton.DelayedPopup)
        self.tb_manual_reduce.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.tb_manual_reduce.setArrowType(Qt.NoArrow)

        self.horizontalLayout_2.addWidget(self.tb_manual_reduce)


        self.horizontalLayout.addWidget(self.f_content)


        self.retranslateUi(DialogReduce)

        QMetaObject.connectSlotsByName(DialogReduce)
    # setupUi

    def retranslateUi(self, DialogReduce):
        DialogReduce.setWindowTitle(QCoreApplication.translate("DialogReduce", u"Reduction", None))
        self.tb_coupon_reduce.setText(QCoreApplication.translate("DialogReduce", u"Coupon", None))
        self.tb_manual_reduce.setText(QCoreApplication.translate("DialogReduce", u"Reduce", None))
    # retranslateUi

