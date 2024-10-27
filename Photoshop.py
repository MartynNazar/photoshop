import os
from PIL import Image, ImageFilter, ImageEnhance

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *

def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap

class PhotoManager:
    def  __init__(self):
        self.photo = None
        self.dir_btn = None
        self.filename = None
        self.image_lbl = None

    def load(self):
        image_path = os.path.join(self.folder, self.filename)
        self.photo = Image.open(image_path)

    def show_images(self, image_lbl):
        pixels = pil2pixmap(self.photo)
        pixels = pixels.scaledToWidth(500)
        image_lbl.setPixmap(pixels)

    def bw(self):
        self.photo = self.photo.convert("L")
        self.show_images(self.image_lbl)

    def leften(self):
        self.photo = self.photo.transpose(Image.ROTATE_90)
        self.show_images(self.image_lbl)

    def mirron(self):
        self.photo = self.photo.transpose(Image.FLIP_LEFT_RIGHT)
        self.show_images(self.image_lbl)

    def risk(self):
        self.photo = self.photo.filter(ImageFilter.SHARPEN)
        self.show_images(self.image_lbl)

    def countery(self):
        self.photo = self.photo.filter(ImageFilter.CONTOUR)
        self.show_images(self.image_lbl)


    def details(self):
        self.photo = self.photo.filter(ImageFilter.DETAIL)
        self.show_images(self.image_lbl)

    def rozmivan(self):
        self.photo = self.photo.filter(ImageFilter.BLUR)
        self.show_images(self.image_lbl)

    def nas(self):
        self.photo = ImageEnhance.Color(self.photo).enhance(1.5)
        self.show_images(self.image_lbl)


app = QApplication([])


app.setStyleSheet("""
        QWidget{
            background: #969696 ;
        }

        QPushButton
        {
            background-color: #4dd5ff ;
            border-width: 9px ;
            border-style: solid ;
            border-color: yellow ;
            border-radius: 20px ;
            font-family: Harrington;
            font-size: 22px ;
            min-width: 6em ;
            padding: 6px ;
            color: purple ;
        }
""")




window = QWidget()

dir_btn = QPushButton('Папка')
image_lbl = QLabel('Картинка')
images_list = QListWidget()
countur = QPushButton('Накладання контурів')
sharpness = QPushButton('Різкість')
mirror = QPushButton('Відзеркалення')
left = QPushButton('Вліво')
chb = QPushButton('Ч/Б')



detalizanion = QPushButton('Збільшення деталізації')
rozmivania = QPushButton('Розмивання')
nasich  = QPushButton('Збільшення насиченості')



mainline = QHBoxLayout()
v1 = QVBoxLayout()
v1.addWidget(dir_btn)
v1.addWidget(images_list)
mainline.addLayout(v1)

v2 = QVBoxLayout()
v2.addWidget(image_lbl)
mainline.addLayout(v2)

h1 = QHBoxLayout()
h1.addWidget(countur)
h1.addWidget(sharpness)
h1.addWidget(mirror)
h1.addWidget(left)
h1.addWidget(chb)
v2.addLayout(h1)

h2 = QHBoxLayout()
h2.addWidget(detalizanion)
h2.addWidget(rozmivania)
h2.addWidget(nasich)
v2.addLayout(h2)


photo_manager = PhotoManager()
photo_manager.image_lbl = image_lbl
def open_folder():
    photo_manager.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(photo_manager.folder)
    images_list.clear()


    #перебирати файли
        #добавляти з потрібним розширенням (endwith)
    images_list.addItems(files)

def show_chosen_image():
    photo_manager.filename = images_list.currentItem().text()
    photo_manager.load()
    photo_manager.show_images(image_lbl)


images_list.currentRowChanged.connect(show_chosen_image)
chb.clicked.connect(photo_manager.bw)
left.clicked.connect(photo_manager.leften)
mirror.clicked.connect(photo_manager.mirron)
sharpness.clicked.connect(photo_manager.risk)
countur.clicked.connect(photo_manager.countery)
detalizanion.clicked.connect(photo_manager.details)
rozmivania.clicked.connect(photo_manager.rozmivan)
nasich.clicked.connect(photo_manager.nas)
dir_btn.clicked.connect(open_folder)
window.setLayout(mainline)
window.show()
app.exec()



