import sys
import plank_form
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QMainWindow()
ui = plank_form.Ui_MainWindow()
ui.setupUi(widget)
# widget.resize(800, 800)
widget.setWindowTitle("plank_form, CV coach")
widget.show()
sys.exit(app.exec_())
