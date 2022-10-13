from PyQt5.QtWidgets import QMainWindow
from core.MySystemTrayIcon import MySystemTrayIcon
from loguru import logger
from ui.main_window import Ui_MainWindow as main_window
from win.close_dialog import close_dialog
from win.lunge_form import lunge_form
from win.plank_form import plank_form
from win.pushup_form import pushup_form
from win.squatting_form import squatting_form


class main_win(QMainWindow, main_window):
    def __init__(self):
        super(main_win, self).__init__()
        self.setupUi(self)

        # 程序托盘图标
        self.show_tray_icon = close_dialog(parent=self)
        self.tray_icon = MySystemTrayIcon()
        self.tray_icon.init(self)  # 将自己传进去

        # 按钮事件绑定
        self.pushButton_1.clicked.connect(self.jump_squatting)
        self.pushButton_2.clicked.connect(self.jump_plank)
        self.pushButton_3.clicked.connect(self.jump_pushup)
        self.pushButton_4.clicked.connect(self.jump_lunge)

    # 跳转页面
    def jump_squatting(self):
        logger.info("Select squatting")
        self.squatting_form = squatting_form()
        self.squatting_form.show()

    def jump_plank(self):
        logger.info("Select plank")
        self.plank_form = plank_form()
        self.plank_form.show()

    def jump_pushup(self):
        logger.info("Select pushup")
        self.pushup_form = pushup_form()
        self.pushup_form.show()

    def jump_lunge(self):
        logger.info("Select lunge")
        self.lunge_form = lunge_form()
        self.lunge_form.show()

    # 重写关闭的逻辑
    def closeEvent(self, event):
        logger.info("Close main window?")
        event.ignore()
        self.show_tray_icon.show()









