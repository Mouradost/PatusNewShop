import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *
from PyQt5.QtPrintSupport import *

from typing import List
from datetime import datetime, timedelta
import logging
import os

from Utilities.CouponGenerator import create_coupon_xml
from Utilities.UiUtilities import displayDbData
from DB.DBHandler import DBHelper
from DB.DbTables import Coupon
from DB.ShopDbInfo import CouponTable


class CouponMakerUi(QDialog):
    def __init__(self, parent=None):
        super(CouponMakerUi, self).__init__(parent=parent)
        uic.loadUi(os.path.join(os.getcwd(), "uis", "coupon_maker.ui"), self)
        self.le_amount.clear()
        self.le_amount.setValidator(QDoubleValidator())
        self.de_start.setDate(datetime.now())
        self.de_end.setDate(datetime.now() + timedelta(weeks=4))
        self.setup_svg_previewers()
        self.pb_print.setVisible(False)

        self.tb_manage_picture.clicked.connect(self.load_side_picture)
        self.tb_manage_preview.clicked.connect(self.preview_coupon)
        self.tb_manage_print.clicked.connect(self.direct_print)
        self.tw_coupon_maker.currentChanged.connect(self.db_load_coupons)
        self.tw_manage_coupons.doubleClicked.connect(self.db_load_selected_coupon)
        self.tb_manage_template.clicked.connect(self.load_template)

        self.tb_load_side_picture.clicked.connect(self.load_side_picture)
        self.tb_load_template.clicked.connect(self.load_template)
        self.tb_preview.clicked.connect(self.preview_coupon)
        self.tb_print.clicked.connect(self.direct_print)
        self.tb_generate.clicked.connect(self.generate_coupon)
        self.db = DBHelper()
        self.template = None
        self.coupons: List[Coupon] = []
        self.coupons_xml: List[str] = []
        self.is_preview: bool = False
        self.saved = False

    def setup_svg_previewers(self):
        self.w_result_preview = QSvgWidget(parent=self.f_preview)
        self.w_template_preview = QSvgWidget(parent=self.f_preview)
        self.f_preview.layout().addWidget(self.w_template_preview)
        self.f_preview.layout().addWidget(self.w_result_preview)
        self.w_manage_preview = QSvgWidget(parent=self.f_manage_preview)
        self.f_manage_preview.layout().addWidget(self.w_manage_preview)

    def load_template(self):
        file_name = QFileDialog.getOpenFileName(
            self,
            "Choose a picture",
            os.path.join(os.getcwd(), "resource", "Coupon_template"),
            "SVG Files (*.svg)",
        )[0]
        if os.path.isfile(file_name):
            if self.tw_coupon_maker.currentIndex():
                self.le_manage_template_path.setText(file_name)
            else:
                self.template = file_name
                self.w_template_preview.load(self.template)

    def load_side_picture(self):
        file_name = QFileDialog.getOpenFileName(
            self,
            "Choose a picture",
            os.path.join(os.getcwd(), "resource", "Coupon_template"),
            "PNG Files (*.png)",
        )[0]
        if os.path.isfile(file_name):
            if self.tw_coupon_maker.currentIndex():
                self.le_manage_picture_path.setText(file_name)
            else:
                self.le_side_picture_path.setText(file_name)

    def generate_coupon(self):
        try:
            if (
                self.template is None
                or len(self.le_amount.text()) == 0
                or len(self.le_side_picture_path.text()) == 0
            ):
                QMessageBox.critical(
                    self,
                    "Pre-setup required",
                    "Please provide a template, a side picture, the amount, date start and date end",
                )
                return
            date_start = self.de_start.date().toString("yyyy-MM-dd")
            date_end = self.de_end.date().toString("yyyy-MM-dd")
            date_format = "%Y-%m-%d"
            date_start = datetime.strptime(date_start, date_format)
            date_end = datetime.strptime(date_end, date_format)
            amount = float(self.le_amount.text())
            start_number = self.db.getLastIdByTableName(CouponTable.TABLE_NAME) + 1
            # start_number = 1
            self.coupons = []
            self.coupons_xml = []
            self.pb_print.setVisible(True)
            self.pb_print.setMaximum(self.sb_count.value())
            self.pb_print.setValue(0)
            for i in range(start_number, start_number + self.sb_count.value()):
                self.pb_print.setValue(i)
                coupon = Coupon(
                    id=i,
                    date_start=date_start,
                    date_end=date_end,
                    date_creation=datetime.now(),
                    amount=amount,
                )
                coupon_xml = create_coupon_xml(
                    coupon=coupon,
                    template=self.template,
                    side_image=self.le_side_picture_path.text(),
                )
                self.coupons.append(coupon)
                self.coupons_xml.append(coupon_xml)
            self.w_result_preview.load(QByteArray(coupon_xml))
            self.pb_print.setVisible(False)
            self.saved = False
        except Exception as e:
            logging.error(f"[COUPON MAKER] Generate coupon failed: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Generate coupon failed")
            msg.setInformativeText("Generate coupon failed")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Error message")
            msg.exec_()

    @pyqtSlot()
    def direct_print(self):
        self.is_preview = False
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.NativeFormat)
        self.print_coupon(printer)

    @pyqtSlot(QPrinter)
    def print_coupon(self, printer: QPrinter = None):
        printer = self.change_paper_size(printer)
        nb_coupons = len(self.coupons_xml) - 1
        self.pb_print.setVisible(True)
        self.pb_print.setMaximum(nb_coupons)
        self.pb_print.setValue(0)
        renderer = QSvgRenderer()
        coupon_painter = QPainter(printer)
        for i, coupon in enumerate(self.coupons_xml):
            self.pb_print.setValue(i)
            renderer.load(QByteArray(coupon))
            renderer.render(coupon_painter)
            if i < nb_coupons:
                printer.newPage()
        self.pb_print.setVisible(False)
        if self.is_preview:
            coupon_painter.end()
        else:
            if coupon_painter.end():
                QMessageBox.information(
                    self,
                    "Print successful",
                    f"The coupon has been printed",
                )
                if not self.saved and not self.tw_coupon_maker.currentIndex():
                    try:
                        self.db.insertCoupons(self.coupons)
                        self.saved = True
                    except Exception as e:
                        QMessageBox.critical(
                            self,
                            "Coupon save failed",
                            f"Coupons could not be saved to the database because {e}",
                        )
            else:
                QMessageBox.warning(
                    self,
                    "Print failed",
                    f"The coupon has not been printed",
                )

            self.show_current_parameters(printer)

    @pyqtSlot()
    def preview_coupon(self):
        self.is_preview = True
        nb_coupons = len(self.coupons_xml)
        if nb_coupons > 3 or nb_coupons < 2:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setFromTo(1, nb_coupons)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer = self.change_paper_size(printer)
            printer_preview_dialog = QPrintPreviewDialog(printer, self)
            printer_preview_dialog.paintRequested.connect(self.print_coupon)
            if printer_preview_dialog.exec():
                QMessageBox.information(
                    self, "Printed from preview", f"Hope you liked it !"
                )
        else:
            QMessageBox.information(
                self,
                "Preview limitation",
                f"Qt bug when previewing 2 to 3 pages please print directly",
            )

    @pyqtSlot(QPrinter)
    def show_current_parameters(self, printer: QPrinter):
        str_parameters = f"""
Printing with the following parameters:
Printer name: {printer.printerName()}
Printer paper source: {printer.paperSource()}
Printer orientation: {"Landscape" if printer.orientation() else "Portrait"}
Printer paper rectangle: {printer.paperRect()}
Printer paper size: {printer.paperSize()}
Printer paper size in millimeter: {printer.paperSize(QPrinter.Millimeter)}
Printer page rectangle: {printer.pageRect()}
Printer page rectangle in millimeter: {printer.pageRect(QPrinter.Millimeter)}
Printer full page: {printer.fullPage()}
Printer color mode: {printer.colorMode()}
Printer copy count: {printer.copyCount()}
Printer output file name: {printer.outputFileName()}
Printer output format: {"NativeFormat" if printer.outputFormat() else "PdfFormat"}"""
        QMessageBox.information(self, "Printer Details", str_parameters)

    def change_paper_size(self, printer: QPrinter) -> QPrinter:
        printer.setPageSize(QPagedPaintDevice.Custom)
        printer.setPaperSource(QPrinter.CustomSource)
        printer.setPaperSize(QSizeF(50, 180), QPrinter.Millimeter)
        printer.setOrientation(QPrinter.Landscape)
        return printer

    @pyqtSlot(int)
    def db_load_coupons(self, current_index: int):
        if current_index:
            try:
                data = self.db.getAllCoupons(True)
                displayDbData(self.tw_manage_coupons, data)
            except Exception as e:
                QMessageBox.critical(self, "Loading all coupons failed", f"{e}")

    def db_load_selected_coupon(self):
        if os.path.isfile(self.le_manage_template_path.text()) and os.path.isfile(
            self.le_manage_picture_path.text()
        ):
            try:
                self.coupons = []
                self.coupons_xml = []
                coupon = self.db.getCouponById(
                    int(
                        self.tw_manage_coupons.item(
                            self.tw_manage_coupons.currentRow(),
                            self.tw_manage_coupons.columnCount() - 1,
                        ).text()
                    )
                )
                if coupon is not None:
                    coupon = coupon.from_db()
                    coupon_xml = create_coupon_xml(
                        coupon=coupon,
                        template=self.le_manage_template_path.text(),
                        side_image=self.le_manage_picture_path.text()
                        if self.le_manage_picture_path.text().strip() != ""
                        else os.path.join(
                            os.getcwd(),
                            "resource",
                            "Coupon_template",
                            "side_picture.png",
                        ),
                    )
                    self.w_manage_preview.load(QByteArray(coupon_xml))
                    self.coupons_xml.append(coupon_xml)
                    self.coupons.append(coupon)
                    self.saved = True
            except Exception as e:
                QMessageBox.critical(self, "Loading selected coupon failed", f"{e}")
        else:
            QMessageBox.information(
                self,
                "Template or Picture missing",
                "Please select a template and a side picture to load a coupon",
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CouponMakerUi()
    main_window.show()
    sys.exit(app.exec_())
