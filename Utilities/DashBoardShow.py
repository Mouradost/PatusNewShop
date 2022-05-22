import itertools
from typing import Callable, List

# import pandas as pd
from DB.DBHandler import DBHelper

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

import datetime
import os


class DashBoard(QWidget):
    def __init__(self, **kwargs) -> None:
        super(DashBoard, self).__init__(objectName="w_reportDashBoard", **kwargs)
        uic.loadUi(os.path.join(os.getcwd(), "uis", "DashBoard.ui"), self)
        self.DB = DBHelper()
        # Dataframes
        # self.df_pointer = pd.DataFrame()
        self.start_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.end_date = (
            datetime.datetime.now() + datetime.timedelta(hours=24)
        ).strftime("%Y-%m-%d %H:%M")
        # Setting up the dates
        self.de_dashboard_date_start.setDateTime(
            QDateTime.fromString(self.start_date, "yyyy-MM-dd HH:mm")
        )
        self.de_dashboard_date_end.setDateTime(
            QDateTime.fromString(self.end_date, "yyyy-MM-dd HH:mm")
        )
        # Connecting the dates
        self.de_dashboard_date_start.dateTimeChanged.connect(self.set_dates)
        self.de_dashboard_date_end.dateTimeChanged.connect(self.set_dates)
        self.set_dates()

        # self.show()

    def set_dates(self) -> None:
        self.start_date = self.de_dashboard_date_start.dateTime().toString(
            "yyyy-MM-dd HH:mm"
        )
        self.end_date = self.de_dashboard_date_end.dateTime().toString(
            "yyyy-MM-dd HH:mm"
        )

        self.update_all()

    def update_all(self) -> None:
        # self.prepare_dataframes()
        self.show_totals()
        self.show_best_selling_products()
        self.show_customer_ranking()
        self.show_worker_ranking()
        self.show_worker_hours_ranking_()
        self.show_worker_payment_()
        # self.show_worker_hours_ranking()

    def show_worker_hours_ranking_(self) -> None:
        data = self.DB.getWorkerHourRankingByDateRange(self.start_date, self.end_date)

        # Prepare
        ranking = []
        for name, date_start, date_end in data:
            date_start = datetime.datetime.strptime(date_start, "%Y-%m-%d %H:%M:%S")
            date_end = datetime.datetime.strptime(date_end, "%Y-%m-%d %H:%M:%S")
            ranking.append((name, date_end - date_start))

        # Aggregate results
        ranking_dict = {}
        for key, group in itertools.groupby(ranking, lambda x: x[0]):
            if key is not None:
                if key not in ranking_dict:
                    ranking_dict[key] = datetime.timedelta(0, 0, 0)
                for _, y in group:
                    ranking_dict[key] += y
        show_dynamic(
            self.f_dashboard_worker_attendance_ranking,
            "Employee Attendance",
            ["Name", "Duration"],
            dict(
                sorted(ranking_dict.items(), key=lambda x: x[1], reverse=True)
            ).items(),
            "",
            None,
        )

    def show_worker_payment_(self) -> None:
        results = self.DB.getWorkerPaymentByDateRange(self.start_date, self.end_date)
        show_dynamic(
            self.f_dashboard_worker_payment,
            "Employee Payment",
            ["Name", "Total amount", "Remaining amount", "Salary"],
            results,
            ["Total amount", "Remaining amount", "Salary"],
            to_money,
        )

    # def prepare_dataframes(self) -> None:
    #     self.df_pointer = pd.read_sql_query(
    #         """
    #         SELECT Pointer.date_start, Pointer.date_end, Workers.name, Workers.id_category, Workers.score  FROM Pointer
    #         LEFT JOIN Workers ON
    #         Pointer.id_worker = Workers._id
    #         """, self.DB.conn)
    #     self.df_pointer.date_start = pd.to_datetime(self.df_pointer.date_start)
    #     self.df_pointer.date_end = pd.to_datetime(self.df_pointer.date_end)
    #     self.df_pointer['duration'] = self.df_pointer.date_end - \
    #         self.df_pointer.date_start

    #     self.df_sells = pd.read_sql_query(
    #         """
    #         SELECT Pointer.date_start, Pointer.date_end, Workers.name, Workers.id_category, Workers.score  FROM Pointer
    #         LEFT JOIN Workers ON
    #         Pointer.id_worker = Workers._id
    #         """, self.DB.conn)

    def show_totals(self) -> None:
        # Retreive the data
        total_expenses = self.DB.getExpensesTotalPriceByDateRange(
            self.start_date, self.end_date
        )

        total_sells = self.DB.getSellsTotalPriceByDateRange(
            self.start_date, self.end_date
        )

        total_gain = total_sells - total_expenses

        # Showing the data
        self.l_dashboard_total_earning.setText(to_money(total_sells))
        self.l_dashboard_total_spending.setText(to_money(total_expenses))
        self.l_dashboard_total_gain.setText(to_money(total_gain))
        if total_gain > 0:
            self.l_dashboard_total_gain.setStyleSheet("QLabel { color: #24ff50; }")
        else:
            self.l_dashboard_total_gain.setStyleSheet("QLabel { color: #9e2800; }")

    def show_customer_ranking(self) -> None:
        ranking = self.DB.getCustomerRankingByDateRange(self.start_date, self.end_date)
        show_dynamic(
            self.f_dashboard_customer_ranking,
            "Customer Ranking",
            ["Name", "Visits", "Total spending"],
            ranking,
            ["Total spending"],
            to_money,
        )

    def show_worker_ranking(self) -> None:
        ranking = self.DB.getWorkerRankingByDateRange(self.start_date, self.end_date)
        show_dynamic(
            self.f_dashboard_worker_ranking,
            "Employee Sells Ranking",
            ["Name", "Total sells"],
            ranking,
            ["Total sells"],
            to_money,
        )

    # def show_worker_hours_ranking(self) -> None:
    #     ranking = self.df_pointer[["name", "duration"]].groupby(['name']).sum()

    #     ranking_score = self.df_pointer[[
    #         "name", 'score']].groupby(['name']).sum()
    #     all_ranking = []
    #     for m, t, s in zip(ranking.index, ranking['duration'], ranking_score['score']):
    #         all_ranking.append([
    #             m,
    #             f"days: {t.components.days}\nhours: {t.components.hours}\nminutes: {t.components.minutes}",
    #             f"{s/t.value:.2%}"])
    #     show_dynamic(
    #         self.f_dashboard_worker_attendance_ranking,
    #         "Employee Attendance",
    #         ["Name", "Duration", "Efficiency"],
    #         all_ranking,
    #         "",
    #         None
    #     )

    def show_best_selling_products(self) -> None:
        ranking = self.DB.getBestSellingProductByDateRange(
            self.start_date, self.end_date
        )
        show_dynamic(
            self.f_dashboard_best_sellin_product,
            "Best selling product",
            ["Name", "Unit", "Quantity", "Price"],
            ranking,
            ["Price"],
            to_money,
        )


def to_money(total: float, currency: str = "DA") -> str:
    return f"{total:,.2f} {currency}"


def show_dynamic(
    container: QFrame,
    title: str,
    fields: List[str],
    ranking: List,
    field_w: List[str],
    wrapper: Callable,
) -> None:
    for child in container.findChildren(QFrame):
        child.deleteLater()
    # Title
    frame = QFrame(parent=container)
    frame.setFrameShape(QFrame.StyledPanel)
    frame.setLineWidth(1)
    frame.setLayout(QHBoxLayout())
    label = QLabel()
    label.setText(title)
    label.setFont(QFont("Times", 22))
    label.setScaledContents(True)
    label.setAlignment(Qt.AlignHCenter)
    # label.setAlignment(Qt.AlignVCenter)
    frame.layout().addWidget(label)
    container.layout().addWidget(frame)

    # frame = QScrollArea(parent=container)

    for i, results in enumerate(ranking):
        frame = QFrame(parent=container)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setLineWidth(1)
        frame.setLayout(QHBoxLayout())
        # Add header
        if i == 0:
            for field in ["Rank"] + fields:
                label = QLabel()
                label.setText(str(field))
                label.setFont(QFont("Times", 16))
                label.setScaledContents(True)
                label.setAlignment(Qt.AlignHCenter)
                label.setAlignment(Qt.AlignVCenter)
                if field == "Rank":
                    label.setMaximumWidth(80)
                frame.layout().addWidget(label)
            container.layout().addWidget(frame)

        # add rank
        frame = QFrame(parent=container)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setLineWidth(1)
        frame.setLayout(QHBoxLayout())

        label = QLabel()
        label.setText(str(i + 1))
        label.setFont(QFont("Times", 14))
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignHCenter)
        label.setAlignment(Qt.AlignVCenter)
        label.setMaximumWidth(80)
        frame.layout().addWidget(label)

        for field, result in zip(fields, results):
            label = QLabel()
            if field in field_w and wrapper is not None and result is not None:
                label.setText(str(wrapper(result)))
            else:
                label.setText(str(result))
            label.setFont(QFont("Times", 14))
            label.setScaledContents(True)
            label.setAlignment(Qt.AlignHCenter)
            label.setAlignment(Qt.AlignVCenter)
            frame.layout().addWidget(label)
        container.layout().addWidget(frame)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = DashBoard()
    window.show()
    sys.exit(app.exec_())
