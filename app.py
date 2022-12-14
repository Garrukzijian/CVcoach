import sys
import os
from PyQt5.QtWidgets import QApplication
from loguru import logger

from utils import global_var as gl, logs
from utils.connect_mysql import db
from win.login_form import login_form
from win.splash.splash import SplashScreen

os.chdir(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.windows = {}

    def run(self, pytest=False):
        logger.info("Start Application ...")

        splash = SplashScreen()
        splash.loadProgress()

        from win.main_win import main_win
        self.windows["main"] = main_win()
        self.windows["login"] = login_form(self.windows["main"])
        self.windows["login"].show()

        splash.finish(self.windows["main"])

        if not pytest:
            sys.exit(self.exec_())


if __name__ == "__main__":
    logs.setting()
    gl.__init()
    db.connect()
    App().run()
