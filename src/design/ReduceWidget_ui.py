# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReduceWidget.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_w_reduce(object):
    def setupUi(self, w_reduce):
        if not w_reduce.objectName():
            w_reduce.setObjectName(u"w_reduce")
        w_reduce.resize(400, 300)
        w_reduce.setStyleSheet(u"*\n"
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
        self.verticalLayout = QVBoxLayout(w_reduce)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.le_reduction = QLineEdit(w_reduce)
        self.le_reduction.setObjectName(u"le_reduction")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_reduction.sizePolicy().hasHeightForWidth())
        self.le_reduction.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.le_reduction.setFont(font)
        self.le_reduction.setLayoutDirection(Qt.LeftToRight)
        self.le_reduction.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)
        self.le_reduction.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.le_reduction)

        self.bb_reduce = QDialogButtonBox(w_reduce)
        self.bb_reduce.setObjectName(u"bb_reduce")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bb_reduce.sizePolicy().hasHeightForWidth())
        self.bb_reduce.setSizePolicy(sizePolicy1)
        self.bb_reduce.setFont(font)
        self.bb_reduce.setLayoutDirection(Qt.LeftToRight)
        self.bb_reduce.setAutoFillBackground(False)
        self.bb_reduce.setOrientation(Qt.Vertical)
        self.bb_reduce.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.bb_reduce.setCenterButtons(True)

        self.verticalLayout.addWidget(self.bb_reduce)


        self.retranslateUi(w_reduce)

        QMetaObject.connectSlotsByName(w_reduce)
    # setupUi

    def retranslateUi(self, w_reduce):
        w_reduce.setWindowTitle(QCoreApplication.translate("w_reduce", u"Reduce", None))
        self.le_reduction.setPlaceholderText(QCoreApplication.translate("w_reduce", u"Given amount", None))
    # retranslateUi

