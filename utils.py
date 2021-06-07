import os

import cv2
from PyQt5.QtGui import QImage


def make_dir():
    os.makedirs("./img", exist_ok=True)
    os.makedirs("./mask", exist_ok=True)
    os.makedirs("./extract", exist_ok=True)
    os.makedirs("./extracted_character_mask", exist_ok=True)


def Qimage_load(path):
    img = cv2.imread(path)
    h, w, c = img.shape
    bytesPerLine = c * w
    qImg = QImage(
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB), w, h, bytesPerLine, QImage.Format_RGB888
    )
    return qImg


if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets, QtGui, QtCore

    app = QtWidgets.QApplication(sys.argv)
    qImg = Qimage_load("1535822464729.jpg")
    pixmap_image = QtGui.QPixmap.fromImage(qImg)
    label_imageDisplay = QtWidgets.QLabel()
    label_imageDisplay.setPixmap(pixmap_image)
    label_imageDisplay.setAlignment(QtCore.Qt.AlignCenter)
    label_imageDisplay.setScaledContents(True)
    label_imageDisplay.setMinimumSize(1, 1)
    label_imageDisplay.show()
    sys.exit(app.exec_())
