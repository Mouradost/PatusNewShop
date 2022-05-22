from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
from typing import List
import json
import base64


app = QApplication(sys.argv)


def openConvertFile(file_paths: List[str]) -> str:
    discription = {"Extension": "", "Data": None}
    with open(file_paths, "rb") as f:
        discription["Extension"] = os.path.splitext(file_paths)[-1]
        discription["Data"] = base64.b64encode(f.read()).decode("ascii")
    return json.dumps(discription)


def loadConvertFile(discription: str) -> None:
    discription = json.loads(discription)
    tmp_file_path = os.path.join(
        os.getcwd(), "tmp", f"temp{discription['Extension']}")
    with open(tmp_file_path, "wb") as f:
        f.write(base64.b64decode(discription["Data"]))
    os.system(tmp_file_path)


files, _ = QFileDialog.getOpenFileName(
    None, "Open File", "")
loadConvertFile(openConvertFile(files))
print(app.exec_())
sys.exit(app.exec_())
