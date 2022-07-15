# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchCoupon.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(404, 212)
        icon = QIcon()
        icon.addFile(u":/Simple icons/simple_icons/fi-rr-menu-dots.svg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"*\n"
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
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.le_quantity = QLineEdit(Dialog)
        self.le_quantity.setObjectName(u"le_quantity")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_quantity.sizePolicy().hasHeightForWidth())
        self.le_quantity.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.le_quantity.setFont(font)
        self.le_quantity.setLayoutDirection(Qt.LeftToRight)
        self.le_quantity.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)

        self.verticalLayout.addWidget(self.le_quantity)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy1)
        self.buttonBox.setFont(font)
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Custom quantity", None))
        self.le_quantity.setText("")
        self.le_quantity.setPlaceholderText(QCoreApplication.translate("Dialog", u"Quantity", None))
    # retranslateUi

