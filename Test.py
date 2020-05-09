import sys
from PyQt5.QtWidgets import QDialog, QApplication
from view import Ui_View

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_View()
        self.ui.setupUi(self)
        self.show()  

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
