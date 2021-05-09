# -*- coding: utf-8 -*-


############################################################
###0            Statement and Documentation              ###

### License
# This project(It includes but is not limited to the source files,
# \images, fonts, icons and documents that we create) use Apache-2.0 License.
# You can find Apache-2.0 in the subjective dir or URL http://www.apache.org/licenses/LICENSE-2.0.
# In this subject, we use some packets that use GPL License.
# For some special reasons, we do not fully comply with the regulations and use the GPL License.
# If the relevant personnel see the project and think it should use the GPL license,
# \we will definitely correct it!
# If you have any ideas about our license, please contact us.

### Code
# We try to comply with the code specification 
# \in PEP8 specification(https://legacy.python.org/dev/peps/pep-0008/).
# But in fact, there are some small adjustments and unique specifications. 
# The details are as follows.
# 1. When you write a single-sentence comment in more than 1 lines, 
# \it is better to break it from the punctuation and write '\' at the beginning of the next line.
# 2. After experiment, for comment, 
# \it is better to keep 2-space width to code and 1-sapce width to '#'.
# 3. In code, 60 '#' and the following title ('###'+ ordinal + middle title +'###')
# \split multiple 'part's of the code;
# \'###'+ keyword split multiple 'block's of the code;
# \A blank line or line comment split multiple 'paragraph's of the code.
# 4. For internationalization and versatility,
# \All the comment in the code are in English.
# 5. While browsing the code, we strongly recommended you use our own font Point Code.


############################################################
###1               Information And Set-up                ###

### Information
__author__ = "Albert Z"
__date__ = "Unpublished"
__version__ = "Unpublished version"
__classification__ = "A project of PointCode organization"
__license__ = "Apache-2.0 License"
__doc__ = """"""


############################################################
###2        Import Part(With Import-Explaination)        ###

### Time
from time import time, sleep  # For counting time

### GUI
from PyQt5.QtCore import *  # For using Qt core functions(installed by pip)
from PyQt5.QtGui import *  # For using Qt window GUI functions(installed by pip)
from PyQt5.QtWidgets import *  # For using Qt classic window widgets(installed by pip)

### System
import sys  # For operating system(built-in)
import os  # (built-in)

### Request functions
from bot import *  # (self-made)
from client import *  # (self-made)


############################################################
###3                  Main Function Part                 ###

class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__(QPixmap('./icon/pat.png'))
        self.show()
        start = time()
        self.load_data()
        end = time()
        _time = end-start
        start = time()
        if _time < 3:
            while time() - start < 3 - _time:
                sleep(0.01)
                app.processEvents()
        self.close()

    def load_data(self):
        app.processEvents()
        self.setupFont()
        self.window = Window()
        app.processEvents()

    def setupFont(self):
        QFontDatabase.addApplicationFont('./font/WQY.ttf')


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.userid = 0
        self.username = ''
        self.setupUI()
        self.showMinimized()

    def setupUI(self):
        self.signin_win = SigninWindow()
        self.register_win = RegisterWindow()
        self.setMainLayout()
        self.setMarginLayout('bsi')
        self.setChatLayout()

    def setMainLayout(self):
        # Start designing GUI
        self.setWindowTitle('Pat++')
        self.setWindowIcon(QIcon('./icon/pat.png'))
        self.setFixedSize(800, 600)
        self.setStyleSheet('background-color:rgb(255, 255, 255)')

        self.main = QHBoxLayout()
        self.setLayout(self.main)
        
        self.margin = QWidget()
        self.margin.setStyleSheet('background-color:rgb(50, 150, 250)')
        self.mLayout = QVBoxLayout()
        self.margin.setLayout(self.mLayout)
        self.main.addWidget(self.margin)

        self.chatbox = QWidget()
        self.chatbox.setStyleSheet('background-color:rgb(240, 240, 240)')
        self.cLayout = QVBoxLayout()
        self.chatbox.setLayout(self.cLayout)
        self.main.addWidget(self.chatbox)

        self.main.setStretch(0, 1)
        self.main.setStretch(1, 3)
        self.main.setSpacing(0)

    def setMarginLayout(self, mode):
        if self.mLayout.count() > 0:
            for i in range(self.mLayout.count()):
                self.mLayout.removeItem(self.mLayout.itemAt(0))

        if mode == 'bsi':  # before sign in 
            self.mLayout.addStretch(6)
            self.pbtn_signin = QPushButton()
            self.pbtn_signin.setText('登录')
            self.pbtn_signin.setFixedSize(175, 45)
            self.pbtn_signin.setStyleSheet('background-color:rgb(80, 200, 180); border:2px; border-radius:20px; padding:2px 4px;')
            self.pbtn_signin.setFont(QFont('文泉驿等宽正黑', 14))
            self.pbtn_signin.clicked.connect(self.signin_win.show)
            self.mLayout.addWidget(self.pbtn_signin)

            self.mLayout.addStretch(1)
            self.pbtn_register = QPushButton()
            self.pbtn_register.setText('注册')
            self.pbtn_register.setFixedSize(175, 45)
            self.pbtn_register.setStyleSheet('background-color:rgb(80, 200, 70); border:2px; border-radius:20px; padding:2px 4px;')
            self.pbtn_register.setFont(QFont('文泉驿等宽正黑', 14))
            self.pbtn_register.clicked.connect(self.register_win.show)
            self.mLayout.addWidget(self.pbtn_register)
            self.mLayout.addStretch(12)

        elif mode == 'asi':  # after sign in
            self.mLayout.addStretch(6)
            self.lb_name = QLabel()
            self.lb_name.setText(self.username)
            self.lb_name.setAlignment(Qt.AlignCenter)
            self.lb_name.setFixedSize(175, 45)
            self.lb_name.setFont(QFont('文泉驿等宽正黑', 14))
            self.mLayout.addWidget(self.lb_name)

            self.mLayout.addStretch(1)
            self.pbtn_quit = QPushButton()
            self.pbtn_quit.setText('退出登录')
            self.pbtn_quit.setFixedSize(175, 45)
            self.pbtn_quit.setStyleSheet('background-color:rgb(80, 200, 70); border:2px; border-radius:20px; padding:2px 4px;')
            self.pbtn_quit.setFont(QFont('文泉驿等宽正黑', 14))
            self.pbtn_quit.clicked.connect(self.quit)
            self.mLayout.addWidget(self.pbtn_quit)

            self.mLayout.addStretch(12)

    def setChatLayout(self):
        self.lb_title = QLabel()
        self.lb_title.setFixedSize(570, 45)
        self.lb_title.setText('聊天机器人——Alpha')
        self.lb_title.setFont(QFont('文泉驿等宽正黑', 13))
        self.lb_title.setAlignment(Qt.AlignCenter)
        self.lb_title.setStyleSheet('background-color:rgb(255, 255, 255); padding:0px; padding:0px; border:2px; border-radius:10px; padding:2px 4px;')
        self.cLayout.addWidget(self.lb_title)

        self.cScrollArea = QScrollArea()
        self.cScrollArea.setStyleSheet('''
        QScrollArea{
        border: 0px solid;
        border-right-width: 1px;
        border-right-color: #dcdbdc;
        background-color: #f5f5f7;
        border-radius:20px; 
        }
        QScrollBar:vertical {
        border: none;
        background: #f5f5f7;
        width: 10px;
        margin: 0px 0 0px 0;
        }
        QScrollBar::handle:vertical {
        background: Gainsboro;
        min-height: 20px;
        border-radius: 5px;
        border: none;
        }
        QScrollBar::add-line:vertical {
        border: 0px solid grey;
        background: #32CC99;
        height: 0px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
        border: 0px solid grey;
        background: #32CC99;
        height: 0px;
        subcontrol-position: top;
        subcontrol-origin: margin;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
        width: 0px;
        height: 0px;
        }''')

        self.areaHeight = 0
        self.chatarea = QWidget()
        self.chatarea.resize(565, self.areaHeight)
        self.chatarea.setStyleSheet('background-color:rgba(0, 0, 0, 0); border:2px; border-radius:20px; padding:2px 4px;')
        self.cScrollArea.setWidget(self.chatarea)

        self.cLayout.addWidget(self.cScrollArea)
        
        self.caLayout = QVBoxLayout()
        self.chatarea.setLayout(self.caLayout)
        self.caLayout.setSpacing(10)

        self.editor = QPlainTextEdit()
        self.editor.setFixedSize(570, 90)
        self.editor.setFont(QFont('文泉驿等宽正黑', 12))
        self.editor.setStyleSheet('background-color:rgb(255, 255, 255); border:2px; border-radius:20px; padding:2px 4px;')
        self.cLayout.addWidget(self.editor)

        self.pbtn_send = QPushButton()
        self.pbtn_send.setFixedSize(570, 40)
        self.pbtn_send.setText('发送')
        self.pbtn_send.setFont(QFont('文泉驿等宽正黑', 13))
        self.pbtn_send.setStyleSheet('background-color:rgb(80, 200, 180); border:2px; border-radius:20px; padding:2px 8px;')
        self.pbtn_send.clicked.connect(self.send)
        self.cLayout.addWidget(self.pbtn_send)

        self.cLayout.setSpacing(7)


    def signin(self):
        self.signin_win.show()
        if self.signin_win.id:
            self.userid = self.signin_win.id
            self.username = self.signin_win.name
            self.setMarginLayout('asi')
        
    def register(self):
        if self.register_win.id:
            self.userid = self.register_win.id
            self.username = self.register_win.name
            self.setMarginLayout('asi')

    def quit(self):
        self.userid = 0
        self.username = ''
        self.signin_win.id = 0
        self.signin_win.id = ''
        self.register_win.id = 0
        self.register_win.name = ''
        self.setMarginLayout('bsi')

    def send(self):
        self.text = self.editor.toPlainText().strip().replace('\n', '')
        if self.text:
            self.span = QHBoxLayout()
            self.box = MessageBox(None, 'user', self.text)

            self.span.addStretch(0)
            self.span.addWidget(self.box)
            self.caLayout.addLayout(self.span)

            self.areaHeight += self.box.h + 10
            self.chatarea.setFixedHeight(self.areaHeight)

            self.cScrollArea.verticalScrollBar().setValue(self.cScrollArea.verticalScrollBar().maximum())
            self.editor.clear()
            self.get()
        else:
            self.editor.clear()

    def get(self):
        self.answer = post(self.text, self.userid).strip()
        self.span = QHBoxLayout()
        self.box = MessageBox(None, 'bot', self.answer)

        self.span.addWidget(self.box)
        self.span.addStretch(0)
        self.caLayout.addLayout(self.span)

        self.areaHeight += self.box.h + 10
        self.chatarea.setFixedHeight(self.areaHeight)

        self.cScrollArea.verticalScrollBar().setValue(self.cScrollArea.verticalScrollBar().maximum())


class SigninWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.id = 0
        self.name = ''
        self.setupUI()

    def setupUI(self):
        self.setStyleSheet('background-color:white')
        self.setFixedSize(650, 400)
        self.setWindowTitle("登录")
        self.setWindowIcon(QIcon('./icon/pat.png'))

        # top picture
        pixmap = QPixmap("./icon/bg.jpg")
        self.pic = pixmap.scaled(650, 140)
        self.lb_pic = QLabel(self)
        self.lb_pic.setPixmap(self.pic)

        # top text
        self.lb_logo = QLabel(self)
        self.lb_logo.setText('Point Code 登录')
        self.lb_logo.setStyleSheet("QWidget{color:white; font-weight:600; background:transparent;font-size:30px; }")
        self.lb_logo.setFont(QFont("文泉驿等宽正黑"))
        self.lb_logo.move(150, 50)
        self.lb_logo.setAlignment(Qt.AlignCenter)
        self.lb_logo.raise_()

        # signin
        self.signin_widget = QWidget(self)
        self.signin_widget.move(0, 140)
        self.signin_widget.resize(650, 260)

        self.hbox = QHBoxLayout()
        # left logo
        self.logolb = QLabel(self)
        self.logopix = QPixmap("./icon/PointCode.png")
        self.logopix_scared = self.logopix.scaled(140, 140)
        self.logolb.setPixmap(self.logopix_scared)
        self.logolb.setAlignment(Qt.AlignCenter)
        self.hbox.addWidget(self.logolb, 1)
        # main form
        self.fmlayout = QFormLayout()
        self.lb_workerid = QLabel("用户ID")
        self.lb_workerid.setFont(QFont("文泉驿等宽正黑", 13))
        self.le_workerid = QLineEdit()
        self.le_workerid.setFixedWidth(270)
        self.le_workerid.setFixedHeight(38)
        self.le_workerid.setFont(QFont("文泉驿等宽正黑", 12))

        self.lb_psw = QLabel("密码")
        self.lb_psw.setFont(QFont("文泉驿等宽正黑", 13))
        self.le_psw = QLineEdit()
        self.le_psw.setEchoMode(QLineEdit.Password)
        self.le_psw.setFixedWidth(270)
        self.le_psw.setFixedHeight(38)
        self.le_psw.setFont(QFont("文泉驿等宽正黑", 12))
        
        self.pbtn_signin = QPushButton("登录")
        self.pbtn_signin.setFixedWidth(270)
        self.pbtn_signin.setFixedHeight(40)
        self.pbtn_signin.setFont(QFont("文泉驿等宽正黑", 13))
        self.pbtn_signin.setStyleSheet("background-color:#2c7adf; color:#fff; border:none; border-radius:12px;")
        self.pbtn_signin.clicked.connect(self.send)

        self.fmlayout.addRow(self.lb_workerid, self.le_workerid)
        self.fmlayout.addRow(self.lb_psw, self.le_psw)
        self.fmlayout.addWidget(self.pbtn_signin)
        self.hbox.setAlignment(Qt.AlignCenter)

        self.fmlayout.setHorizontalSpacing(20)
        self.fmlayout.setVerticalSpacing(12)

        self.hbox.addLayout(self.fmlayout, 2)

        self.signin_widget.setLayout(self.hbox)

    def send(self):
        id = self.le_workerid.text()
        psw = self.le_psw.text()
        if ' ' in id or ' ' in psw:
            QMessageBox.warning(self, '错误', '用户ID或密码中不得包含空格', QMessageBox.Ok)
        else:
            self.data = signin(id, psw)
            if self.data['value']:
                QMessageBox.information(self, '成功', '登录成功', QMessageBox.Ok)
                self.id = id
                self.name = self.data['value']
                self.close()
            else:
                QMessageBox.warning(self, '错误', '用户ID或密码错误！', QMessageBox.Ok)
    def closeEvent(self, event):
        window.signin()


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.id = 0
        self.name = ''
        self.setupUI()

    def setupUI(self):
        self.setStyleSheet('background-color:white')
        self.setFixedSize(650, 400)
        self.setWindowTitle("注册")
        self.setWindowIcon(QIcon('./icon/pat.png'))

        # top picture
        pixmap = QPixmap("./icon/bg.jpg")
        self.pic = pixmap.scaled(650, 140)
        self.lb_pic = QLabel(self)
        self.lb_pic.setPixmap(self.pic)

        # top text
        self.lb_logo = QLabel(self)
        self.lb_logo.setText('Point Code 注册')
        self.lb_logo.setStyleSheet("QWidget{color:white; font-weight:600; background:transparent; font-size:30px; }")
        self.lb_logo.setFont(QFont("文泉驿等宽正黑"))
        self.lb_logo.move(150, 50)
        self.lb_logo.setAlignment(Qt.AlignCenter)
        self.lb_logo.raise_()

        # signin
        self.register = QWidget(self)
        self.register.move(0, 140)
        self.register.resize(650, 260)

        self.hbox = QHBoxLayout()
        # left logo
        self.logolb = QLabel(self)
        self.logopix = QPixmap("./icon/PointCode.png")
        self.logopix_scared = self.logopix.scaled(140, 140)
        self.logolb.setPixmap(self.logopix_scared)
        self.logolb.setAlignment(Qt.AlignCenter)
        self.hbox.addWidget(self.logolb, 1)
        # main form
        self.fmlayout = QFormLayout()
        self.lb_name = QLabel("用户名")
        self.lb_name.setFont(QFont("文泉驿等宽正黑", 13))
        self.le_name = QLineEdit()
        self.le_name.setFixedWidth(270)
        self.le_name.setFixedHeight(38)
        self.le_name.setFont(QFont("文泉驿等宽正黑", 12))

        self.lb_psw = QLabel("密码")
        self.lb_psw.setFont(QFont("文泉驿等宽正黑", 13))
        self.le_psw = QLineEdit()
        self.le_psw.setFixedWidth(270)
        self.le_psw.setFixedHeight(38)
        self.le_psw.setFont(QFont("文泉驿等宽正黑", 12))

        self.pbtn_register = QPushButton("注册")
        self.pbtn_register.setFixedWidth(270)
        self.pbtn_register.setFixedHeight(40)
        self.pbtn_register.setFont(QFont("文泉驿等宽正黑", 13))
        self.pbtn_register.setStyleSheet("background-color:#2c7adf; color:#fff; border:none; border-radius:12px;")
        self.pbtn_register.clicked.connect(self.send)

        self.fmlayout.addRow(self.lb_name, self.le_name)
        self.fmlayout.addRow(self.lb_psw, self.le_psw)
        self.fmlayout.addWidget(self.pbtn_register)
        self.hbox.setAlignment(Qt.AlignCenter)

        self.fmlayout.setHorizontalSpacing(20)
        self.fmlayout.setVerticalSpacing(12)

        self.hbox.addLayout(self.fmlayout, 2)

        self.register.setLayout(self.hbox)

    def send(self):
        name = self.le_name.text()
        psw = self.le_psw.text()
        if len(psw) < 8 or len(psw) > 16:
            QMessageBox.warning(self, '错误', '密码长度必须在8-16位之间', QMessageBox.Ok)
        elif ' ' in name or ' ' in psw:
            QMessageBox.warning(self, '错误', '用户名或密码中不得包含空格', QMessageBox.Ok)
        else:
            self.data = register(name, psw)
            QMessageBox.information(self, '成功', f"注册成功，请记住用户ID：{self.data['value']}，下次登录时使用。", QMessageBox.Ok)
            self.id = self.data['value']
            self.name = name
            self.close()

    def closeEvent(self, event):
        window.register()


class MessageBox(QTextBrowser):
    def __init__(self, parent, mode, text):
        super().__init__(parent)
        self.mode = mode
        self.text = text
        self.len = len(text)
        self.setupUI()

    def setupUI(self):
        if self.mode == 'user':
            self.setStyleSheet('background-color: rgb(90, 160, 210); border:2px; border-radius:15px; padding:2px 4px;')
        elif self.mode == 'bot':
            self.setStyleSheet('background-color: rgb(255, 255, 255); border:2px; border-radius:15px; padding:2px 4px;')
        self.setFont(QFont("文泉驿等宽正黑", 12))
        self.setText(self.text)
        self.setAlignment(Qt.AlignTop)
        if self.len <= 20:
            self.w = self.len*18+30
            self.h = 35
            self.setFixedSize(self.w, self.h)
        else:
            self.w = 370
            self.h = 22*(self.len//20+1)+10
            self.setFixedSize(self.w, self.h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = SplashScreen()
    window = splash.window
    qApp.processEvents()
    sys.exit(app.exec_())