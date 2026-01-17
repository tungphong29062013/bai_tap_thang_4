import sys
from PySide6.QtWidgets import QLineEdit, QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("cộng hai số")
window.setFixedSize(400,200)

label1=QLabel("nhập số a")
label2=QLabel("nhập số b")
a=QLineEdit()
b=QLineEdit()
add=QPushButton("CỘNG HAI SỐ")
subtract=QPushButton("TRỪ HAI SỐ")

def tinh_tong():
    try:
        num1=int(a.text())
        num2=int(b.text())
        tong=num1+num2
        QMessageBox.information(window,"kết quả",f"tổng={tong}")
    except:
        QMessageBox.warning(window,"yêu cầu sửa lại","hãy nhập đúng số đừng nhập ký tự")

add.clicked.connect(tinh_tong)

def tinh_hieu():
    try:
        num1=int(a.text())
        num2=int(b.text())
        hieu=num1-num2
        QMessageBox.information(window,"kết quả",f"hiệu={hieu}")
    except:
        QMessageBox.warning(window,"yêu cầu sửa lại","hãy nhập đúng số đừng nhập ký tự")
subtract.clicked.connect(tinh_hieu)

layout=QVBoxLayout()
layout.addWidget(label1)
layout.addWidget(a)
layout.addWidget(label2)
layout.addWidget(b)
layout.addWidget(add)
layout.addWidget(subtract)

window.setLayout(layout)
window.show()
sys.exit(app.exec())

