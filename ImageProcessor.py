import os
from PIL import Image,  ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class ImageProcessor:
    def __init__(self):
        self.original = None
        self.filename = None
        self.dir = None
        self.save_dir = "edited/"


    def loadImage(self, filename, dir):
        self.filename = filename
        self.dir = dir
        path = os.path.join(self.dir, self.filename)
        self.original = Image.open(path)
    def showImage(self, path, label):
        label.hide()
        pixmap = QPixmap(path)
        
        w = label.width()
        h = label.height()

        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.show()
    def do_bw(self):
        self.original = self.original.convert("L")

    def saveAndShowImage(self):
        pass
    def left(self):
        pass
    def blur(self):
        pass