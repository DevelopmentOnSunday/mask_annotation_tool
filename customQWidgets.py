import sys
from PyQt5.QtCore import QPoint, Qt, QSize, QRect
from PyQt5.QtWidgets import QWidget, QApplication, QAction, QFileDialog, QShortcut
from PyQt5.QtGui import (
    QKeySequence,
    QPixmap,
    QPainter,
    QPen,
    QColor,
    QPainterPath,
    QImage,
)


class QMaskCanvas(QWidget):
    def __init__(self, size):
        super().__init__()
        self.drawingPath = None
        self.image = QPixmap.fromImage(
            QImage(QSize(size[1], size[0]), QImage.Format_ARGB32)
        )
        # self.image = QPixmap("img.png")

        self.resize(self.image.width(), self.image.height())
        self.setMouseTracking(True)
        self.pos = None
        # pen size modulation
        self.pen_size = 20
        self._clear_size = 20

        self.shortcut_size_up = QShortcut(QKeySequence("w"), self)
        self.shortcut_size_down = QShortcut(QKeySequence("s"), self)
        self.shortcut_pen_change = QShortcut(QKeySequence("q"), self)
        self.shortcut_size_up.activated.connect(self.penSizeUp)
        self.shortcut_size_down.activated.connect(self.penSizeDown)
        self.shortcut_pen_change.activated.connect(self.penModeChange)
        self.change = True
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)
        if self.drawingPath:
            if self.change:
                painter.setPen(
                    QPen(
                        QColor(121, 252, 50, 100),
                        self.pen_size,
                        Qt.SolidLine,
                        Qt.RoundCap,
                    )
                )
            else:
                painter.setPen(
                    QPen(
                        QColor(121, 252, 50, 100),
                        self.pen_size,
                        Qt.SolidLine,
                        Qt.RoundCap,
                    )
                )
                r = QRect(QPoint(), self.pen_size * QSize())
                painter.setCompositionMode(QPainter.CompositionMode_Clear)
                painter.eraseRect(r)
            painter.drawPath(self.drawingPath)
        painter.setPen(QPen(QColor(255, 0, 0, 200), 1, Qt.SolidLine, Qt.RoundCap))
        if self.pos:
            painter.drawEllipse(self.pos, self.pen_size // 2, self.pen_size // 2)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawingPath = QPainterPath()
            self.drawingPath.moveTo(event.pos())

    def mouseMoveEvent(self, event):
        self.pos = event.pos()
        if event.buttons() and Qt.LeftButton and self.drawingPath:
            self.drawingPath.lineTo(event.pos())
        self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawingPath:
            painter = QPainter(self.image)
            if self.change:
                painter.setPen(
                    QPen(
                        QColor(121, 252, 50, 100),
                        self.pen_size,
                        Qt.SolidLine,
                        Qt.RoundCap,
                    )
                )
            else:
                painter.setPen(
                    QPen(
                        QColor(121, 252, 50, 100),
                        self.pen_size,
                        Qt.SolidLine,
                        Qt.RoundCap,
                    )
                )
                r = QRect(QPoint(), self.pen_size * QSize())
                painter.setCompositionMode(QPainter.CompositionMode_Clear)
                painter.eraseRect(r)
            painter.drawPath(self.drawingPath)
            self.drawingPath = None
            self.update()

    def penSizeUp(self):
        self.pen_size += 2
        self.update()

    def penSizeDown(self):
        self.pen_size -= 2
        self.update()

    def penModeChange(self):
        self.change = not self.change

    # def image(self):
    #     pass
    # return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = QMaskCanvas((600, 800))
    sys.exit(app.exec_())
