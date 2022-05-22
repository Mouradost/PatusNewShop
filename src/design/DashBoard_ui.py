# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashBoard.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QScrollArea, QSizePolicy,
    QWidget)

class Ui_w_dashboard(object):
    def setupUi(self, w_dashboard):
        if not w_dashboard.objectName():
            w_dashboard.setObjectName(u"w_dashboard")
        w_dashboard.resize(955, 785)
        w_dashboard.setStyleSheet(u"#w_dashboard{\n"
"  background: rgba(70, 70, 70, 0.7);\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"QWidget\n"
"{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(250, 250, 250);\n"
"}\n"
"QLabel:hover{\n"
"    color: rgb(0, 250, 250);\n"
"}\n"
"\n"
"QDateEdite{\n"
"    border: none;\n"
"    border-radius: 20%;\n"
"    background: rgb(129, 129, 129);\n"
"}\n"
"\n"
"#sa{\n"
"    border: none;\n"
"    border-radius: 1%;\n"
"  	background: transparent;\n"
"    margin: 0px;\n"
"	margin-top: 0px;\n"
"	margin-bottom: 0px;\n"
"    padding: 0px;\n"
"    font-size: 24px;\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"#f_date_start{\n"
"    color: rgb(250, 250, 250);\n"
"    border: none;\n"
"    border-radius: 20%;\n"
"    border-top-left-radius: 0%;\n"
"    border-bottom-left-radius: 0%;\n"
"    background: rgb(129, 129, 129);\n"
"    margin: 2px;\n"
"	margin-top: 10px;\n"
"	margin-bottom: 10px;\n"
"    padding: 10px;\n"
"    font-size: 24px;\n"
"    text-align: center;\n"
"}\n"
"\n"
""
                        "\n"
"#f_date_start:hover{\n"
"	background: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"#f_date_end{\n"
"   	color: rgb(250, 250, 250);\n"
"    border: none;\n"
"    border-radius: 20%;\n"
"    border-top-right-radius: 0%;\n"
"    border-bottom-right-radius: 0%;\n"
"    background: rgb(129, 129, 129);\n"
"    margin: 2px;\n"
"	margin-top: 10px;\n"
"	margin-bottom: 10px;\n"
"    padding: 10px;\n"
"    font-size: 24px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"\n"
"\n"
"#f_date_end:hover{\n"
"	background: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"#f_dashboard_total_spending{\n"
"    color: rgb(250, 250, 250);\n"
"    border: none;\n"
"    border-radius: 20%;\n"
"    background: rgb(129, 129, 129);\n"
"    margin: 2px;\n"
"    padding: 10px;\n"
"    font-size: 24px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#f_dashboard_total_earning{\n"
"    color: rgb(250, 250, 250);\n"
"    border: none;\n"
"    border-radius: 20%;\n"
"    background: rgb(129, 129, 129);\n"
"    margin: 2px;\n"
"    padding: 10px;\n"
"    font-size: "
                        "24px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#f_dashboard_total_gain{\n"
"    color: rgb(250, 250, 250);\n"
"    border: none;\n"
"    border-radius: 20%;\n"
"    background: rgb(129, 129, 129);\n"
"    margin: 2px;\n"
"    padding: 10px;\n"
"    font-size: 24px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#f_dashboard_customer_ranking{\n"
"    color: rgb(250, 250, 250);\n"
"    border: none;\n"
"    border-radius: 20%;\n"
"    background: rgb(129, 129, 129);\n"
"    margin: 2px;\n"
"    padding: 10px;\n"
"    font-size: 24px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#f_dashboard_worker_ranking{\n"
"    color: rgb(250, 250, 250);\n"
"    border: none;\n"
"    border-radius: 20%;\n"
"    background: rgb(129, 129, 129);\n"
"    margin: 2px;\n"
"    padding: 10px;\n"
"    font-size: 24px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#f_dashboard_worker_payment{\n"
"    color: rgb(250, 250, 250);\n"
"    border: none;\n"
"    border-radius: 20%;\n"
"    background: rgb(129, 129, 129);\n"
"    margin: 2px;\n"
" "
                        "   padding: 10px;\n"
"    font-size: 24px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#f_dashboard_worker_attendance_ranking{\n"
"    color: rgb(250, 250, 250);\n"
"    border: none;\n"
"    border-radius: 20%;\n"
"    background: rgb(129, 129, 129);\n"
"    margin: 2px;\n"
"    padding: 10px;\n"
"    font-size: 24px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#f_dashboard_best_sellin_product{\n"
"    color: rgb(250, 250, 250);\n"
"    border: none;\n"
"    border-radius: 20%;\n"
"    background: rgb(129, 129, 129);\n"
"    margin: 2px;\n"
"    padding: 10px;\n"
"    font-size: 24px;\n"
"    text-align: center;\n"
"\n"
"}")
        self.gridLayout = QGridLayout(w_dashboard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.f_date_start = QFrame(w_dashboard)
        self.f_date_start.setObjectName(u"f_date_start")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_date_start.sizePolicy().hasHeightForWidth())
        self.f_date_start.setSizePolicy(sizePolicy)
        self.f_date_start.setFrameShape(QFrame.StyledPanel)
        self.f_date_start.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.f_date_start)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.f_date_start)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_10)

        self.de_dashboard_date_end = QDateTimeEdit(self.f_date_start)
        self.de_dashboard_date_end.setObjectName(u"de_dashboard_date_end")
        font1 = QFont()
        font1.setPointSize(14)
        self.de_dashboard_date_end.setFont(font1)
        self.de_dashboard_date_end.setStyleSheet(u"QWidget\n"
"{\n"
"	background-color: rgb(150, 188, 182);\n"
"}")
        self.de_dashboard_date_end.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.de_dashboard_date_end)


        self.gridLayout.addWidget(self.f_date_start, 1, 1, 1, 1)

        self.f_date_end = QFrame(w_dashboard)
        self.f_date_end.setObjectName(u"f_date_end")
        sizePolicy.setHeightForWidth(self.f_date_end.sizePolicy().hasHeightForWidth())
        self.f_date_end.setSizePolicy(sizePolicy)
        self.f_date_end.setStyleSheet(u"")
        self.f_date_end.setFrameShape(QFrame.StyledPanel)
        self.f_date_end.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.f_date_end)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.f_date_end)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.de_dashboard_date_start = QDateTimeEdit(self.f_date_end)
        self.de_dashboard_date_start.setObjectName(u"de_dashboard_date_start")
        self.de_dashboard_date_start.setFont(font1)
        self.de_dashboard_date_start.setStyleSheet(u"QWidget\n"
"{\n"
"	background-color: rgb(150, 188, 182);\n"
"}")
        self.de_dashboard_date_start.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.de_dashboard_date_start)


        self.gridLayout.addWidget(self.f_date_end, 1, 0, 1, 1)

        self.sa = QScrollArea(w_dashboard)
        self.sa.setObjectName(u"sa")
        self.sa.setStyleSheet(u"")
        self.sa.setFrameShape(QFrame.VLine)
        self.sa.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 947, 701))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.f_dashboard_best_sellin_product = QFrame(self.scrollAreaWidgetContents)
        self.f_dashboard_best_sellin_product.setObjectName(u"f_dashboard_best_sellin_product")
        sizePolicy.setHeightForWidth(self.f_dashboard_best_sellin_product.sizePolicy().hasHeightForWidth())
        self.f_dashboard_best_sellin_product.setSizePolicy(sizePolicy)
        self.f_dashboard_best_sellin_product.setStyleSheet(u"")
        self.f_dashboard_best_sellin_product.setFrameShape(QFrame.StyledPanel)
        self.f_dashboard_best_sellin_product.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.f_dashboard_best_sellin_product)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.f_dashboard_best_sellin_product)
        self.label_25.setObjectName(u"label_25")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_25.setFont(font2)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_31.addWidget(self.label_25, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.f_dashboard_best_sellin_product, 1, 0, 1, 1)

        self.f_dashboard_worker_ranking = QFrame(self.scrollAreaWidgetContents)
        self.f_dashboard_worker_ranking.setObjectName(u"f_dashboard_worker_ranking")
        sizePolicy.setHeightForWidth(self.f_dashboard_worker_ranking.sizePolicy().hasHeightForWidth())
        self.f_dashboard_worker_ranking.setSizePolicy(sizePolicy)
        self.f_dashboard_worker_ranking.setStyleSheet(u"")
        self.f_dashboard_worker_ranking.setFrameShape(QFrame.StyledPanel)
        self.f_dashboard_worker_ranking.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.f_dashboard_worker_ranking)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.f_dashboard_worker_ranking)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_28.addWidget(self.label_19, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.f_dashboard_worker_ranking, 2, 0, 1, 1)

        self.f_dashboard_worker_attendance_ranking = QFrame(self.scrollAreaWidgetContents)
        self.f_dashboard_worker_attendance_ranking.setObjectName(u"f_dashboard_worker_attendance_ranking")
        sizePolicy.setHeightForWidth(self.f_dashboard_worker_attendance_ranking.sizePolicy().hasHeightForWidth())
        self.f_dashboard_worker_attendance_ranking.setSizePolicy(sizePolicy)
        self.f_dashboard_worker_attendance_ranking.setStyleSheet(u"")
        self.f_dashboard_worker_attendance_ranking.setFrameShape(QFrame.StyledPanel)
        self.f_dashboard_worker_attendance_ranking.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.f_dashboard_worker_attendance_ranking)
        self.gridLayout_32.setSpacing(0)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.f_dashboard_worker_attendance_ranking)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.label_11, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.f_dashboard_worker_attendance_ranking, 3, 0, 1, 1)

        self.f_dashboard_customer_ranking = QFrame(self.scrollAreaWidgetContents)
        self.f_dashboard_customer_ranking.setObjectName(u"f_dashboard_customer_ranking")
        sizePolicy.setHeightForWidth(self.f_dashboard_customer_ranking.sizePolicy().hasHeightForWidth())
        self.f_dashboard_customer_ranking.setSizePolicy(sizePolicy)
        self.f_dashboard_customer_ranking.setStyleSheet(u"")
        self.f_dashboard_customer_ranking.setFrameShape(QFrame.StyledPanel)
        self.f_dashboard_customer_ranking.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.f_dashboard_customer_ranking)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.f_dashboard_customer_ranking)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.f_dashboard_customer_ranking, 5, 0, 1, 1)

        self.f_dashboard_totals = QFrame(self.scrollAreaWidgetContents)
        self.f_dashboard_totals.setObjectName(u"f_dashboard_totals")
        sizePolicy.setHeightForWidth(self.f_dashboard_totals.sizePolicy().hasHeightForWidth())
        self.f_dashboard_totals.setSizePolicy(sizePolicy)
        self.f_dashboard_totals.setStyleSheet(u"")
        self.f_dashboard_totals.setFrameShape(QFrame.StyledPanel)
        self.f_dashboard_totals.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.f_dashboard_totals)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.f_dashboard_total_earning = QFrame(self.f_dashboard_totals)
        self.f_dashboard_total_earning.setObjectName(u"f_dashboard_total_earning")
        sizePolicy.setHeightForWidth(self.f_dashboard_total_earning.sizePolicy().hasHeightForWidth())
        self.f_dashboard_total_earning.setSizePolicy(sizePolicy)
        self.f_dashboard_total_earning.setStyleSheet(u"")
        self.f_dashboard_total_earning.setFrameShape(QFrame.StyledPanel)
        self.f_dashboard_total_earning.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.f_dashboard_total_earning)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.f_dashboard_total_earning)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(22)
        font3.setBold(True)
        self.label_8.setFont(font3)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_8, 0, 0, 1, 1)

        self.l_dashboard_total_earning = QLabel(self.f_dashboard_total_earning)
        self.l_dashboard_total_earning.setObjectName(u"l_dashboard_total_earning")
        sizePolicy1.setHeightForWidth(self.l_dashboard_total_earning.sizePolicy().hasHeightForWidth())
        self.l_dashboard_total_earning.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(22)
        self.l_dashboard_total_earning.setFont(font4)
        self.l_dashboard_total_earning.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.l_dashboard_total_earning, 1, 0, 1, 1)


        self.horizontalLayout_57.addWidget(self.f_dashboard_total_earning)

        self.f_dashboard_total_spending = QFrame(self.f_dashboard_totals)
        self.f_dashboard_total_spending.setObjectName(u"f_dashboard_total_spending")
        sizePolicy.setHeightForWidth(self.f_dashboard_total_spending.sizePolicy().hasHeightForWidth())
        self.f_dashboard_total_spending.setSizePolicy(sizePolicy)
        self.f_dashboard_total_spending.setFrameShape(QFrame.StyledPanel)
        self.f_dashboard_total_spending.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.f_dashboard_total_spending)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.f_dashboard_total_spending)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_4, 0, 0, 1, 1)

        self.l_dashboard_total_spending = QLabel(self.f_dashboard_total_spending)
        self.l_dashboard_total_spending.setObjectName(u"l_dashboard_total_spending")
        sizePolicy1.setHeightForWidth(self.l_dashboard_total_spending.sizePolicy().hasHeightForWidth())
        self.l_dashboard_total_spending.setSizePolicy(sizePolicy1)
        self.l_dashboard_total_spending.setFont(font4)
        self.l_dashboard_total_spending.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.l_dashboard_total_spending, 1, 0, 1, 1)


        self.horizontalLayout_57.addWidget(self.f_dashboard_total_spending)

        self.f_dashboard_total_gain = QFrame(self.f_dashboard_totals)
        self.f_dashboard_total_gain.setObjectName(u"f_dashboard_total_gain")
        sizePolicy.setHeightForWidth(self.f_dashboard_total_gain.sizePolicy().hasHeightForWidth())
        self.f_dashboard_total_gain.setSizePolicy(sizePolicy)
        self.f_dashboard_total_gain.setFrameShape(QFrame.StyledPanel)
        self.f_dashboard_total_gain.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.f_dashboard_total_gain)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.l_dashboard_total_gain = QLabel(self.f_dashboard_total_gain)
        self.l_dashboard_total_gain.setObjectName(u"l_dashboard_total_gain")
        sizePolicy1.setHeightForWidth(self.l_dashboard_total_gain.sizePolicy().hasHeightForWidth())
        self.l_dashboard_total_gain.setSizePolicy(sizePolicy1)
        self.l_dashboard_total_gain.setFont(font4)
        self.l_dashboard_total_gain.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.l_dashboard_total_gain, 2, 0, 1, 1)

        self.label_7 = QLabel(self.f_dashboard_total_gain)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_7, 1, 0, 1, 1)


        self.horizontalLayout_57.addWidget(self.f_dashboard_total_gain)


        self.gridLayout_2.addWidget(self.f_dashboard_totals, 0, 0, 1, 1)

        self.f_dashboard_worker_payment = QFrame(self.scrollAreaWidgetContents)
        self.f_dashboard_worker_payment.setObjectName(u"f_dashboard_worker_payment")
        sizePolicy.setHeightForWidth(self.f_dashboard_worker_payment.sizePolicy().hasHeightForWidth())
        self.f_dashboard_worker_payment.setSizePolicy(sizePolicy)
        self.f_dashboard_worker_payment.setStyleSheet(u"")
        self.f_dashboard_worker_payment.setFrameShape(QFrame.StyledPanel)
        self.f_dashboard_worker_payment.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.f_dashboard_worker_payment)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.f_dashboard_worker_payment)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_35.addWidget(self.label_14, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.f_dashboard_worker_payment, 4, 0, 1, 1)

        self.sa.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.sa, 2, 0, 1, 2)


        self.retranslateUi(w_dashboard)

        QMetaObject.connectSlotsByName(w_dashboard)
    # setupUi

    def retranslateUi(self, w_dashboard):
        w_dashboard.setWindowTitle(QCoreApplication.translate("w_dashboard", u"Form", None))
        self.label_10.setText(QCoreApplication.translate("w_dashboard", u"End", None))
        self.label_9.setText(QCoreApplication.translate("w_dashboard", u"Start", None))
        self.label_25.setText(QCoreApplication.translate("w_dashboard", u"Best Selling Products", None))
        self.label_19.setText(QCoreApplication.translate("w_dashboard", u"Employee Sells Ranking", None))
        self.label_11.setText(QCoreApplication.translate("w_dashboard", u"Employee Attendance", None))
        self.label.setText(QCoreApplication.translate("w_dashboard", u"Customer Ranking", None))
        self.label_8.setText(QCoreApplication.translate("w_dashboard", u"Total earning", None))
        self.l_dashboard_total_earning.setText(QCoreApplication.translate("w_dashboard", u"5000", None))
        self.label_4.setText(QCoreApplication.translate("w_dashboard", u"Total spending", None))
        self.l_dashboard_total_spending.setText(QCoreApplication.translate("w_dashboard", u"5000", None))
        self.l_dashboard_total_gain.setText(QCoreApplication.translate("w_dashboard", u"5000", None))
        self.label_7.setText(QCoreApplication.translate("w_dashboard", u"Total gain", None))
        self.label_14.setText(QCoreApplication.translate("w_dashboard", u"Employee Payment", None))
    # retranslateUi

