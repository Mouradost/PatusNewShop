from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from PyQt5.QtWebKit import *
# from PyQt5.QtWebEngineWidgets import QWebEnginePage
import sys


app = QApplication(sys.argv)
files, _ = QFileDialog.getOpenFileName(
    None, "Open File", "", "PDF Files (*.pdf)")

print(files)
# web = QWebView()
# web.settings.setAttribute(QWebSettings.PluginsEnabled, True)
# web.load(QUrl("C:\\Users\\mouradost\\Desktop\\STGM_SPRINGER\\root.pdf"))
# web.show()
app.exec_()
