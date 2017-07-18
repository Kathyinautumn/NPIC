import sys

from PyQt5.QtWidgets import QApplication, QDialog

from final_login import *  # here you need to correct the names
from log import logger

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    ui = Ui_Login()
    ui.setupUi(window)
    window.show()
    logger.info("monitor running")

    sys.exit(app.exec_())
