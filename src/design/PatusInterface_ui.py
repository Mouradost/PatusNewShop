# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PatusInterface.ui'
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
    QDateEdit, QDateTimeEdit, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLCDNumber,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_PatusMainWindow(object):
    def setupUi(self, PatusMainWindow):
        if not PatusMainWindow.objectName():
            PatusMainWindow.setObjectName(u"PatusMainWindow")
        PatusMainWindow.resize(1100, 816)
        PatusMainWindow.setMinimumSize(QSize(1100, 800))
        icon = QIcon()
        icon.addFile(u":/Simple icons/patus_logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        PatusMainWindow.setWindowIcon(icon)
        PatusMainWindow.setStyleSheet(u"#page_tables{\n"
"	border-image: url(resource/Restaurant_plan/plan.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QToolButton\n"
"{ \n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
""
                        "}\n"
"\n"
"\n"
"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
"    font-size: 24px;\n"
"}\n"
"QLineEdit:pressed{\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 3px;\n"
"    border-radius: 20px;\n"
"	border-style: line;\n"
"    font-size: 24px;\n"
"}\n"
"QFrame\n"
"{\n"
""
                        "	background-color: rgb(192, 192, 192)\n"
"}\n"
"QWidget\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QTabBar::scroller {width: 80px;}")
        self.w_background = QWidget(PatusMainWindow)
        self.w_background.setObjectName(u"w_background")
        self.verticalLayout = QVBoxLayout(self.w_background)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.f_main = QFrame(self.w_background)
        self.f_main.setObjectName(u"f_main")
        self.f_main.setTabletTracking(False)
        self.f_main.setStyleSheet(u"")
        self.f_main.setFrameShape(QFrame.StyledPanel)
        self.f_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.f_main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.f_sideBar = QFrame(self.f_main)
        self.f_sideBar.setObjectName(u"f_sideBar")
        self.f_sideBar.setMinimumSize(QSize(100, 0))
        self.f_sideBar.setMaximumSize(QSize(100, 16777215))
        self.f_sideBar.setTabletTracking(False)
        self.f_sideBar.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(190, 190, 190)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 50px 50px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(225, 225, 225, 255);\n"
"	border-style: inset;\n"
"}")
        self.f_sideBar.setFrameShape(QFrame.StyledPanel)
        self.f_sideBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_sideBar)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.btn_logInOut = QPushButton(self.f_sideBar)
        self.btn_logInOut.setObjectName(u"btn_logInOut")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_logInOut.sizePolicy().hasHeightForWidth())
        self.btn_logInOut.setSizePolicy(sizePolicy)
        self.btn_logInOut.setTabletTracking(False)
        icon1 = QIcon()
        icon1.addFile(u":/Simple icons/simple_icons/fi-rr-user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logInOut.setIcon(icon1)
        self.btn_logInOut.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btn_logInOut)

        self.btn_tables = QPushButton(self.f_sideBar)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_tables.sizePolicy().hasHeightForWidth())
        self.btn_tables.setSizePolicy(sizePolicy)
        self.btn_tables.setTabletTracking(False)
        icon2 = QIcon()
        icon2.addFile(u":/Simple icons/simple_icons/fi-rr-terrace.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_tables.setIcon(icon2)
        self.btn_tables.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btn_tables)

        self.btn_cashRegister = QPushButton(self.f_sideBar)
        self.btn_cashRegister.setObjectName(u"btn_cashRegister")
        self.btn_cashRegister.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_cashRegister.sizePolicy().hasHeightForWidth())
        self.btn_cashRegister.setSizePolicy(sizePolicy)
        self.btn_cashRegister.setTabletTracking(False)
        icon3 = QIcon()
        icon3.addFile(u":/Simple icons/simple_icons/fi-rr-shop.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cashRegister.setIcon(icon3)
        self.btn_cashRegister.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btn_cashRegister)

        self.btn_reservation = QPushButton(self.f_sideBar)
        self.btn_reservation.setObjectName(u"btn_reservation")
        self.btn_reservation.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_reservation.sizePolicy().hasHeightForWidth())
        self.btn_reservation.setSizePolicy(sizePolicy)
        self.btn_reservation.setTabletTracking(False)
        icon4 = QIcon()
        icon4.addFile(u":/Simple icons/simple_icons/fi-rr-phone-call.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reservation.setIcon(icon4)
        self.btn_reservation.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btn_reservation)

        self.btn_waste = QPushButton(self.f_sideBar)
        self.btn_waste.setObjectName(u"btn_waste")
        self.btn_waste.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_waste.sizePolicy().hasHeightForWidth())
        self.btn_waste.setSizePolicy(sizePolicy)
        self.btn_waste.setTabletTracking(False)
        icon5 = QIcon()
        icon5.addFile(u":/Simple icons/simple_icons/fi-rr-sad.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_waste.setIcon(icon5)
        self.btn_waste.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btn_waste)

        self.btn_databaseOverview = QPushButton(self.f_sideBar)
        self.btn_databaseOverview.setObjectName(u"btn_databaseOverview")
        self.btn_databaseOverview.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_databaseOverview.sizePolicy().hasHeightForWidth())
        self.btn_databaseOverview.setSizePolicy(sizePolicy)
        self.btn_databaseOverview.setTabletTracking(False)
        icon6 = QIcon()
        icon6.addFile(u":/Simple icons/simple_icons/fi-rr-home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_databaseOverview.setIcon(icon6)
        self.btn_databaseOverview.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btn_databaseOverview)

        self.btn_productReceipt = QPushButton(self.f_sideBar)
        self.btn_productReceipt.setObjectName(u"btn_productReceipt")
        self.btn_productReceipt.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_productReceipt.sizePolicy().hasHeightForWidth())
        self.btn_productReceipt.setSizePolicy(sizePolicy)
        self.btn_productReceipt.setTabletTracking(False)
        icon7 = QIcon()
        icon7.addFile(u":/Simple icons/simple_icons/fi-rr-list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_productReceipt.setIcon(icon7)
        self.btn_productReceipt.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btn_productReceipt)

        self.btn_database = QPushButton(self.f_sideBar)
        self.btn_database.setObjectName(u"btn_database")
        self.btn_database.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_database.sizePolicy().hasHeightForWidth())
        self.btn_database.setSizePolicy(sizePolicy)
        self.btn_database.setTabletTracking(False)
        icon8 = QIcon()
        icon8.addFile(u":/Simple icons/simple_icons/fi-rr-database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_database.setIcon(icon8)
        self.btn_database.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btn_database)

        self.btn_workerStatus = QPushButton(self.f_sideBar)
        self.btn_workerStatus.setObjectName(u"btn_workerStatus")
        self.btn_workerStatus.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_workerStatus.sizePolicy().hasHeightForWidth())
        self.btn_workerStatus.setSizePolicy(sizePolicy)
        self.btn_workerStatus.setTabletTracking(False)
        icon9 = QIcon()
        icon9.addFile(u":/Simple icons/simple_icons/fi-rr-data-transfer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_workerStatus.setIcon(icon9)
        self.btn_workerStatus.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btn_workerStatus)

        self.btn_statistic = QPushButton(self.f_sideBar)
        self.btn_statistic.setObjectName(u"btn_statistic")
        self.btn_statistic.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_statistic.sizePolicy().hasHeightForWidth())
        self.btn_statistic.setSizePolicy(sizePolicy)
        self.btn_statistic.setTabletTracking(False)
        icon10 = QIcon()
        icon10.addFile(u":/Simple icons/simple_icons/fi-rr-stats.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_statistic.setIcon(icon10)
        self.btn_statistic.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btn_statistic)

        self.btn_exit = QPushButton(self.f_sideBar)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setTabletTracking(False)
        icon11 = QIcon()
        icon11.addFile(u":/Simple icons/simple_icons/fi-rr-sign-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon11)
        self.btn_exit.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btn_exit)


        self.horizontalLayout.addWidget(self.f_sideBar)

        self.f_body = QFrame(self.f_main)
        self.f_body.setObjectName(u"f_body")
        self.f_body.setTabletTracking(False)
        self.f_body.setStyleSheet(u"#f_body{\n"
"background-color: rgba(208, 208, 208, 150);\n"
"}")
        self.f_body.setFrameShape(QFrame.StyledPanel)
        self.f_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.f_body)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 1, 1, 1)
        self.f_header = QFrame(self.f_body)
        self.f_header.setObjectName(u"f_header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.f_header.sizePolicy().hasHeightForWidth())
        self.f_header.setSizePolicy(sizePolicy1)
        self.f_header.setMinimumSize(QSize(0, 50))
        self.f_header.setTabletTracking(False)
        self.f_header.setStyleSheet(u"#f_header{\n"
"	background-color: qlineargradient(spread:reflect, x1:0.460227, y1:1, x2:1, y2:1, stop:0 rgba(218, 218, 218, 255), stop:0.625 rgba(135, 135, 135, 255));\n"
"}")
        self.f_header.setFrameShape(QFrame.StyledPanel)
        self.f_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.f_header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.f_btn_sideBar = QFrame(self.f_header)
        self.f_btn_sideBar.setObjectName(u"f_btn_sideBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.f_btn_sideBar.sizePolicy().hasHeightForWidth())
        self.f_btn_sideBar.setSizePolicy(sizePolicy2)
        self.f_btn_sideBar.setMinimumSize(QSize(50, 50))
        self.f_btn_sideBar.setMaximumSize(QSize(50, 50))
        self.f_btn_sideBar.setTabletTracking(False)
        self.f_btn_sideBar.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color:  rgba(223, 223, 223, 200);\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	background: rgba(225, 225, 225, 20);\n"
"	border-width: 2px;\n"
"    border-radius: 2px;\n"
"	qproperty-iconSize: 32px 32px;\n"
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
"	background: rgba(225, 225, 225, 255);\n"
"	border-style: inset;\n"
"}")
        self.f_btn_sideBar.setFrameShape(QFrame.StyledPanel)
        self.f_btn_sideBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.f_btn_sideBar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_sideBar = QPushButton(self.f_btn_sideBar)
        self.btn_sideBar.setObjectName(u"btn_sideBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_sideBar.sizePolicy().hasHeightForWidth())
        self.btn_sideBar.setSizePolicy(sizePolicy3)
        self.btn_sideBar.setTabletTracking(False)
        icon12 = QIcon()
        icon12.addFile(u":/Simple icons/simple_icons/fi-rr-align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sideBar.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.btn_sideBar)


        self.horizontalLayout_3.addWidget(self.f_btn_sideBar)

        self.f_headerInfo = QFrame(self.f_header)
        self.f_headerInfo.setObjectName(u"f_headerInfo")
        sizePolicy1.setHeightForWidth(self.f_headerInfo.sizePolicy().hasHeightForWidth())
        self.f_headerInfo.setSizePolicy(sizePolicy1)
        self.f_headerInfo.setTabletTracking(False)
        self.f_headerInfo.setStyleSheet(u"*\n"
"{\n"
"	color: rgb(33, 33, 33);\n"
"	font: 12pt \"Times New Roman\";\n"
"    border-radius: 30px;\n"
"	padding: 2px;\n"
"}\n"
"QLabel\n"
"{\n"
"	background: transparent\n"
"}")
        self.f_headerInfo.setFrameShape(QFrame.StyledPanel)
        self.f_headerInfo.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.f_headerInfo)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.l_monthSells = QLabel(self.f_headerInfo)
        self.l_monthSells.setObjectName(u"l_monthSells")
        sizePolicy1.setHeightForWidth(self.l_monthSells.sizePolicy().hasHeightForWidth())
        self.l_monthSells.setSizePolicy(sizePolicy1)
        self.l_monthSells.setTabletTracking(False)
        self.l_monthSells.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l_monthSells, 2, 1, 1, 1)

        self.l_busyTables = QLabel(self.f_headerInfo)
        self.l_busyTables.setObjectName(u"l_busyTables")
        sizePolicy1.setHeightForWidth(self.l_busyTables.sizePolicy().hasHeightForWidth())
        self.l_busyTables.setSizePolicy(sizePolicy1)
        self.l_busyTables.setTabletTracking(False)
        self.l_busyTables.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l_busyTables, 2, 0, 1, 1)

        self.l_freeTables = QLabel(self.f_headerInfo)
        self.l_freeTables.setObjectName(u"l_freeTables")
        sizePolicy1.setHeightForWidth(self.l_freeTables.sizePolicy().hasHeightForWidth())
        self.l_freeTables.setSizePolicy(sizePolicy1)
        self.l_freeTables.setTabletTracking(False)
        self.l_freeTables.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l_freeTables, 0, 0, 1, 1)

        self.l_daySells = QLabel(self.f_headerInfo)
        self.l_daySells.setObjectName(u"l_daySells")
        sizePolicy1.setHeightForWidth(self.l_daySells.sizePolicy().hasHeightForWidth())
        self.l_daySells.setSizePolicy(sizePolicy1)
        self.l_daySells.setTabletTracking(False)
        self.l_daySells.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l_daySells, 0, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.f_headerInfo)

        self.f_btn_fullScreen = QFrame(self.f_header)
        self.f_btn_fullScreen.setObjectName(u"f_btn_fullScreen")
        sizePolicy2.setHeightForWidth(self.f_btn_fullScreen.sizePolicy().hasHeightForWidth())
        self.f_btn_fullScreen.setSizePolicy(sizePolicy2)
        self.f_btn_fullScreen.setMinimumSize(QSize(180, 50))
        self.f_btn_fullScreen.setMaximumSize(QSize(250, 50))
        self.f_btn_fullScreen.setTabletTracking(False)
        self.f_btn_fullScreen.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color:  rgba(223, 223, 223, 200);\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	background: rgba(225, 225, 225, 20);\n"
"	border-width: 2px;\n"
"    border-radius: 2px;\n"
"	qproperty-iconSize: 32px 32px;\n"
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
"	background: rgba(225, 225, 225, 255);\n"
"	border-style: inset;\n"
"}")
        self.f_btn_fullScreen.setFrameShape(QFrame.StyledPanel)
        self.f_btn_fullScreen.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.f_btn_fullScreen)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_couponGenerator = QPushButton(self.f_btn_fullScreen)
        self.btn_couponGenerator.setObjectName(u"btn_couponGenerator")
        self.btn_couponGenerator.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.btn_couponGenerator.sizePolicy().hasHeightForWidth())
        self.btn_couponGenerator.setSizePolicy(sizePolicy3)
        self.btn_couponGenerator.setTabletTracking(False)
        icon13 = QIcon()
        icon13.addFile(u":/Simple icons/simple_icons/fi-rr-ticket.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_couponGenerator.setIcon(icon13)

        self.horizontalLayout_5.addWidget(self.btn_couponGenerator)

        self.btn_customPrint = QPushButton(self.f_btn_fullScreen)
        self.btn_customPrint.setObjectName(u"btn_customPrint")
        self.btn_customPrint.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.btn_customPrint.sizePolicy().hasHeightForWidth())
        self.btn_customPrint.setSizePolicy(sizePolicy3)
        self.btn_customPrint.setTabletTracking(False)
        icon14 = QIcon()
        icon14.addFile(u":/Simple icons/simple_icons/fi-rr-print.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_customPrint.setIcon(icon14)

        self.horizontalLayout_5.addWidget(self.btn_customPrint)

        self.btn_blockNote = QPushButton(self.f_btn_fullScreen)
        self.btn_blockNote.setObjectName(u"btn_blockNote")
        self.btn_blockNote.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.btn_blockNote.sizePolicy().hasHeightForWidth())
        self.btn_blockNote.setSizePolicy(sizePolicy3)
        self.btn_blockNote.setTabletTracking(False)
        icon15 = QIcon()
        icon15.addFile(u":/Simple icons/simple_icons/fi-rr-call-incoming.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_blockNote.setIcon(icon15)

        self.horizontalLayout_5.addWidget(self.btn_blockNote)

        self.btn_notification = QPushButton(self.f_btn_fullScreen)
        self.btn_notification.setObjectName(u"btn_notification")
        self.btn_notification.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.btn_notification.sizePolicy().hasHeightForWidth())
        self.btn_notification.setSizePolicy(sizePolicy3)
        self.btn_notification.setTabletTracking(False)
        icon16 = QIcon()
        icon16.addFile(u":/Simple icons/simple_icons/fi-rr-envelope-marker.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_notification.setIcon(icon16)

        self.horizontalLayout_5.addWidget(self.btn_notification)

        self.btn_setting = QPushButton(self.f_btn_fullScreen)
        self.btn_setting.setObjectName(u"btn_setting")
        sizePolicy3.setHeightForWidth(self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy3)
        self.btn_setting.setTabletTracking(False)
        icon17 = QIcon()
        icon17.addFile(u":/Simple icons/simple_icons/fi-rr-settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting.setIcon(icon17)

        self.horizontalLayout_5.addWidget(self.btn_setting)

        self.btn_fullScreen = QPushButton(self.f_btn_fullScreen)
        self.btn_fullScreen.setObjectName(u"btn_fullScreen")
        sizePolicy3.setHeightForWidth(self.btn_fullScreen.sizePolicy().hasHeightForWidth())
        self.btn_fullScreen.setSizePolicy(sizePolicy3)
        self.btn_fullScreen.setTabletTracking(False)
        icon18 = QIcon()
        icon18.addFile(u":/Simple icons/simple_icons/fi-rr-compress.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fullScreen.setIcon(icon18)

        self.horizontalLayout_5.addWidget(self.btn_fullScreen)


        self.horizontalLayout_3.addWidget(self.f_btn_fullScreen)


        self.verticalLayout_3.addWidget(self.f_header)

        self.f_content = QFrame(self.f_body)
        self.f_content.setObjectName(u"f_content")
        self.f_content.setTabletTracking(False)
        self.f_content.setFrameShape(QFrame.StyledPanel)
        self.f_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.f_content)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.sw_content = QStackedWidget(self.f_content)
        self.sw_content.setObjectName(u"sw_content")
        self.sw_content.setTabletTracking(False)
        self.sw_content.setStyleSheet(u"")
        self.sw_content.setFrameShape(QFrame.Box)
        self.page_standBy = QWidget()
        self.page_standBy.setObjectName(u"page_standBy")
        self.gridLayout = QGridLayout(self.page_standBy)
        self.gridLayout.setObjectName(u"gridLayout")
        self.hs_standByR = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.hs_standByR, 1, 2, 1, 1)

        self.vs_standByT = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.vs_standByT, 0, 1, 1, 1)

        self.f_standBy = QFrame(self.page_standBy)
        self.f_standBy.setObjectName(u"f_standBy")
        sizePolicy3.setHeightForWidth(self.f_standBy.sizePolicy().hasHeightForWidth())
        self.f_standBy.setSizePolicy(sizePolicy3)
        self.f_standBy.setMinimumSize(QSize(350, 200))
        self.f_standBy.setMaximumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        self.f_standBy.setFont(font)
        self.f_standBy.setStyleSheet(u"*\n"
"{\n"
"	background-color: rgba(149, 149, 149, 200);\n"
"	color: rgb(230, 230, 230);\n"
"	font: 28pt \"Times New Roman\";\n"
"    border-radius: 30px;\n"
"	padding: 2px;\n"
"}\n"
"QLabel\n"
"{\n"
"	background: transparent\n"
"}")
        self.f_standBy.setFrameShape(QFrame.StyledPanel)
        self.f_standBy.setFrameShadow(QFrame.Raised)
        self.f_standBy.setLineWidth(1)
        self.verticalLayout_4 = QVBoxLayout(self.f_standBy)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.l_date = QLabel(self.f_standBy)
        self.l_date.setObjectName(u"l_date")
        self.l_date.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.l_date)

        self.l_time = QLabel(self.f_standBy)
        self.l_time.setObjectName(u"l_time")
        self.l_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.l_time)

        self.l_welcomeMsg = QLabel(self.f_standBy)
        self.l_welcomeMsg.setObjectName(u"l_welcomeMsg")
        self.l_welcomeMsg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.l_welcomeMsg)


        self.gridLayout.addWidget(self.f_standBy, 1, 1, 1, 1)

        self.hs_standByL = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.hs_standByL, 1, 0, 1, 1)

        self.vs_standByB = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.vs_standByB, 2, 1, 1, 1)

        self.sw_content.addWidget(self.page_standBy)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.gridLayout_3 = QGridLayout(self.page_login)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.f_longin = QFrame(self.page_login)
        self.f_longin.setObjectName(u"f_longin")
        sizePolicy.setHeightForWidth(self.f_longin.sizePolicy().hasHeightForWidth())
        self.f_longin.setSizePolicy(sizePolicy)
        self.f_longin.setMinimumSize(QSize(100, 200))
        self.f_longin.setMaximumSize(QSize(400, 16777215))
        self.f_longin.setStyleSheet(u"*\n"
"{\n"
"	background: rgb(0, 0, 0);\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	color: white;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"	background:rgba(72, 72, 72, 200);\n"
"	border-width: 6px;\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"\n"
"#btn_biometric:hover\n"
"{\n"
"	background: rgba(225, 225, 225, 120);\n"
"}\n"
"\n"
"#btn_biometric:pressed\n"
"{\n"
"	background: rgba(225, 225, 225, 150);\n"
"}\n"
"\n"
"\n"
"QPushButton\n"
"{ \n"
"	alternate-background-color: rgb(0, 0, 0);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 100px 100px;\n"
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
"	background: rgba(225, 225, 225, 255);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(207, 207, 207);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072\n"
"}\n"
"")
        self.f_longin.setFrameShape(QFrame.StyledPanel)
        self.f_longin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.f_longin)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_biometric = QPushButton(self.f_longin)
        self.btn_biometric.setObjectName(u"btn_biometric")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_biometric.sizePolicy().hasHeightForWidth())
        self.btn_biometric.setSizePolicy(sizePolicy4)
        self.btn_biometric.setMinimumSize(QSize(200, 200))
        self.btn_biometric.setMaximumSize(QSize(400, 400))
        self.btn_biometric.setLayoutDirection(Qt.LeftToRight)
        icon19 = QIcon()
        icon19.addFile(u":/Simple icons/simple_icons/fi-rr-fingerprint.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_biometric.setIcon(icon19)

        self.verticalLayout_5.addWidget(self.btn_biometric)

        self.le_username = QLineEdit(self.f_longin)
        self.le_username.setObjectName(u"le_username")
        self.le_username.setMaxLength(20)
        self.le_username.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.le_username)

        self.le_password = QLineEdit(self.f_longin)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setMaxLength(15)
        self.le_password.setEchoMode(QLineEdit.Password)
        self.le_password.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.le_password)

        self.btn_loginConfirm = QPushButton(self.f_longin)
        self.btn_loginConfirm.setObjectName(u"btn_loginConfirm")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_loginConfirm.sizePolicy().hasHeightForWidth())
        self.btn_loginConfirm.setSizePolicy(sizePolicy5)
        self.btn_loginConfirm.setMinimumSize(QSize(0, 50))
        self.btn_loginConfirm.setMaximumSize(QSize(16777215, 50))
        self.btn_loginConfirm.setCheckable(True)

        self.verticalLayout_5.addWidget(self.btn_loginConfirm)


        self.gridLayout_3.addWidget(self.f_longin, 0, 1, 1, 1)

        self.hs_loginR = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.hs_loginR, 0, 2, 1, 1)

        self.hs_loginL = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.hs_loginL, 0, 0, 1, 1)

        self.sw_content.addWidget(self.page_login)
        self.page_tables = QWidget()
        self.page_tables.setObjectName(u"page_tables")
        self.page_tables.setStyleSheet(u"*\n"
"{\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	padding: 2px;\n"
"}\n"
"QPushButton\n"
"{ \n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 255);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
" }\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-style: dashed;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.page_tables)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.sw_content.addWidget(self.page_tables)
        self.page_cashRegister = QWidget()
        self.page_cashRegister.setObjectName(u"page_cashRegister")
        self.page_cashRegister.setStyleSheet(u"QPushButton\n"
"{ \n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	padding: 2px;\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 50px 50px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(225, 225, 225, 255);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	alignment: \"center\"\n"
"}")
        self.gridLayout_5 = QGridLayout(self.page_cashRegister)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.f_orderDashboard = QFrame(self.page_cashRegister)
        self.f_orderDashboard.setObjectName(u"f_orderDashboard")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.f_orderDashboard.sizePolicy().hasHeightForWidth())
        self.f_orderDashboard.setSizePolicy(sizePolicy6)
        self.f_orderDashboard.setMinimumSize(QSize(200, 0))
        self.f_orderDashboard.setMaximumSize(QSize(600, 16777215))
        self.f_orderDashboard.setTabletTracking(False)
        self.f_orderDashboard.setStyleSheet(u"\n"
"QPushButton\n"
"{ \n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.f_orderDashboard.setFrameShape(QFrame.StyledPanel)
        self.f_orderDashboard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.f_orderDashboard)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.f_orderDashboard)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setTabletTracking(False)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.l_cashRegisterTicketNumberTitle = QLabel(self.frame_5)
        self.l_cashRegisterTicketNumberTitle.setObjectName(u"l_cashRegisterTicketNumberTitle")
        self.l_cashRegisterTicketNumberTitle.setTabletTracking(False)

        self.horizontalLayout_31.addWidget(self.l_cashRegisterTicketNumberTitle)

        self.l_cashRegisterTicketNumber = QLabel(self.frame_5)
        self.l_cashRegisterTicketNumber.setObjectName(u"l_cashRegisterTicketNumber")
        self.l_cashRegisterTicketNumber.setTabletTracking(False)
        self.l_cashRegisterTicketNumber.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.l_cashRegisterTicketNumber)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.frame_9 = QFrame(self.f_orderDashboard)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setTabletTracking(False)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.l_cashRegisterTableNumberTitle = QLabel(self.frame_9)
        self.l_cashRegisterTableNumberTitle.setObjectName(u"l_cashRegisterTableNumberTitle")
        self.l_cashRegisterTableNumberTitle.setTabletTracking(False)

        self.horizontalLayout_32.addWidget(self.l_cashRegisterTableNumberTitle)

        self.l_cashRegisterTableNumber = QLabel(self.frame_9)
        self.l_cashRegisterTableNumber.setObjectName(u"l_cashRegisterTableNumber")
        self.l_cashRegisterTableNumber.setTabletTracking(False)
        self.l_cashRegisterTableNumber.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.l_cashRegisterTableNumber)

        self.btn_cashRegisterChangeTable = QPushButton(self.frame_9)
        self.btn_cashRegisterChangeTable.setObjectName(u"btn_cashRegisterChangeTable")
        sizePolicy4.setHeightForWidth(self.btn_cashRegisterChangeTable.sizePolicy().hasHeightForWidth())
        self.btn_cashRegisterChangeTable.setSizePolicy(sizePolicy4)
        self.btn_cashRegisterChangeTable.setMaximumSize(QSize(50, 16777215))
        self.btn_cashRegisterChangeTable.setTabletTracking(False)
        icon20 = QIcon()
        icon20.addFile(u":/Simple icons/simple_icons/fi-rr-apps-sort.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cashRegisterChangeTable.setIcon(icon20)
        self.btn_cashRegisterChangeTable.setIconSize(QSize(32, 32))

        self.horizontalLayout_32.addWidget(self.btn_cashRegisterChangeTable)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.f_orderPlace = QFrame(self.f_orderDashboard)
        self.f_orderPlace.setObjectName(u"f_orderPlace")
        self.f_orderPlace.setEnabled(False)
        sizePolicy.setHeightForWidth(self.f_orderPlace.sizePolicy().hasHeightForWidth())
        self.f_orderPlace.setSizePolicy(sizePolicy)
        self.f_orderPlace.setMaximumSize(QSize(2000, 16777215))
        self.f_orderPlace.setTabletTracking(False)
        self.f_orderPlace.setStyleSheet(u"QRadioButton::indicator::checked\n"
"{\n"
"	border:1px solid black;\n"
"	border-radius: 8px;\n"
"	background-color: gray;\n"
"}\n"
"\n"
"QRadioButton::indicator::unChecked\n"
"{\n"
"	border:1px solid black;\n"
"	border-radius: 8px;\n"
"	background-color: white;\n"
"}")
        self.f_orderPlace.setFrameShape(QFrame.StyledPanel)
        self.f_orderPlace.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.f_orderPlace)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.rb_takeAway = QRadioButton(self.f_orderPlace)
        self.rb_takeAway.setObjectName(u"rb_takeAway")
        self.rb_takeAway.setEnabled(False)
        sizePolicy.setHeightForWidth(self.rb_takeAway.sizePolicy().hasHeightForWidth())
        self.rb_takeAway.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        self.rb_takeAway.setFont(font1)
        self.rb_takeAway.setMouseTracking(True)
        self.rb_takeAway.setTabletTracking(False)
        icon21 = QIcon()
        icon21.addFile(u":/Simple icons/simple_icons/fi-rr-truck-side.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rb_takeAway.setIcon(icon21)
        self.rb_takeAway.setIconSize(QSize(24, 24))
        self.rb_takeAway.setCheckable(True)
        self.rb_takeAway.setChecked(True)

        self.horizontalLayout_56.addWidget(self.rb_takeAway)

        self.rb_onTable = QRadioButton(self.f_orderPlace)
        self.rb_onTable.setObjectName(u"rb_onTable")
        self.rb_onTable.setEnabled(False)
        sizePolicy.setHeightForWidth(self.rb_onTable.sizePolicy().hasHeightForWidth())
        self.rb_onTable.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        self.rb_onTable.setFont(font2)
        self.rb_onTable.setMouseTracking(True)
        self.rb_onTable.setTabletTracking(False)
        self.rb_onTable.setIcon(icon2)
        self.rb_onTable.setIconSize(QSize(24, 24))

        self.horizontalLayout_56.addWidget(self.rb_onTable)


        self.verticalLayout_7.addWidget(self.f_orderPlace)

        self.f_cashCommand = QFrame(self.f_orderDashboard)
        self.f_cashCommand.setObjectName(u"f_cashCommand")
        self.f_cashCommand.setTabletTracking(False)
        self.f_cashCommand.setFrameShape(QFrame.StyledPanel)
        self.f_cashCommand.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.f_cashCommand)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 5)
        self.f_orderNav = QFrame(self.f_cashCommand)
        self.f_orderNav.setObjectName(u"f_orderNav")
        self.f_orderNav.setTabletTracking(False)
        self.f_orderNav.setFrameShape(QFrame.StyledPanel)
        self.f_orderNav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.f_orderNav)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.f_ticket = QFrame(self.f_orderNav)
        self.f_ticket.setObjectName(u"f_ticket")
        sizePolicy.setHeightForWidth(self.f_ticket.sizePolicy().hasHeightForWidth())
        self.f_ticket.setSizePolicy(sizePolicy)
        self.f_ticket.setMaximumSize(QSize(40, 16777215))
        self.f_ticket.setTabletTracking(False)
        self.f_ticket.setFrameShape(QFrame.StyledPanel)
        self.f_ticket.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.f_ticket)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_cashRegisterDeleteCurrent = QPushButton(self.f_ticket)
        self.btn_cashRegisterDeleteCurrent.setObjectName(u"btn_cashRegisterDeleteCurrent")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_cashRegisterDeleteCurrent.sizePolicy().hasHeightForWidth())
        self.btn_cashRegisterDeleteCurrent.setSizePolicy(sizePolicy7)
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.btn_cashRegisterDeleteCurrent.setFont(font3)
        self.btn_cashRegisterDeleteCurrent.setTabletTracking(False)
        icon22 = QIcon()
        icon22.addFile(u":/Simple icons/simple_icons/fi-rr-delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cashRegisterDeleteCurrent.setIcon(icon22)
        self.btn_cashRegisterDeleteCurrent.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.btn_cashRegisterDeleteCurrent)

        self.btn_cashRegisterClear = QPushButton(self.f_ticket)
        self.btn_cashRegisterClear.setObjectName(u"btn_cashRegisterClear")
        sizePolicy7.setHeightForWidth(self.btn_cashRegisterClear.sizePolicy().hasHeightForWidth())
        self.btn_cashRegisterClear.setSizePolicy(sizePolicy7)
        self.btn_cashRegisterClear.setFont(font3)
        self.btn_cashRegisterClear.setTabletTracking(False)
        icon23 = QIcon()
        icon23.addFile(u":/Simple icons/simple_icons/fi-rr-broom.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cashRegisterClear.setIcon(icon23)
        self.btn_cashRegisterClear.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.btn_cashRegisterClear)

        self.btn_cashRegisterResume = QPushButton(self.f_ticket)
        self.btn_cashRegisterResume.setObjectName(u"btn_cashRegisterResume")
        sizePolicy7.setHeightForWidth(self.btn_cashRegisterResume.sizePolicy().hasHeightForWidth())
        self.btn_cashRegisterResume.setSizePolicy(sizePolicy7)
        self.btn_cashRegisterResume.setFont(font3)
        self.btn_cashRegisterResume.setTabletTracking(False)
        icon24 = QIcon()
        icon24.addFile(u":/Simple icons/simple_icons/fi-rr-time-fast.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cashRegisterResume.setIcon(icon24)
        self.btn_cashRegisterResume.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.btn_cashRegisterResume)

        self.btn_cashRegisterHold = QPushButton(self.f_ticket)
        self.btn_cashRegisterHold.setObjectName(u"btn_cashRegisterHold")
        sizePolicy7.setHeightForWidth(self.btn_cashRegisterHold.sizePolicy().hasHeightForWidth())
        self.btn_cashRegisterHold.setSizePolicy(sizePolicy7)
        self.btn_cashRegisterHold.setFont(font3)
        self.btn_cashRegisterHold.setTabletTracking(False)
        icon25 = QIcon()
        icon25.addFile(u":/Simple icons/simple_icons/fi-rr-time-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cashRegisterHold.setIcon(icon25)
        self.btn_cashRegisterHold.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.btn_cashRegisterHold)


        self.horizontalLayout_6.addWidget(self.f_ticket)

        self.f_totalInfo = QFrame(self.f_orderNav)
        self.f_totalInfo.setObjectName(u"f_totalInfo")
        self.f_totalInfo.setTabletTracking(False)
        self.f_totalInfo.setStyleSheet(u"QLCDNumber\n"
"{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.f_totalInfo.setFrameShape(QFrame.StyledPanel)
        self.f_totalInfo.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.f_totalInfo)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.l_taxDa = QLabel(self.f_totalInfo)
        self.l_taxDa.setObjectName(u"l_taxDa")
        sizePolicy.setHeightForWidth(self.l_taxDa.sizePolicy().hasHeightForWidth())
        self.l_taxDa.setSizePolicy(sizePolicy)
        self.l_taxDa.setMaximumSize(QSize(40, 16777215))
        self.l_taxDa.setFont(font3)
        self.l_taxDa.setTabletTracking(False)
        self.l_taxDa.setFrameShadow(QFrame.Plain)
        self.l_taxDa.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l_taxDa, 1, 2, 1, 1)

        self.l_totalTtc = QLabel(self.f_totalInfo)
        self.l_totalTtc.setObjectName(u"l_totalTtc")
        sizePolicy6.setHeightForWidth(self.l_totalTtc.sizePolicy().hasHeightForWidth())
        self.l_totalTtc.setSizePolicy(sizePolicy6)
        self.l_totalTtc.setFont(font3)
        self.l_totalTtc.setTabletTracking(False)
        self.l_totalTtc.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l_totalTtc, 2, 0, 1, 1)

        self.l_da = QLabel(self.f_totalInfo)
        self.l_da.setObjectName(u"l_da")
        sizePolicy.setHeightForWidth(self.l_da.sizePolicy().hasHeightForWidth())
        self.l_da.setSizePolicy(sizePolicy)
        self.l_da.setMaximumSize(QSize(40, 16777215))
        self.l_da.setFont(font3)
        self.l_da.setTabletTracking(False)
        self.l_da.setFrameShadow(QFrame.Plain)
        self.l_da.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l_da, 0, 2, 1, 1)

        self.lcdN_totalHtt = QLCDNumber(self.f_totalInfo)
        self.lcdN_totalHtt.setObjectName(u"lcdN_totalHtt")
        sizePolicy.setHeightForWidth(self.lcdN_totalHtt.sizePolicy().hasHeightForWidth())
        self.lcdN_totalHtt.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setBold(False)
        self.lcdN_totalHtt.setFont(font4)
        self.lcdN_totalHtt.setTabletTracking(False)
        self.lcdN_totalHtt.setFrameShape(QFrame.StyledPanel)
        self.lcdN_totalHtt.setFrameShadow(QFrame.Plain)
        self.lcdN_totalHtt.setLineWidth(1)
        self.lcdN_totalHtt.setSmallDecimalPoint(True)
        self.lcdN_totalHtt.setDigitCount(7)
        self.lcdN_totalHtt.setProperty("value", 0.000000000000000)

        self.gridLayout_8.addWidget(self.lcdN_totalHtt, 0, 1, 1, 1)

        self.lcdN_tax = QLCDNumber(self.f_totalInfo)
        self.lcdN_tax.setObjectName(u"lcdN_tax")
        sizePolicy.setHeightForWidth(self.lcdN_tax.sizePolicy().hasHeightForWidth())
        self.lcdN_tax.setSizePolicy(sizePolicy)
        self.lcdN_tax.setFont(font4)
        self.lcdN_tax.setTabletTracking(False)
        self.lcdN_tax.setFrameShape(QFrame.StyledPanel)
        self.lcdN_tax.setFrameShadow(QFrame.Plain)
        self.lcdN_tax.setLineWidth(1)
        self.lcdN_tax.setSmallDecimalPoint(True)
        self.lcdN_tax.setDigitCount(7)
        self.lcdN_tax.setProperty("value", 0.000000000000000)

        self.gridLayout_8.addWidget(self.lcdN_tax, 1, 1, 1, 1)

        self.l_totalHtt = QLabel(self.f_totalInfo)
        self.l_totalHtt.setObjectName(u"l_totalHtt")
        sizePolicy6.setHeightForWidth(self.l_totalHtt.sizePolicy().hasHeightForWidth())
        self.l_totalHtt.setSizePolicy(sizePolicy6)
        self.l_totalHtt.setFont(font3)
        self.l_totalHtt.setTabletTracking(False)
        self.l_totalHtt.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l_totalHtt, 0, 0, 1, 1)

        self.lcdN_totalTtc = QLCDNumber(self.f_totalInfo)
        self.lcdN_totalTtc.setObjectName(u"lcdN_totalTtc")
        sizePolicy.setHeightForWidth(self.lcdN_totalTtc.sizePolicy().hasHeightForWidth())
        self.lcdN_totalTtc.setSizePolicy(sizePolicy)
        self.lcdN_totalTtc.setFont(font4)
        self.lcdN_totalTtc.setTabletTracking(False)
        self.lcdN_totalTtc.setFrameShape(QFrame.StyledPanel)
        self.lcdN_totalTtc.setFrameShadow(QFrame.Plain)
        self.lcdN_totalTtc.setLineWidth(1)
        self.lcdN_totalTtc.setSmallDecimalPoint(True)
        self.lcdN_totalTtc.setDigitCount(7)
        self.lcdN_totalTtc.setProperty("value", 0.000000000000000)

        self.gridLayout_8.addWidget(self.lcdN_totalTtc, 2, 1, 1, 1)

        self.l_tax = QLabel(self.f_totalInfo)
        self.l_tax.setObjectName(u"l_tax")
        sizePolicy6.setHeightForWidth(self.l_tax.sizePolicy().hasHeightForWidth())
        self.l_tax.setSizePolicy(sizePolicy6)
        self.l_tax.setFont(font3)
        self.l_tax.setTabletTracking(False)
        self.l_tax.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l_tax, 1, 0, 1, 1)

        self.l_TtcDa = QLabel(self.f_totalInfo)
        self.l_TtcDa.setObjectName(u"l_TtcDa")
        sizePolicy.setHeightForWidth(self.l_TtcDa.sizePolicy().hasHeightForWidth())
        self.l_TtcDa.setSizePolicy(sizePolicy)
        self.l_TtcDa.setMaximumSize(QSize(40, 16777215))
        self.l_TtcDa.setFont(font3)
        self.l_TtcDa.setTabletTracking(False)
        self.l_TtcDa.setFrameShadow(QFrame.Plain)
        self.l_TtcDa.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l_TtcDa, 2, 2, 1, 1)


        self.horizontalLayout_6.addWidget(self.f_totalInfo)

        self.f_cashButtons = QFrame(self.f_orderNav)
        self.f_cashButtons.setObjectName(u"f_cashButtons")
        self.f_cashButtons.setMaximumSize(QSize(50, 16777215))
        self.f_cashButtons.setTabletTracking(False)
        self.f_cashButtons.setFrameShape(QFrame.StyledPanel)
        self.f_cashButtons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.f_cashButtons)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.btn_cashRegisterReduce = QPushButton(self.f_cashButtons)
        self.btn_cashRegisterReduce.setObjectName(u"btn_cashRegisterReduce")
        sizePolicy4.setHeightForWidth(self.btn_cashRegisterReduce.sizePolicy().hasHeightForWidth())
        self.btn_cashRegisterReduce.setSizePolicy(sizePolicy4)
        self.btn_cashRegisterReduce.setMaximumSize(QSize(50, 16777215))
        self.btn_cashRegisterReduce.setTabletTracking(False)
        icon26 = QIcon()
        icon26.addFile(u":/Simple icons/simple_icons/fi-rr-smile-wink.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cashRegisterReduce.setIcon(icon26)
        self.btn_cashRegisterReduce.setIconSize(QSize(32, 32))

        self.verticalLayout_15.addWidget(self.btn_cashRegisterReduce)

        self.btn_cashRegisterTicketKitchen = QPushButton(self.f_cashButtons)
        self.btn_cashRegisterTicketKitchen.setObjectName(u"btn_cashRegisterTicketKitchen")
        sizePolicy4.setHeightForWidth(self.btn_cashRegisterTicketKitchen.sizePolicy().hasHeightForWidth())
        self.btn_cashRegisterTicketKitchen.setSizePolicy(sizePolicy4)
        self.btn_cashRegisterTicketKitchen.setMaximumSize(QSize(50, 16777215))
        self.btn_cashRegisterTicketKitchen.setTabletTracking(False)
        icon27 = QIcon()
        icon27.addFile(u":/Simple icons/simple_icons/fi-rr-room-service.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cashRegisterTicketKitchen.setIcon(icon27)
        self.btn_cashRegisterTicketKitchen.setIconSize(QSize(32, 32))

        self.verticalLayout_15.addWidget(self.btn_cashRegisterTicketKitchen)

        self.btn_cashRegisterTicket = QPushButton(self.f_cashButtons)
        self.btn_cashRegisterTicket.setObjectName(u"btn_cashRegisterTicket")
        sizePolicy4.setHeightForWidth(self.btn_cashRegisterTicket.sizePolicy().hasHeightForWidth())
        self.btn_cashRegisterTicket.setSizePolicy(sizePolicy4)
        self.btn_cashRegisterTicket.setMaximumSize(QSize(50, 16777215))
        self.btn_cashRegisterTicket.setTabletTracking(False)
        self.btn_cashRegisterTicket.setIcon(icon14)
        self.btn_cashRegisterTicket.setIconSize(QSize(32, 32))

        self.verticalLayout_15.addWidget(self.btn_cashRegisterTicket)

        self.btn_cashRegisterPay = QPushButton(self.f_cashButtons)
        self.btn_cashRegisterPay.setObjectName(u"btn_cashRegisterPay")
        sizePolicy4.setHeightForWidth(self.btn_cashRegisterPay.sizePolicy().hasHeightForWidth())
        self.btn_cashRegisterPay.setSizePolicy(sizePolicy4)
        self.btn_cashRegisterPay.setMaximumSize(QSize(50, 16777215))
        self.btn_cashRegisterPay.setTabletTracking(False)
        icon28 = QIcon()
        icon28.addFile(u":/Simple icons/simple_icons/fi-rr-dollar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cashRegisterPay.setIcon(icon28)
        self.btn_cashRegisterPay.setIconSize(QSize(32, 32))

        self.verticalLayout_15.addWidget(self.btn_cashRegisterPay)


        self.horizontalLayout_6.addWidget(self.f_cashButtons)


        self.verticalLayout_9.addWidget(self.f_orderNav)

        self.f_orderWorker = QFrame(self.f_cashCommand)
        self.f_orderWorker.setObjectName(u"f_orderWorker")
        self.f_orderWorker.setTabletTracking(False)
        self.f_orderWorker.setFrameShape(QFrame.StyledPanel)
        self.f_orderWorker.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.f_orderWorker)
        self.horizontalLayout_63.setSpacing(5)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.l_orderWorker = QLabel(self.f_orderWorker)
        self.l_orderWorker.setObjectName(u"l_orderWorker")
        sizePolicy6.setHeightForWidth(self.l_orderWorker.sizePolicy().hasHeightForWidth())
        self.l_orderWorker.setSizePolicy(sizePolicy6)
        self.l_orderWorker.setFont(font3)
        self.l_orderWorker.setTabletTracking(False)

        self.horizontalLayout_63.addWidget(self.l_orderWorker)

        self.cb_orderWorker = QComboBox(self.f_orderWorker)
        self.cb_orderWorker.setObjectName(u"cb_orderWorker")
        self.cb_orderWorker.setEnabled(False)
        self.cb_orderWorker.setTabletTracking(False)

        self.horizontalLayout_63.addWidget(self.cb_orderWorker)


        self.verticalLayout_9.addWidget(self.f_orderWorker)


        self.verticalLayout_7.addWidget(self.f_cashCommand)

        self.f_orderCustomer = QFrame(self.f_orderDashboard)
        self.f_orderCustomer.setObjectName(u"f_orderCustomer")
        self.f_orderCustomer.setTabletTracking(False)
        self.f_orderCustomer.setFrameShape(QFrame.StyledPanel)
        self.f_orderCustomer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.f_orderCustomer)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.l_orderCustomer = QLabel(self.f_orderCustomer)
        self.l_orderCustomer.setObjectName(u"l_orderCustomer")
        sizePolicy6.setHeightForWidth(self.l_orderCustomer.sizePolicy().hasHeightForWidth())
        self.l_orderCustomer.setSizePolicy(sizePolicy6)
        self.l_orderCustomer.setFont(font3)
        self.l_orderCustomer.setTabletTracking(False)

        self.horizontalLayout_7.addWidget(self.l_orderCustomer)

        self.cb_orderCustomer = QComboBox(self.f_orderCustomer)
        self.cb_orderCustomer.setObjectName(u"cb_orderCustomer")
        self.cb_orderCustomer.setTabletTracking(False)

        self.horizontalLayout_7.addWidget(self.cb_orderCustomer)


        self.verticalLayout_7.addWidget(self.f_orderCustomer)

        self.tw_orderList = QTableWidget(self.f_orderDashboard)
        self.tw_orderList.setObjectName(u"tw_orderList")
        self.tw_orderList.setMinimumSize(QSize(0, 0))
        self.tw_orderList.setTabletTracking(False)
        self.tw_orderList.setLayoutDirection(Qt.LeftToRight)
        self.tw_orderList.setFrameShape(QFrame.StyledPanel)
        self.tw_orderList.setFrameShadow(QFrame.Sunken)
        self.tw_orderList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_orderList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_orderList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_orderList.setTextElideMode(Qt.ElideMiddle)
        self.tw_orderList.setSortingEnabled(True)
        self.tw_orderList.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_7.addWidget(self.tw_orderList)

        self.groupBox_2 = QGroupBox(self.f_orderDashboard)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        font5 = QFont()
        font5.setPointSize(14)
        self.groupBox_2.setFont(font5)
        self.groupBox_2.setTabletTracking(False)
        self.verticalLayout_50 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.le_cashRegisterComment = QTextEdit(self.groupBox_2)
        self.le_cashRegisterComment.setObjectName(u"le_cashRegisterComment")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.le_cashRegisterComment.sizePolicy().hasHeightForWidth())
        self.le_cashRegisterComment.setSizePolicy(sizePolicy8)
        self.le_cashRegisterComment.setMaximumSize(QSize(16777215, 100))
        font6 = QFont()
        font6.setPointSize(12)
        self.le_cashRegisterComment.setFont(font6)
        self.le_cashRegisterComment.setTabletTracking(False)

        self.verticalLayout_50.addWidget(self.le_cashRegisterComment)


        self.verticalLayout_7.addWidget(self.groupBox_2)


        self.gridLayout_5.addWidget(self.f_orderDashboard, 0, 1, 1, 1)

        self.f_foodMenu = QFrame(self.page_cashRegister)
        self.f_foodMenu.setObjectName(u"f_foodMenu")
        self.f_foodMenu.setTabletTracking(False)
        self.f_foodMenu.setFrameShape(QFrame.StyledPanel)
        self.f_foodMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.f_foodMenu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tw_foodMenu = QTabWidget(self.f_foodMenu)
        self.tw_foodMenu.setObjectName(u"tw_foodMenu")
        sizePolicy4.setHeightForWidth(self.tw_foodMenu.sizePolicy().hasHeightForWidth())
        self.tw_foodMenu.setSizePolicy(sizePolicy4)
        self.tw_foodMenu.setMinimumSize(QSize(400, 0))
        font7 = QFont()
        font7.setPointSize(16)
        self.tw_foodMenu.setFont(font7)
        self.tw_foodMenu.setMouseTracking(True)
        self.tw_foodMenu.setTabletTracking(True)
        self.tw_foodMenu.setStyleSheet(u"")
        self.tw_foodMenu.setIconSize(QSize(64, 64))
        self.tab_salade = QWidget()
        self.tab_salade.setObjectName(u"tab_salade")
        self.gridLayout_12 = QGridLayout(self.tab_salade)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.sa_salade = QScrollArea(self.tab_salade)
        self.sa_salade.setObjectName(u"sa_salade")
        self.sa_salade.setTabletTracking(False)
        self.sa_salade.setWidgetResizable(True)
        self.w_salade = QWidget()
        self.w_salade.setObjectName(u"w_salade")
        self.w_salade.setGeometry(QRect(0, 0, 374, 617))
        self.gridLayout_13 = QGridLayout(self.w_salade)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_7 = QFrame(self.w_salade)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(200, 200))
        self.frame_7.setTabletTracking(False)
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.verticalLayout_57 = QVBoxLayout(self.frame_7)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(200, 200))
        self.label_15.setTabletTracking(False)
        self.label_15.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_15.setScaledContents(True)

        self.verticalLayout_57.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setTabletTracking(False)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_57.addWidget(self.label_16)

        self.frame_15 = QFrame(self.frame_7)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(200, 100))
        self.frame_15.setTabletTracking(False)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_34.setSpacing(5)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.pushButton_38 = QPushButton(self.frame_15)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setTabletTracking(False)

        self.horizontalLayout_34.addWidget(self.pushButton_38)

        self.pushButton_39 = QPushButton(self.frame_15)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setTabletTracking(False)

        self.horizontalLayout_34.addWidget(self.pushButton_39)


        self.verticalLayout_57.addWidget(self.frame_15)


        self.gridLayout_13.addWidget(self.frame_7, 0, 0, 1, 1)

        self.frame_16 = QFrame(self.w_salade)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(200, 200))
        self.frame_16.setTabletTracking(False)
        self.frame_16.setFrameShape(QFrame.Box)
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.verticalLayout_58 = QVBoxLayout(self.frame_16)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.label_17 = QLabel(self.frame_16)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(200, 200))
        self.label_17.setTabletTracking(False)
        self.label_17.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_17.setScaledContents(True)

        self.verticalLayout_58.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_16)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setTabletTracking(False)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_58.addWidget(self.label_18)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(200, 100))
        self.frame_17.setTabletTracking(False)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_35.setSpacing(5)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.pushButton_40 = QPushButton(self.frame_17)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setTabletTracking(False)

        self.horizontalLayout_35.addWidget(self.pushButton_40)

        self.pushButton_41 = QPushButton(self.frame_17)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setTabletTracking(False)

        self.horizontalLayout_35.addWidget(self.pushButton_41)


        self.verticalLayout_58.addWidget(self.frame_17)


        self.gridLayout_13.addWidget(self.frame_16, 0, 2, 1, 1)

        self.frame_39 = QFrame(self.w_salade)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMaximumSize(QSize(200, 200))
        self.frame_39.setTabletTracking(False)
        self.frame_39.setFrameShape(QFrame.Box)
        self.frame_39.setFrameShadow(QFrame.Plain)
        self.verticalLayout_91 = QVBoxLayout(self.frame_39)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.label_32 = QLabel(self.frame_39)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(200, 200))
        self.label_32.setTabletTracking(False)
        self.label_32.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_32.setScaledContents(True)

        self.verticalLayout_91.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_39)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setTabletTracking(False)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_91.addWidget(self.label_33)

        self.frame_42 = QFrame(self.frame_39)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(200, 100))
        self.frame_42.setTabletTracking(False)
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_68.setSpacing(5)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.pushButton_56 = QPushButton(self.frame_42)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setTabletTracking(False)

        self.horizontalLayout_68.addWidget(self.pushButton_56)

        self.pushButton_57 = QPushButton(self.frame_42)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setTabletTracking(False)

        self.horizontalLayout_68.addWidget(self.pushButton_57)


        self.verticalLayout_91.addWidget(self.frame_42)


        self.gridLayout_13.addWidget(self.frame_39, 0, 1, 1, 1)

        self.sa_salade.setWidget(self.w_salade)

        self.gridLayout_12.addWidget(self.sa_salade, 0, 0, 1, 1)

        icon29 = QIcon()
        icon29.addFile(u":/Simple icons/simple_icons/fi-rr-salad.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_foodMenu.addTab(self.tab_salade, icon29, "")
        self.tab_meal = QWidget()
        self.tab_meal.setObjectName(u"tab_meal")
        self.verticalLayout_10 = QVBoxLayout(self.tab_meal)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.sa_meal = QScrollArea(self.tab_meal)
        self.sa_meal.setObjectName(u"sa_meal")
        self.sa_meal.setWidgetResizable(True)
        self.w_meal = QWidget()
        self.w_meal.setObjectName(u"w_meal")
        self.w_meal.setGeometry(QRect(0, 0, 374, 617))
        self.gridLayout_6 = QGridLayout(self.w_meal)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_18 = QFrame(self.w_meal)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(200, 200))
        self.frame_18.setFrameShape(QFrame.Box)
        self.frame_18.setFrameShadow(QFrame.Plain)
        self.verticalLayout_59 = QVBoxLayout(self.frame_18)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.label_19 = QLabel(self.frame_18)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(200, 200))
        self.label_19.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_19.setScaledContents(True)

        self.verticalLayout_59.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_59.addWidget(self.label_20)

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(200, 100))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_36.setSpacing(5)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.pushButton_42 = QPushButton(self.frame_19)
        self.pushButton_42.setObjectName(u"pushButton_42")

        self.horizontalLayout_36.addWidget(self.pushButton_42)

        self.pushButton_43 = QPushButton(self.frame_19)
        self.pushButton_43.setObjectName(u"pushButton_43")

        self.horizontalLayout_36.addWidget(self.pushButton_43)


        self.verticalLayout_59.addWidget(self.frame_19)


        self.gridLayout_6.addWidget(self.frame_18, 0, 0, 1, 1)

        self.frame_20 = QFrame(self.w_meal)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(200, 200))
        self.frame_20.setFrameShape(QFrame.Box)
        self.frame_20.setFrameShadow(QFrame.Plain)
        self.verticalLayout_60 = QVBoxLayout(self.frame_20)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_21 = QLabel(self.frame_20)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(200, 200))
        self.label_21.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_21.setScaledContents(True)

        self.verticalLayout_60.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_20)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_60.addWidget(self.label_22)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(200, 100))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_37.setSpacing(5)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.pushButton_44 = QPushButton(self.frame_21)
        self.pushButton_44.setObjectName(u"pushButton_44")

        self.horizontalLayout_37.addWidget(self.pushButton_44)

        self.pushButton_45 = QPushButton(self.frame_21)
        self.pushButton_45.setObjectName(u"pushButton_45")

        self.horizontalLayout_37.addWidget(self.pushButton_45)


        self.verticalLayout_60.addWidget(self.frame_21)


        self.gridLayout_6.addWidget(self.frame_20, 0, 1, 1, 1)

        self.frame_41 = QFrame(self.w_meal)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(200, 200))
        self.frame_41.setFrameShape(QFrame.Box)
        self.frame_41.setFrameShadow(QFrame.Plain)
        self.verticalLayout_90 = QVBoxLayout(self.frame_41)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.label_29 = QLabel(self.frame_41)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(200, 200))
        self.label_29.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_29.setScaledContents(True)

        self.verticalLayout_90.addWidget(self.label_29)

        self.label_31 = QLabel(self.frame_41)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_90.addWidget(self.label_31)

        self.frame_44 = QFrame(self.frame_41)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMaximumSize(QSize(200, 100))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_65.setSpacing(5)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.pushButton_54 = QPushButton(self.frame_44)
        self.pushButton_54.setObjectName(u"pushButton_54")

        self.horizontalLayout_65.addWidget(self.pushButton_54)

        self.pushButton_55 = QPushButton(self.frame_44)
        self.pushButton_55.setObjectName(u"pushButton_55")

        self.horizontalLayout_65.addWidget(self.pushButton_55)


        self.verticalLayout_90.addWidget(self.frame_44)


        self.gridLayout_6.addWidget(self.frame_41, 0, 2, 1, 1)

        self.sa_meal.setWidget(self.w_meal)

        self.verticalLayout_10.addWidget(self.sa_meal)

        icon30 = QIcon()
        icon30.addFile(u":/Simple icons/simple_icons/fi-rr-utensils.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_foodMenu.addTab(self.tab_meal, icon30, "")
        self.tab_pizza = QWidget()
        self.tab_pizza.setObjectName(u"tab_pizza")
        self.verticalLayout_11 = QVBoxLayout(self.tab_pizza)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.sa_pizza = QScrollArea(self.tab_pizza)
        self.sa_pizza.setObjectName(u"sa_pizza")
        self.sa_pizza.setWidgetResizable(True)
        self.w_pizza = QWidget()
        self.w_pizza.setObjectName(u"w_pizza")
        self.w_pizza.setGeometry(QRect(0, 0, 374, 617))
        self.gridLayout_7 = QGridLayout(self.w_pizza)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame = QFrame(self.w_pizza)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(200, 200))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_43 = QVBoxLayout(self.frame)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 200))
        self.label.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_43.addWidget(self.label)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_5)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(200, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_25.addWidget(self.pushButton_4)

        self.pushButton_14 = QPushButton(self.frame_2)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_25.addWidget(self.pushButton_14)


        self.verticalLayout_43.addWidget(self.frame_2)


        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.w_pizza)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(200, 200))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout_44 = QVBoxLayout(self.frame_3)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 200))
        self.label_2.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_44.addWidget(self.label_2)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.label_6)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(200, 100))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.pushButton_15 = QPushButton(self.frame_4)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_26.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.frame_4)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_26.addWidget(self.pushButton_16)


        self.verticalLayout_44.addWidget(self.frame_4)


        self.gridLayout_7.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_48 = QFrame(self.w_pizza)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMaximumSize(QSize(200, 200))
        self.frame_48.setFrameShape(QFrame.Box)
        self.frame_48.setFrameShadow(QFrame.Plain)
        self.verticalLayout_92 = QVBoxLayout(self.frame_48)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.label_3 = QLabel(self.frame_48)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(200, 200))
        self.label_3.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_92.addWidget(self.label_3)

        self.label_7 = QLabel(self.frame_48)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_92.addWidget(self.label_7)

        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMaximumSize(QSize(200, 100))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_69.setSpacing(5)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.pushButton_17 = QPushButton(self.frame_49)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_69.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.frame_49)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_69.addWidget(self.pushButton_18)


        self.verticalLayout_92.addWidget(self.frame_49)


        self.gridLayout_7.addWidget(self.frame_48, 0, 2, 1, 1)

        self.sa_pizza.setWidget(self.w_pizza)

        self.verticalLayout_11.addWidget(self.sa_pizza)

        icon31 = QIcon()
        icon31.addFile(u":/Simple icons/simple_icons/fi-rr-pizza-slice.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_foodMenu.addTab(self.tab_pizza, icon31, "")
        self.tab_coldDrink = QWidget()
        self.tab_coldDrink.setObjectName(u"tab_coldDrink")
        self.verticalLayout_12 = QVBoxLayout(self.tab_coldDrink)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.sa_coldDrink = QScrollArea(self.tab_coldDrink)
        self.sa_coldDrink.setObjectName(u"sa_coldDrink")
        self.sa_coldDrink.setWidgetResizable(True)
        self.w_coldDrink = QWidget()
        self.w_coldDrink.setObjectName(u"w_coldDrink")
        self.w_coldDrink.setGeometry(QRect(0, 0, 374, 617))
        self.gridLayout_11 = QGridLayout(self.w_coldDrink)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_24 = QFrame(self.w_coldDrink)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(200, 200))
        self.frame_24.setFrameShape(QFrame.Box)
        self.frame_24.setFrameShadow(QFrame.Plain)
        self.verticalLayout_62 = QVBoxLayout(self.frame_24)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.label_25 = QLabel(self.frame_24)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(200, 200))
        self.label_25.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_25.setScaledContents(True)

        self.verticalLayout_62.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_24)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.label_26)

        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(200, 100))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_39.setSpacing(5)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.pushButton_48 = QPushButton(self.frame_25)
        self.pushButton_48.setObjectName(u"pushButton_48")

        self.horizontalLayout_39.addWidget(self.pushButton_48)

        self.pushButton_49 = QPushButton(self.frame_25)
        self.pushButton_49.setObjectName(u"pushButton_49")

        self.horizontalLayout_39.addWidget(self.pushButton_49)


        self.verticalLayout_62.addWidget(self.frame_25)


        self.gridLayout_11.addWidget(self.frame_24, 0, 1, 1, 1)

        self.frame_22 = QFrame(self.w_coldDrink)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(200, 200))
        self.frame_22.setFrameShape(QFrame.Box)
        self.frame_22.setFrameShadow(QFrame.Plain)
        self.verticalLayout_61 = QVBoxLayout(self.frame_22)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.label_23 = QLabel(self.frame_22)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(200, 200))
        self.label_23.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_23.setScaledContents(True)

        self.verticalLayout_61.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_22)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_61.addWidget(self.label_24)

        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(200, 100))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.pushButton_46 = QPushButton(self.frame_23)
        self.pushButton_46.setObjectName(u"pushButton_46")

        self.horizontalLayout_38.addWidget(self.pushButton_46)

        self.pushButton_47 = QPushButton(self.frame_23)
        self.pushButton_47.setObjectName(u"pushButton_47")

        self.horizontalLayout_38.addWidget(self.pushButton_47)


        self.verticalLayout_61.addWidget(self.frame_23)


        self.gridLayout_11.addWidget(self.frame_22, 0, 0, 1, 1)

        self.frame_50 = QFrame(self.w_coldDrink)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(200, 200))
        self.frame_50.setFrameShape(QFrame.Box)
        self.frame_50.setFrameShadow(QFrame.Plain)
        self.verticalLayout_95 = QVBoxLayout(self.frame_50)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.label_34 = QLabel(self.frame_50)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(200, 200))
        self.label_34.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_34.setScaledContents(True)

        self.verticalLayout_95.addWidget(self.label_34)

        self.label_41 = QLabel(self.frame_50)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_95.addWidget(self.label_41)

        self.frame_51 = QFrame(self.frame_50)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMaximumSize(QSize(200, 100))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_72.setSpacing(5)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.pushButton_64 = QPushButton(self.frame_51)
        self.pushButton_64.setObjectName(u"pushButton_64")

        self.horizontalLayout_72.addWidget(self.pushButton_64)

        self.pushButton_65 = QPushButton(self.frame_51)
        self.pushButton_65.setObjectName(u"pushButton_65")

        self.horizontalLayout_72.addWidget(self.pushButton_65)


        self.verticalLayout_95.addWidget(self.frame_51)


        self.gridLayout_11.addWidget(self.frame_50, 0, 2, 1, 1)

        self.sa_coldDrink.setWidget(self.w_coldDrink)

        self.verticalLayout_12.addWidget(self.sa_coldDrink)

        icon32 = QIcon()
        icon32.addFile(u":/Simple icons/simple_icons/fi-rr-drink-alt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_foodMenu.addTab(self.tab_coldDrink, icon32, "")
        self.tab_hotDrink = QWidget()
        self.tab_hotDrink.setObjectName(u"tab_hotDrink")
        self.verticalLayout_13 = QVBoxLayout(self.tab_hotDrink)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sa_hotDrink = QScrollArea(self.tab_hotDrink)
        self.sa_hotDrink.setObjectName(u"sa_hotDrink")
        self.sa_hotDrink.setWidgetResizable(True)
        self.w_hotDrink = QWidget()
        self.w_hotDrink.setObjectName(u"w_hotDrink")
        self.w_hotDrink.setGeometry(QRect(0, 0, 374, 617))
        self.gridLayout_16 = QGridLayout(self.w_hotDrink)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_28 = QFrame(self.w_hotDrink)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(200, 200))
        self.frame_28.setFrameShape(QFrame.Box)
        self.frame_28.setFrameShadow(QFrame.Plain)
        self.verticalLayout_67 = QVBoxLayout(self.frame_28)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_35 = QLabel(self.frame_28)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(200, 200))
        self.label_35.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_35.setScaledContents(True)

        self.verticalLayout_67.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_28)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.label_36)

        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(200, 100))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_44.setSpacing(5)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.pushButton_58 = QPushButton(self.frame_30)
        self.pushButton_58.setObjectName(u"pushButton_58")

        self.horizontalLayout_44.addWidget(self.pushButton_58)

        self.pushButton_59 = QPushButton(self.frame_30)
        self.pushButton_59.setObjectName(u"pushButton_59")

        self.horizontalLayout_44.addWidget(self.pushButton_59)


        self.verticalLayout_67.addWidget(self.frame_30)


        self.gridLayout_16.addWidget(self.frame_28, 0, 1, 1, 1)

        self.frame_26 = QFrame(self.w_hotDrink)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(200, 200))
        self.frame_26.setFrameShape(QFrame.Box)
        self.frame_26.setFrameShadow(QFrame.Plain)
        self.verticalLayout_63 = QVBoxLayout(self.frame_26)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.label_27 = QLabel(self.frame_26)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(200, 200))
        self.label_27.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_27.setScaledContents(True)

        self.verticalLayout_63.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_26)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_63.addWidget(self.label_28)

        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(200, 100))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_40.setSpacing(5)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.pushButton_50 = QPushButton(self.frame_27)
        self.pushButton_50.setObjectName(u"pushButton_50")

        self.horizontalLayout_40.addWidget(self.pushButton_50)

        self.pushButton_51 = QPushButton(self.frame_27)
        self.pushButton_51.setObjectName(u"pushButton_51")

        self.horizontalLayout_40.addWidget(self.pushButton_51)


        self.verticalLayout_63.addWidget(self.frame_27)


        self.gridLayout_16.addWidget(self.frame_26, 0, 0, 1, 1)

        self.frame_52 = QFrame(self.w_hotDrink)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(200, 200))
        self.frame_52.setFrameShape(QFrame.Box)
        self.frame_52.setFrameShadow(QFrame.Plain)
        self.verticalLayout_96 = QVBoxLayout(self.frame_52)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.label_44 = QLabel(self.frame_52)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(200, 200))
        self.label_44.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_44.setScaledContents(True)

        self.verticalLayout_96.addWidget(self.label_44)

        self.label_45 = QLabel(self.frame_52)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_96.addWidget(self.label_45)

        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(200, 100))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_73.setSpacing(5)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.pushButton_70 = QPushButton(self.frame_53)
        self.pushButton_70.setObjectName(u"pushButton_70")

        self.horizontalLayout_73.addWidget(self.pushButton_70)

        self.pushButton_71 = QPushButton(self.frame_53)
        self.pushButton_71.setObjectName(u"pushButton_71")

        self.horizontalLayout_73.addWidget(self.pushButton_71)


        self.verticalLayout_96.addWidget(self.frame_53)


        self.gridLayout_16.addWidget(self.frame_52, 0, 2, 1, 1)

        self.sa_hotDrink.setWidget(self.w_hotDrink)

        self.verticalLayout_13.addWidget(self.sa_hotDrink)

        icon33 = QIcon()
        icon33.addFile(u":/Simple icons/simple_icons/fi-rr-coffee.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_foodMenu.addTab(self.tab_hotDrink, icon33, "")
        self.tab_dessert = QWidget()
        self.tab_dessert.setObjectName(u"tab_dessert")
        self.verticalLayout_14 = QVBoxLayout(self.tab_dessert)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.sa_dessert = QScrollArea(self.tab_dessert)
        self.sa_dessert.setObjectName(u"sa_dessert")
        self.sa_dessert.setWidgetResizable(True)
        self.w_dessert = QWidget()
        self.w_dessert.setObjectName(u"w_dessert")
        self.w_dessert.setGeometry(QRect(0, 0, 374, 617))
        self.gridLayout_17 = QGridLayout(self.w_dessert)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_36 = QFrame(self.w_dessert)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(200, 200))
        self.frame_36.setFrameShape(QFrame.Box)
        self.frame_36.setFrameShadow(QFrame.Plain)
        self.verticalLayout_69 = QVBoxLayout(self.frame_36)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.label_39 = QLabel(self.frame_36)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(200, 200))
        self.label_39.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_39.setScaledContents(True)

        self.verticalLayout_69.addWidget(self.label_39)

        self.label_40 = QLabel(self.frame_36)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.label_40)

        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(200, 100))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_46.setSpacing(5)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.pushButton_62 = QPushButton(self.frame_37)
        self.pushButton_62.setObjectName(u"pushButton_62")

        self.horizontalLayout_46.addWidget(self.pushButton_62)

        self.pushButton_63 = QPushButton(self.frame_37)
        self.pushButton_63.setObjectName(u"pushButton_63")

        self.horizontalLayout_46.addWidget(self.pushButton_63)


        self.verticalLayout_69.addWidget(self.frame_37)


        self.gridLayout_17.addWidget(self.frame_36, 0, 1, 1, 1)

        self.frame_34 = QFrame(self.w_dessert)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(200, 200))
        self.frame_34.setFrameShape(QFrame.Box)
        self.frame_34.setFrameShadow(QFrame.Plain)
        self.verticalLayout_68 = QVBoxLayout(self.frame_34)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_37 = QLabel(self.frame_34)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(200, 200))
        self.label_37.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_37.setScaledContents(True)

        self.verticalLayout_68.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_34)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_68.addWidget(self.label_38)

        self.comboBox = QComboBox(self.frame_34)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_68.addWidget(self.comboBox)

        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(200, 100))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_45.setSpacing(5)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.pushButton_60 = QPushButton(self.frame_35)
        self.pushButton_60.setObjectName(u"pushButton_60")

        self.horizontalLayout_45.addWidget(self.pushButton_60)

        self.pushButton_61 = QPushButton(self.frame_35)
        self.pushButton_61.setObjectName(u"pushButton_61")

        self.horizontalLayout_45.addWidget(self.pushButton_61)


        self.verticalLayout_68.addWidget(self.frame_35)


        self.gridLayout_17.addWidget(self.frame_34, 0, 0, 1, 1)

        self.frame_54 = QFrame(self.w_dessert)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(200, 200))
        self.frame_54.setFrameShape(QFrame.Box)
        self.frame_54.setFrameShadow(QFrame.Plain)
        self.verticalLayout_97 = QVBoxLayout(self.frame_54)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.label_46 = QLabel(self.frame_54)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(200, 200))
        self.label_46.setPixmap(QPixmap(u":/Tab/menu.png"))
        self.label_46.setScaledContents(True)

        self.verticalLayout_97.addWidget(self.label_46)

        self.label_47 = QLabel(self.frame_54)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout_97.addWidget(self.label_47)

        self.frame_55 = QFrame(self.frame_54)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMaximumSize(QSize(200, 100))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_74.setSpacing(5)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.pushButton_72 = QPushButton(self.frame_55)
        self.pushButton_72.setObjectName(u"pushButton_72")

        self.horizontalLayout_74.addWidget(self.pushButton_72)

        self.pushButton_73 = QPushButton(self.frame_55)
        self.pushButton_73.setObjectName(u"pushButton_73")

        self.horizontalLayout_74.addWidget(self.pushButton_73)


        self.verticalLayout_97.addWidget(self.frame_55)


        self.gridLayout_17.addWidget(self.frame_54, 0, 2, 1, 1)

        self.sa_dessert.setWidget(self.w_dessert)

        self.verticalLayout_14.addWidget(self.sa_dessert)

        icon34 = QIcon()
        icon34.addFile(u":/Simple icons/simple_icons/fi-rr-cake-birthday.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_foodMenu.addTab(self.tab_dessert, icon34, "")

        self.verticalLayout_6.addWidget(self.tw_foodMenu)


        self.gridLayout_5.addWidget(self.f_foodMenu, 0, 0, 1, 1)

        self.sw_content.addWidget(self.page_cashRegister)
        self.page_reservation = QWidget()
        self.page_reservation.setObjectName(u"page_reservation")
        self.horizontalLayout_51 = QHBoxLayout(self.page_reservation)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.f_reservationInputs = QFrame(self.page_reservation)
        self.f_reservationInputs.setObjectName(u"f_reservationInputs")
        self.f_reservationInputs.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_reservationInputs.setFrameShape(QFrame.StyledPanel)
        self.f_reservationInputs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.f_reservationInputs)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.gb_reservation = QGroupBox(self.f_reservationInputs)
        self.gb_reservation.setObjectName(u"gb_reservation")
        self.gb_reservation.setFont(font3)
        self.gb_reservation.setStyleSheet(u"")
        self.verticalLayout_73 = QVBoxLayout(self.gb_reservation)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.le_reservationName = QLineEdit(self.gb_reservation)
        self.le_reservationName.setObjectName(u"le_reservationName")
        self.le_reservationName.setMaxLength(20)
        self.le_reservationName.setClearButtonEnabled(True)

        self.verticalLayout_73.addWidget(self.le_reservationName)

        self.le_reservationPhone = QLineEdit(self.gb_reservation)
        self.le_reservationPhone.setObjectName(u"le_reservationPhone")
        self.le_reservationPhone.setMaxLength(30)
        self.le_reservationPhone.setClearButtonEnabled(True)

        self.verticalLayout_73.addWidget(self.le_reservationPhone)

        self.le_reservationNbPerson = QLineEdit(self.gb_reservation)
        self.le_reservationNbPerson.setObjectName(u"le_reservationNbPerson")
        self.le_reservationNbPerson.setMaxLength(20)
        self.le_reservationNbPerson.setClearButtonEnabled(True)

        self.verticalLayout_73.addWidget(self.le_reservationNbPerson)

        self.dte_reservation = QDateTimeEdit(self.gb_reservation)
        self.dte_reservation.setObjectName(u"dte_reservation")
        self.dte_reservation.setFont(font5)
        self.dte_reservation.setCurrentSection(QDateTimeEdit.YearSection)
        self.dte_reservation.setCalendarPopup(True)

        self.verticalLayout_73.addWidget(self.dte_reservation)

        self.tw_reservationTable = QTableWidget(self.gb_reservation)
        self.tw_reservationTable.setObjectName(u"tw_reservationTable")
        font8 = QFont()
        font8.setFamilies([u"Times New Roman"])
        font8.setPointSize(18)
        font8.setBold(False)
        font8.setItalic(False)
        self.tw_reservationTable.setFont(font8)
        self.tw_reservationTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_reservationTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_reservationTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_reservationTable.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_reservationTable.verticalHeader().setCascadingSectionResizes(True)
        self.tw_reservationTable.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_73.addWidget(self.tw_reservationTable)


        self.verticalLayout_72.addWidget(self.gb_reservation)

        self.f_expenseDbBtn_5 = QFrame(self.f_reservationInputs)
        self.f_expenseDbBtn_5.setObjectName(u"f_expenseDbBtn_5")
        sizePolicy1.setHeightForWidth(self.f_expenseDbBtn_5.sizePolicy().hasHeightForWidth())
        self.f_expenseDbBtn_5.setSizePolicy(sizePolicy1)
        self.f_expenseDbBtn_5.setFrameShape(QFrame.StyledPanel)
        self.f_expenseDbBtn_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.f_expenseDbBtn_5)
        self.horizontalLayout_50.setSpacing(5)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.btn_reservationAdd = QPushButton(self.f_expenseDbBtn_5)
        self.btn_reservationAdd.setObjectName(u"btn_reservationAdd")
        icon35 = QIcon()
        icon35.addFile(u":/Simple icons/simple_icons/fi-rr-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reservationAdd.setIcon(icon35)
        self.btn_reservationAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_50.addWidget(self.btn_reservationAdd)

        self.btn_reservationEdit = QPushButton(self.f_expenseDbBtn_5)
        self.btn_reservationEdit.setObjectName(u"btn_reservationEdit")
        self.btn_reservationEdit.setEnabled(False)
        icon36 = QIcon()
        icon36.addFile(u":/Simple icons/simple_icons/fi-rr-edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reservationEdit.setIcon(icon36)
        self.btn_reservationEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_50.addWidget(self.btn_reservationEdit)

        self.btn_reservationDelete = QPushButton(self.f_expenseDbBtn_5)
        self.btn_reservationDelete.setObjectName(u"btn_reservationDelete")
        self.btn_reservationDelete.setEnabled(False)
        self.btn_reservationDelete.setIcon(icon22)
        self.btn_reservationDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_50.addWidget(self.btn_reservationDelete)

        self.btn_reservationClear = QPushButton(self.f_expenseDbBtn_5)
        self.btn_reservationClear.setObjectName(u"btn_reservationClear")
        self.btn_reservationClear.setEnabled(True)
        self.btn_reservationClear.setIcon(icon23)
        self.btn_reservationClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_50.addWidget(self.btn_reservationClear)


        self.verticalLayout_72.addWidget(self.f_expenseDbBtn_5)


        self.horizontalLayout_51.addWidget(self.f_reservationInputs)

        self.f_reservationDb = QFrame(self.page_reservation)
        self.f_reservationDb.setObjectName(u"f_reservationDb")
        self.f_reservationDb.setStyleSheet(u"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.f_reservationDb.setFrameShape(QFrame.StyledPanel)
        self.f_reservationDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.f_reservationDb)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.frame_10 = QFrame(self.f_reservationDb)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.cb_reservationSearchType = QComboBox(self.frame_10)
        self.cb_reservationSearchType.addItem("")
        self.cb_reservationSearchType.addItem("")
        self.cb_reservationSearchType.setObjectName(u"cb_reservationSearchType")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.cb_reservationSearchType.sizePolicy().hasHeightForWidth())
        self.cb_reservationSearchType.setSizePolicy(sizePolicy9)

        self.horizontalLayout_52.addWidget(self.cb_reservationSearchType)

        self.le_reservationSearch = QLineEdit(self.frame_10)
        self.le_reservationSearch.setObjectName(u"le_reservationSearch")
        sizePolicy9.setHeightForWidth(self.le_reservationSearch.sizePolicy().hasHeightForWidth())
        self.le_reservationSearch.setSizePolicy(sizePolicy9)
        self.le_reservationSearch.setClearButtonEnabled(True)

        self.horizontalLayout_52.addWidget(self.le_reservationSearch)

        self.btn_reservationSearch = QPushButton(self.frame_10)
        self.btn_reservationSearch.setObjectName(u"btn_reservationSearch")
        icon37 = QIcon()
        icon37.addFile(u":/Simple icons/simple_icons/fi-rr-search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reservationSearch.setIcon(icon37)

        self.horizontalLayout_52.addWidget(self.btn_reservationSearch)


        self.verticalLayout_71.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.f_reservationDb)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.cb_reservationDate = QCheckBox(self.frame_11)
        self.cb_reservationDate.setObjectName(u"cb_reservationDate")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.cb_reservationDate.sizePolicy().hasHeightForWidth())
        self.cb_reservationDate.setSizePolicy(sizePolicy10)
        self.cb_reservationDate.setFont(font6)

        self.horizontalLayout_53.addWidget(self.cb_reservationDate)

        self.de_reservationSearchDate = QDateEdit(self.frame_11)
        self.de_reservationSearchDate.setObjectName(u"de_reservationSearchDate")
        self.de_reservationSearchDate.setEnabled(False)
        self.de_reservationSearchDate.setFont(font5)
        self.de_reservationSearchDate.setAlignment(Qt.AlignCenter)
        self.de_reservationSearchDate.setProperty("showGroupSeparator", False)
        self.de_reservationSearchDate.setCurrentSection(QDateTimeEdit.YearSection)
        self.de_reservationSearchDate.setCalendarPopup(True)

        self.horizontalLayout_53.addWidget(self.de_reservationSearchDate)


        self.verticalLayout_71.addWidget(self.frame_11)

        self.tw_reservation = QTableWidget(self.f_reservationDb)
        self.tw_reservation.setObjectName(u"tw_reservation")
        self.tw_reservation.setFont(font8)
        self.tw_reservation.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_reservation.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_reservation.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_reservation.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_reservation.verticalHeader().setCascadingSectionResizes(True)
        self.tw_reservation.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_71.addWidget(self.tw_reservation)


        self.horizontalLayout_51.addWidget(self.f_reservationDb)

        self.sw_content.addWidget(self.page_reservation)
        self.page_waste = QWidget()
        self.page_waste.setObjectName(u"page_waste")
        self.horizontalLayout_24 = QHBoxLayout(self.page_waste)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.w_wasteCustom = QFrame(self.page_waste)
        self.w_wasteCustom.setObjectName(u"w_wasteCustom")
        self.w_wasteCustom.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.verticalLayout_29 = QVBoxLayout(self.w_wasteCustom)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.groupBox_4 = QGroupBox(self.w_wasteCustom)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font5)
        self.verticalLayout_74 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.cb_wasteStockWorkerId = QComboBox(self.groupBox_4)
        self.cb_wasteStockWorkerId.setObjectName(u"cb_wasteStockWorkerId")

        self.verticalLayout_74.addWidget(self.cb_wasteStockWorkerId)

        self.le_wasteStockQuantity = QLineEdit(self.groupBox_4)
        self.le_wasteStockQuantity.setObjectName(u"le_wasteStockQuantity")

        self.verticalLayout_74.addWidget(self.le_wasteStockQuantity)

        self.tw_wasteStock = QTableWidget(self.groupBox_4)
        self.tw_wasteStock.setObjectName(u"tw_wasteStock")
        font9 = QFont()
        font9.setFamilies([u"Times New Roman"])
        font9.setPointSize(18)
        self.tw_wasteStock.setFont(font9)
        self.tw_wasteStock.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_74.addWidget(self.tw_wasteStock)

        self.frame_29 = QFrame(self.groupBox_4)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy11 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy11)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.btn_wasteStockClear = QPushButton(self.frame_29)
        self.btn_wasteStockClear.setObjectName(u"btn_wasteStockClear")
        self.btn_wasteStockClear.setIcon(icon23)
        self.btn_wasteStockClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_30.addWidget(self.btn_wasteStockClear)

        self.btn_wasteStockSave = QPushButton(self.frame_29)
        self.btn_wasteStockSave.setObjectName(u"btn_wasteStockSave")
        icon38 = QIcon()
        icon38.addFile(u":/Simple icons/simple_icons/fi-rr-pharmacy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_wasteStockSave.setIcon(icon38)
        self.btn_wasteStockSave.setIconSize(QSize(32, 32))

        self.horizontalLayout_30.addWidget(self.btn_wasteStockSave)


        self.verticalLayout_74.addWidget(self.frame_29)


        self.verticalLayout_29.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.w_wasteCustom)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font5)
        self.verticalLayout_54 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.cb_wasteCustomWorkerId = QComboBox(self.groupBox_3)
        self.cb_wasteCustomWorkerId.setObjectName(u"cb_wasteCustomWorkerId")

        self.verticalLayout_54.addWidget(self.cb_wasteCustomWorkerId)

        self.le_wasteCustomName = QLineEdit(self.groupBox_3)
        self.le_wasteCustomName.setObjectName(u"le_wasteCustomName")

        self.verticalLayout_54.addWidget(self.le_wasteCustomName)

        self.cb_wasteCustomCategory = QComboBox(self.groupBox_3)
        self.cb_wasteCustomCategory.setObjectName(u"cb_wasteCustomCategory")

        self.verticalLayout_54.addWidget(self.cb_wasteCustomCategory)

        self.le_wasteCustomQuantity = QLineEdit(self.groupBox_3)
        self.le_wasteCustomQuantity.setObjectName(u"le_wasteCustomQuantity")

        self.verticalLayout_54.addWidget(self.le_wasteCustomQuantity)

        self.le_wasteCustomPrice = QLineEdit(self.groupBox_3)
        self.le_wasteCustomPrice.setObjectName(u"le_wasteCustomPrice")

        self.verticalLayout_54.addWidget(self.le_wasteCustomPrice)

        self.frame1 = QFrame(self.groupBox_3)
        self.frame1.setObjectName(u"frame1")
        sizePolicy11.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy11)
        self.frame1.setStyleSheet(u"")
        self.horizontalLayout_29 = QHBoxLayout(self.frame1)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.btn_wasteCustomClear = QPushButton(self.frame1)
        self.btn_wasteCustomClear.setObjectName(u"btn_wasteCustomClear")
        self.btn_wasteCustomClear.setIcon(icon23)
        self.btn_wasteCustomClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_29.addWidget(self.btn_wasteCustomClear)

        self.btn_wasteCustomSave = QPushButton(self.frame1)
        self.btn_wasteCustomSave.setObjectName(u"btn_wasteCustomSave")
        self.btn_wasteCustomSave.setIcon(icon38)
        self.btn_wasteCustomSave.setIconSize(QSize(32, 32))

        self.horizontalLayout_29.addWidget(self.btn_wasteCustomSave)


        self.verticalLayout_54.addWidget(self.frame1)


        self.verticalLayout_29.addWidget(self.groupBox_3)


        self.horizontalLayout_24.addWidget(self.w_wasteCustom)

        self.w_wasteStock = QFrame(self.page_waste)
        self.w_wasteStock.setObjectName(u"w_wasteStock")
        self.w_wasteStock.setMinimumSize(QSize(200, 0))
        self.w_wasteStock.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.verticalLayout_36 = QVBoxLayout(self.w_wasteStock)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.tw_waste = QTableWidget(self.w_wasteStock)
        self.tw_waste.setObjectName(u"tw_waste")
        self.tw_waste.setFont(font9)
        self.tw_waste.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_36.addWidget(self.tw_waste)


        self.horizontalLayout_24.addWidget(self.w_wasteStock)

        self.sw_content.addWidget(self.page_waste)
        self.page_overview = QWidget()
        self.page_overview.setObjectName(u"page_overview")
        self.horizontalLayout_33 = QHBoxLayout(self.page_overview)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_12 = QFrame(self.page_overview)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_12)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.l_stock = QLabel(self.frame_12)
        self.l_stock.setObjectName(u"l_stock")
        font10 = QFont()
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setUnderline(True)
        self.l_stock.setFont(font10)
        self.l_stock.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.l_stock)

        self.frame_38 = QFrame(self.frame_12)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.rb_stockIngredients = QRadioButton(self.frame_38)
        self.rb_stockIngredients.setObjectName(u"rb_stockIngredients")
        self.rb_stockIngredients.setFont(font6)
        self.rb_stockIngredients.setChecked(True)

        self.horizontalLayout_57.addWidget(self.rb_stockIngredients)

        self.rb_stockOthers = QRadioButton(self.frame_38)
        self.rb_stockOthers.setObjectName(u"rb_stockOthers")
        self.rb_stockOthers.setFont(font6)

        self.horizontalLayout_57.addWidget(self.rb_stockOthers)


        self.verticalLayout_49.addWidget(self.frame_38)

        self.tw_stock = QTableWidget(self.frame_12)
        self.tw_stock.setObjectName(u"tw_stock")
        font11 = QFont()
        font11.setFamilies([u"Times New Roman"])
        font11.setPointSize(22)
        self.tw_stock.setFont(font11)
        self.tw_stock.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_49.addWidget(self.tw_stock)


        self.horizontalLayout_33.addWidget(self.frame_12)

        self.sw_content.addWidget(self.page_overview)
        self.page_productReceipt = QWidget()
        self.page_productReceipt.setObjectName(u"page_productReceipt")
        self.gridLayout_14 = QGridLayout(self.page_productReceipt)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_6 = QFrame(self.page_productReceipt)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_6)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.l_productReceiptSelection = QLabel(self.frame_6)
        self.l_productReceiptSelection.setObjectName(u"l_productReceiptSelection")
        font12 = QFont()
        font12.setFamilies([u"Times New Roman"])
        font12.setPointSize(14)
        font12.setBold(True)
        self.l_productReceiptSelection.setFont(font12)

        self.verticalLayout_48.addWidget(self.l_productReceiptSelection)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Sunken)
        self.gridLayout_22 = QGridLayout(self.frame_14)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.l_ingredient_2 = QLabel(self.frame_14)
        self.l_ingredient_2.setObjectName(u"l_ingredient_2")
        sizePolicy.setHeightForWidth(self.l_ingredient_2.sizePolicy().hasHeightForWidth())
        self.l_ingredient_2.setSizePolicy(sizePolicy)
        font13 = QFont()
        font13.setFamilies([u"Times New Roman"])
        font13.setPointSize(14)
        self.l_ingredient_2.setFont(font13)
        self.l_ingredient_2.setAlignment(Qt.AlignCenter)
        self.l_ingredient_2.setMargin(5)

        self.gridLayout_22.addWidget(self.l_ingredient_2, 2, 0, 1, 1)

        self.cb_productReceiptMenuItem = QComboBox(self.frame_14)
        self.cb_productReceiptMenuItem.setObjectName(u"cb_productReceiptMenuItem")
        sizePolicy9.setHeightForWidth(self.cb_productReceiptMenuItem.sizePolicy().hasHeightForWidth())
        self.cb_productReceiptMenuItem.setSizePolicy(sizePolicy9)

        self.gridLayout_22.addWidget(self.cb_productReceiptMenuItem, 2, 1, 1, 1)


        self.verticalLayout_48.addWidget(self.frame_14)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setInputMethodHints(Qt.ImhDigitsOnly)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Sunken)
        self.gridLayout_15 = QGridLayout(self.frame_8)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.btn_productReceiptAdd = QPushButton(self.frame_8)
        self.btn_productReceiptAdd.setObjectName(u"btn_productReceiptAdd")
        self.btn_productReceiptAdd.setIcon(icon35)
        self.btn_productReceiptAdd.setIconSize(QSize(32, 32))

        self.gridLayout_15.addWidget(self.btn_productReceiptAdd, 1, 3, 1, 1)

        self.cb_productReceiptIngredientName = QComboBox(self.frame_8)
        self.cb_productReceiptIngredientName.setObjectName(u"cb_productReceiptIngredientName")
        sizePolicy9.setHeightForWidth(self.cb_productReceiptIngredientName.sizePolicy().hasHeightForWidth())
        self.cb_productReceiptIngredientName.setSizePolicy(sizePolicy9)

        self.gridLayout_15.addWidget(self.cb_productReceiptIngredientName, 1, 1, 1, 1)

        self.btn_productReceiptRemove = QPushButton(self.frame_8)
        self.btn_productReceiptRemove.setObjectName(u"btn_productReceiptRemove")
        self.btn_productReceiptRemove.setEnabled(False)
        icon39 = QIcon()
        icon39.addFile(u":/Simple icons/simple_icons/fi-rr-cross-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_productReceiptRemove.setIcon(icon39)
        self.btn_productReceiptRemove.setIconSize(QSize(32, 32))

        self.gridLayout_15.addWidget(self.btn_productReceiptRemove, 1, 5, 1, 1)

        self.le_productReceiptIngredientQuantity = QLineEdit(self.frame_8)
        self.le_productReceiptIngredientQuantity.setObjectName(u"le_productReceiptIngredientQuantity")
        sizePolicy5.setHeightForWidth(self.le_productReceiptIngredientQuantity.sizePolicy().hasHeightForWidth())
        self.le_productReceiptIngredientQuantity.setSizePolicy(sizePolicy5)
        self.le_productReceiptIngredientQuantity.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)
        self.le_productReceiptIngredientQuantity.setClearButtonEnabled(True)

        self.gridLayout_15.addWidget(self.le_productReceiptIngredientQuantity, 1, 2, 1, 1)

        self.btn_productReceiptEdit = QPushButton(self.frame_8)
        self.btn_productReceiptEdit.setObjectName(u"btn_productReceiptEdit")
        self.btn_productReceiptEdit.setEnabled(False)
        self.btn_productReceiptEdit.setIcon(icon36)
        self.btn_productReceiptEdit.setIconSize(QSize(32, 32))

        self.gridLayout_15.addWidget(self.btn_productReceiptEdit, 1, 4, 1, 1)

        self.l_ingredient = QLabel(self.frame_8)
        self.l_ingredient.setObjectName(u"l_ingredient")
        sizePolicy.setHeightForWidth(self.l_ingredient.sizePolicy().hasHeightForWidth())
        self.l_ingredient.setSizePolicy(sizePolicy)
        self.l_ingredient.setFont(font13)
        self.l_ingredient.setAlignment(Qt.AlignCenter)
        self.l_ingredient.setMargin(5)

        self.gridLayout_15.addWidget(self.l_ingredient, 1, 0, 1, 1)

        self.btn_productReceiptClear = QPushButton(self.frame_8)
        self.btn_productReceiptClear.setObjectName(u"btn_productReceiptClear")
        self.btn_productReceiptClear.setEnabled(True)
        self.btn_productReceiptClear.setIcon(icon23)
        self.btn_productReceiptClear.setIconSize(QSize(32, 32))

        self.gridLayout_15.addWidget(self.btn_productReceiptClear, 1, 6, 1, 1)


        self.verticalLayout_48.addWidget(self.frame_8)

        self.tw_productReceiptIngredientList = QTableWidget(self.frame_6)
        self.tw_productReceiptIngredientList.setObjectName(u"tw_productReceiptIngredientList")
        self.tw_productReceiptIngredientList.setFont(font11)
        self.tw_productReceiptIngredientList.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_48.addWidget(self.tw_productReceiptIngredientList)

        self.frame_31 = QFrame(self.frame_6)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Sunken)
        self.gridLayout_23 = QGridLayout(self.frame_31)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.l_ingredient_7 = QLabel(self.frame_31)
        self.l_ingredient_7.setObjectName(u"l_ingredient_7")
        sizePolicy.setHeightForWidth(self.l_ingredient_7.sizePolicy().hasHeightForWidth())
        self.l_ingredient_7.setSizePolicy(sizePolicy)
        self.l_ingredient_7.setFont(font12)
        self.l_ingredient_7.setAlignment(Qt.AlignCenter)
        self.l_ingredient_7.setMargin(5)

        self.gridLayout_23.addWidget(self.l_ingredient_7, 2, 2, 1, 1)

        self.l_ingredient_5 = QLabel(self.frame_31)
        self.l_ingredient_5.setObjectName(u"l_ingredient_5")
        sizePolicy.setHeightForWidth(self.l_ingredient_5.sizePolicy().hasHeightForWidth())
        self.l_ingredient_5.setSizePolicy(sizePolicy)
        self.l_ingredient_5.setFont(font12)
        self.l_ingredient_5.setAlignment(Qt.AlignCenter)
        self.l_ingredient_5.setMargin(5)

        self.gridLayout_23.addWidget(self.l_ingredient_5, 2, 0, 1, 1)

        self.l_ingredient_8 = QLabel(self.frame_31)
        self.l_ingredient_8.setObjectName(u"l_ingredient_8")
        sizePolicy.setHeightForWidth(self.l_ingredient_8.sizePolicy().hasHeightForWidth())
        self.l_ingredient_8.setSizePolicy(sizePolicy)
        self.l_ingredient_8.setFont(font12)
        self.l_ingredient_8.setAlignment(Qt.AlignCenter)
        self.l_ingredient_8.setMargin(5)

        self.gridLayout_23.addWidget(self.l_ingredient_8, 2, 3, 1, 1)

        self.l_productReceiptQuantity = QLabel(self.frame_31)
        self.l_productReceiptQuantity.setObjectName(u"l_productReceiptQuantity")
        sizePolicy.setHeightForWidth(self.l_productReceiptQuantity.sizePolicy().hasHeightForWidth())
        self.l_productReceiptQuantity.setSizePolicy(sizePolicy)
        self.l_productReceiptQuantity.setFont(font13)
        self.l_productReceiptQuantity.setAlignment(Qt.AlignCenter)
        self.l_productReceiptQuantity.setMargin(5)

        self.gridLayout_23.addWidget(self.l_productReceiptQuantity, 3, 3, 1, 1)

        self.l_productReceiptPrice = QLabel(self.frame_31)
        self.l_productReceiptPrice.setObjectName(u"l_productReceiptPrice")
        sizePolicy.setHeightForWidth(self.l_productReceiptPrice.sizePolicy().hasHeightForWidth())
        self.l_productReceiptPrice.setSizePolicy(sizePolicy)
        self.l_productReceiptPrice.setFont(font13)
        self.l_productReceiptPrice.setAlignment(Qt.AlignCenter)
        self.l_productReceiptPrice.setMargin(5)

        self.gridLayout_23.addWidget(self.l_productReceiptPrice, 3, 2, 1, 1)

        self.l_productReceiptEstimatedProductionPrice = QLabel(self.frame_31)
        self.l_productReceiptEstimatedProductionPrice.setObjectName(u"l_productReceiptEstimatedProductionPrice")
        sizePolicy.setHeightForWidth(self.l_productReceiptEstimatedProductionPrice.sizePolicy().hasHeightForWidth())
        self.l_productReceiptEstimatedProductionPrice.setSizePolicy(sizePolicy)
        self.l_productReceiptEstimatedProductionPrice.setFont(font13)
        self.l_productReceiptEstimatedProductionPrice.setAlignment(Qt.AlignCenter)
        self.l_productReceiptEstimatedProductionPrice.setMargin(5)

        self.gridLayout_23.addWidget(self.l_productReceiptEstimatedProductionPrice, 3, 0, 1, 1)


        self.verticalLayout_48.addWidget(self.frame_31)


        self.gridLayout_14.addWidget(self.frame_6, 0, 0, 1, 1)

        self.sw_content.addWidget(self.page_productReceipt)
        self.page_database = QWidget()
        self.page_database.setObjectName(u"page_database")
        self.gridLayout_9 = QGridLayout(self.page_database)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tw_database = QTabWidget(self.page_database)
        self.tw_database.setObjectName(u"tw_database")
        font14 = QFont()
        font14.setPointSize(18)
        self.tw_database.setFont(font14)
        self.tw_database.setStyleSheet(u"")
        self.tw_database.setIconSize(QSize(35, 35))
        self.tab_menu = QWidget()
        self.tab_menu.setObjectName(u"tab_menu")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_menu)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.f_menuItemInputs = QFrame(self.tab_menu)
        self.f_menuItemInputs.setObjectName(u"f_menuItemInputs")
        self.f_menuItemInputs.setMaximumSize(QSize(800, 16777215))
        self.f_menuItemInputs.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_menuItemInputs.setFrameShape(QFrame.StyledPanel)
        self.f_menuItemInputs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.f_menuItemInputs)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(9, -1, -1, -1)
        self.gb_menuItem = QGroupBox(self.f_menuItemInputs)
        self.gb_menuItem.setObjectName(u"gb_menuItem")
        self.gb_menuItem.setFont(font5)
        self.gb_menuItem.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.gb_menuItem)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.f_menuItemPic = QFrame(self.gb_menuItem)
        self.f_menuItemPic.setObjectName(u"f_menuItemPic")
        sizePolicy12 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.f_menuItemPic.sizePolicy().hasHeightForWidth())
        self.f_menuItemPic.setSizePolicy(sizePolicy12)
        self.f_menuItemPic.setMinimumSize(QSize(200, 200))
        self.f_menuItemPic.setMaximumSize(QSize(800, 300))
        self.f_menuItemPic.setLayoutDirection(Qt.LeftToRight)
        self.f_menuItemPic.setStyleSheet(u"")
        self.f_menuItemPic.setFrameShape(QFrame.StyledPanel)
        self.f_menuItemPic.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.f_menuItemPic)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.l_menuItemPicture = QLabel(self.f_menuItemPic)
        self.l_menuItemPicture.setObjectName(u"l_menuItemPicture")
        sizePolicy.setHeightForWidth(self.l_menuItemPicture.sizePolicy().hasHeightForWidth())
        self.l_menuItemPicture.setSizePolicy(sizePolicy)
        self.l_menuItemPicture.setMinimumSize(QSize(250, 200))
        self.l_menuItemPicture.setMaximumSize(QSize(300, 300))
        self.l_menuItemPicture.setBaseSize(QSize(200, 200))
        font15 = QFont()
        font15.setPointSize(20)
        self.l_menuItemPicture.setFont(font15)
        self.l_menuItemPicture.setLayoutDirection(Qt.LeftToRight)
        self.l_menuItemPicture.setAutoFillBackground(False)
        self.l_menuItemPicture.setStyleSheet(u"")
        self.l_menuItemPicture.setFrameShape(QFrame.Box)
        self.l_menuItemPicture.setFrameShadow(QFrame.Plain)
        self.l_menuItemPicture.setScaledContents(True)
        self.l_menuItemPicture.setAlignment(Qt.AlignCenter)
        self.l_menuItemPicture.setWordWrap(False)

        self.horizontalLayout_17.addWidget(self.l_menuItemPicture)

        self.f_finishProductPictureSetting = QFrame(self.f_menuItemPic)
        self.f_finishProductPictureSetting.setObjectName(u"f_finishProductPictureSetting")
        self.f_finishProductPictureSetting.setFrameShape(QFrame.StyledPanel)
        self.f_finishProductPictureSetting.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.f_finishProductPictureSetting)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.btn_menuItemPicture = QPushButton(self.f_finishProductPictureSetting)
        self.btn_menuItemPicture.setObjectName(u"btn_menuItemPicture")
        sizePolicy12.setHeightForWidth(self.btn_menuItemPicture.sizePolicy().hasHeightForWidth())
        self.btn_menuItemPicture.setSizePolicy(sizePolicy12)
        icon40 = QIcon()
        icon40.addFile(u":/Simple icons/simple_icons/fi-rr-picture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menuItemPicture.setIcon(icon40)
        self.btn_menuItemPicture.setIconSize(QSize(32, 32))

        self.verticalLayout_41.addWidget(self.btn_menuItemPicture)

        self.btn_menuItemPictureClear = QPushButton(self.f_finishProductPictureSetting)
        self.btn_menuItemPictureClear.setObjectName(u"btn_menuItemPictureClear")
        sizePolicy12.setHeightForWidth(self.btn_menuItemPictureClear.sizePolicy().hasHeightForWidth())
        self.btn_menuItemPictureClear.setSizePolicy(sizePolicy12)
        self.btn_menuItemPictureClear.setIcon(icon23)
        self.btn_menuItemPictureClear.setIconSize(QSize(32, 32))

        self.verticalLayout_41.addWidget(self.btn_menuItemPictureClear)


        self.horizontalLayout_17.addWidget(self.f_finishProductPictureSetting)


        self.verticalLayout_19.addWidget(self.f_menuItemPic)

        self.le_menuItemName = QLineEdit(self.gb_menuItem)
        self.le_menuItemName.setObjectName(u"le_menuItemName")
        self.le_menuItemName.setMaxLength(150)
        self.le_menuItemName.setClearButtonEnabled(True)

        self.verticalLayout_19.addWidget(self.le_menuItemName)

        self.cb_menuItemCategory = QComboBox(self.gb_menuItem)
        self.cb_menuItemCategory.addItem("")
        self.cb_menuItemCategory.addItem("")
        self.cb_menuItemCategory.addItem("")
        self.cb_menuItemCategory.addItem("")
        self.cb_menuItemCategory.addItem("")
        self.cb_menuItemCategory.addItem("")
        self.cb_menuItemCategory.setObjectName(u"cb_menuItemCategory")
        self.cb_menuItemCategory.setFrame(True)

        self.verticalLayout_19.addWidget(self.cb_menuItemCategory)

        self.cb_menuItemCategoryCustom = QComboBox(self.gb_menuItem)
        self.cb_menuItemCategoryCustom.setObjectName(u"cb_menuItemCategoryCustom")

        self.verticalLayout_19.addWidget(self.cb_menuItemCategoryCustom)

        self.le_menuItemUnit = QLineEdit(self.gb_menuItem)
        self.le_menuItemUnit.setObjectName(u"le_menuItemUnit")

        self.verticalLayout_19.addWidget(self.le_menuItemUnit)

        self.le_menuItemUnitQuantity = QLineEdit(self.gb_menuItem)
        self.le_menuItemUnitQuantity.setObjectName(u"le_menuItemUnitQuantity")
        self.le_menuItemUnitQuantity.setMaxLength(20)
        self.le_menuItemUnitQuantity.setClearButtonEnabled(True)

        self.verticalLayout_19.addWidget(self.le_menuItemUnitQuantity)

        self.le_menuItemPrice = QLineEdit(self.gb_menuItem)
        self.le_menuItemPrice.setObjectName(u"le_menuItemPrice")
        self.le_menuItemPrice.setMaxLength(20)
        self.le_menuItemPrice.setClearButtonEnabled(True)

        self.verticalLayout_19.addWidget(self.le_menuItemPrice)


        self.verticalLayout_18.addWidget(self.gb_menuItem)

        self.f_menuItemDbBtn = QFrame(self.f_menuItemInputs)
        self.f_menuItemDbBtn.setObjectName(u"f_menuItemDbBtn")
        sizePolicy1.setHeightForWidth(self.f_menuItemDbBtn.sizePolicy().hasHeightForWidth())
        self.f_menuItemDbBtn.setSizePolicy(sizePolicy1)
        self.f_menuItemDbBtn.setFrameShape(QFrame.StyledPanel)
        self.f_menuItemDbBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.f_menuItemDbBtn)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.btn_menuItemAdd = QPushButton(self.f_menuItemDbBtn)
        self.btn_menuItemAdd.setObjectName(u"btn_menuItemAdd")
        self.btn_menuItemAdd.setIcon(icon35)
        self.btn_menuItemAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_16.addWidget(self.btn_menuItemAdd)

        self.btn_menuItemEdit = QPushButton(self.f_menuItemDbBtn)
        self.btn_menuItemEdit.setObjectName(u"btn_menuItemEdit")
        self.btn_menuItemEdit.setEnabled(False)
        self.btn_menuItemEdit.setIcon(icon36)
        self.btn_menuItemEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_16.addWidget(self.btn_menuItemEdit)

        self.btn_menuItemDelete = QPushButton(self.f_menuItemDbBtn)
        self.btn_menuItemDelete.setObjectName(u"btn_menuItemDelete")
        self.btn_menuItemDelete.setEnabled(False)
        self.btn_menuItemDelete.setIcon(icon22)
        self.btn_menuItemDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_16.addWidget(self.btn_menuItemDelete)

        self.btn_menuItemClear = QPushButton(self.f_menuItemDbBtn)
        self.btn_menuItemClear.setObjectName(u"btn_menuItemClear")
        self.btn_menuItemClear.setEnabled(True)
        self.btn_menuItemClear.setIcon(icon23)
        self.btn_menuItemClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_16.addWidget(self.btn_menuItemClear)


        self.verticalLayout_18.addWidget(self.f_menuItemDbBtn)


        self.horizontalLayout_8.addWidget(self.f_menuItemInputs)

        self.f_menuItemDb = QFrame(self.tab_menu)
        self.f_menuItemDb.setObjectName(u"f_menuItemDb")
        sizePolicy3.setHeightForWidth(self.f_menuItemDb.sizePolicy().hasHeightForWidth())
        self.f_menuItemDb.setSizePolicy(sizePolicy3)
        self.f_menuItemDb.setFrameShape(QFrame.StyledPanel)
        self.f_menuItemDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.f_menuItemDb)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.tw_menuItem = QTableWidget(self.f_menuItemDb)
        self.tw_menuItem.setObjectName(u"tw_menuItem")
        self.tw_menuItem.setFont(font9)
        self.tw_menuItem.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_menuItem.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_menuItem.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_menuItem.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_menuItem.verticalHeader().setCascadingSectionResizes(True)
        self.tw_menuItem.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_17.addWidget(self.tw_menuItem)


        self.horizontalLayout_8.addWidget(self.f_menuItemDb)

        icon41 = QIcon()
        icon41.addFile(u":/Simple icons/simple_icons/fi-rr-hamburger.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_database.addTab(self.tab_menu, icon41, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_19 = QGridLayout(self.tab)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.f_menuCategoryCustomDb = QFrame(self.tab)
        self.f_menuCategoryCustomDb.setObjectName(u"f_menuCategoryCustomDb")
        self.f_menuCategoryCustomDb.setFrameShape(QFrame.StyledPanel)
        self.f_menuCategoryCustomDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.f_menuCategoryCustomDb)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.tw_menuCategoryCustom = QTableWidget(self.f_menuCategoryCustomDb)
        self.tw_menuCategoryCustom.setObjectName(u"tw_menuCategoryCustom")
        self.tw_menuCategoryCustom.setFont(font9)
        self.tw_menuCategoryCustom.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_menuCategoryCustom.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_menuCategoryCustom.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_menuCategoryCustom.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_menuCategoryCustom.verticalHeader().setCascadingSectionResizes(True)
        self.tw_menuCategoryCustom.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_77.addWidget(self.tw_menuCategoryCustom)


        self.gridLayout_19.addWidget(self.f_menuCategoryCustomDb, 0, 1, 1, 1)

        self.f_menuCategoryCustom = QFrame(self.tab)
        self.f_menuCategoryCustom.setObjectName(u"f_menuCategoryCustom")
        self.f_menuCategoryCustom.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.f_menuCategoryCustom.setFrameShape(QFrame.StyledPanel)
        self.f_menuCategoryCustom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.f_menuCategoryCustom)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.gb_menuCategoryCustom = QGroupBox(self.f_menuCategoryCustom)
        self.gb_menuCategoryCustom.setObjectName(u"gb_menuCategoryCustom")
        self.gb_menuCategoryCustom.setFont(font5)
        self.gb_menuCategoryCustom.setStyleSheet(u"")
        self.gb_menuCategoryCustom.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_76 = QVBoxLayout(self.gb_menuCategoryCustom)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.le_menuCategoryCustomName = QLineEdit(self.gb_menuCategoryCustom)
        self.le_menuCategoryCustomName.setObjectName(u"le_menuCategoryCustomName")
        self.le_menuCategoryCustomName.setMaxLength(40)
        self.le_menuCategoryCustomName.setClearButtonEnabled(True)

        self.verticalLayout_76.addWidget(self.le_menuCategoryCustomName)

        self.cb_menuCategoryCustomPrinting = QComboBox(self.gb_menuCategoryCustom)
        self.cb_menuCategoryCustomPrinting.addItem("")
        self.cb_menuCategoryCustomPrinting.addItem("")
        self.cb_menuCategoryCustomPrinting.addItem("")
        self.cb_menuCategoryCustomPrinting.setObjectName(u"cb_menuCategoryCustomPrinting")

        self.verticalLayout_76.addWidget(self.cb_menuCategoryCustomPrinting)


        self.verticalLayout_75.addWidget(self.gb_menuCategoryCustom)

        self.f_menuCategoryCustomDbBtn = QFrame(self.f_menuCategoryCustom)
        self.f_menuCategoryCustomDbBtn.setObjectName(u"f_menuCategoryCustomDbBtn")
        sizePolicy1.setHeightForWidth(self.f_menuCategoryCustomDbBtn.sizePolicy().hasHeightForWidth())
        self.f_menuCategoryCustomDbBtn.setSizePolicy(sizePolicy1)
        self.f_menuCategoryCustomDbBtn.setFrameShape(QFrame.StyledPanel)
        self.f_menuCategoryCustomDbBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.f_menuCategoryCustomDbBtn)
        self.horizontalLayout_54.setSpacing(5)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.btn_menuCategoryCustomAdd = QPushButton(self.f_menuCategoryCustomDbBtn)
        self.btn_menuCategoryCustomAdd.setObjectName(u"btn_menuCategoryCustomAdd")
        self.btn_menuCategoryCustomAdd.setIcon(icon35)
        self.btn_menuCategoryCustomAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_54.addWidget(self.btn_menuCategoryCustomAdd)

        self.btn_menuCategoryCustomEdit = QPushButton(self.f_menuCategoryCustomDbBtn)
        self.btn_menuCategoryCustomEdit.setObjectName(u"btn_menuCategoryCustomEdit")
        self.btn_menuCategoryCustomEdit.setEnabled(False)
        self.btn_menuCategoryCustomEdit.setIcon(icon36)
        self.btn_menuCategoryCustomEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_54.addWidget(self.btn_menuCategoryCustomEdit)

        self.btn_menuCategoryCustomDelete = QPushButton(self.f_menuCategoryCustomDbBtn)
        self.btn_menuCategoryCustomDelete.setObjectName(u"btn_menuCategoryCustomDelete")
        self.btn_menuCategoryCustomDelete.setEnabled(False)
        self.btn_menuCategoryCustomDelete.setIcon(icon22)
        self.btn_menuCategoryCustomDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_54.addWidget(self.btn_menuCategoryCustomDelete)

        self.btn_menuCategoryCustomClear = QPushButton(self.f_menuCategoryCustomDbBtn)
        self.btn_menuCategoryCustomClear.setObjectName(u"btn_menuCategoryCustomClear")
        self.btn_menuCategoryCustomClear.setEnabled(True)
        self.btn_menuCategoryCustomClear.setIcon(icon23)
        self.btn_menuCategoryCustomClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_54.addWidget(self.btn_menuCategoryCustomClear)


        self.verticalLayout_75.addWidget(self.f_menuCategoryCustomDbBtn)


        self.gridLayout_19.addWidget(self.f_menuCategoryCustom, 0, 0, 1, 1)

        icon42 = QIcon()
        icon42.addFile(u":/Simple icons/simple_icons/fi-rr-book-alt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_database.addTab(self.tab, icon42, "")
        self.tab_supplement = QWidget()
        self.tab_supplement.setObjectName(u"tab_supplement")
        self.horizontalLayout_49 = QHBoxLayout(self.tab_supplement)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.f_supplementInputs = QFrame(self.tab_supplement)
        self.f_supplementInputs.setObjectName(u"f_supplementInputs")
        self.f_supplementInputs.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_supplementInputs.setFrameShape(QFrame.StyledPanel)
        self.f_supplementInputs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.f_supplementInputs)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.gb_supplement = QGroupBox(self.f_supplementInputs)
        self.gb_supplement.setObjectName(u"gb_supplement")
        self.gb_supplement.setFont(font3)
        self.gb_supplement.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.verticalLayout_70 = QVBoxLayout(self.gb_supplement)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.le_supplementName = QLineEdit(self.gb_supplement)
        self.le_supplementName.setObjectName(u"le_supplementName")
        self.le_supplementName.setMaxLength(150)
        self.le_supplementName.setClearButtonEnabled(True)

        self.verticalLayout_70.addWidget(self.le_supplementName)

        self.cb_supplementProduct = QComboBox(self.gb_supplement)
        self.cb_supplementProduct.setObjectName(u"cb_supplementProduct")

        self.verticalLayout_70.addWidget(self.cb_supplementProduct)

        self.le_supplementQuantity = QLineEdit(self.gb_supplement)
        self.le_supplementQuantity.setObjectName(u"le_supplementQuantity")
        self.le_supplementQuantity.setMaxLength(20)
        self.le_supplementQuantity.setClearButtonEnabled(True)

        self.verticalLayout_70.addWidget(self.le_supplementQuantity)

        self.le_supplementPrice = QLineEdit(self.gb_supplement)
        self.le_supplementPrice.setObjectName(u"le_supplementPrice")
        self.le_supplementPrice.setMaxLength(20)
        self.le_supplementPrice.setClearButtonEnabled(True)

        self.verticalLayout_70.addWidget(self.le_supplementPrice)


        self.verticalLayout_66.addWidget(self.gb_supplement)

        self.f_expenseDbBtn_4 = QFrame(self.f_supplementInputs)
        self.f_expenseDbBtn_4.setObjectName(u"f_expenseDbBtn_4")
        sizePolicy1.setHeightForWidth(self.f_expenseDbBtn_4.sizePolicy().hasHeightForWidth())
        self.f_expenseDbBtn_4.setSizePolicy(sizePolicy1)
        self.f_expenseDbBtn_4.setFrameShape(QFrame.StyledPanel)
        self.f_expenseDbBtn_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.f_expenseDbBtn_4)
        self.horizontalLayout_48.setSpacing(5)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.btn_supplementAdd = QPushButton(self.f_expenseDbBtn_4)
        self.btn_supplementAdd.setObjectName(u"btn_supplementAdd")
        self.btn_supplementAdd.setIcon(icon35)
        self.btn_supplementAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_48.addWidget(self.btn_supplementAdd)

        self.btn_supplementEdit = QPushButton(self.f_expenseDbBtn_4)
        self.btn_supplementEdit.setObjectName(u"btn_supplementEdit")
        self.btn_supplementEdit.setEnabled(False)
        self.btn_supplementEdit.setIcon(icon36)
        self.btn_supplementEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_48.addWidget(self.btn_supplementEdit)

        self.btn_supplementDelete = QPushButton(self.f_expenseDbBtn_4)
        self.btn_supplementDelete.setObjectName(u"btn_supplementDelete")
        self.btn_supplementDelete.setEnabled(False)
        self.btn_supplementDelete.setIcon(icon22)
        self.btn_supplementDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_48.addWidget(self.btn_supplementDelete)

        self.btn_supplementClear = QPushButton(self.f_expenseDbBtn_4)
        self.btn_supplementClear.setObjectName(u"btn_supplementClear")
        self.btn_supplementClear.setEnabled(True)
        self.btn_supplementClear.setIcon(icon23)
        self.btn_supplementClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_48.addWidget(self.btn_supplementClear)


        self.verticalLayout_66.addWidget(self.f_expenseDbBtn_4)


        self.horizontalLayout_49.addWidget(self.f_supplementInputs)

        self.f_supplementDb = QFrame(self.tab_supplement)
        self.f_supplementDb.setObjectName(u"f_supplementDb")
        self.f_supplementDb.setFrameShape(QFrame.StyledPanel)
        self.f_supplementDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.f_supplementDb)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.tw_supplement = QTableWidget(self.f_supplementDb)
        self.tw_supplement.setObjectName(u"tw_supplement")
        self.tw_supplement.setFont(font8)
        self.tw_supplement.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_supplement.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_supplement.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_supplement.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_supplement.verticalHeader().setCascadingSectionResizes(True)
        self.tw_supplement.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_65.addWidget(self.tw_supplement)


        self.horizontalLayout_49.addWidget(self.f_supplementDb)

        icon43 = QIcon()
        icon43.addFile(u":/Simple icons/simple_icons/fi-rr-confetti.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_database.addTab(self.tab_supplement, icon43, "")
        self.tab_expense = QWidget()
        self.tab_expense.setObjectName(u"tab_expense")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_expense)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.f_expenseInputs = QFrame(self.tab_expense)
        self.f_expenseInputs.setObjectName(u"f_expenseInputs")
        self.f_expenseInputs.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_expenseInputs.setFrameShape(QFrame.StyledPanel)
        self.f_expenseInputs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.f_expenseInputs)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gb_expense = QGroupBox(self.f_expenseInputs)
        self.gb_expense.setObjectName(u"gb_expense")
        self.gb_expense.setFont(font5)
        self.gb_expense.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.verticalLayout_21 = QVBoxLayout(self.gb_expense)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.le_expenseName = QLineEdit(self.gb_expense)
        self.le_expenseName.setObjectName(u"le_expenseName")
        self.le_expenseName.setMaxLength(40)
        self.le_expenseName.setClearButtonEnabled(True)

        self.verticalLayout_21.addWidget(self.le_expenseName)

        self.cb_expenseCategory = QComboBox(self.gb_expense)
        self.cb_expenseCategory.setObjectName(u"cb_expenseCategory")

        self.verticalLayout_21.addWidget(self.cb_expenseCategory)

        self.le_expenseUnit = QLineEdit(self.gb_expense)
        self.le_expenseUnit.setObjectName(u"le_expenseUnit")
        self.le_expenseUnit.setMaxLength(20)
        self.le_expenseUnit.setClearButtonEnabled(True)

        self.verticalLayout_21.addWidget(self.le_expenseUnit)

        self.le_expenseQuantity = QLineEdit(self.gb_expense)
        self.le_expenseQuantity.setObjectName(u"le_expenseQuantity")
        self.le_expenseQuantity.setMaxLength(20)
        self.le_expenseQuantity.setClearButtonEnabled(True)

        self.verticalLayout_21.addWidget(self.le_expenseQuantity)

        self.le_expensePrice = QLineEdit(self.gb_expense)
        self.le_expensePrice.setObjectName(u"le_expensePrice")
        self.le_expensePrice.setMaxLength(20)
        self.le_expensePrice.setClearButtonEnabled(True)

        self.verticalLayout_21.addWidget(self.le_expensePrice)

        self.cb_expenseSupplier = QComboBox(self.gb_expense)
        self.cb_expenseSupplier.addItem("")
        self.cb_expenseSupplier.setObjectName(u"cb_expenseSupplier")

        self.verticalLayout_21.addWidget(self.cb_expenseSupplier)

        self.cb_expensePayed = QCheckBox(self.gb_expense)
        self.cb_expensePayed.setObjectName(u"cb_expensePayed")
        self.cb_expensePayed.setFont(font3)
        self.cb_expensePayed.setLayoutDirection(Qt.LeftToRight)
        self.cb_expensePayed.setIcon(icon28)
        self.cb_expensePayed.setIconSize(QSize(32, 32))
        self.cb_expensePayed.setChecked(True)

        self.verticalLayout_21.addWidget(self.cb_expensePayed)


        self.verticalLayout_20.addWidget(self.gb_expense)

        self.f_expenseDbBtn = QFrame(self.f_expenseInputs)
        self.f_expenseDbBtn.setObjectName(u"f_expenseDbBtn")
        sizePolicy1.setHeightForWidth(self.f_expenseDbBtn.sizePolicy().hasHeightForWidth())
        self.f_expenseDbBtn.setSizePolicy(sizePolicy1)
        self.f_expenseDbBtn.setFrameShape(QFrame.StyledPanel)
        self.f_expenseDbBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.f_expenseDbBtn)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.btn_expenseAdd = QPushButton(self.f_expenseDbBtn)
        self.btn_expenseAdd.setObjectName(u"btn_expenseAdd")
        self.btn_expenseAdd.setIcon(icon35)
        self.btn_expenseAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_18.addWidget(self.btn_expenseAdd)

        self.btn_expenseEdit = QPushButton(self.f_expenseDbBtn)
        self.btn_expenseEdit.setObjectName(u"btn_expenseEdit")
        self.btn_expenseEdit.setEnabled(False)
        self.btn_expenseEdit.setIcon(icon36)
        self.btn_expenseEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_18.addWidget(self.btn_expenseEdit)

        self.btn_expenseDelete = QPushButton(self.f_expenseDbBtn)
        self.btn_expenseDelete.setObjectName(u"btn_expenseDelete")
        self.btn_expenseDelete.setEnabled(False)
        self.btn_expenseDelete.setIcon(icon22)
        self.btn_expenseDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_18.addWidget(self.btn_expenseDelete)

        self.btn_expenseClear = QPushButton(self.f_expenseDbBtn)
        self.btn_expenseClear.setObjectName(u"btn_expenseClear")
        self.btn_expenseClear.setEnabled(True)
        self.btn_expenseClear.setIcon(icon23)
        self.btn_expenseClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_18.addWidget(self.btn_expenseClear)


        self.verticalLayout_20.addWidget(self.f_expenseDbBtn)


        self.horizontalLayout_9.addWidget(self.f_expenseInputs)

        self.f_expenseDb = QFrame(self.tab_expense)
        self.f_expenseDb.setObjectName(u"f_expenseDb")
        self.f_expenseDb.setFrameShape(QFrame.StyledPanel)
        self.f_expenseDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.f_expenseDb)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.tw_expense = QTableWidget(self.f_expenseDb)
        self.tw_expense.setObjectName(u"tw_expense")
        self.tw_expense.setFont(font9)
        self.tw_expense.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_expense.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_expense.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_expense.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_expense.verticalHeader().setCascadingSectionResizes(True)
        self.tw_expense.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_22.addWidget(self.tw_expense)


        self.horizontalLayout_9.addWidget(self.f_expenseDb)

        icon44 = QIcon()
        icon44.addFile(u":/Simple icons/simple_icons/fi-rr-shopping-cart-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_database.addTab(self.tab_expense, icon44, "")
        self.tab_expenseCategory = QWidget()
        self.tab_expenseCategory.setObjectName(u"tab_expenseCategory")
        self.horizontalLayout_42 = QHBoxLayout(self.tab_expenseCategory)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.f_expenseCategoryInputs = QFrame(self.tab_expenseCategory)
        self.f_expenseCategoryInputs.setObjectName(u"f_expenseCategoryInputs")
        self.f_expenseCategoryInputs.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_expenseCategoryInputs.setFrameShape(QFrame.StyledPanel)
        self.f_expenseCategoryInputs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.f_expenseCategoryInputs)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.gb_expenseCategory = QGroupBox(self.f_expenseCategoryInputs)
        self.gb_expenseCategory.setObjectName(u"gb_expenseCategory")
        self.gb_expenseCategory.setFont(font5)
        self.gb_expenseCategory.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.gb_expenseCategory.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_53 = QVBoxLayout(self.gb_expenseCategory)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.le_expenseCategoryName = QLineEdit(self.gb_expenseCategory)
        self.le_expenseCategoryName.setObjectName(u"le_expenseCategoryName")
        self.le_expenseCategoryName.setMaxLength(40)
        self.le_expenseCategoryName.setClearButtonEnabled(True)

        self.verticalLayout_53.addWidget(self.le_expenseCategoryName)

        self.cb_expenseCategorySaveToStock = QCheckBox(self.gb_expenseCategory)
        self.cb_expenseCategorySaveToStock.setObjectName(u"cb_expenseCategorySaveToStock")
        self.cb_expenseCategorySaveToStock.setFont(font3)
        self.cb_expenseCategorySaveToStock.setLayoutDirection(Qt.LeftToRight)
        icon45 = QIcon()
        icon45.addFile(u":/Simple icons/simple_icons/fi-rr-cursor-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_expenseCategorySaveToStock.setIcon(icon45)
        self.cb_expenseCategorySaveToStock.setIconSize(QSize(32, 32))
        self.cb_expenseCategorySaveToStock.setChecked(True)

        self.verticalLayout_53.addWidget(self.cb_expenseCategorySaveToStock)

        self.cb_expenseCategoryIsIngredient = QCheckBox(self.gb_expenseCategory)
        self.cb_expenseCategoryIsIngredient.setObjectName(u"cb_expenseCategoryIsIngredient")
        self.cb_expenseCategoryIsIngredient.setFont(font3)
        self.cb_expenseCategoryIsIngredient.setLayoutDirection(Qt.LeftToRight)
        self.cb_expenseCategoryIsIngredient.setIcon(icon45)
        self.cb_expenseCategoryIsIngredient.setIconSize(QSize(32, 32))
        self.cb_expenseCategoryIsIngredient.setChecked(True)

        self.verticalLayout_53.addWidget(self.cb_expenseCategoryIsIngredient)


        self.verticalLayout_52.addWidget(self.gb_expenseCategory)

        self.f_expenseCategoryDbBtn = QFrame(self.f_expenseCategoryInputs)
        self.f_expenseCategoryDbBtn.setObjectName(u"f_expenseCategoryDbBtn")
        sizePolicy1.setHeightForWidth(self.f_expenseCategoryDbBtn.sizePolicy().hasHeightForWidth())
        self.f_expenseCategoryDbBtn.setSizePolicy(sizePolicy1)
        self.f_expenseCategoryDbBtn.setFrameShape(QFrame.StyledPanel)
        self.f_expenseCategoryDbBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.f_expenseCategoryDbBtn)
        self.horizontalLayout_41.setSpacing(5)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.btn_expenseCategoryAdd = QPushButton(self.f_expenseCategoryDbBtn)
        self.btn_expenseCategoryAdd.setObjectName(u"btn_expenseCategoryAdd")
        self.btn_expenseCategoryAdd.setIcon(icon35)
        self.btn_expenseCategoryAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_41.addWidget(self.btn_expenseCategoryAdd)

        self.btn_expenseCategoryEdit = QPushButton(self.f_expenseCategoryDbBtn)
        self.btn_expenseCategoryEdit.setObjectName(u"btn_expenseCategoryEdit")
        self.btn_expenseCategoryEdit.setEnabled(False)
        self.btn_expenseCategoryEdit.setIcon(icon36)
        self.btn_expenseCategoryEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_41.addWidget(self.btn_expenseCategoryEdit)

        self.btn_expenseCategoryDelete = QPushButton(self.f_expenseCategoryDbBtn)
        self.btn_expenseCategoryDelete.setObjectName(u"btn_expenseCategoryDelete")
        self.btn_expenseCategoryDelete.setEnabled(False)
        self.btn_expenseCategoryDelete.setIcon(icon22)
        self.btn_expenseCategoryDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_41.addWidget(self.btn_expenseCategoryDelete)

        self.btn_expenseCategoryClear = QPushButton(self.f_expenseCategoryDbBtn)
        self.btn_expenseCategoryClear.setObjectName(u"btn_expenseCategoryClear")
        self.btn_expenseCategoryClear.setEnabled(True)
        self.btn_expenseCategoryClear.setIcon(icon23)
        self.btn_expenseCategoryClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_41.addWidget(self.btn_expenseCategoryClear)


        self.verticalLayout_52.addWidget(self.f_expenseCategoryDbBtn)


        self.horizontalLayout_42.addWidget(self.f_expenseCategoryInputs)

        self.f_expenseCategoryDb = QFrame(self.tab_expenseCategory)
        self.f_expenseCategoryDb.setObjectName(u"f_expenseCategoryDb")
        self.f_expenseCategoryDb.setFrameShape(QFrame.StyledPanel)
        self.f_expenseCategoryDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.f_expenseCategoryDb)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.tw_expenseCategory = QTableWidget(self.f_expenseCategoryDb)
        self.tw_expenseCategory.setObjectName(u"tw_expenseCategory")
        self.tw_expenseCategory.setFont(font9)
        self.tw_expenseCategory.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_expenseCategory.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_expenseCategory.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_expenseCategory.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_expenseCategory.verticalHeader().setCascadingSectionResizes(True)
        self.tw_expenseCategory.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_51.addWidget(self.tw_expenseCategory)


        self.horizontalLayout_42.addWidget(self.f_expenseCategoryDb)

        icon46 = QIcon()
        icon46.addFile(u":/Simple icons/simple_icons/fi-rr-shopping-cart-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_database.addTab(self.tab_expenseCategory, icon46, "")
        self.tab_supplier = QWidget()
        self.tab_supplier.setObjectName(u"tab_supplier")
        self.horizontalLayout_47 = QHBoxLayout(self.tab_supplier)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.f_supplierInputs = QFrame(self.tab_supplier)
        self.f_supplierInputs.setObjectName(u"f_supplierInputs")
        self.f_supplierInputs.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_supplierInputs.setFrameShape(QFrame.StyledPanel)
        self.f_supplierInputs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.f_supplierInputs)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.gb_supplier = QGroupBox(self.f_supplierInputs)
        self.gb_supplier.setObjectName(u"gb_supplier")
        self.gb_supplier.setFont(font3)
        self.gb_supplier.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.verticalLayout_64 = QVBoxLayout(self.gb_supplier)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.le_supplierName = QLineEdit(self.gb_supplier)
        self.le_supplierName.setObjectName(u"le_supplierName")
        self.le_supplierName.setMaxLength(150)
        self.le_supplierName.setClearButtonEnabled(True)

        self.verticalLayout_64.addWidget(self.le_supplierName)

        self.le_supplierPhone = QLineEdit(self.gb_supplier)
        self.le_supplierPhone.setObjectName(u"le_supplierPhone")
        self.le_supplierPhone.setMaxLength(20)
        self.le_supplierPhone.setClearButtonEnabled(True)

        self.verticalLayout_64.addWidget(self.le_supplierPhone)

        self.le_supplierAddress = QLineEdit(self.gb_supplier)
        self.le_supplierAddress.setObjectName(u"le_supplierAddress")
        self.le_supplierAddress.setMaxLength(250)
        self.le_supplierAddress.setClearButtonEnabled(True)

        self.verticalLayout_64.addWidget(self.le_supplierAddress)

        self.le_supplierMail = QLineEdit(self.gb_supplier)
        self.le_supplierMail.setObjectName(u"le_supplierMail")
        self.le_supplierMail.setMaxLength(20)
        self.le_supplierMail.setClearButtonEnabled(True)

        self.verticalLayout_64.addWidget(self.le_supplierMail)


        self.verticalLayout_56.addWidget(self.gb_supplier)

        self.f_expenseDbBtn_3 = QFrame(self.f_supplierInputs)
        self.f_expenseDbBtn_3.setObjectName(u"f_expenseDbBtn_3")
        sizePolicy1.setHeightForWidth(self.f_expenseDbBtn_3.sizePolicy().hasHeightForWidth())
        self.f_expenseDbBtn_3.setSizePolicy(sizePolicy1)
        self.f_expenseDbBtn_3.setFrameShape(QFrame.StyledPanel)
        self.f_expenseDbBtn_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.f_expenseDbBtn_3)
        self.horizontalLayout_43.setSpacing(5)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.btn_supplierAdd = QPushButton(self.f_expenseDbBtn_3)
        self.btn_supplierAdd.setObjectName(u"btn_supplierAdd")
        self.btn_supplierAdd.setIcon(icon35)
        self.btn_supplierAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_43.addWidget(self.btn_supplierAdd)

        self.btn_supplierEdit = QPushButton(self.f_expenseDbBtn_3)
        self.btn_supplierEdit.setObjectName(u"btn_supplierEdit")
        self.btn_supplierEdit.setEnabled(False)
        self.btn_supplierEdit.setIcon(icon36)
        self.btn_supplierEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_43.addWidget(self.btn_supplierEdit)

        self.btn_supplierDelete = QPushButton(self.f_expenseDbBtn_3)
        self.btn_supplierDelete.setObjectName(u"btn_supplierDelete")
        self.btn_supplierDelete.setEnabled(False)
        self.btn_supplierDelete.setIcon(icon22)
        self.btn_supplierDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_43.addWidget(self.btn_supplierDelete)

        self.btn_supplierClear = QPushButton(self.f_expenseDbBtn_3)
        self.btn_supplierClear.setObjectName(u"btn_supplierClear")
        self.btn_supplierClear.setEnabled(True)
        self.btn_supplierClear.setIcon(icon23)
        self.btn_supplierClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_43.addWidget(self.btn_supplierClear)


        self.verticalLayout_56.addWidget(self.f_expenseDbBtn_3)


        self.horizontalLayout_47.addWidget(self.f_supplierInputs)

        self.f_supplierDb = QFrame(self.tab_supplier)
        self.f_supplierDb.setObjectName(u"f_supplierDb")
        self.f_supplierDb.setFrameShape(QFrame.StyledPanel)
        self.f_supplierDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.f_supplierDb)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.tw_supplier = QTableWidget(self.f_supplierDb)
        self.tw_supplier.setObjectName(u"tw_supplier")
        self.tw_supplier.setFont(font8)
        self.tw_supplier.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_supplier.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_supplier.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_supplier.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_supplier.verticalHeader().setCascadingSectionResizes(True)
        self.tw_supplier.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_55.addWidget(self.tw_supplier)


        self.horizontalLayout_47.addWidget(self.f_supplierDb)

        self.tw_database.addTab(self.tab_supplier, icon21, "")
        self.tab_customer = QWidget()
        self.tab_customer.setObjectName(u"tab_customer")
        self.horizontalLayout_10 = QHBoxLayout(self.tab_customer)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.f_customerInput = QFrame(self.tab_customer)
        self.f_customerInput.setObjectName(u"f_customerInput")
        self.f_customerInput.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_customerInput.setFrameShape(QFrame.StyledPanel)
        self.f_customerInput.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.f_customerInput)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.gb_customer = QGroupBox(self.f_customerInput)
        self.gb_customer.setObjectName(u"gb_customer")
        self.gb_customer.setFont(font5)
        self.gb_customer.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"")
        self.verticalLayout_24 = QVBoxLayout(self.gb_customer)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.f_customerPic = QFrame(self.gb_customer)
        self.f_customerPic.setObjectName(u"f_customerPic")
        sizePolicy12.setHeightForWidth(self.f_customerPic.sizePolicy().hasHeightForWidth())
        self.f_customerPic.setSizePolicy(sizePolicy12)
        self.f_customerPic.setMinimumSize(QSize(100, 100))
        self.f_customerPic.setMaximumSize(QSize(800, 300))
        self.f_customerPic.setLayoutDirection(Qt.LeftToRight)
        self.f_customerPic.setStyleSheet(u"")
        self.f_customerPic.setFrameShape(QFrame.StyledPanel)
        self.f_customerPic.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.f_customerPic)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.l_customerPicture = QLabel(self.f_customerPic)
        self.l_customerPicture.setObjectName(u"l_customerPicture")
        sizePolicy.setHeightForWidth(self.l_customerPicture.sizePolicy().hasHeightForWidth())
        self.l_customerPicture.setSizePolicy(sizePolicy)
        self.l_customerPicture.setMinimumSize(QSize(250, 200))
        self.l_customerPicture.setMaximumSize(QSize(300, 300))
        self.l_customerPicture.setBaseSize(QSize(200, 200))
        self.l_customerPicture.setFont(font15)
        self.l_customerPicture.setLayoutDirection(Qt.LeftToRight)
        self.l_customerPicture.setAutoFillBackground(False)
        self.l_customerPicture.setStyleSheet(u"")
        self.l_customerPicture.setFrameShape(QFrame.Box)
        self.l_customerPicture.setFrameShadow(QFrame.Plain)
        self.l_customerPicture.setScaledContents(True)
        self.l_customerPicture.setAlignment(Qt.AlignCenter)
        self.l_customerPicture.setWordWrap(False)

        self.horizontalLayout_27.addWidget(self.l_customerPicture)

        self.f_customerSetting = QFrame(self.f_customerPic)
        self.f_customerSetting.setObjectName(u"f_customerSetting")
        self.f_customerSetting.setFrameShape(QFrame.StyledPanel)
        self.f_customerSetting.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.f_customerSetting)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.btn_customerPicture = QPushButton(self.f_customerSetting)
        self.btn_customerPicture.setObjectName(u"btn_customerPicture")
        sizePolicy12.setHeightForWidth(self.btn_customerPicture.sizePolicy().hasHeightForWidth())
        self.btn_customerPicture.setSizePolicy(sizePolicy12)
        self.btn_customerPicture.setIcon(icon40)
        self.btn_customerPicture.setIconSize(QSize(32, 32))

        self.verticalLayout_45.addWidget(self.btn_customerPicture)

        self.btn_customerPictureClear = QPushButton(self.f_customerSetting)
        self.btn_customerPictureClear.setObjectName(u"btn_customerPictureClear")
        sizePolicy12.setHeightForWidth(self.btn_customerPictureClear.sizePolicy().hasHeightForWidth())
        self.btn_customerPictureClear.setSizePolicy(sizePolicy12)
        self.btn_customerPictureClear.setIcon(icon23)
        self.btn_customerPictureClear.setIconSize(QSize(32, 32))

        self.verticalLayout_45.addWidget(self.btn_customerPictureClear)


        self.horizontalLayout_27.addWidget(self.f_customerSetting)


        self.verticalLayout_24.addWidget(self.f_customerPic)

        self.le_customerName = QLineEdit(self.gb_customer)
        self.le_customerName.setObjectName(u"le_customerName")
        self.le_customerName.setInputMethodHints(Qt.ImhHiddenText)
        self.le_customerName.setMaxLength(150)
        self.le_customerName.setClearButtonEnabled(True)

        self.verticalLayout_24.addWidget(self.le_customerName)

        self.le_customerPhone = QLineEdit(self.gb_customer)
        self.le_customerPhone.setObjectName(u"le_customerPhone")
        self.le_customerPhone.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)
        self.le_customerPhone.setMaxLength(20)
        self.le_customerPhone.setClearButtonEnabled(True)

        self.verticalLayout_24.addWidget(self.le_customerPhone)

        self.le_customerAddress = QLineEdit(self.gb_customer)
        self.le_customerAddress.setObjectName(u"le_customerAddress")
        self.le_customerAddress.setMaxLength(250)
        self.le_customerAddress.setClearButtonEnabled(True)

        self.verticalLayout_24.addWidget(self.le_customerAddress)

        self.le_customerScore = QLineEdit(self.gb_customer)
        self.le_customerScore.setObjectName(u"le_customerScore")
        self.le_customerScore.setInputMethodHints(Qt.ImhDigitsOnly)
        self.le_customerScore.setMaxLength(32767)
        self.le_customerScore.setClearButtonEnabled(True)

        self.verticalLayout_24.addWidget(self.le_customerScore)


        self.verticalLayout_40.addWidget(self.gb_customer)

        self.f_customerDbBtn = QFrame(self.f_customerInput)
        self.f_customerDbBtn.setObjectName(u"f_customerDbBtn")
        sizePolicy1.setHeightForWidth(self.f_customerDbBtn.sizePolicy().hasHeightForWidth())
        self.f_customerDbBtn.setSizePolicy(sizePolicy1)
        self.f_customerDbBtn.setFrameShape(QFrame.StyledPanel)
        self.f_customerDbBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.f_customerDbBtn)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.btn_customerAdd = QPushButton(self.f_customerDbBtn)
        self.btn_customerAdd.setObjectName(u"btn_customerAdd")
        self.btn_customerAdd.setIcon(icon35)
        self.btn_customerAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_19.addWidget(self.btn_customerAdd)

        self.btn_customerEdit = QPushButton(self.f_customerDbBtn)
        self.btn_customerEdit.setObjectName(u"btn_customerEdit")
        self.btn_customerEdit.setEnabled(False)
        self.btn_customerEdit.setIcon(icon36)
        self.btn_customerEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_19.addWidget(self.btn_customerEdit)

        self.btn_customerDelete = QPushButton(self.f_customerDbBtn)
        self.btn_customerDelete.setObjectName(u"btn_customerDelete")
        self.btn_customerDelete.setEnabled(False)
        self.btn_customerDelete.setIcon(icon22)
        self.btn_customerDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_19.addWidget(self.btn_customerDelete)

        self.btn_customerClear = QPushButton(self.f_customerDbBtn)
        self.btn_customerClear.setObjectName(u"btn_customerClear")
        self.btn_customerClear.setEnabled(True)
        self.btn_customerClear.setIcon(icon23)
        self.btn_customerClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_19.addWidget(self.btn_customerClear)


        self.verticalLayout_40.addWidget(self.f_customerDbBtn)


        self.horizontalLayout_10.addWidget(self.f_customerInput)

        self.f_cutosmerDb = QFrame(self.tab_customer)
        self.f_cutosmerDb.setObjectName(u"f_cutosmerDb")
        self.f_cutosmerDb.setFrameShape(QFrame.StyledPanel)
        self.f_cutosmerDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.f_cutosmerDb)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.tw_customer = QTableWidget(self.f_cutosmerDb)
        self.tw_customer.setObjectName(u"tw_customer")
        self.tw_customer.setFont(font9)
        self.tw_customer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_customer.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_customer.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_customer.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_customer.verticalHeader().setCascadingSectionResizes(True)
        self.tw_customer.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_23.addWidget(self.tw_customer)


        self.horizontalLayout_10.addWidget(self.f_cutosmerDb)

        icon47 = QIcon()
        icon47.addFile(u":/Simple icons/simple_icons/fi-rr-comment-user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_database.addTab(self.tab_customer, icon47, "")
        self.tab_worker = QWidget()
        self.tab_worker.setObjectName(u"tab_worker")
        self.horizontalLayout_11 = QHBoxLayout(self.tab_worker)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.f_workerInput = QFrame(self.tab_worker)
        self.f_workerInput.setObjectName(u"f_workerInput")
        self.f_workerInput.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
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
        self.f_workerInput.setFrameShape(QFrame.StyledPanel)
        self.f_workerInput.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.f_workerInput)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.gb_worker = QGroupBox(self.f_workerInput)
        self.gb_worker.setObjectName(u"gb_worker")
        self.gb_worker.setFont(font5)
        self.gb_worker.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.gb_worker)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.f_workerPic = QFrame(self.gb_worker)
        self.f_workerPic.setObjectName(u"f_workerPic")
        sizePolicy12.setHeightForWidth(self.f_workerPic.sizePolicy().hasHeightForWidth())
        self.f_workerPic.setSizePolicy(sizePolicy12)
        self.f_workerPic.setMinimumSize(QSize(50, 50))
        self.f_workerPic.setMaximumSize(QSize(800, 300))
        self.f_workerPic.setLayoutDirection(Qt.LeftToRight)
        self.f_workerPic.setStyleSheet(u"")
        self.f_workerPic.setFrameShape(QFrame.StyledPanel)
        self.f_workerPic.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.f_workerPic)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.l_workerPicture = QLabel(self.f_workerPic)
        self.l_workerPicture.setObjectName(u"l_workerPicture")
        sizePolicy.setHeightForWidth(self.l_workerPicture.sizePolicy().hasHeightForWidth())
        self.l_workerPicture.setSizePolicy(sizePolicy)
        self.l_workerPicture.setMinimumSize(QSize(50, 50))
        self.l_workerPicture.setMaximumSize(QSize(300, 300))
        self.l_workerPicture.setBaseSize(QSize(200, 200))
        self.l_workerPicture.setFont(font15)
        self.l_workerPicture.setLayoutDirection(Qt.LeftToRight)
        self.l_workerPicture.setAutoFillBackground(False)
        self.l_workerPicture.setStyleSheet(u"")
        self.l_workerPicture.setFrameShape(QFrame.Box)
        self.l_workerPicture.setFrameShadow(QFrame.Plain)
        self.l_workerPicture.setScaledContents(True)
        self.l_workerPicture.setAlignment(Qt.AlignCenter)
        self.l_workerPicture.setWordWrap(False)

        self.horizontalLayout_28.addWidget(self.l_workerPicture)

        self.f_workerPictureSetting = QFrame(self.f_workerPic)
        self.f_workerPictureSetting.setObjectName(u"f_workerPictureSetting")
        self.f_workerPictureSetting.setFrameShape(QFrame.StyledPanel)
        self.f_workerPictureSetting.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.f_workerPictureSetting)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.btn_workerPicture = QPushButton(self.f_workerPictureSetting)
        self.btn_workerPicture.setObjectName(u"btn_workerPicture")
        sizePolicy12.setHeightForWidth(self.btn_workerPicture.sizePolicy().hasHeightForWidth())
        self.btn_workerPicture.setSizePolicy(sizePolicy12)
        self.btn_workerPicture.setIcon(icon40)
        self.btn_workerPicture.setIconSize(QSize(32, 32))

        self.verticalLayout_46.addWidget(self.btn_workerPicture)

        self.btn_workerPictureClear = QPushButton(self.f_workerPictureSetting)
        self.btn_workerPictureClear.setObjectName(u"btn_workerPictureClear")
        sizePolicy12.setHeightForWidth(self.btn_workerPictureClear.sizePolicy().hasHeightForWidth())
        self.btn_workerPictureClear.setSizePolicy(sizePolicy12)
        self.btn_workerPictureClear.setIcon(icon23)
        self.btn_workerPictureClear.setIconSize(QSize(32, 32))

        self.verticalLayout_46.addWidget(self.btn_workerPictureClear)


        self.horizontalLayout_28.addWidget(self.f_workerPictureSetting)


        self.verticalLayout_25.addWidget(self.f_workerPic)

        self.le_workerName = QLineEdit(self.gb_worker)
        self.le_workerName.setObjectName(u"le_workerName")
        self.le_workerName.setMaxLength(40)
        self.le_workerName.setClearButtonEnabled(True)

        self.verticalLayout_25.addWidget(self.le_workerName)

        self.cb_workerCategory = QComboBox(self.gb_worker)
        self.cb_workerCategory.setObjectName(u"cb_workerCategory")

        self.verticalLayout_25.addWidget(self.cb_workerCategory)

        self.le_workerUsername = QLineEdit(self.gb_worker)
        self.le_workerUsername.setObjectName(u"le_workerUsername")
        self.le_workerUsername.setMaxLength(20)
        self.le_workerUsername.setClearButtonEnabled(True)

        self.verticalLayout_25.addWidget(self.le_workerUsername)

        self.le_workerPassword = QLineEdit(self.gb_worker)
        self.le_workerPassword.setObjectName(u"le_workerPassword")
        self.le_workerPassword.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.le_workerPassword.setMaxLength(20)
        self.le_workerPassword.setEchoMode(QLineEdit.Password)
        self.le_workerPassword.setClearButtonEnabled(True)

        self.verticalLayout_25.addWidget(self.le_workerPassword)

        self.le_workerPhone = QLineEdit(self.gb_worker)
        self.le_workerPhone.setObjectName(u"le_workerPhone")
        self.le_workerPhone.setMaxLength(20)
        self.le_workerPhone.setClearButtonEnabled(True)

        self.verticalLayout_25.addWidget(self.le_workerPhone)

        self.le_workerAddress = QLineEdit(self.gb_worker)
        self.le_workerAddress.setObjectName(u"le_workerAddress")
        self.le_workerAddress.setMaxLength(250)
        self.le_workerAddress.setClearButtonEnabled(True)

        self.verticalLayout_25.addWidget(self.le_workerAddress)

        self.le_workerSalary = QLineEdit(self.gb_worker)
        self.le_workerSalary.setObjectName(u"le_workerSalary")

        self.verticalLayout_25.addWidget(self.le_workerSalary)

        self.le_workerScore = QLineEdit(self.gb_worker)
        self.le_workerScore.setObjectName(u"le_workerScore")
        self.le_workerScore.setMaxLength(20)
        self.le_workerScore.setClearButtonEnabled(True)

        self.verticalLayout_25.addWidget(self.le_workerScore)

        self.frame_33 = QFrame(self.gb_worker)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy1.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy1)
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.le_workerCv = QLineEdit(self.frame_33)
        self.le_workerCv.setObjectName(u"le_workerCv")
        self.le_workerCv.setEnabled(False)
        self.le_workerCv.setMaxLength(20)
        self.le_workerCv.setClearButtonEnabled(True)

        self.horizontalLayout_58.addWidget(self.le_workerCv)

        self.btn_workerAddCv = QPushButton(self.frame_33)
        self.btn_workerAddCv.setObjectName(u"btn_workerAddCv")
        sizePolicy12.setHeightForWidth(self.btn_workerAddCv.sizePolicy().hasHeightForWidth())
        self.btn_workerAddCv.setSizePolicy(sizePolicy12)
        icon48 = QIcon()
        icon48.addFile(u":/Simple icons/simple_icons/fi-rr-file-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_workerAddCv.setIcon(icon48)
        self.btn_workerAddCv.setIconSize(QSize(32, 32))

        self.horizontalLayout_58.addWidget(self.btn_workerAddCv)

        self.btn_workerOpenCv = QPushButton(self.frame_33)
        self.btn_workerOpenCv.setObjectName(u"btn_workerOpenCv")
        sizePolicy12.setHeightForWidth(self.btn_workerOpenCv.sizePolicy().hasHeightForWidth())
        self.btn_workerOpenCv.setSizePolicy(sizePolicy12)
        icon49 = QIcon()
        icon49.addFile(u":/Simple icons/simple_icons/fi-rr-search-alt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_workerOpenCv.setIcon(icon49)
        self.btn_workerOpenCv.setIconSize(QSize(32, 32))

        self.horizontalLayout_58.addWidget(self.btn_workerOpenCv)

        self.btn_workerClearCv = QPushButton(self.frame_33)
        self.btn_workerClearCv.setObjectName(u"btn_workerClearCv")
        sizePolicy12.setHeightForWidth(self.btn_workerClearCv.sizePolicy().hasHeightForWidth())
        self.btn_workerClearCv.setSizePolicy(sizePolicy12)
        self.btn_workerClearCv.setIcon(icon23)
        self.btn_workerClearCv.setIconSize(QSize(32, 32))

        self.horizontalLayout_58.addWidget(self.btn_workerClearCv)


        self.verticalLayout_25.addWidget(self.frame_33)


        self.verticalLayout_35.addWidget(self.gb_worker)

        self.f_workerDbBtn = QFrame(self.f_workerInput)
        self.f_workerDbBtn.setObjectName(u"f_workerDbBtn")
        sizePolicy1.setHeightForWidth(self.f_workerDbBtn.sizePolicy().hasHeightForWidth())
        self.f_workerDbBtn.setSizePolicy(sizePolicy1)
        self.f_workerDbBtn.setFrameShape(QFrame.StyledPanel)
        self.f_workerDbBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.f_workerDbBtn)
        self.horizontalLayout_20.setSpacing(5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.btn_workerAdd = QPushButton(self.f_workerDbBtn)
        self.btn_workerAdd.setObjectName(u"btn_workerAdd")
        self.btn_workerAdd.setIcon(icon35)
        self.btn_workerAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.btn_workerAdd)

        self.btn_workerEdit = QPushButton(self.f_workerDbBtn)
        self.btn_workerEdit.setObjectName(u"btn_workerEdit")
        self.btn_workerEdit.setEnabled(False)
        self.btn_workerEdit.setIcon(icon36)
        self.btn_workerEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.btn_workerEdit)

        self.btn_workerDelete = QPushButton(self.f_workerDbBtn)
        self.btn_workerDelete.setObjectName(u"btn_workerDelete")
        self.btn_workerDelete.setEnabled(False)
        self.btn_workerDelete.setIcon(icon22)
        self.btn_workerDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.btn_workerDelete)

        self.btn_workerClear = QPushButton(self.f_workerDbBtn)
        self.btn_workerClear.setObjectName(u"btn_workerClear")
        self.btn_workerClear.setEnabled(True)
        self.btn_workerClear.setIcon(icon23)
        self.btn_workerClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.btn_workerClear)


        self.verticalLayout_35.addWidget(self.f_workerDbBtn)


        self.horizontalLayout_11.addWidget(self.f_workerInput)

        self.f_workerDb = QFrame(self.tab_worker)
        self.f_workerDb.setObjectName(u"f_workerDb")
        self.f_workerDb.setFrameShape(QFrame.StyledPanel)
        self.f_workerDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.f_workerDb)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.tw_worker = QTableWidget(self.f_workerDb)
        self.tw_worker.setObjectName(u"tw_worker")
        self.tw_worker.setFont(font9)
        self.tw_worker.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_worker.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_worker.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_worker.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_worker.verticalHeader().setCascadingSectionResizes(True)
        self.tw_worker.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_30.addWidget(self.tw_worker)


        self.horizontalLayout_11.addWidget(self.f_workerDb)

        icon50 = QIcon()
        icon50.addFile(u":/Simple icons/simple_icons/fi-rr-id-badge.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_database.addTab(self.tab_worker, icon50, "")
        self.tab_category = QWidget()
        self.tab_category.setObjectName(u"tab_category")
        self.horizontalLayout_14 = QHBoxLayout(self.tab_category)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.f_categoryInput = QFrame(self.tab_category)
        self.f_categoryInput.setObjectName(u"f_categoryInput")
        self.f_categoryInput.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_categoryInput.setFrameShape(QFrame.StyledPanel)
        self.f_categoryInput.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.f_categoryInput)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.gb_category = QGroupBox(self.f_categoryInput)
        self.gb_category.setObjectName(u"gb_category")
        self.gb_category.setFont(font5)
        self.gb_category.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.verticalLayout_28 = QVBoxLayout(self.gb_category)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.le_categoryName = QLineEdit(self.gb_category)
        self.le_categoryName.setObjectName(u"le_categoryName")
        self.le_categoryName.setMaxLength(20)
        self.le_categoryName.setClearButtonEnabled(True)

        self.verticalLayout_28.addWidget(self.le_categoryName)

        self.frame_32 = QFrame(self.gb_category)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_32)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.cb_categoryLevelCashier = QCheckBox(self.frame_32)
        self.cb_categoryLevelCashier.setObjectName(u"cb_categoryLevelCashier")
        self.cb_categoryLevelCashier.setIcon(icon3)
        self.cb_categoryLevelCashier.setIconSize(QSize(32, 32))

        self.gridLayout_24.addWidget(self.cb_categoryLevelCashier, 0, 1, 1, 1)

        self.cb_categoryLevelWaste = QCheckBox(self.frame_32)
        self.cb_categoryLevelWaste.setObjectName(u"cb_categoryLevelWaste")
        self.cb_categoryLevelWaste.setIcon(icon5)
        self.cb_categoryLevelWaste.setIconSize(QSize(32, 32))

        self.gridLayout_24.addWidget(self.cb_categoryLevelWaste, 1, 1, 1, 1)

        self.cb_categoryLevelTables = QCheckBox(self.frame_32)
        self.cb_categoryLevelTables.setObjectName(u"cb_categoryLevelTables")
        self.cb_categoryLevelTables.setIcon(icon2)
        self.cb_categoryLevelTables.setIconSize(QSize(32, 32))

        self.gridLayout_24.addWidget(self.cb_categoryLevelTables, 0, 0, 1, 1)

        self.cb_categoryLevelStock = QCheckBox(self.frame_32)
        self.cb_categoryLevelStock.setObjectName(u"cb_categoryLevelStock")
        self.cb_categoryLevelStock.setIcon(icon49)
        self.cb_categoryLevelStock.setIconSize(QSize(32, 32))

        self.gridLayout_24.addWidget(self.cb_categoryLevelStock, 2, 0, 1, 1)

        self.cb_categoryLevelReservation = QCheckBox(self.frame_32)
        self.cb_categoryLevelReservation.setObjectName(u"cb_categoryLevelReservation")
        self.cb_categoryLevelReservation.setIcon(icon4)
        self.cb_categoryLevelReservation.setIconSize(QSize(32, 32))

        self.gridLayout_24.addWidget(self.cb_categoryLevelReservation, 1, 0, 1, 1)

        self.cb_categoryLevelReceipt = QCheckBox(self.frame_32)
        self.cb_categoryLevelReceipt.setObjectName(u"cb_categoryLevelReceipt")
        self.cb_categoryLevelReceipt.setIcon(icon7)
        self.cb_categoryLevelReceipt.setIconSize(QSize(32, 32))

        self.gridLayout_24.addWidget(self.cb_categoryLevelReceipt, 2, 1, 1, 1)

        self.cb_categoryLevelDb = QCheckBox(self.frame_32)
        self.cb_categoryLevelDb.setObjectName(u"cb_categoryLevelDb")
        self.cb_categoryLevelDb.setIcon(icon8)
        self.cb_categoryLevelDb.setIconSize(QSize(32, 32))

        self.gridLayout_24.addWidget(self.cb_categoryLevelDb, 3, 0, 1, 1)

        self.cb_categoryLevelPhone = QCheckBox(self.frame_32)
        self.cb_categoryLevelPhone.setObjectName(u"cb_categoryLevelPhone")
        self.cb_categoryLevelPhone.setIcon(icon9)
        self.cb_categoryLevelPhone.setIconSize(QSize(32, 32))

        self.gridLayout_24.addWidget(self.cb_categoryLevelPhone, 3, 1, 1, 1)

        self.cb_categoryLevelStat = QCheckBox(self.frame_32)
        self.cb_categoryLevelStat.setObjectName(u"cb_categoryLevelStat")
        self.cb_categoryLevelStat.setIcon(icon10)
        self.cb_categoryLevelStat.setIconSize(QSize(32, 32))

        self.gridLayout_24.addWidget(self.cb_categoryLevelStat, 4, 0, 1, 2)


        self.verticalLayout_28.addWidget(self.frame_32)


        self.verticalLayout_37.addWidget(self.gb_category)

        self.f_categoryDbBtn = QFrame(self.f_categoryInput)
        self.f_categoryDbBtn.setObjectName(u"f_categoryDbBtn")
        sizePolicy1.setHeightForWidth(self.f_categoryDbBtn.sizePolicy().hasHeightForWidth())
        self.f_categoryDbBtn.setSizePolicy(sizePolicy1)
        self.f_categoryDbBtn.setFrameShape(QFrame.StyledPanel)
        self.f_categoryDbBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.f_categoryDbBtn)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.btn_categoryAdd = QPushButton(self.f_categoryDbBtn)
        self.btn_categoryAdd.setObjectName(u"btn_categoryAdd")
        self.btn_categoryAdd.setIcon(icon35)
        self.btn_categoryAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_23.addWidget(self.btn_categoryAdd)

        self.btn_categoryEdit = QPushButton(self.f_categoryDbBtn)
        self.btn_categoryEdit.setObjectName(u"btn_categoryEdit")
        self.btn_categoryEdit.setEnabled(False)
        self.btn_categoryEdit.setIcon(icon36)
        self.btn_categoryEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_23.addWidget(self.btn_categoryEdit)

        self.btn_categoryDelete = QPushButton(self.f_categoryDbBtn)
        self.btn_categoryDelete.setObjectName(u"btn_categoryDelete")
        self.btn_categoryDelete.setEnabled(False)
        self.btn_categoryDelete.setIcon(icon22)
        self.btn_categoryDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_23.addWidget(self.btn_categoryDelete)

        self.btn_categoryClear = QPushButton(self.f_categoryDbBtn)
        self.btn_categoryClear.setObjectName(u"btn_categoryClear")
        self.btn_categoryClear.setEnabled(True)
        self.btn_categoryClear.setIcon(icon23)
        self.btn_categoryClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_23.addWidget(self.btn_categoryClear)


        self.verticalLayout_37.addWidget(self.f_categoryDbBtn)


        self.horizontalLayout_14.addWidget(self.f_categoryInput)

        self.f_categoryDb = QFrame(self.tab_category)
        self.f_categoryDb.setObjectName(u"f_categoryDb")
        self.f_categoryDb.setFrameShape(QFrame.StyledPanel)
        self.f_categoryDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.f_categoryDb)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.tw_category = QTableWidget(self.f_categoryDb)
        self.tw_category.setObjectName(u"tw_category")
        self.tw_category.setFont(font9)
        self.tw_category.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_category.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_category.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_category.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_category.verticalHeader().setCascadingSectionResizes(True)
        self.tw_category.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_33.addWidget(self.tw_category)


        self.horizontalLayout_14.addWidget(self.f_categoryDb)

        icon51 = QIcon()
        icon51.addFile(u":/Simple icons/simple_icons/fi-rr-diploma.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_database.addTab(self.tab_category, icon51, "")
        self.tab_sell = QWidget()
        self.tab_sell.setObjectName(u"tab_sell")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_sell)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.f_sellInput = QFrame(self.tab_sell)
        self.f_sellInput.setObjectName(u"f_sellInput")
        self.f_sellInput.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_sellInput.setFrameShape(QFrame.StyledPanel)
        self.f_sellInput.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.f_sellInput)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.gb_sell = QGroupBox(self.f_sellInput)
        self.gb_sell.setObjectName(u"gb_sell")
        self.gb_sell.setFont(font5)
        self.gb_sell.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.verticalLayout_26 = QVBoxLayout(self.gb_sell)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.cb_sellIdWorker = QComboBox(self.gb_sell)
        self.cb_sellIdWorker.setObjectName(u"cb_sellIdWorker")

        self.verticalLayout_26.addWidget(self.cb_sellIdWorker)

        self.cb_sellIdCustomer = QComboBox(self.gb_sell)
        self.cb_sellIdCustomer.setObjectName(u"cb_sellIdCustomer")

        self.verticalLayout_26.addWidget(self.cb_sellIdCustomer)

        self.dte_sellDate = QDateTimeEdit(self.gb_sell)
        self.dte_sellDate.setObjectName(u"dte_sellDate")
        self.dte_sellDate.setFont(font5)
        self.dte_sellDate.setCalendarPopup(True)

        self.verticalLayout_26.addWidget(self.dte_sellDate)

        self.le_sellTotal = QLineEdit(self.gb_sell)
        self.le_sellTotal.setObjectName(u"le_sellTotal")
        self.le_sellTotal.setMaxLength(20)
        self.le_sellTotal.setClearButtonEnabled(True)

        self.verticalLayout_26.addWidget(self.le_sellTotal)

        self.le_sellNbCovers = QLineEdit(self.gb_sell)
        self.le_sellNbCovers.setObjectName(u"le_sellNbCovers")
        self.le_sellNbCovers.setMaxLength(20)
        self.le_sellNbCovers.setClearButtonEnabled(True)

        self.verticalLayout_26.addWidget(self.le_sellNbCovers)


        self.verticalLayout_39.addWidget(self.gb_sell)

        self.f_sellDbBtn = QFrame(self.f_sellInput)
        self.f_sellDbBtn.setObjectName(u"f_sellDbBtn")
        sizePolicy1.setHeightForWidth(self.f_sellDbBtn.sizePolicy().hasHeightForWidth())
        self.f_sellDbBtn.setSizePolicy(sizePolicy1)
        self.f_sellDbBtn.setFrameShape(QFrame.StyledPanel)
        self.f_sellDbBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.f_sellDbBtn)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.btn_sellAdd = QPushButton(self.f_sellDbBtn)
        self.btn_sellAdd.setObjectName(u"btn_sellAdd")
        self.btn_sellAdd.setIcon(icon35)
        self.btn_sellAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.btn_sellAdd)

        self.btn_sellEdit = QPushButton(self.f_sellDbBtn)
        self.btn_sellEdit.setObjectName(u"btn_sellEdit")
        self.btn_sellEdit.setEnabled(False)
        self.btn_sellEdit.setIcon(icon36)
        self.btn_sellEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.btn_sellEdit)

        self.btn_sellDelete = QPushButton(self.f_sellDbBtn)
        self.btn_sellDelete.setObjectName(u"btn_sellDelete")
        self.btn_sellDelete.setEnabled(False)
        self.btn_sellDelete.setIcon(icon22)
        self.btn_sellDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.btn_sellDelete)

        self.btn_sellClear = QPushButton(self.f_sellDbBtn)
        self.btn_sellClear.setObjectName(u"btn_sellClear")
        self.btn_sellClear.setEnabled(True)
        self.btn_sellClear.setIcon(icon23)
        self.btn_sellClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.btn_sellClear)

        self.btn_sellShow = QPushButton(self.f_sellDbBtn)
        self.btn_sellShow.setObjectName(u"btn_sellShow")
        self.btn_sellShow.setEnabled(False)
        icon52 = QIcon()
        icon52.addFile(u":/Simple icons/simple_icons/fi-rr-upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sellShow.setIcon(icon52)
        self.btn_sellShow.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.btn_sellShow)

        self.btn_sellLoad = QPushButton(self.f_sellDbBtn)
        self.btn_sellLoad.setObjectName(u"btn_sellLoad")
        self.btn_sellLoad.setEnabled(False)
        icon53 = QIcon()
        icon53.addFile(u":/Simple icons/simple_icons/fi-rr-calculator.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sellLoad.setIcon(icon53)
        self.btn_sellLoad.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.btn_sellLoad)

        self.btn_sellHistory = QPushButton(self.f_sellDbBtn)
        self.btn_sellHistory.setObjectName(u"btn_sellHistory")
        self.btn_sellHistory.setEnabled(False)
        icon54 = QIcon()
        icon54.addFile(u":/Simple icons/simple_icons/fi-rr-incognito.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sellHistory.setIcon(icon54)
        self.btn_sellHistory.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.btn_sellHistory)


        self.verticalLayout_39.addWidget(self.f_sellDbBtn)


        self.horizontalLayout_12.addWidget(self.f_sellInput)

        self.f_sellDb = QFrame(self.tab_sell)
        self.f_sellDb.setObjectName(u"f_sellDb")
        self.f_sellDb.setStyleSheet(u"")
        self.f_sellDb.setFrameShape(QFrame.StyledPanel)
        self.f_sellDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.f_sellDb)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.tb_sellOpenBrowser = QToolButton(self.f_sellDb)
        self.tb_sellOpenBrowser.setObjectName(u"tb_sellOpenBrowser")
        sizePolicy.setHeightForWidth(self.tb_sellOpenBrowser.sizePolicy().hasHeightForWidth())
        self.tb_sellOpenBrowser.setSizePolicy(sizePolicy)
        self.tb_sellOpenBrowser.setIcon(icon54)
        self.tb_sellOpenBrowser.setIconSize(QSize(32, 32))
        self.tb_sellOpenBrowser.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_31.addWidget(self.tb_sellOpenBrowser)

        self.tw_sell = QTableWidget(self.f_sellDb)
        self.tw_sell.setObjectName(u"tw_sell")
        self.tw_sell.setFont(font9)
        self.tw_sell.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_sell.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_sell.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_sell.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_sell.verticalHeader().setCascadingSectionResizes(True)
        self.tw_sell.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_31.addWidget(self.tw_sell)


        self.horizontalLayout_12.addWidget(self.f_sellDb)

        self.tw_database.addTab(self.tab_sell, icon28, "")
        self.tab_table = QWidget()
        self.tab_table.setObjectName(u"tab_table")
        self.horizontalLayout_13 = QHBoxLayout(self.tab_table)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.f_tableInput = QFrame(self.tab_table)
        self.f_tableInput.setObjectName(u"f_tableInput")
        self.f_tableInput.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_tableInput.setFrameShape(QFrame.StyledPanel)
        self.f_tableInput.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.f_tableInput)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.gb_expense_6 = QGroupBox(self.f_tableInput)
        self.gb_expense_6.setObjectName(u"gb_expense_6")
        self.gb_expense_6.setFont(font5)
        self.gb_expense_6.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"")
        self.verticalLayout_27 = QVBoxLayout(self.gb_expense_6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.le_tableName = QLineEdit(self.gb_expense_6)
        self.le_tableName.setObjectName(u"le_tableName")
        self.le_tableName.setMaxLength(20)
        self.le_tableName.setClearButtonEnabled(True)

        self.verticalLayout_27.addWidget(self.le_tableName)

        self.le_tableId = QLineEdit(self.gb_expense_6)
        self.le_tableId.setObjectName(u"le_tableId")
        self.le_tableId.setMaxLength(20)
        self.le_tableId.setClearButtonEnabled(True)

        self.verticalLayout_27.addWidget(self.le_tableId)

        self.le_tableSeats = QLineEdit(self.gb_expense_6)
        self.le_tableSeats.setObjectName(u"le_tableSeats")
        self.le_tableSeats.setMaxLength(20)
        self.le_tableSeats.setClearButtonEnabled(True)

        self.verticalLayout_27.addWidget(self.le_tableSeats)

        self.le_tableComment = QLineEdit(self.gb_expense_6)
        self.le_tableComment.setObjectName(u"le_tableComment")
        self.le_tableComment.setMaxLength(30)
        self.le_tableComment.setClearButtonEnabled(True)

        self.verticalLayout_27.addWidget(self.le_tableComment)


        self.verticalLayout_38.addWidget(self.gb_expense_6)

        self.f_tableDbBtn = QFrame(self.f_tableInput)
        self.f_tableDbBtn.setObjectName(u"f_tableDbBtn")
        sizePolicy1.setHeightForWidth(self.f_tableDbBtn.sizePolicy().hasHeightForWidth())
        self.f_tableDbBtn.setSizePolicy(sizePolicy1)
        self.f_tableDbBtn.setFrameShape(QFrame.StyledPanel)
        self.f_tableDbBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.f_tableDbBtn)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.btn_tableAdd = QPushButton(self.f_tableDbBtn)
        self.btn_tableAdd.setObjectName(u"btn_tableAdd")
        self.btn_tableAdd.setIcon(icon35)
        self.btn_tableAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_22.addWidget(self.btn_tableAdd)

        self.btn_tableEdit = QPushButton(self.f_tableDbBtn)
        self.btn_tableEdit.setObjectName(u"btn_tableEdit")
        self.btn_tableEdit.setEnabled(False)
        self.btn_tableEdit.setIcon(icon36)
        self.btn_tableEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_22.addWidget(self.btn_tableEdit)

        self.btn_tableDelete = QPushButton(self.f_tableDbBtn)
        self.btn_tableDelete.setObjectName(u"btn_tableDelete")
        self.btn_tableDelete.setEnabled(False)
        self.btn_tableDelete.setIcon(icon22)
        self.btn_tableDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_22.addWidget(self.btn_tableDelete)

        self.btn_tableClear = QPushButton(self.f_tableDbBtn)
        self.btn_tableClear.setObjectName(u"btn_tableClear")
        self.btn_tableClear.setEnabled(True)
        self.btn_tableClear.setIcon(icon23)
        self.btn_tableClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_22.addWidget(self.btn_tableClear)


        self.verticalLayout_38.addWidget(self.f_tableDbBtn)


        self.horizontalLayout_13.addWidget(self.f_tableInput)

        self.f_tableDb = QFrame(self.tab_table)
        self.f_tableDb.setObjectName(u"f_tableDb")
        self.f_tableDb.setFrameShape(QFrame.StyledPanel)
        self.f_tableDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.f_tableDb)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.tw_table = QTableWidget(self.f_tableDb)
        self.tw_table.setObjectName(u"tw_table")
        self.tw_table.setFont(font9)
        self.tw_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_table.verticalHeader().setCascadingSectionResizes(True)
        self.tw_table.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_32.addWidget(self.tw_table)


        self.horizontalLayout_13.addWidget(self.f_tableDb)

        self.tw_database.addTab(self.tab_table, icon2, "")
        self.tab_pointer = QWidget()
        self.tab_pointer.setObjectName(u"tab_pointer")
        self.horizontalLayout_15 = QHBoxLayout(self.tab_pointer)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.f_pointerDb = QFrame(self.tab_pointer)
        self.f_pointerDb.setObjectName(u"f_pointerDb")
        self.f_pointerDb.setFrameShape(QFrame.StyledPanel)
        self.f_pointerDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.f_pointerDb)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.groupBox = QGroupBox(self.f_pointerDb)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font5)
        self.groupBox.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.verticalLayout_47 = QVBoxLayout(self.groupBox)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.tw_pointer = QTableWidget(self.groupBox)
        self.tw_pointer.setObjectName(u"tw_pointer")
        self.tw_pointer.setFont(font9)
        self.tw_pointer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_pointer.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_pointer.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_pointer.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_pointer.verticalHeader().setCascadingSectionResizes(True)
        self.tw_pointer.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_47.addWidget(self.tw_pointer)


        self.verticalLayout_34.addWidget(self.groupBox)


        self.horizontalLayout_15.addWidget(self.f_pointerDb)

        self.tw_database.addTab(self.tab_pointer, icon49, "")
        self.tab_stock = QWidget()
        self.tab_stock.setObjectName(u"tab_stock")
        self.horizontalLayout_60 = QHBoxLayout(self.tab_stock)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.f_tableInput_2 = QFrame(self.tab_stock)
        self.f_tableInput_2.setObjectName(u"f_tableInput_2")
        self.f_tableInput_2.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.f_tableInput_2.setFrameShape(QFrame.StyledPanel)
        self.f_tableInput_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.f_tableInput_2)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.gb_stock = QGroupBox(self.f_tableInput_2)
        self.gb_stock.setObjectName(u"gb_stock")
        self.gb_stock.setFont(font5)
        self.gb_stock.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"")
        self.verticalLayout_79 = QVBoxLayout(self.gb_stock)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.le_stockProductName = QLineEdit(self.gb_stock)
        self.le_stockProductName.setObjectName(u"le_stockProductName")
        self.le_stockProductName.setMaxLength(20)
        self.le_stockProductName.setClearButtonEnabled(True)

        self.verticalLayout_79.addWidget(self.le_stockProductName)

        self.cb_stockCategory = QComboBox(self.gb_stock)
        self.cb_stockCategory.setObjectName(u"cb_stockCategory")

        self.verticalLayout_79.addWidget(self.cb_stockCategory)

        self.le_stockUnit = QLineEdit(self.gb_stock)
        self.le_stockUnit.setObjectName(u"le_stockUnit")
        self.le_stockUnit.setMaxLength(20)
        self.le_stockUnit.setClearButtonEnabled(True)

        self.verticalLayout_79.addWidget(self.le_stockUnit)

        self.le_stockQuantity = QLineEdit(self.gb_stock)
        self.le_stockQuantity.setObjectName(u"le_stockQuantity")
        self.le_stockQuantity.setMaxLength(30)
        self.le_stockQuantity.setClearButtonEnabled(True)

        self.verticalLayout_79.addWidget(self.le_stockQuantity)

        self.cb_stockIsIngredient = QCheckBox(self.gb_stock)
        self.cb_stockIsIngredient.setObjectName(u"cb_stockIsIngredient")
        self.cb_stockIsIngredient.setFont(font3)
        self.cb_stockIsIngredient.setLayoutDirection(Qt.LeftToRight)
        self.cb_stockIsIngredient.setIcon(icon45)
        self.cb_stockIsIngredient.setIconSize(QSize(32, 32))
        self.cb_stockIsIngredient.setChecked(True)

        self.verticalLayout_79.addWidget(self.cb_stockIsIngredient)


        self.verticalLayout_42.addWidget(self.gb_stock)

        self.f_tableDbBtn_2 = QFrame(self.f_tableInput_2)
        self.f_tableDbBtn_2.setObjectName(u"f_tableDbBtn_2")
        sizePolicy1.setHeightForWidth(self.f_tableDbBtn_2.sizePolicy().hasHeightForWidth())
        self.f_tableDbBtn_2.setSizePolicy(sizePolicy1)
        self.f_tableDbBtn_2.setFrameShape(QFrame.StyledPanel)
        self.f_tableDbBtn_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.f_tableDbBtn_2)
        self.horizontalLayout_59.setSpacing(5)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.btn_stockAdd = QPushButton(self.f_tableDbBtn_2)
        self.btn_stockAdd.setObjectName(u"btn_stockAdd")
        self.btn_stockAdd.setIcon(icon35)
        self.btn_stockAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_59.addWidget(self.btn_stockAdd)

        self.btn_stockEdit = QPushButton(self.f_tableDbBtn_2)
        self.btn_stockEdit.setObjectName(u"btn_stockEdit")
        self.btn_stockEdit.setEnabled(False)
        self.btn_stockEdit.setIcon(icon36)
        self.btn_stockEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_59.addWidget(self.btn_stockEdit)

        self.btn_stockDelete = QPushButton(self.f_tableDbBtn_2)
        self.btn_stockDelete.setObjectName(u"btn_stockDelete")
        self.btn_stockDelete.setEnabled(False)
        self.btn_stockDelete.setIcon(icon22)
        self.btn_stockDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_59.addWidget(self.btn_stockDelete)

        self.btn_stockClear = QPushButton(self.f_tableDbBtn_2)
        self.btn_stockClear.setObjectName(u"btn_stockClear")
        self.btn_stockClear.setEnabled(True)
        self.btn_stockClear.setIcon(icon23)
        self.btn_stockClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_59.addWidget(self.btn_stockClear)


        self.verticalLayout_42.addWidget(self.f_tableDbBtn_2)


        self.horizontalLayout_60.addWidget(self.f_tableInput_2)

        self.f_stockDb = QFrame(self.tab_stock)
        self.f_stockDb.setObjectName(u"f_stockDb")
        self.f_stockDb.setFrameShape(QFrame.StyledPanel)
        self.f_stockDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.f_stockDb)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.tw_stockDb = QTableWidget(self.f_stockDb)
        self.tw_stockDb.setObjectName(u"tw_stockDb")
        self.tw_stockDb.setFont(font9)
        self.tw_stockDb.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_stockDb.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_stockDb.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_stockDb.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_stockDb.verticalHeader().setCascadingSectionResizes(True)
        self.tw_stockDb.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_80.addWidget(self.tw_stockDb)


        self.horizontalLayout_60.addWidget(self.f_stockDb)

        self.tw_database.addTab(self.tab_stock, icon6, "")
        self.tab_uploader = QWidget()
        self.tab_uploader.setObjectName(u"tab_uploader")
        self.horizontalLayout_62 = QHBoxLayout(self.tab_uploader)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.f_tableInput_3 = QFrame(self.tab_uploader)
        self.f_tableInput_3.setObjectName(u"f_tableInput_3")
        self.f_tableInput_3.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_tableInput_3.setFrameShape(QFrame.StyledPanel)
        self.f_tableInput_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.f_tableInput_3)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.gb_doccuments = QGroupBox(self.f_tableInput_3)
        self.gb_doccuments.setObjectName(u"gb_doccuments")
        self.gb_doccuments.setFont(font5)
        self.gb_doccuments.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.verticalLayout_83 = QVBoxLayout(self.gb_doccuments)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.le_docName = QLineEdit(self.gb_doccuments)
        self.le_docName.setObjectName(u"le_docName")
        self.le_docName.setMaxLength(80)
        self.le_docName.setClearButtonEnabled(True)

        self.verticalLayout_83.addWidget(self.le_docName)

        self.dte_docDate = QDateTimeEdit(self.gb_doccuments)
        self.dte_docDate.setObjectName(u"dte_docDate")
        self.dte_docDate.setFont(font5)
        self.dte_docDate.setCalendarPopup(True)

        self.verticalLayout_83.addWidget(self.dte_docDate)

        self.le_docComment = QLineEdit(self.gb_doccuments)
        self.le_docComment.setObjectName(u"le_docComment")
        self.le_docComment.setMaxLength(250)
        self.le_docComment.setClearButtonEnabled(True)

        self.verticalLayout_83.addWidget(self.le_docComment)

        self.frame_40 = QFrame(self.gb_doccuments)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy1.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy1)
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.le_docPath = QLineEdit(self.frame_40)
        self.le_docPath.setObjectName(u"le_docPath")
        self.le_docPath.setEnabled(False)
        self.le_docPath.setMaxLength(20)
        self.le_docPath.setClearButtonEnabled(True)

        self.horizontalLayout_64.addWidget(self.le_docPath)

        self.btn_docAddFile = QPushButton(self.frame_40)
        self.btn_docAddFile.setObjectName(u"btn_docAddFile")
        sizePolicy12.setHeightForWidth(self.btn_docAddFile.sizePolicy().hasHeightForWidth())
        self.btn_docAddFile.setSizePolicy(sizePolicy12)
        self.btn_docAddFile.setIcon(icon48)
        self.btn_docAddFile.setIconSize(QSize(32, 32))

        self.horizontalLayout_64.addWidget(self.btn_docAddFile)

        self.btn_docOpenFile = QPushButton(self.frame_40)
        self.btn_docOpenFile.setObjectName(u"btn_docOpenFile")
        sizePolicy12.setHeightForWidth(self.btn_docOpenFile.sizePolicy().hasHeightForWidth())
        self.btn_docOpenFile.setSizePolicy(sizePolicy12)
        self.btn_docOpenFile.setIcon(icon49)
        self.btn_docOpenFile.setIconSize(QSize(32, 32))

        self.horizontalLayout_64.addWidget(self.btn_docOpenFile)

        self.btn_docClearFile = QPushButton(self.frame_40)
        self.btn_docClearFile.setObjectName(u"btn_docClearFile")
        sizePolicy12.setHeightForWidth(self.btn_docClearFile.sizePolicy().hasHeightForWidth())
        self.btn_docClearFile.setSizePolicy(sizePolicy12)
        self.btn_docClearFile.setIcon(icon23)
        self.btn_docClearFile.setIconSize(QSize(32, 32))

        self.horizontalLayout_64.addWidget(self.btn_docClearFile)


        self.verticalLayout_83.addWidget(self.frame_40)


        self.verticalLayout_82.addWidget(self.gb_doccuments)

        self.f_tableDbBtn_3 = QFrame(self.f_tableInput_3)
        self.f_tableDbBtn_3.setObjectName(u"f_tableDbBtn_3")
        sizePolicy1.setHeightForWidth(self.f_tableDbBtn_3.sizePolicy().hasHeightForWidth())
        self.f_tableDbBtn_3.setSizePolicy(sizePolicy1)
        self.f_tableDbBtn_3.setFrameShape(QFrame.StyledPanel)
        self.f_tableDbBtn_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.f_tableDbBtn_3)
        self.horizontalLayout_61.setSpacing(5)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.btn_docAdd = QPushButton(self.f_tableDbBtn_3)
        self.btn_docAdd.setObjectName(u"btn_docAdd")
        self.btn_docAdd.setIcon(icon35)
        self.btn_docAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_61.addWidget(self.btn_docAdd)

        self.btn_docEdit = QPushButton(self.f_tableDbBtn_3)
        self.btn_docEdit.setObjectName(u"btn_docEdit")
        self.btn_docEdit.setEnabled(False)
        self.btn_docEdit.setIcon(icon36)
        self.btn_docEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_61.addWidget(self.btn_docEdit)

        self.btn_docDelete = QPushButton(self.f_tableDbBtn_3)
        self.btn_docDelete.setObjectName(u"btn_docDelete")
        self.btn_docDelete.setEnabled(False)
        self.btn_docDelete.setIcon(icon22)
        self.btn_docDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_61.addWidget(self.btn_docDelete)

        self.btn_docClear = QPushButton(self.f_tableDbBtn_3)
        self.btn_docClear.setObjectName(u"btn_docClear")
        self.btn_docClear.setEnabled(True)
        self.btn_docClear.setIcon(icon23)
        self.btn_docClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_61.addWidget(self.btn_docClear)


        self.verticalLayout_82.addWidget(self.f_tableDbBtn_3)


        self.horizontalLayout_62.addWidget(self.f_tableInput_3)

        self.f_stockDb_2 = QFrame(self.tab_uploader)
        self.f_stockDb_2.setObjectName(u"f_stockDb_2")
        self.f_stockDb_2.setFrameShape(QFrame.StyledPanel)
        self.f_stockDb_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.f_stockDb_2)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.tw_documentDb = QTableWidget(self.f_stockDb_2)
        self.tw_documentDb.setObjectName(u"tw_documentDb")
        self.tw_documentDb.setFont(font9)
        self.tw_documentDb.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_documentDb.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_documentDb.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_documentDb.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_documentDb.verticalHeader().setCascadingSectionResizes(True)
        self.tw_documentDb.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_81.addWidget(self.tw_documentDb)


        self.horizontalLayout_62.addWidget(self.f_stockDb_2)

        self.tw_database.addTab(self.tab_uploader, icon52, "")
        self.tab_tableOwnership = QWidget()
        self.tab_tableOwnership.setObjectName(u"tab_tableOwnership")
        self.horizontalLayout_67 = QHBoxLayout(self.tab_tableOwnership)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.f_tableOwnershipInput = QFrame(self.tab_tableOwnership)
        self.f_tableOwnershipInput.setObjectName(u"f_tableOwnershipInput")
        self.f_tableOwnershipInput.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_tableOwnershipInput.setFrameShape(QFrame.StyledPanel)
        self.f_tableOwnershipInput.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.f_tableOwnershipInput)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.gb_tableOwnership = QGroupBox(self.f_tableOwnershipInput)
        self.gb_tableOwnership.setObjectName(u"gb_tableOwnership")
        self.gb_tableOwnership.setFont(font5)
        self.gb_tableOwnership.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.verticalLayout_89 = QVBoxLayout(self.gb_tableOwnership)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.cb_tableOwnershipTableId = QComboBox(self.gb_tableOwnership)
        self.cb_tableOwnershipTableId.setObjectName(u"cb_tableOwnershipTableId")
        sizePolicy13 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.cb_tableOwnershipTableId.sizePolicy().hasHeightForWidth())
        self.cb_tableOwnershipTableId.setSizePolicy(sizePolicy13)

        self.verticalLayout_89.addWidget(self.cb_tableOwnershipTableId)

        self.cb_tableOwnershipWorkerId = QComboBox(self.gb_tableOwnership)
        self.cb_tableOwnershipWorkerId.setObjectName(u"cb_tableOwnershipWorkerId")

        self.verticalLayout_89.addWidget(self.cb_tableOwnershipWorkerId)


        self.verticalLayout_88.addWidget(self.gb_tableOwnership)

        self.f_tableDbBtn_4 = QFrame(self.f_tableOwnershipInput)
        self.f_tableDbBtn_4.setObjectName(u"f_tableDbBtn_4")
        sizePolicy1.setHeightForWidth(self.f_tableDbBtn_4.sizePolicy().hasHeightForWidth())
        self.f_tableDbBtn_4.setSizePolicy(sizePolicy1)
        self.f_tableDbBtn_4.setFrameShape(QFrame.StyledPanel)
        self.f_tableDbBtn_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.f_tableDbBtn_4)
        self.horizontalLayout_66.setSpacing(5)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.btn_tableOwnershipAdd = QPushButton(self.f_tableDbBtn_4)
        self.btn_tableOwnershipAdd.setObjectName(u"btn_tableOwnershipAdd")
        self.btn_tableOwnershipAdd.setIcon(icon35)
        self.btn_tableOwnershipAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_66.addWidget(self.btn_tableOwnershipAdd)

        self.btn_tableOwnershipEdit = QPushButton(self.f_tableDbBtn_4)
        self.btn_tableOwnershipEdit.setObjectName(u"btn_tableOwnershipEdit")
        self.btn_tableOwnershipEdit.setEnabled(False)
        self.btn_tableOwnershipEdit.setIcon(icon36)
        self.btn_tableOwnershipEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_66.addWidget(self.btn_tableOwnershipEdit)

        self.btn_tableOwnershipDelete = QPushButton(self.f_tableDbBtn_4)
        self.btn_tableOwnershipDelete.setObjectName(u"btn_tableOwnershipDelete")
        self.btn_tableOwnershipDelete.setEnabled(False)
        self.btn_tableOwnershipDelete.setIcon(icon22)
        self.btn_tableOwnershipDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_66.addWidget(self.btn_tableOwnershipDelete)

        self.btn_tableOwnershipClear = QPushButton(self.f_tableDbBtn_4)
        self.btn_tableOwnershipClear.setObjectName(u"btn_tableOwnershipClear")
        self.btn_tableOwnershipClear.setEnabled(True)
        self.btn_tableOwnershipClear.setIcon(icon23)
        self.btn_tableOwnershipClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_66.addWidget(self.btn_tableOwnershipClear)


        self.verticalLayout_88.addWidget(self.f_tableDbBtn_4)


        self.horizontalLayout_67.addWidget(self.f_tableOwnershipInput)

        self.f_tableOwnershipDb = QFrame(self.tab_tableOwnership)
        self.f_tableOwnershipDb.setObjectName(u"f_tableOwnershipDb")
        sizePolicy14 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.f_tableOwnershipDb.sizePolicy().hasHeightForWidth())
        self.f_tableOwnershipDb.setSizePolicy(sizePolicy14)
        self.f_tableOwnershipDb.setFrameShape(QFrame.StyledPanel)
        self.f_tableOwnershipDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.f_tableOwnershipDb)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.tw_tableOwnershipDb = QTableWidget(self.f_tableOwnershipDb)
        self.tw_tableOwnershipDb.setObjectName(u"tw_tableOwnershipDb")
        self.tw_tableOwnershipDb.setFont(font9)
        self.tw_tableOwnershipDb.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_tableOwnershipDb.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_tableOwnershipDb.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_tableOwnershipDb.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_tableOwnershipDb.verticalHeader().setCascadingSectionResizes(True)
        self.tw_tableOwnershipDb.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_87.addWidget(self.tw_tableOwnershipDb)


        self.horizontalLayout_67.addWidget(self.f_tableOwnershipDb)

        icon55 = QIcon()
        icon55.addFile(u":/Simple icons/simple_icons/fi-rr-package.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_database.addTab(self.tab_tableOwnership, icon55, "")
        self.tab_payement = QWidget()
        self.tab_payement.setObjectName(u"tab_payement")
        self.horizontalLayout_78 = QHBoxLayout(self.tab_payement)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.f_paymentInput = QFrame(self.tab_payement)
        self.f_paymentInput.setObjectName(u"f_paymentInput")
        self.f_paymentInput.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_paymentInput.setFrameShape(QFrame.StyledPanel)
        self.f_paymentInput.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.f_paymentInput)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.gb_payment = QGroupBox(self.f_paymentInput)
        self.gb_payment.setObjectName(u"gb_payment")
        self.gb_payment.setFont(font5)
        self.gb_payment.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.verticalLayout_100 = QVBoxLayout(self.gb_payment)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.cb_payment_worker = QComboBox(self.gb_payment)
        self.cb_payment_worker.setObjectName(u"cb_payment_worker")
        sizePolicy13.setHeightForWidth(self.cb_payment_worker.sizePolicy().hasHeightForWidth())
        self.cb_payment_worker.setSizePolicy(sizePolicy13)

        self.verticalLayout_100.addWidget(self.cb_payment_worker)

        self.de_payment_date = QDateEdit(self.gb_payment)
        self.de_payment_date.setObjectName(u"de_payment_date")
        self.de_payment_date.setFont(font5)
        self.de_payment_date.setDateTime(QDateTime(QDate(2022, 5, 13), QTime(0, 0, 0)))
        self.de_payment_date.setCurrentSection(QDateTimeEdit.YearSection)
        self.de_payment_date.setCalendarPopup(True)

        self.verticalLayout_100.addWidget(self.de_payment_date)

        self.le_payment_amount = QLineEdit(self.gb_payment)
        self.le_payment_amount.setObjectName(u"le_payment_amount")

        self.verticalLayout_100.addWidget(self.le_payment_amount)


        self.verticalLayout_99.addWidget(self.gb_payment)

        self.f_paymentDbBtn = QFrame(self.f_paymentInput)
        self.f_paymentDbBtn.setObjectName(u"f_paymentDbBtn")
        sizePolicy1.setHeightForWidth(self.f_paymentDbBtn.sizePolicy().hasHeightForWidth())
        self.f_paymentDbBtn.setSizePolicy(sizePolicy1)
        self.f_paymentDbBtn.setFrameShape(QFrame.StyledPanel)
        self.f_paymentDbBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.f_paymentDbBtn)
        self.horizontalLayout_75.setSpacing(5)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.btn_paymentAdd = QPushButton(self.f_paymentDbBtn)
        self.btn_paymentAdd.setObjectName(u"btn_paymentAdd")
        self.btn_paymentAdd.setIcon(icon35)
        self.btn_paymentAdd.setIconSize(QSize(32, 32))

        self.horizontalLayout_75.addWidget(self.btn_paymentAdd)

        self.btn_paymentEdit = QPushButton(self.f_paymentDbBtn)
        self.btn_paymentEdit.setObjectName(u"btn_paymentEdit")
        self.btn_paymentEdit.setEnabled(False)
        self.btn_paymentEdit.setIcon(icon36)
        self.btn_paymentEdit.setIconSize(QSize(32, 32))

        self.horizontalLayout_75.addWidget(self.btn_paymentEdit)

        self.btn_paymentDelete = QPushButton(self.f_paymentDbBtn)
        self.btn_paymentDelete.setObjectName(u"btn_paymentDelete")
        self.btn_paymentDelete.setEnabled(False)
        self.btn_paymentDelete.setIcon(icon22)
        self.btn_paymentDelete.setIconSize(QSize(32, 32))

        self.horizontalLayout_75.addWidget(self.btn_paymentDelete)

        self.btn_paymentClear = QPushButton(self.f_paymentDbBtn)
        self.btn_paymentClear.setObjectName(u"btn_paymentClear")
        self.btn_paymentClear.setEnabled(True)
        self.btn_paymentClear.setIcon(icon23)
        self.btn_paymentClear.setIconSize(QSize(32, 32))

        self.horizontalLayout_75.addWidget(self.btn_paymentClear)


        self.verticalLayout_99.addWidget(self.f_paymentDbBtn)


        self.horizontalLayout_78.addWidget(self.f_paymentInput)

        self.f_paymentDb = QFrame(self.tab_payement)
        self.f_paymentDb.setObjectName(u"f_paymentDb")
        sizePolicy14.setHeightForWidth(self.f_paymentDb.sizePolicy().hasHeightForWidth())
        self.f_paymentDb.setSizePolicy(sizePolicy14)
        self.f_paymentDb.setFrameShape(QFrame.StyledPanel)
        self.f_paymentDb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.f_paymentDb)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.tw_paymentDb = QTableWidget(self.f_paymentDb)
        self.tw_paymentDb.setObjectName(u"tw_paymentDb")
        self.tw_paymentDb.setFont(font9)
        self.tw_paymentDb.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_paymentDb.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_paymentDb.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_paymentDb.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_paymentDb.verticalHeader().setCascadingSectionResizes(True)
        self.tw_paymentDb.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_98.addWidget(self.tw_paymentDb)


        self.horizontalLayout_78.addWidget(self.f_paymentDb)

        icon56 = QIcon()
        icon56.addFile(u":/Simple icons/simple_icons/fi-rr-hand-holding-heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tw_database.addTab(self.tab_payement, icon56, "")

        self.gridLayout_9.addWidget(self.tw_database, 0, 0, 1, 1)

        self.sw_content.addWidget(self.page_database)
        self.page_workerStatus = QWidget()
        self.page_workerStatus.setObjectName(u"page_workerStatus")
        self.page_workerStatus.setStyleSheet(u"QPushButton\n"
"{ \n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	padding: 2px;\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 50px 50px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(225, 225, 225, 255);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	alignment: \"center\"\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	alignment: \"center\";\n"
"	background: rgba(225, 225, 225, 200);\n"
"}")
        self.gridLayout_20 = QGridLayout(self.page_workerStatus)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.sa_workerStatus = QScrollArea(self.page_workerStatus)
        self.sa_workerStatus.setObjectName(u"sa_workerStatus")
        self.sa_workerStatus.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.sa_workerStatus.setWidgetResizable(True)
        self.w_workerStats = QWidget()
        self.w_workerStats.setObjectName(u"w_workerStats")
        self.w_workerStats.setGeometry(QRect(0, 0, 411, 175))
        self.gridLayout_21 = QGridLayout(self.w_workerStats)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame_13 = QFrame(self.w_workerStats)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(200, 200))
        self.frame_13.setFrameShape(QFrame.Box)
        self.frame_13.setFrameShadow(QFrame.Plain)
        self.verticalLayout_78 = QVBoxLayout(self.frame_13)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.label_30 = QLabel(self.frame_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_78.addWidget(self.label_30)

        self.textEdit = QTextEdit(self.frame_13)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_78.addWidget(self.textEdit)

        self.frame_291 = QFrame(self.frame_13)
        self.frame_291.setObjectName(u"frame_291")
        self.frame_291.setMaximumSize(QSize(200, 100))
        self.frame_291.setFrameShape(QFrame.StyledPanel)
        self.frame_291.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_291)
        self.horizontalLayout_55.setSpacing(5)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.pushButton_52 = QPushButton(self.frame_291)
        self.pushButton_52.setObjectName(u"pushButton_52")

        self.horizontalLayout_55.addWidget(self.pushButton_52)

        self.pushButton_53 = QPushButton(self.frame_291)
        self.pushButton_53.setObjectName(u"pushButton_53")

        self.horizontalLayout_55.addWidget(self.pushButton_53)


        self.verticalLayout_78.addWidget(self.frame_291)


        self.gridLayout_21.addWidget(self.frame_13, 0, 0, 1, 1)

        self.frame_43 = QFrame(self.w_workerStats)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMaximumSize(QSize(200, 200))
        self.frame_43.setFrameShape(QFrame.Box)
        self.frame_43.setFrameShadow(QFrame.Plain)
        self.verticalLayout_93 = QVBoxLayout(self.frame_43)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.label_42 = QLabel(self.frame_43)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.verticalLayout_93.addWidget(self.label_42)

        self.textEdit_2 = QTextEdit(self.frame_43)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verticalLayout_93.addWidget(self.textEdit_2)

        self.frame_45 = QFrame(self.frame_43)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMaximumSize(QSize(200, 100))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_70.setSpacing(5)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.pushButton_66 = QPushButton(self.frame_45)
        self.pushButton_66.setObjectName(u"pushButton_66")

        self.horizontalLayout_70.addWidget(self.pushButton_66)

        self.pushButton_67 = QPushButton(self.frame_45)
        self.pushButton_67.setObjectName(u"pushButton_67")

        self.horizontalLayout_70.addWidget(self.pushButton_67)


        self.verticalLayout_93.addWidget(self.frame_45)


        self.gridLayout_21.addWidget(self.frame_43, 0, 1, 1, 1)

        self.frame_46 = QFrame(self.w_workerStats)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMaximumSize(QSize(200, 200))
        self.frame_46.setFrameShape(QFrame.Box)
        self.frame_46.setFrameShadow(QFrame.Plain)
        self.verticalLayout_94 = QVBoxLayout(self.frame_46)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.label_43 = QLabel(self.frame_46)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_94.addWidget(self.label_43)

        self.textEdit_3 = QTextEdit(self.frame_46)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.verticalLayout_94.addWidget(self.textEdit_3)

        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(200, 100))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_71.setSpacing(5)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.pushButton_68 = QPushButton(self.frame_47)
        self.pushButton_68.setObjectName(u"pushButton_68")

        self.horizontalLayout_71.addWidget(self.pushButton_68)

        self.pushButton_69 = QPushButton(self.frame_47)
        self.pushButton_69.setObjectName(u"pushButton_69")

        self.horizontalLayout_71.addWidget(self.pushButton_69)


        self.verticalLayout_94.addWidget(self.frame_47)


        self.gridLayout_21.addWidget(self.frame_46, 0, 2, 1, 1)

        self.sa_workerStatus.setWidget(self.w_workerStats)

        self.gridLayout_20.addWidget(self.sa_workerStatus, 0, 0, 1, 1)

        self.sw_content.addWidget(self.page_workerStatus)
        self.page_stats = QWidget()
        self.page_stats.setObjectName(u"page_stats")
        self.page_stats.setStyleSheet(u"")
        self.gridLayout_18 = QGridLayout(self.page_stats)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.sw_content.addWidget(self.page_stats)

        self.verticalLayout_16.addWidget(self.sw_content)


        self.verticalLayout_3.addWidget(self.f_content)

        self.f_footer = QFrame(self.f_body)
        self.f_footer.setObjectName(u"f_footer")
        self.f_footer.setMinimumSize(QSize(0, 20))
        self.f_footer.setMaximumSize(QSize(16777215, 40))
        self.f_footer.setTabletTracking(False)
        self.f_footer.setStyleSheet(u"#f_footer{\n"
"	background-color: qlineargradient(spread:reflect, x1:0.512, y1:1, x2:1, y2:0.994, stop:0 rgba(190, 190, 190, 200), stop:1 rgba(131, 131, 131, 20));\n"
"}\n"
"\n"
"\n"
"QPushButton\n"
"{ \n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 0);\n"
"	border-width: 0px;\n"
"    border-radius: 0px;\n"
"	qproperty-iconSize: 16px 16px;\n"
"	border-style: dashed;\n"
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
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}")
        self.f_footer.setFrameShape(QFrame.StyledPanel)
        self.f_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.f_footer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.l_version = QLabel(self.f_footer)
        self.l_version.setObjectName(u"l_version")
        self.l_version.setFont(font1)
        self.l_version.setTabletTracking(False)
        self.l_version.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.l_version)

        self.l_serverStatus = QLabel(self.f_footer)
        self.l_serverStatus.setObjectName(u"l_serverStatus")
        self.l_serverStatus.setFont(font1)
        self.l_serverStatus.setTabletTracking(False)
        self.l_serverStatus.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.l_serverStatus)

        self.l_creator = QLabel(self.f_footer)
        self.l_creator.setObjectName(u"l_creator")
        self.l_creator.setFont(font1)
        self.l_creator.setTabletTracking(False)
        self.l_creator.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.l_creator)

        self.btn_logs = QPushButton(self.f_footer)
        self.btn_logs.setObjectName(u"btn_logs")
        self.btn_logs.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.btn_logs.sizePolicy().hasHeightForWidth())
        self.btn_logs.setSizePolicy(sizePolicy4)
        self.btn_logs.setMaximumSize(QSize(20, 16777215))
        icon57 = QIcon()
        icon57.addFile(u":/Simple icons/simple_icons/fi-rr-shield-interrogation.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logs.setIcon(icon57)
        self.btn_logs.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.btn_logs)


        self.verticalLayout_3.addWidget(self.f_footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.f_body)

        self.f_notification = QFrame(self.f_main)
        self.f_notification.setObjectName(u"f_notification")
        self.f_notification.setMinimumSize(QSize(400, 0))
        self.f_notification.setMaximumSize(QSize(500, 16777215))
        self.f_notification.setFrameShape(QFrame.StyledPanel)
        self.f_notification.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.f_notification)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.scrollArea = QScrollArea(self.f_notification)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.WinPanel)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 376, 748))
        self.verticalLayout_85 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.w_notification = QWidget(self.scrollAreaWidgetContents)
        self.w_notification.setObjectName(u"w_notification")
        self.w_notification.setStyleSheet(u"*\n"
"{\n"
"	font: 14pt \"Times New Roman\";\n"
"}")
        self.verticalLayout_86 = QVBoxLayout(self.w_notification)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")

        self.verticalLayout_85.addWidget(self.w_notification)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_84.addWidget(self.scrollArea)

        self.btn_notification_clear = QPushButton(self.f_notification)
        self.btn_notification_clear.setObjectName(u"btn_notification_clear")
        self.btn_notification_clear.setFont(font5)
        self.btn_notification_clear.setIcon(icon23)

        self.verticalLayout_84.addWidget(self.btn_notification_clear)


        self.horizontalLayout.addWidget(self.f_notification)


        self.verticalLayout.addWidget(self.f_main)

        PatusMainWindow.setCentralWidget(self.w_background)

        self.retranslateUi(PatusMainWindow)
        self.cb_reservationDate.clicked["bool"].connect(self.de_reservationSearchDate.setEnabled)
        self.btn_productReceiptClear.clicked.connect(self.le_productReceiptIngredientQuantity.clear)

        self.sw_content.setCurrentIndex(0)
        self.tw_foodMenu.setCurrentIndex(0)
        self.tw_database.setCurrentIndex(0)
        self.cb_menuItemCategory.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PatusMainWindow)
    # setupUi

    def retranslateUi(self, PatusMainWindow):
        PatusMainWindow.setWindowTitle(QCoreApplication.translate("PatusMainWindow", u"Patus", None))
        self.btn_logInOut.setText("")
        self.btn_tables.setText("")
        self.btn_cashRegister.setText("")
        self.btn_reservation.setText("")
        self.btn_waste.setText("")
        self.btn_databaseOverview.setText("")
        self.btn_productReceipt.setText("")
        self.btn_database.setText("")
        self.btn_workerStatus.setText("")
        self.btn_statistic.setText("")
        self.btn_exit.setText("")
        self.btn_sideBar.setText("")
        self.l_monthSells.setText(QCoreApplication.translate("PatusMainWindow", u"Total day sells: 0", None))
        self.l_busyTables.setText(QCoreApplication.translate("PatusMainWindow", u"Busy tables: 8", None))
        self.l_freeTables.setText(QCoreApplication.translate("PatusMainWindow", u"Free tables: 12", None))
        self.l_daySells.setText(QCoreApplication.translate("PatusMainWindow", u"Total month sells: 0", None))
        self.btn_couponGenerator.setText("")
        self.btn_customPrint.setText("")
        self.btn_blockNote.setText("")
        self.btn_notification.setText("")
        self.btn_setting.setText("")
        self.btn_fullScreen.setText("")
        self.l_date.setText(QCoreApplication.translate("PatusMainWindow", u"2021-08-24", None))
        self.l_time.setText(QCoreApplication.translate("PatusMainWindow", u"20:00:00", None))
        self.l_welcomeMsg.setText(QCoreApplication.translate("PatusMainWindow", u"Welcome to Patus", None))
        self.btn_biometric.setText("")
        self.le_username.setText("")
        self.le_username.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Username", None))
        self.le_password.setText("")
        self.le_password.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Password", None))
        self.btn_loginConfirm.setText(QCoreApplication.translate("PatusMainWindow", u"Login", None))
#if QT_CONFIG(shortcut)
        self.btn_loginConfirm.setShortcut(QCoreApplication.translate("PatusMainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.l_cashRegisterTicketNumberTitle.setText(QCoreApplication.translate("PatusMainWindow", u"Ticket Number", None))
        self.l_cashRegisterTicketNumber.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.l_cashRegisterTableNumberTitle.setText(QCoreApplication.translate("PatusMainWindow", u"Table Number", None))
        self.l_cashRegisterTableNumber.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.btn_cashRegisterChangeTable.setText("")
        self.rb_takeAway.setText(QCoreApplication.translate("PatusMainWindow", u"Take away", None))
        self.rb_onTable.setText(QCoreApplication.translate("PatusMainWindow", u"On table", None))
        self.btn_cashRegisterDeleteCurrent.setText("")
        self.btn_cashRegisterClear.setText("")
        self.btn_cashRegisterResume.setText("")
        self.btn_cashRegisterHold.setText("")
        self.l_taxDa.setText(QCoreApplication.translate("PatusMainWindow", u"DA", None))
        self.l_totalTtc.setText(QCoreApplication.translate("PatusMainWindow", u"Final Total", None))
        self.l_da.setText(QCoreApplication.translate("PatusMainWindow", u"DA", None))
        self.l_totalHtt.setText(QCoreApplication.translate("PatusMainWindow", u"Total", None))
        self.l_tax.setText(QCoreApplication.translate("PatusMainWindow", u"Reduction", None))
        self.l_TtcDa.setText(QCoreApplication.translate("PatusMainWindow", u"DA", None))
        self.btn_cashRegisterReduce.setText("")
        self.btn_cashRegisterTicketKitchen.setText("")
        self.btn_cashRegisterTicket.setText("")
        self.btn_cashRegisterPay.setText("")
        self.l_orderWorker.setText(QCoreApplication.translate("PatusMainWindow", u"Worker name", None))
        self.l_orderCustomer.setText(QCoreApplication.translate("PatusMainWindow", u"Customer name", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PatusMainWindow", u"Comment", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_38.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_39.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_40.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_41.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.label_32.setText("")
        self.label_33.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_56.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_57.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.tw_foodMenu.setTabText(self.tw_foodMenu.indexOf(self.tab_salade), "")
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_42.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_43.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_44.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_45.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.label_29.setText("")
        self.label_31.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_54.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_55.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.tw_foodMenu.setTabText(self.tw_foodMenu.indexOf(self.tab_meal), "")
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_4.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_14.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.label_2.setText("")
        self.label_6.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_15.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_16.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.label_3.setText("")
        self.label_7.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_17.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_18.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.tw_foodMenu.setTabText(self.tw_foodMenu.indexOf(self.tab_pizza), "")
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_48.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_49.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_46.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_47.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.label_34.setText("")
        self.label_41.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_64.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_65.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.tw_foodMenu.setTabText(self.tw_foodMenu.indexOf(self.tab_coldDrink), "")
        self.label_35.setText("")
        self.label_36.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_58.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_59.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_50.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_51.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.label_44.setText("")
        self.label_45.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_70.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_71.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.tw_foodMenu.setTabText(self.tw_foodMenu.indexOf(self.tab_hotDrink), "")
        self.label_39.setText("")
        self.label_40.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_62.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_63.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.label_37.setText("")
        self.label_38.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("PatusMainWindow", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("PatusMainWindow", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("PatusMainWindow", u"3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("PatusMainWindow", u"4", None))

        self.pushButton_60.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_61.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.label_46.setText("")
        self.label_47.setText(QCoreApplication.translate("PatusMainWindow", u"Burger", None))
        self.pushButton_72.setText(QCoreApplication.translate("PatusMainWindow", u"+", None))
        self.pushButton_73.setText(QCoreApplication.translate("PatusMainWindow", u"-", None))
        self.tw_foodMenu.setTabText(self.tw_foodMenu.indexOf(self.tab_dessert), "")
        self.gb_reservation.setTitle(QCoreApplication.translate("PatusMainWindow", u"Reservation", None))
        self.le_reservationName.setText("")
        self.le_reservationName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.le_reservationPhone.setText("")
        self.le_reservationPhone.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Phone", None))
        self.le_reservationNbPerson.setText("")
        self.le_reservationNbPerson.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Number of person", None))
        self.dte_reservation.setDisplayFormat(QCoreApplication.translate("PatusMainWindow", u"yyyy-MM-dd HH:mm", None))
        self.btn_reservationAdd.setText("")
        self.btn_reservationEdit.setText("")
        self.btn_reservationDelete.setText("")
        self.btn_reservationClear.setText("")
        self.cb_reservationSearchType.setItemText(0, QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.cb_reservationSearchType.setItemText(1, QCoreApplication.translate("PatusMainWindow", u"Phone", None))

        self.le_reservationSearch.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Search", None))
        self.btn_reservationSearch.setText("")
        self.cb_reservationDate.setText(QCoreApplication.translate("PatusMainWindow", u"Use date", None))
        self.de_reservationSearchDate.setDisplayFormat(QCoreApplication.translate("PatusMainWindow", u"yyyy-MM-dd", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("PatusMainWindow", u"Waste from Stock", None))
        self.le_wasteStockQuantity.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Quantity", None))
        self.btn_wasteStockClear.setText("")
        self.btn_wasteStockSave.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("PatusMainWindow", u"Other Waste", None))
        self.le_wasteCustomName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.le_wasteCustomQuantity.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Quantity", None))
        self.le_wasteCustomPrice.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Price", None))
        self.btn_wasteCustomClear.setText("")
        self.btn_wasteCustomSave.setText("")
        self.l_stock.setText(QCoreApplication.translate("PatusMainWindow", u"Stock", None))
        self.rb_stockIngredients.setText(QCoreApplication.translate("PatusMainWindow", u"Ingredients", None))
        self.rb_stockOthers.setText(QCoreApplication.translate("PatusMainWindow", u"Others", None))
        self.l_productReceiptSelection.setText(QCoreApplication.translate("PatusMainWindow", u"Menu Item Receipt", None))
        self.l_ingredient_2.setText(QCoreApplication.translate("PatusMainWindow", u"Menu Item", None))
        self.btn_productReceiptAdd.setText("")
        self.btn_productReceiptRemove.setText("")
        self.le_productReceiptIngredientQuantity.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Quantity", None))
        self.btn_productReceiptEdit.setText("")
        self.l_ingredient.setText(QCoreApplication.translate("PatusMainWindow", u"Ingredient", None))
        self.btn_productReceiptClear.setText("")
        self.l_ingredient_7.setText(QCoreApplication.translate("PatusMainWindow", u"Sell price", None))
        self.l_ingredient_5.setText(QCoreApplication.translate("PatusMainWindow", u"Estimated production price", None))
        self.l_ingredient_8.setText(QCoreApplication.translate("PatusMainWindow", u"Estimated quantity", None))
        self.l_productReceiptQuantity.setText(QCoreApplication.translate("PatusMainWindow", u"0", None))
        self.l_productReceiptPrice.setText(QCoreApplication.translate("PatusMainWindow", u"0", None))
        self.l_productReceiptEstimatedProductionPrice.setText(QCoreApplication.translate("PatusMainWindow", u"0", None))
        self.gb_menuItem.setTitle(QCoreApplication.translate("PatusMainWindow", u"Menu Item", None))
        self.l_menuItemPicture.setText("")
        self.btn_menuItemPicture.setText("")
        self.btn_menuItemPictureClear.setText("")
        self.le_menuItemName.setText("")
        self.le_menuItemName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.cb_menuItemCategory.setItemText(0, QCoreApplication.translate("PatusMainWindow", u"Salade", None))
        self.cb_menuItemCategory.setItemText(1, QCoreApplication.translate("PatusMainWindow", u"Meal", None))
        self.cb_menuItemCategory.setItemText(2, QCoreApplication.translate("PatusMainWindow", u"Pizza", None))
        self.cb_menuItemCategory.setItemText(3, QCoreApplication.translate("PatusMainWindow", u"Cold Drink", None))
        self.cb_menuItemCategory.setItemText(4, QCoreApplication.translate("PatusMainWindow", u"Hot Drink", None))
        self.cb_menuItemCategory.setItemText(5, QCoreApplication.translate("PatusMainWindow", u"Dessert", None))

        self.le_menuItemUnit.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Unit", None))
        self.le_menuItemUnitQuantity.setText("")
        self.le_menuItemUnitQuantity.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Unit Quantity", None))
        self.le_menuItemPrice.setText("")
        self.le_menuItemPrice.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Unit Price", None))
        self.btn_menuItemAdd.setText("")
        self.btn_menuItemEdit.setText("")
        self.btn_menuItemDelete.setText("")
        self.btn_menuItemClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_menu), "")
        self.gb_menuCategoryCustom.setTitle(QCoreApplication.translate("PatusMainWindow", u"Menu Category", None))
        self.le_menuCategoryCustomName.setText("")
        self.le_menuCategoryCustomName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.cb_menuCategoryCustomPrinting.setItemText(0, QCoreApplication.translate("PatusMainWindow", u"Kitchen", None))
        self.cb_menuCategoryCustomPrinting.setItemText(1, QCoreApplication.translate("PatusMainWindow", u"Pizza Yolo", None))
        self.cb_menuCategoryCustomPrinting.setItemText(2, QCoreApplication.translate("PatusMainWindow", u"Bar", None))

        self.btn_menuCategoryCustomAdd.setText("")
        self.btn_menuCategoryCustomEdit.setText("")
        self.btn_menuCategoryCustomDelete.setText("")
        self.btn_menuCategoryCustomClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab), "")
        self.gb_supplement.setTitle(QCoreApplication.translate("PatusMainWindow", u"Supplement", None))
        self.le_supplementName.setText("")
        self.le_supplementName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.le_supplementQuantity.setText("")
        self.le_supplementQuantity.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Quantity", None))
        self.le_supplementPrice.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Price", None))
        self.btn_supplementAdd.setText("")
        self.btn_supplementEdit.setText("")
        self.btn_supplementDelete.setText("")
        self.btn_supplementClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_supplement), "")
        self.gb_expense.setTitle(QCoreApplication.translate("PatusMainWindow", u"Expense", None))
        self.le_expenseName.setText("")
        self.le_expenseName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.le_expenseUnit.setText("")
        self.le_expenseUnit.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Unit", None))
        self.le_expenseQuantity.setText("")
        self.le_expenseQuantity.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Quantity", None))
        self.le_expensePrice.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Total price", None))
        self.cb_expenseSupplier.setItemText(0, QCoreApplication.translate("PatusMainWindow", u"None", None))

        self.cb_expensePayed.setText(QCoreApplication.translate("PatusMainWindow", u"Is payed ?", None))
        self.btn_expenseAdd.setText("")
        self.btn_expenseEdit.setText("")
        self.btn_expenseDelete.setText("")
        self.btn_expenseClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_expense), "")
        self.gb_expenseCategory.setTitle(QCoreApplication.translate("PatusMainWindow", u"Expense Category", None))
        self.le_expenseCategoryName.setText("")
        self.le_expenseCategoryName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.cb_expenseCategorySaveToStock.setText(QCoreApplication.translate("PatusMainWindow", u"Save to stock ?", None))
        self.cb_expenseCategoryIsIngredient.setText(QCoreApplication.translate("PatusMainWindow", u"Is ingredient ?", None))
        self.btn_expenseCategoryAdd.setText("")
        self.btn_expenseCategoryEdit.setText("")
        self.btn_expenseCategoryDelete.setText("")
        self.btn_expenseCategoryClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_expenseCategory), "")
        self.gb_supplier.setTitle(QCoreApplication.translate("PatusMainWindow", u"Supplier", None))
        self.le_supplierName.setText("")
        self.le_supplierName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.le_supplierPhone.setText("")
        self.le_supplierPhone.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Phone", None))
        self.le_supplierAddress.setText("")
        self.le_supplierAddress.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Address", None))
        self.le_supplierMail.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Mail", None))
        self.btn_supplierAdd.setText("")
        self.btn_supplierEdit.setText("")
        self.btn_supplierDelete.setText("")
        self.btn_supplierClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_supplier), "")
        self.gb_customer.setTitle(QCoreApplication.translate("PatusMainWindow", u"Customer", None))
        self.l_customerPicture.setText("")
        self.btn_customerPicture.setText("")
        self.btn_customerPictureClear.setText("")
        self.le_customerName.setText("")
        self.le_customerName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"First and Last Name", None))
        self.le_customerPhone.setText("")
        self.le_customerPhone.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Phone", None))
        self.le_customerAddress.setText("")
        self.le_customerAddress.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Address", None))
        self.le_customerScore.setInputMask("")
        self.le_customerScore.setText("")
        self.le_customerScore.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Score", None))
        self.btn_customerAdd.setText("")
        self.btn_customerEdit.setText("")
        self.btn_customerDelete.setText("")
        self.btn_customerClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_customer), "")
        self.gb_worker.setTitle(QCoreApplication.translate("PatusMainWindow", u"Worker", None))
        self.l_workerPicture.setText("")
        self.btn_workerPicture.setText("")
        self.btn_workerPictureClear.setText("")
        self.le_workerName.setText("")
        self.le_workerName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"First and Last Name", None))
        self.le_workerUsername.setText("")
        self.le_workerUsername.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Username", None))
        self.le_workerPassword.setText("")
        self.le_workerPassword.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Password", None))
        self.le_workerPhone.setText("")
        self.le_workerPhone.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Phone", None))
        self.le_workerAddress.setText("")
        self.le_workerAddress.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Address", None))
        self.le_workerSalary.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Salary", None))
        self.le_workerScore.setText("")
        self.le_workerScore.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Score", None))
        self.le_workerCv.setText("")
        self.le_workerCv.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"CV extension", None))
        self.btn_workerAddCv.setText("")
        self.btn_workerOpenCv.setText("")
        self.btn_workerClearCv.setText("")
        self.btn_workerAdd.setText("")
        self.btn_workerEdit.setText("")
        self.btn_workerDelete.setText("")
        self.btn_workerClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_worker), "")
        self.gb_category.setTitle(QCoreApplication.translate("PatusMainWindow", u"Worker Category", None))
        self.le_categoryName.setText("")
        self.le_categoryName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.cb_categoryLevelCashier.setText(QCoreApplication.translate("PatusMainWindow", u"Cashier", None))
        self.cb_categoryLevelWaste.setText(QCoreApplication.translate("PatusMainWindow", u"Waste", None))
        self.cb_categoryLevelTables.setText(QCoreApplication.translate("PatusMainWindow", u"Tables", None))
        self.cb_categoryLevelStock.setText(QCoreApplication.translate("PatusMainWindow", u"Stock", None))
        self.cb_categoryLevelReservation.setText(QCoreApplication.translate("PatusMainWindow", u"Reservation", None))
        self.cb_categoryLevelReceipt.setText(QCoreApplication.translate("PatusMainWindow", u"Receipt", None))
        self.cb_categoryLevelDb.setText(QCoreApplication.translate("PatusMainWindow", u"DataBase", None))
        self.cb_categoryLevelPhone.setText(QCoreApplication.translate("PatusMainWindow", u"Phones", None))
        self.cb_categoryLevelStat.setText(QCoreApplication.translate("PatusMainWindow", u"DashBoard", None))
        self.btn_categoryAdd.setText("")
        self.btn_categoryEdit.setText("")
        self.btn_categoryDelete.setText("")
        self.btn_categoryClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_category), "")
        self.gb_sell.setTitle(QCoreApplication.translate("PatusMainWindow", u"Sell", None))
        self.dte_sellDate.setDisplayFormat(QCoreApplication.translate("PatusMainWindow", u"yyyy-MM-dd HH:mm:ss", None))
        self.le_sellTotal.setText("")
        self.le_sellTotal.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Total", None))
        self.le_sellNbCovers.setText("")
        self.le_sellNbCovers.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Number of covers", None))
        self.btn_sellAdd.setText("")
        self.btn_sellEdit.setText("")
        self.btn_sellDelete.setText("")
        self.btn_sellClear.setText("")
        self.btn_sellShow.setText("")
        self.btn_sellLoad.setText("")
        self.btn_sellHistory.setText("")
        self.tb_sellOpenBrowser.setText(QCoreApplication.translate("PatusMainWindow", u"Ticket History Browser", None))
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_sell), "")
        self.gb_expense_6.setTitle(QCoreApplication.translate("PatusMainWindow", u"Table", None))
        self.le_tableName.setText("")
        self.le_tableName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.le_tableId.setText("")
        self.le_tableId.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Table Number", None))
        self.le_tableSeats.setText("")
        self.le_tableSeats.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Number of seats", None))
        self.le_tableComment.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Comment", None))
        self.btn_tableAdd.setText("")
        self.btn_tableEdit.setText("")
        self.btn_tableDelete.setText("")
        self.btn_tableClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_table), "")
        self.groupBox.setTitle(QCoreApplication.translate("PatusMainWindow", u"History", None))
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_pointer), "")
        self.gb_stock.setTitle(QCoreApplication.translate("PatusMainWindow", u"Stock", None))
        self.le_stockProductName.setText("")
        self.le_stockProductName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.le_stockUnit.setText("")
        self.le_stockUnit.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Stock unit", None))
        self.le_stockQuantity.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Stock quantity", None))
        self.cb_stockIsIngredient.setText(QCoreApplication.translate("PatusMainWindow", u"Is ingredient ?", None))
        self.btn_stockAdd.setText("")
        self.btn_stockEdit.setText("")
        self.btn_stockDelete.setText("")
        self.btn_stockClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_stock), "")
        self.gb_doccuments.setTitle(QCoreApplication.translate("PatusMainWindow", u"Doccuments", None))
        self.le_docName.setText("")
        self.le_docName.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Name", None))
        self.dte_docDate.setDisplayFormat(QCoreApplication.translate("PatusMainWindow", u"yyyy-MM-dd HH:mm:ss", None))
        self.le_docComment.setText("")
        self.le_docComment.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Comment", None))
        self.le_docPath.setText("")
        self.le_docPath.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Doc extension", None))
        self.btn_docAddFile.setText("")
        self.btn_docOpenFile.setText("")
        self.btn_docClearFile.setText("")
        self.btn_docAdd.setText("")
        self.btn_docEdit.setText("")
        self.btn_docDelete.setText("")
        self.btn_docClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_uploader), "")
        self.gb_tableOwnership.setTitle(QCoreApplication.translate("PatusMainWindow", u"Table Ownership", None))
        self.btn_tableOwnershipAdd.setText("")
        self.btn_tableOwnershipEdit.setText("")
        self.btn_tableOwnershipDelete.setText("")
        self.btn_tableOwnershipClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_tableOwnership), "")
        self.gb_payment.setTitle(QCoreApplication.translate("PatusMainWindow", u"Eployee payment", None))
        self.de_payment_date.setDisplayFormat(QCoreApplication.translate("PatusMainWindow", u"yyyy-MM-dd", None))
        self.le_payment_amount.setPlaceholderText(QCoreApplication.translate("PatusMainWindow", u"Amount", None))
        self.btn_paymentAdd.setText("")
        self.btn_paymentEdit.setText("")
        self.btn_paymentDelete.setText("")
        self.btn_paymentClear.setText("")
        self.tw_database.setTabText(self.tw_database.indexOf(self.tab_payement), "")
        self.label_30.setText(QCoreApplication.translate("PatusMainWindow", u"Mourad", None))
        self.pushButton_52.setText(QCoreApplication.translate("PatusMainWindow", u"Send", None))
        self.pushButton_53.setText(QCoreApplication.translate("PatusMainWindow", u"Ring", None))
        self.label_42.setText(QCoreApplication.translate("PatusMainWindow", u"Mourad", None))
        self.pushButton_66.setText(QCoreApplication.translate("PatusMainWindow", u"Send", None))
        self.pushButton_67.setText(QCoreApplication.translate("PatusMainWindow", u"Ring", None))
        self.label_43.setText(QCoreApplication.translate("PatusMainWindow", u"Mourad", None))
        self.pushButton_68.setText(QCoreApplication.translate("PatusMainWindow", u"Send", None))
        self.pushButton_69.setText(QCoreApplication.translate("PatusMainWindow", u"Ring", None))
        self.l_version.setText(QCoreApplication.translate("PatusMainWindow", u"Patus 1.0.1", None))
        self.l_serverStatus.setText(QCoreApplication.translate("PatusMainWindow", u"Server Starting", None))
        self.l_creator.setText(QCoreApplication.translate("PatusMainWindow", u"Made by Lablack Mourad", None))
        self.btn_logs.setText("")
        self.btn_notification_clear.setText(QCoreApplication.translate("PatusMainWindow", u"Clear all notifications", None))
    # retranslateUi

