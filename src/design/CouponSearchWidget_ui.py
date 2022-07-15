# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CouponSearchWidget.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(676, 587)
        Form.setStyleSheet(u"*\n"
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
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_coupon_id = QLineEdit(Form)
        self.le_coupon_id.setObjectName(u"le_coupon_id")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_coupon_id.sizePolicy().hasHeightForWidth())
        self.le_coupon_id.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.le_coupon_id.setFont(font)
        self.le_coupon_id.setLayoutDirection(Qt.LeftToRight)
        self.le_coupon_id.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)
        self.le_coupon_id.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.le_coupon_id)

        self.btn_search = QPushButton(Form)
        self.btn_search.setObjectName(u"btn_search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/Simple icons/simple_icons/fi-rr-search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon)
        self.btn_search.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_search)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.te_coupon_info = QTextEdit(Form)
        self.te_coupon_info.setObjectName(u"te_coupon_info")
        self.te_coupon_info.setReadOnly(True)

        self.verticalLayout.addWidget(self.te_coupon_info)

        self.bb_coupon = QDialogButtonBox(Form)
        self.bb_coupon.setObjectName(u"bb_coupon")
        sizePolicy.setHeightForWidth(self.bb_coupon.sizePolicy().hasHeightForWidth())
        self.bb_coupon.setSizePolicy(sizePolicy)
        self.bb_coupon.setFont(font)
        self.bb_coupon.setLayoutDirection(Qt.LeftToRight)
        self.bb_coupon.setAutoFillBackground(False)
        self.bb_coupon.setOrientation(Qt.Vertical)
        self.bb_coupon.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.bb_coupon.setCenterButtons(True)

        self.verticalLayout.addWidget(self.bb_coupon)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.le_coupon_id.setText("")
        self.le_coupon_id.setPlaceholderText(QCoreApplication.translate("Form", u"Coupon Number", None))
        self.btn_search.setText(QCoreApplication.translate("Form", u"Search", None))
    # retranslateUi

