import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QShortcut
from PyQt5.QtGui import (
    QPixmap,
    QImage,
    QKeySequence,
    QPainter,
    QPen,
    QColor,
    QPainterPath,
)
from PyQt5.QtCore import Qt, QSize

from utils import Qimage_load
from customQWidgets import QMaskCanvas


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.qimg_image_orig = Qimage_load("img.png")
        # self.qimg_image_mask = Qimage_load('1535822464729.jpg')
        # self.qimg_image_extract = Qimage_load('1535822464729.jpg')

        self.qimg_image_mask = QImage(
            QSize(self.qimg_image_orig.width(), self.qimg_image_orig.height()),
            QImage.Format_ARGB32,
        )
        self.qimg_image_extract = QImage(
            QSize(self.qimg_image_orig.width(), self.qimg_image_orig.height()),
            QImage.Format_ARGB32,
        )
        self.qimg_mask_paint = QImage(
            QSize(self.qimg_image_orig.width(), self.qimg_image_orig.height()),
            QImage.Format_ARGB32,
        )

        self.qpix_image_orig = QPixmap.fromImage(self.qimg_image_orig)
        self.qpix_image_mask = QPixmap.fromImage(self.qimg_image_mask)
        self.qpix_image_extract = QPixmap.fromImage(self.qimg_image_extract)
        self.qpix_mask_paint = QPixmap.fromImage(self.qimg_mask_paint)

        self.lbl_image_orig = QLabel("image", self)
        self.lbl_image_mask = QLabel("mask", self)
        self.lbl_image_extract = QLabel("extract", self)
        # self.lbl_mask_paint = QLabel('mask paint',self)
        self.lbl_mask_paint = QMaskCanvas(
            (self.qimg_image_orig.height(), self.qimg_image_orig.width())
        )

        self.lbl_image_orig.setPixmap(self.qpix_image_orig)
        self.lbl_image_orig.setAlignment(Qt.AlignCenter)

        self.lbl_image_mask.setPixmap(self.qpix_image_mask)
        self.lbl_image_mask.setAlignment(Qt.AlignCenter)

        self.lbl_image_extract.setPixmap(self.qpix_image_extract)
        self.lbl_image_extract.setAlignment(Qt.AlignCenter)

        grid = QGridLayout()
        grid.addWidget(self.lbl_image_orig, 0, 0)
        grid.addWidget(self.lbl_image_mask, 0, 1)
        grid.addWidget(self.lbl_image_extract, 0, 2)

        grid.addWidget(self.lbl_mask_paint, 0, 0)

        self.setLayout(grid)
        self.setWindowTitle("MaskTool")
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
