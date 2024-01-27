from PyQt5.QtWidgets import (QApplication, QLabel,
    QListWidget, QTextEdit, QWidget, 
    QPushButton, QLineEdit, QListWidget, QHBoxLayout, 
    QVBoxLayout, QFileDialog, QMessageBox)
import os
from ImageProcessor import ImageProcessor




app = QApplication([])
window = QWidget()
window.setWindowTitle("Easy editor")
window.resize(1000, 600)
bn = QFileDialog()

main_line = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()
button_line = QHBoxLayout()
image = QLabel("image")
btn_folder = QPushButton("Floder")
photo_list = QListWidget()
turn_left =  QPushButton("Вліво")
turn_right =  QPushButton("Вправо")
mirror =  QPushButton("Відзиркалити")
color_photo =  QPushButton("Ч/Б")
blur = QPushButton("Розмиття")
rizkict =  QPushButton("Різкість")


line1.addWidget(btn_folder)
line1.addWidget(photo_list)
line2.addWidget(image)
line2.addLayout(button_line)
main_line.addLayout(line1)
main_line.addLayout(line2)



button_line.addWidget(turn_left)
button_line.addWidget(turn_right)
button_line.addWidget(mirror)
button_line.addWidget(color_photo)
button_line.addWidget(blur)
button_line.addWidget(rizkict)

window.setLayout(main_line)

btn_folder.setStyleSheet('''
background-color: #2734e8;
color: #ffbb00                
''')


photo_list.setStyleSheet('''
background-color: #ffbb00;
color: #2734e8                
''')




turn_left.setStyleSheet('''
background-color: #2734e8;
color: #ffbb00                
''')

turn_right.setStyleSheet('''
background-color: #ffbb00;
color: #2734e8                
''')

mirror.setStyleSheet('''
background-color: #2734e8;
color: #ffbb00                
''')


color_photo.setStyleSheet('''
background-color: #ffbb00;
color: #2734e8                
''')

rizkict.setStyleSheet('''
background-color: #2734e8;
color: #ffbb00                
''')


window.setStyleSheet('''
background-color: #00ab7a              
''')


def filter (files):
    img_files = []
    filters = ['png', 'jpg', 'jpeg', 'gif']
    for file in files:
        if file.split('.')[-1] in filters:
            img_files.append(file)

    return img_files
    



def showFloder():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    filenames = filter (os.listdir(workdir))
    photo_list.addItems(filenames)

btn_folder.clicked.connect(showFloder)


workImage = ImageProcessor(image)

def showChosenItem():
    filename = photo_list.currentItem().text()
    workImage.loadImage(filename, workdir)
    workImage.showImage(os.path.join(workdir, filename))



photo_list.currentRowChanged.connect(showChosenItem)
color_photo.clicked.connect(workImage.do_bw)
turn_left.clicked.connect(workImage.left)
turn_right.clicked.connect(workImage.right)
rizkict.clicked.connect(workImage.sharp)
mirror.clicked.connect(workImage.mirrorer)
blur.clicked.connect(workImage.blur)
window.show()
app.exec_()