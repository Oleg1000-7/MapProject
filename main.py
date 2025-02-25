import sys

from PyQt6.QtCore import QByteArray
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow

import requests

api_server = "https://static-maps.yandex.ru/v1"

lon = "37.677751"
lat = "55.757718"
delta1 = "1.0"
delta2 = "1.0"
apikey = ""


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update_map()

    def update_map(self):
        pixmap = QPixmap()
        pixmap.loadFromData(self.get_map())
        self.image.setPixmap(pixmap)

    def get_map(self):
        params = {
            "ll": ",".join([lon, lat]),
            "spn": ",".join([delta1, delta2]),
            "apikey": apikey,
        }
        response = requests.get(api_server, params=params)
        return QByteArray(response.content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
