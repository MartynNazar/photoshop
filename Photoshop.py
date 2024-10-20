import os
from PIL import Image

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

    def load(self):
        image_path = os.path.join(self.folder, self.filename)
        self.photo = Image.open(image_path)

    def show_images(self, image_lbl):
        pixels = pil2pixmap(self.photo)
        pixels = pixels.scaledToWidth(500)
        image_lbl.setPixmap(pixels)



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
filter1_btn = QPushButton('Фільтер1')
filter2_btn = QPushButton('Фільтер2')
filter3_btn = QPushButton('Фільтер3')
filter4_btn = QPushButton('Фільтер4')
filter5_btn = QPushButton('Фільтер5')



mainline = QHBoxLayout()
v1 = QVBoxLayout()
v1.addWidget(dir_btn)
v1.addWidget(images_list)
mainline.addLayout(v1)

v2 = QVBoxLayout()
v2.addWidget(image_lbl)
mainline.addLayout(v2)

h1 = QHBoxLayout()
h1.addWidget(filter1_btn)
h1.addWidget(filter2_btn)
h1.addWidget(filter3_btn)
h1.addWidget(filter4_btn)
h1.addWidget(filter5_btn)
v2.addLayout(h1)

photo_manager = PhotoManager()

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
dir_btn.clicked.connect(open_folder)
window.setLayout(mainline)
window.show()
app.exec()



