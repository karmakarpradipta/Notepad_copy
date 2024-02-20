import sys
from PySide6 import QtWidgets
from Notepad_ui import Ui_MainWindow
from statusbar_info import StatusBarInfo
from PySide6.QtCore import QCoreApplication

class MyStatusBar(StatusBarInfo):
    def __init__(self):
        super().__init__()

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.customStatusBarWidget = MyStatusBar()
        self.statusBar().addPermanentWidget(self.customStatusBarWidget)
        self.ui.textEdit.cursorPositionChanged.connect(self.update_cursor_position)

    def update_cursor_position(self):
        cursor = self.ui.textEdit.textCursor()
        cursor_line = cursor.blockNumber()+1
        cursor_column = cursor.columnNumber()+1
        # self.ui.statusbar.ql_cordinate.setText(QCoreApplication.translate("Form", u"Ln 1, Col 1", None))
        position_string = f"Ln {cursor_line}, Col {cursor_column}"
        self.customStatusBarWidget.ql_cordinate.setText(position_string)
        print()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
