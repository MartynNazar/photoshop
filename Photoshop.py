from PyQt5.QtWidgets import *


app = QApplication([])


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


window.setLayout(mainline)
window.show()
app.exec()