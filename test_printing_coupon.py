from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtWebEngineWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.coupon_path = "./Patus-coupon-tiny.svg"
        self.current_viewer = None

        self.w_main = QWidget(self)
        self.v_layout = QVBoxLayout(self.w_main)
        self.w_main.setLayout(self.v_layout)

        self.f_engine = QFrame(self.w_main)
        self.h_layout_engine = QHBoxLayout()
        self.f_engine.setLayout(self.h_layout_engine)

        self.f_size = QFrame(self.w_main)
        self.h_layout_size = QHBoxLayout()
        self.f_size.setLayout(self.h_layout_size)

        self.f_btn = QFrame(self.w_main)
        self.h_layout = QHBoxLayout()
        self.f_btn.setLayout(self.h_layout)

        self.coupon_preview = QSvgWidget(parent=self.w_main)
        self.coupon_preview.load(self.coupon_path)
        self.coupon_preview.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.current_viewer = self.coupon_preview

        self.coupon_preview_web = QWebEngineView(parent=self.w_main)
        self.coupon_preview_web.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.coupon_preview_web.setVisible(False)

        self.btn_loader = QPushButton(self)
        self.btn_loader.setText("Load")
        self.btn_loader.clicked.connect(self.load_coupon)
        self.h_layout.addWidget(self.btn_loader)

        self.btn_preview = QPushButton(self)
        self.btn_preview.setText("Preview")
        self.btn_preview.clicked.connect(self.preview_coupon)
        self.h_layout.addWidget(self.btn_preview)

        self.btn = QPushButton(self)
        self.btn.setText("Print")
        self.btn.clicked.connect(self.print_coupon)
        self.h_layout.addWidget(self.btn)

        self.btn_bf = QPushButton(self)
        self.btn_bf.setText("Brute force")
        self.btn_bf.clicked.connect(self.print_brute_force_coupon)
        self.h_layout.addWidget(self.btn_bf)

        self.btn_ps = QPushButton(self)
        self.btn_ps.setText("Show printer details")
        self.btn_ps.clicked.connect(self.show_current_parameters)
        self.h_layout.addWidget(self.btn_ps)

        self.cb_over_write = QCheckBox("Over write print settings", self.f_size)
        self.h_layout_size.addWidget(self.cb_over_write)

        self.cb_format = QComboBox(self.f_engine)
        self.cb_format.addItems(["Pdf Format", "Native Format"])
        self.cb_format.currentIndexChanged.connect(self.change_output_format)
        self.h_layout_size.addWidget(self.cb_format)

        self.cb_orientation = QComboBox(self.f_engine)
        self.cb_orientation.addItems(["Portrait", "Landscape"])
        self.cb_orientation.currentIndexChanged.connect(self.change_printer_orientation)
        self.h_layout_size.addWidget(self.cb_orientation)

        self.sb_height = QSpinBox(self.f_size)
        self.sb_height.setMaximum(1000)
        self.sb_height.setValue(50)
        self.h_layout_size.addWidget(self.sb_height)

        self.sb_weight = QSpinBox(self.f_size)
        self.sb_weight.setMaximum(1000)
        self.sb_weight.setValue(180)
        self.h_layout_size.addWidget(self.sb_weight)

        self.btn_submit = QPushButton(self)
        self.btn_submit.setText("Submit")
        self.btn_submit.clicked.connect(self.change_paper_size)
        self.h_layout_size.addWidget(self.btn_submit)

        self.v_layout.addWidget(self.coupon_preview)
        self.v_layout.addWidget(self.coupon_preview_web)
        self.v_layout.addWidget(self.f_engine)
        self.v_layout.addWidget(self.f_size)
        self.v_layout.addWidget(self.f_btn)

        self.setCentralWidget(self.w_main)
        self.setGeometry(QRect(600, 300, 800, 400))
        self.setWindowTitle("Test print coupon")
        self.setup_printer()
        self.setup_engine_choices()

    def setup_engine_choices(self):
        self.printer_name = QLineEdit(self.f_engine)
        self.printer_name.setPlaceholderText("Printer Name")
        self.h_layout_engine.addWidget(self.printer_name)
        self.l_engine = QLabel("Choose an engine", self.f_engine)
        self.cb_engine = QComboBox(self.f_engine)
        self.cb_engine.addItems(["SVG engine", "Web engine"])
        self.cb_engine.currentIndexChanged.connect(self.change_engine_view)
        self.h_layout_engine.addWidget(self.l_engine)
        self.h_layout_engine.addWidget(self.cb_engine)

    def setup_printer(self):
        self.printer = QPrinter(QPrinter.HighResolution)
        self.printer.setOrientation(QPrinter.Portrait)
        self.printer.setPaperSize(QSizeF(180, 50), QPrinter.Millimeter)

    @pyqtSlot(int)
    def change_printer_orientation(self, orientation):
        self.printer.setOrientation(orientation)

    @pyqtSlot(int)
    def change_engine_view(self, engine_type: int):
        if engine_type == 0:
            self.current_viewer = self.coupon_preview
            self.coupon_preview.setVisible(True)
            self.coupon_preview_web.setVisible(False)
            self.coupon_preview.load(self.coupon_path)
        else:
            self.current_viewer = self.coupon_preview_web
            self.coupon_preview_web.setVisible(True)
            self.coupon_preview.setVisible(False)
            self.coupon_preview_web.load(QUrl(self.coupon_path))

    @pyqtSlot()
    def change_paper_size(self):
        height, weight = self.sb_height.value(), self.sb_weight.value()
        self.printer.setPageSize(QPagedPaintDevice.Custom)
        self.printer.setPaperSource(QPrinter.CustomSource)
        self.printer.setPaperSize(QSizeF(height, weight), QPrinter.Millimeter)
        self.printer.setOrientation(
            QPrinter.Orientation(self.cb_orientation.currentIndex())
        )
        self.printer.setOutputFormat(
            QPrinter.OutputFormat(self.cb_format.currentIndex())
        )

    @pyqtSlot(int)
    def change_output_format(self, output_format: int):
        self.printer.setOutputFormat(QPrinter.OutputFormat(output_format))

    @pyqtSlot()
    def load_coupon(self):
        self.coupon_path = QFileDialog.getOpenFileName(
            self,
            "Select a coupon template",
            "./resource/Patus_coupon_template",
            "SVG Files (*.svg)",
            "SVG Files (*.svg)",
        )[0]
        if isinstance(self.current_viewer, QWebEngineView):
            self.coupon_preview_web.load(QUrl(self.coupon_path))
        else:
            self.coupon_preview.load(self.coupon_path)

    @pyqtSlot()
    def print_brute_force_coupon(self):
        if isinstance(self.current_viewer, QWebEngineView):
            QMessageBox.warning(
                self,
                "Under development",
                "Web engine does not have printing function yet",
            )
        else:
            if self.printer_name.text().strip() == "":
                self.printer.setOutputFileName("test-print.pdf")
            else:
                self.printer.setPrinterName(self.printer_name.text())
            renderer = QSvgRenderer(self.coupon_path)
            if renderer.isValid():
                coupon_painter = QPainter(self.printer)
                renderer.render(coupon_painter)
                if coupon_painter.end():
                    QMessageBox.information(
                        self,
                        "Print successful",
                        f"The file {self.coupon_path} has been printed",
                    )
                else:
                    QMessageBox.warning(
                        self,
                        "Print failed",
                        f"The file {self.coupon_path} has not been printed",
                    )
            else:
                QMessageBox.warning(
                    self, "Print failed", f"Could not read the file {self.coupon_path}"
                )

            self.show_current_parameters()

    @pyqtSlot()
    def print_coupon(self):
        if self.cb_orientation.currentIndex():
            print_dialog = QPrintDialog(self.printer, self)
            if print_dialog.exec() == QDialog.Accepted:
                self.process_printing()
        else:
            rsp = QMessageBox.question(
                self,
                "Non native printing",
                "OS can not handle non-native printers\nDo you want to let us handle it ?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if rsp == QMessageBox.Yes:
                self.process_printing()

    @pyqtSlot()
    def preview_coupon(self):
        if isinstance(self.current_viewer, QWebEngineView):
            QMessageBox.warning(
                self,
                "Under development",
                "Web engine does not have printing preview function yet",
            )
        else:
            printer_preview_dialog = QPrintPreviewDialog(self.printer, self)
            printer_preview_dialog.paintRequested.connect(self.print_preview_coupon)
            if printer_preview_dialog.exec():
                QMessageBox.information(
                    self, "Print from preview", f"Hope you liked it !"
                )

    @pyqtSlot(QPrinter)
    def print_preview_coupon(self, printer: QPrinter) -> None:
        if isinstance(self.current_viewer, QWebEngineView):
            QMessageBox.warning(
                self,
                "Under development",
                "Web engine does not have printing function yet",
            )
            return
        else:
            renderer = QSvgRenderer(self.coupon_path)
            if renderer.isValid():
                coupon_painter = QPainter(printer)
                renderer.render(coupon_painter)
                coupon_painter.end()
            else:
                QMessageBox.warning(
                    self,
                    "Preview failed",
                    f"Could not read the file {self.coupon_path}",
                )
        self.show_current_parameters()

    @pyqtSlot()
    def show_current_parameters(self):
        str_parameters = f"""
Printing with the following parameters:
Printer name: {self.printer.printerName()}
Printer paper source: {self.printer.paperSource()}
Printer orientation: {"Landscape" if self.printer.orientation() else "Portrait"}
Printer paper size: {self.printer.paperSize()}
Printer paper size in millimeter: {self.printer.paperSize(QPrinter.Millimeter)}
Printer full page: {self.printer.fullPage()}
Printer color mode: {self.printer.colorMode()}
Printer copy count: {self.printer.copyCount()}
Printer output file name: {self.printer.outputFileName()}
Printer output format: {"NativeFormat" if self.printer.outputFormat() else "PdfFormat"}"""
        QMessageBox.information(self, "Printer Details", str_parameters)

    def process_printing(self):
        self.printer_name.setText(self.printer.printerName())
        if self.cb_over_write.isChecked():
            self.change_paper_size()
        if isinstance(self.current_viewer, QWebEngineView):
            QMessageBox.warning(
                self,
                "Under development",
                "Web engine does not have printing function yet",
            )
            return
        else:
            renderer = QSvgRenderer(self.coupon_path)
            if renderer.isValid():
                coupon_painter = QPainter(self.printer)
                renderer.render(coupon_painter)
                if coupon_painter.end():
                    QMessageBox.information(
                        self,
                        "Print successful",
                        f"The file {self.coupon_path} has been printed",
                    )
                else:
                    QMessageBox.warning(
                        self,
                        "Print failed",
                        f"The file {self.coupon_path} has not been printed",
                    )
            else:
                QMessageBox.warning(
                    self,
                    "Print failed",
                    f"Could not render the file {self.coupon_path}",
                )

        self.show_current_parameters()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
