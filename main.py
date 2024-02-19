import sys
from PySide6 import QtWidgets
from Notepad_ui import Ui_MainWindow
from statusbar_info import StatusBarInfo

class MyWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

class MyStatusBar(StatusBarInfo):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("border:none;")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    window = MyWindow()
    window.setupUi(mainwindow)
    customStatusBarWidget = MyStatusBar()
    mainwindow.statusBar().addPermanentWidget(customStatusBarWidget)
    mainwindow.show()
    sys.exit(app.exec_())