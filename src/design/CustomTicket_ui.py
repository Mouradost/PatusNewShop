# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CustomTicket.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(981, 411)
        Dialog.setMinimumSize(QSize(900, 400))
        icon = QIcon()
        icon.addFile(u":/Simple icons/simple_icons/fi-rr-print.svg", QSize(), QIcon.Normal, QIcon.Off)
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
"	background-color: rgb(136, 136, 136);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.le_qr_code = QLineEdit(self.frame_2)
        self.le_qr_code.setObjectName(u"le_qr_code")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_qr_code)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.le_image = QLineEdit(self.frame_2)
        self.le_image.setObjectName(u"le_image")
        self.le_image.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.le_image)

        self.te_text = QLineEdit(self.frame_2)
        self.te_text.setObjectName(u"te_text")
        self.te_text.setMaxLength(200)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.te_text)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_clear_all = QPushButton(self.frame_3)
        self.btn_clear_all.setObjectName(u"btn_clear_all")
        icon1 = QIcon()
        icon1.addFile(u":/Simple icons/simple_icons/fi-rr-broom.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_all.setIcon(icon1)
        self.btn_clear_all.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_clear_all)

        self.btn_open_image = QPushButton(self.frame_3)
        self.btn_open_image.setObjectName(u"btn_open_image")
        icon2 = QIcon()
        icon2.addFile(u":/Simple icons/simple_icons/fi-rr-picture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_image.setIcon(icon2)
        self.btn_open_image.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_open_image)

        self.btn_print = QPushButton(self.frame_3)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setIcon(icon)
        self.btn_print.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_print)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Custom ticket print", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Custom Ticket Printer", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Text", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"QR code", None))
        self.le_qr_code.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Image", None))
        self.le_image.setPlaceholderText("")
        self.te_text.setPlaceholderText("")
        self.btn_clear_all.setText(QCoreApplication.translate("Dialog", u"Clear all", None))
        self.btn_open_image.setText(QCoreApplication.translate("Dialog", u"Open an image", None))
        self.btn_print.setText(QCoreApplication.translate("Dialog", u"Print", None))
    # retranslateUi

