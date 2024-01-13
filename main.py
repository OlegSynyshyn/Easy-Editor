from PyQt5.QtWidgets import (QApplication, QLabel,
    QListWidget, QTextEdit, QWidget, 
    QPushButton, QLineEdit, QListWidget, QHBoxLayout, 
    QVBoxLayout, QFileDialog)
import os
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
button_line.addWidget(rizkict)

window.setLayout(main_line)






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










window.show()
app.exec_()