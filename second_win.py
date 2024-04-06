from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
from second_win import *
class TestWin(QWidget):
    def __init__(self):
        ''' окно, в котором располагается приветствие '''
        super().__init__()
        self.initUI() # создаём и настраиваем графические элементы:
        self.connects() #устанавливает связи между элементами
        self.set_appear()#устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.show()# старт:
    def initUI(self):
        ''' создаёт графические элементы '''
        self.btn_next = QPushButton(txt_next, self)
        self.line_name = QLineEdit(txt_hintname)
        self.line_name = QLineEdit(txt_hintage)
        self.line_name = QLineEdit(txt_hinttest1)
        self.line_name = QLineEdit(txt_hinttest2)
        self.line_name = QLineEdit(txt_hinttest3)
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QVBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        

    def next_click(self):
        self.tw = TestWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
