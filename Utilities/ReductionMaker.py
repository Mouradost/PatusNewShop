from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import logging
import os
from datetime import datetime

from DB.DBHandler import DBHelper


class ReductionMaker(QDialog):
    def __init__(self, parent=None):
        super(ReductionMaker, self).__init__(parent=parent)
        uic.loadUi(os.path.join(os.getcwd(), "uis", "ReductionMaker.ui"), self)
        self.db = DBHelper()
        self.tb_coupon_reduce.clicked.connect(self.coupon_search)
        self.tb_manual_reduce.clicked.connect(self.manual_reduce)
        self.reduction = 0.0

    def clear_content(self):
        for child in self.f_content.findChildren(QWidget):
            child.deleteLater()
        for child in self.f_content.findChildren(QToolButton):
            child.deleteLater()

    def manual_reduce(self):
        self.clear_content()
        self.reduce_widget = ReduceWidget(self)
        self.reduce_widget.reductionChanged.connect(self.updateReduction)
        self.f_content.layout().addWidget(self.reduce_widget)

    def coupon_search(self):
        self.clear_content()
        self.coupon_search_widget = CouponSearchWidget(self.db, self)
        self.coupon_search_widget.reductionChanged.connect(self.updateReduction)
        self.f_content.layout().addWidget(self.coupon_search_widget)

    @pyqtSlot(float)
    def updateReduction(self, reduction: float):
        self.reduction = reduction


class CouponSearchWidget(QWidget):
    reductionChanged = pyqtSignal(float)

    def __init__(self, db: DBHelper, parent=None):
        super(CouponSearchWidget, self).__init__(parent)
        uic.loadUi(os.path.join(os.getcwd(), "uis", "CouponSearchWidget.ui"), self)
        self.db = db
        self.coupon = None
        self.parent_widget = parent
        self.btn_search.clicked.connect(self.get_coupon)
        self.le_coupon_id.clear()
        self.le_coupon_id.setValidator(QIntValidator())
        self.bb_coupon.accepted.connect(self.check_info)
        self.bb_coupon.rejected.connect(parent.reject)

    def get_coupon(self):
        try:
            self.coupon = self.db.getCouponById(int(self.le_coupon_id.text()))
            self.te_coupon_info.clear()
            if self.coupon is None:
                self.te_coupon_info.append("Coupon not found")
                self.reduction = 0.0
            else:
                self.te_coupon_info.append(self.coupon.to_str())
                self.reduction = self.coupon.amount
        except Exception as e:
            logging.error(f"[CouponSearchWidget] {e}")
            QMessageBox.warning(
                self,
                "Coupon error",
                f"{e}",
            )

    def check_info(self):
        try:
            if self.coupon is None:
                QMessageBox.information(
                    self,
                    "Coupon not found",
                    "There is no coupon selected please search a valid coupon or click on cancel",
                )
            else:
                if self.coupon.is_used:
                    QMessageBox.information(
                        self,
                        "Coupon used",
                        "The coupon selected is used and can't be applied to this order",
                    )
                else:
                    if (
                        datetime.strptime(self.coupon.date_end, "%Y-%m-%d %H:%M:%S")
                        < datetime.now()
                    ):
                        QMessageBox.information(
                            self,
                            "Coupon expired",
                            "The coupon selected is expired and can't be applied to this order",
                        )
                    else:
                        self.reductionChanged.emit(self.reduction)
                        self.coupon.is_used = True
                        self.db.updateCoupon(self.coupon)
                        self.parent_widget.accept()
        except Exception as e:
            logging.error(f"[CouponSearchWidget] {e}")
            QMessageBox.warning(
                self,
                "Coupon error",
                f"{e}",
            )


class ReduceWidget(QWidget):
    reductionChanged = pyqtSignal(float)

    def __init__(self, parent=None):
        super(ReduceWidget, self).__init__(parent)
        uic.loadUi(os.path.join(os.getcwd(), "uis", "ReduceWidget.ui"), self)
        self.le_reduction.clear()
        self.le_reduction.setValidator(QDoubleValidator())
        self.le_reduction.textChanged.connect(self.set_reduction)
        self.bb_reduce.accepted.connect(parent.accept)
        self.bb_reduce.rejected.connect(parent.reject)

    @pyqtSlot(str)
    def set_reduction(self, txt: str):
        try:
            if len(txt) > 0:
                self.reduction = float(txt)
                self.reductionChanged.emit(self.reduction)
            else:
                self.reduction = 0.0
                self.reductionChanged.emit(self.reduction)
        except Exception as e:
            logging.error(f"[ReduceWidget] {e}")
            QMessageBox.warning(
                self,
                "Reduction error",
                f"{e}",
            )
