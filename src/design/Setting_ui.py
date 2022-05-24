# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setting.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(860, 674)
        Dialog.setMinimumSize(QSize(860, 600))
        icon = QIcon()
        icon.addFile(u":/Simple icons/simple_icons/fi-rr-settings-sliders.svg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"*\n"
"{\n"
"	font: 26pt \"MS Shell Dlg 2\";\n"
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
"	background: rgba(225, 225, 225);\n"
"	border-style: dashed;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(136, 136, 136);\n"
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
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.l_title = QLabel(self.frame)
        self.l_title.setObjectName(u"l_title")
        self.l_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.l_title)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.le_ip = QLineEdit(self.frame)
        self.le_ip.setObjectName(u"le_ip")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_ip.sizePolicy().hasHeightForWidth())
        self.le_ip.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.le_ip)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.sb_port = QSpinBox(self.frame)
        self.sb_port.setObjectName(u"sb_port")
        self.sb_port.setEnabled(False)
        sizePolicy.setHeightForWidth(self.sb_port.sizePolicy().hasHeightForWidth())
        self.sb_port.setSizePolicy(sizePolicy)
        self.sb_port.setMaximum(100000)

        self.horizontalLayout_2.addWidget(self.sb_port)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.label_3)

        self.sb_maxClients = QSpinBox(self.frame)
        self.sb_maxClients.setObjectName(u"sb_maxClients")
        sizePolicy.setHeightForWidth(self.sb_maxClients.sizePolicy().hasHeightForWidth())
        self.sb_maxClients.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.sb_maxClients)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.le_cashier_ip = QLineEdit(self.frame)
        self.le_cashier_ip.setObjectName(u"le_cashier_ip")
        sizePolicy.setHeightForWidth(self.le_cashier_ip.sizePolicy().hasHeightForWidth())
        self.le_cashier_ip.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.le_cashier_ip)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.le_kitchen_ip = QLineEdit(self.frame)
        self.le_kitchen_ip.setObjectName(u"le_kitchen_ip")
        sizePolicy.setHeightForWidth(self.le_kitchen_ip.sizePolicy().hasHeightForWidth())
        self.le_kitchen_ip.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.le_kitchen_ip)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.le_pizza_ip = QLineEdit(self.frame)
        self.le_pizza_ip.setObjectName(u"le_pizza_ip")
        sizePolicy.setHeightForWidth(self.le_pizza_ip.sizePolicy().hasHeightForWidth())
        self.le_pizza_ip.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.le_pizza_ip)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.le_bar_ip = QLineEdit(self.frame)
        self.le_bar_ip.setObjectName(u"le_bar_ip")
        sizePolicy.setHeightForWidth(self.le_bar_ip.sizePolicy().hasHeightForWidth())
        self.le_bar_ip.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.le_bar_ip)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.cb_drawer_pin = QComboBox(self.frame)
        self.cb_drawer_pin.addItem("")
        self.cb_drawer_pin.addItem("")
        self.cb_drawer_pin.setObjectName(u"cb_drawer_pin")

        self.horizontalLayout_8.addWidget(self.cb_drawer_pin)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy1)
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Setting", None))
        self.l_title.setText(QCoreApplication.translate("Dialog", u"Setting modification for the SERVER", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"SERVER IP", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"SERVER PORT", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"SERVER MAX CLIENTS", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"CASHIER IP", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"KITCHEN IP", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"PIZZA IP", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"BAR IP", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"DRAWER PIN", None))
        self.cb_drawer_pin.setItemText(0, QCoreApplication.translate("Dialog", u"2", None))
        self.cb_drawer_pin.setItemText(1, QCoreApplication.translate("Dialog", u"5", None))

    # retranslateUi

