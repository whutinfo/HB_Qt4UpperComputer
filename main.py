# -*- coding:utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication
import login_face



if __name__ == "__main__":
    app = QApplication(sys.argv)

    home = login_face.mainWindow()
    home.show()
    # 调用应用的exec_()方法时，应用会进入主循环，主循环会监听和分发事件。
    sys.exit(app.exec_())
