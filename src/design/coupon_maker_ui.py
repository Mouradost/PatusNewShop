# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coupon_maker.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateEdit, QDateTimeEdit,
    QDialog, QFormLayout, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QProgressBar,
    QSizePolicy, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1082, 700)
        Dialog.setMinimumSize(QSize(800, 700))
        icon = QIcon()
        icon.addFile(u":/Simple icons/simple_icons/fi-rr-ticket.svg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tw_coupon_maker = QTabWidget(Dialog)
        self.tw_coupon_maker.setObjectName(u"tw_coupon_maker")
        self.tab_create_coupon = QWidget()
        self.tab_create_coupon.setObjectName(u"tab_create_coupon")
        self.verticalLayout_3 = QVBoxLayout(self.tab_create_coupon)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.tab_create_coupon)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_3)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_amount = QLineEdit(self.frame_3)
        self.le_amount.setObjectName(u"le_amount")
        font1 = QFont()
        font1.setPointSize(12)
        self.le_amount.setFont(font1)
        self.le_amount.setInputMethodHints(Qt.ImhPreferNumbers)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_amount)

        self.de_start = QDateEdit(self.frame_3)
        self.de_start.setObjectName(u"de_start")
        self.de_start.setFont(font1)
        self.de_start.setCurrentSection(QDateTimeEdit.DaySection)
        self.de_start.setCalendarPopup(True)
        self.de_start.setDate(QDate(2022, 5, 28))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.de_start)

        self.de_end = QDateEdit(self.frame_3)
        self.de_end.setObjectName(u"de_end")
        self.de_end.setFont(font1)
        self.de_end.setCurrentSection(QDateTimeEdit.DaySection)
        self.de_end.setCalendarPopup(True)
        self.de_end.setDate(QDate(2022, 6, 28))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.de_end)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.le_side_picture_path = QLineEdit(self.frame_3)
        self.le_side_picture_path.setObjectName(u"le_side_picture_path")
        self.le_side_picture_path.setEnabled(True)
        self.le_side_picture_path.setFont(font1)
        self.le_side_picture_path.setInputMethodHints(Qt.ImhPreferNumbers)
        self.le_side_picture_path.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.le_side_picture_path)

        self.sb_count = QSpinBox(self.frame_3)
        self.sb_count.setObjectName(u"sb_count")
        self.sb_count.setFont(font1)
        self.sb_count.setMinimum(1)
        self.sb_count.setMaximum(100)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.sb_count)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.f_preview = QFrame(self.tab_create_coupon)
        self.f_preview.setObjectName(u"f_preview")
        self.f_preview.setMinimumSize(QSize(180, 50))
        self.f_preview.setFrameShape(QFrame.StyledPanel)
        self.f_preview.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_preview)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_3.addWidget(self.f_preview)

        self.frame_2 = QFrame(self.tab_create_coupon)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_load_template = QToolButton(self.frame_2)
        self.tb_load_template.setObjectName(u"tb_load_template")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tb_load_template.sizePolicy().hasHeightForWidth())
        self.tb_load_template.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/Simple icons/simple_icons/fi-rr-upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_load_template.setIcon(icon1)
        self.tb_load_template.setIconSize(QSize(32, 32))
        self.tb_load_template.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.tb_load_template)

        self.tb_load_side_picture = QToolButton(self.frame_2)
        self.tb_load_side_picture.setObjectName(u"tb_load_side_picture")
        sizePolicy1.setHeightForWidth(self.tb_load_side_picture.sizePolicy().hasHeightForWidth())
        self.tb_load_side_picture.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u":/Simple icons/simple_icons/fi-rr-picture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_load_side_picture.setIcon(icon2)
        self.tb_load_side_picture.setIconSize(QSize(32, 32))
        self.tb_load_side_picture.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.tb_load_side_picture)

        self.tb_generate = QToolButton(self.frame_2)
        self.tb_generate.setObjectName(u"tb_generate")
        sizePolicy1.setHeightForWidth(self.tb_generate.sizePolicy().hasHeightForWidth())
        self.tb_generate.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u":/Simple icons/simple_icons/fi-rr-palette.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_generate.setIcon(icon3)
        self.tb_generate.setIconSize(QSize(32, 32))
        self.tb_generate.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.tb_generate)

        self.tb_preview = QToolButton(self.frame_2)
        self.tb_preview.setObjectName(u"tb_preview")
        sizePolicy1.setHeightForWidth(self.tb_preview.sizePolicy().hasHeightForWidth())
        self.tb_preview.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/Simple icons/simple_icons/fi-rr-print.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_preview.setIcon(icon4)
        self.tb_preview.setIconSize(QSize(32, 32))
        self.tb_preview.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.tb_preview)

        self.tb_print = QToolButton(self.frame_2)
        self.tb_print.setObjectName(u"tb_print")
        sizePolicy1.setHeightForWidth(self.tb_print.sizePolicy().hasHeightForWidth())
        self.tb_print.setSizePolicy(sizePolicy1)
        self.tb_print.setIcon(icon4)
        self.tb_print.setIconSize(QSize(32, 32))
        self.tb_print.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.tb_print)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.tw_coupon_maker.addTab(self.tab_create_coupon, "")
        self.tab_manage_coupon = QWidget()
        self.tab_manage_coupon.setObjectName(u"tab_manage_coupon")
        self.verticalLayout_4 = QVBoxLayout(self.tab_manage_coupon)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tw_manage_coupons = QTableWidget(self.tab_manage_coupon)
        self.tw_manage_coupons.setObjectName(u"tw_manage_coupons")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tw_manage_coupons.sizePolicy().hasHeightForWidth())
        self.tw_manage_coupons.setSizePolicy(sizePolicy2)
        self.tw_manage_coupons.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_manage_coupons.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_4.addWidget(self.tw_manage_coupons)

        self.f_manage_preview = QFrame(self.tab_manage_coupon)
        self.f_manage_preview.setObjectName(u"f_manage_preview")
        self.f_manage_preview.setMinimumSize(QSize(180, 50))
        self.f_manage_preview.setFrameShape(QFrame.StyledPanel)
        self.f_manage_preview.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.f_manage_preview)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.verticalLayout_4.addWidget(self.f_manage_preview)

        self.le_manage_template_path = QLineEdit(self.tab_manage_coupon)
        self.le_manage_template_path.setObjectName(u"le_manage_template_path")
        self.le_manage_template_path.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.le_manage_template_path)

        self.le_manage_picture_path = QLineEdit(self.tab_manage_coupon)
        self.le_manage_picture_path.setObjectName(u"le_manage_picture_path")
        self.le_manage_picture_path.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.le_manage_picture_path)

        self.frame_4 = QFrame(self.tab_manage_coupon)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tb_manage_template = QToolButton(self.frame_4)
        self.tb_manage_template.setObjectName(u"tb_manage_template")
        sizePolicy1.setHeightForWidth(self.tb_manage_template.sizePolicy().hasHeightForWidth())
        self.tb_manage_template.setSizePolicy(sizePolicy1)
        self.tb_manage_template.setIcon(icon1)
        self.tb_manage_template.setIconSize(QSize(32, 32))
        self.tb_manage_template.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.tb_manage_template)

        self.tb_manage_picture = QToolButton(self.frame_4)
        self.tb_manage_picture.setObjectName(u"tb_manage_picture")
        sizePolicy1.setHeightForWidth(self.tb_manage_picture.sizePolicy().hasHeightForWidth())
        self.tb_manage_picture.setSizePolicy(sizePolicy1)
        self.tb_manage_picture.setIcon(icon2)
        self.tb_manage_picture.setIconSize(QSize(32, 32))
        self.tb_manage_picture.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.tb_manage_picture)

        self.tb_manage_preview = QToolButton(self.frame_4)
        self.tb_manage_preview.setObjectName(u"tb_manage_preview")
        sizePolicy1.setHeightForWidth(self.tb_manage_preview.sizePolicy().hasHeightForWidth())
        self.tb_manage_preview.setSizePolicy(sizePolicy1)
        self.tb_manage_preview.setIcon(icon4)
        self.tb_manage_preview.setIconSize(QSize(32, 32))
        self.tb_manage_preview.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.tb_manage_preview)

        self.tb_manage_print = QToolButton(self.frame_4)
        self.tb_manage_print.setObjectName(u"tb_manage_print")
        sizePolicy1.setHeightForWidth(self.tb_manage_print.sizePolicy().hasHeightForWidth())
        self.tb_manage_print.setSizePolicy(sizePolicy1)
        self.tb_manage_print.setIcon(icon4)
        self.tb_manage_print.setIconSize(QSize(32, 32))
        self.tb_manage_print.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.tb_manage_print)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.tw_coupon_maker.addTab(self.tab_manage_coupon, "")

        self.verticalLayout.addWidget(self.tw_coupon_maker)

        self.pb_print = QProgressBar(Dialog)
        self.pb_print.setObjectName(u"pb_print")
        self.pb_print.setEnabled(True)
        self.pb_print.setValue(0)

        self.verticalLayout.addWidget(self.pb_print)


        self.retranslateUi(Dialog)

        self.tw_coupon_maker.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Coupon Generator", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.de_start.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd-MMM-yyyy", None))
        self.de_end.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd-MMM-yyyy", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Date Start", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Date End", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Side Picture", None))
        self.le_side_picture_path.setPlaceholderText(QCoreApplication.translate("Dialog", u"Path", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Quantity", None))
        self.tb_load_template.setText(QCoreApplication.translate("Dialog", u"Load Template", None))
        self.tb_load_side_picture.setText(QCoreApplication.translate("Dialog", u"Load Side Picture", None))
        self.tb_generate.setText(QCoreApplication.translate("Dialog", u"Generate", None))
        self.tb_preview.setText(QCoreApplication.translate("Dialog", u"Preview Print", None))
        self.tb_print.setText(QCoreApplication.translate("Dialog", u"Print", None))
        self.tw_coupon_maker.setTabText(self.tw_coupon_maker.indexOf(self.tab_create_coupon), QCoreApplication.translate("Dialog", u"Create", None))
        self.le_manage_template_path.setPlaceholderText(QCoreApplication.translate("Dialog", u"Template path", None))
        self.le_manage_picture_path.setPlaceholderText(QCoreApplication.translate("Dialog", u"Side picture path", None))
        self.tb_manage_template.setText(QCoreApplication.translate("Dialog", u"Load Template", None))
        self.tb_manage_picture.setText(QCoreApplication.translate("Dialog", u"Load Side Picture", None))
        self.tb_manage_preview.setText(QCoreApplication.translate("Dialog", u"Print preview", None))
        self.tb_manage_print.setText(QCoreApplication.translate("Dialog", u"Print", None))
        self.tw_coupon_maker.setTabText(self.tw_coupon_maker.indexOf(self.tab_manage_coupon), QCoreApplication.translate("Dialog", u"Manage", None))
    # retranslateUi

