import sys
from PyQt5.QtWidgets import QDialog, QApplication
from view import Ui_View

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_View()
        self.ui.setupUi(self)
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    app.exec()
    # sys.exit(app.exec_())
