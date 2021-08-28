import sys

from PyQt5.QtWidgets import *

from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtCore import *


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        # BROWSER
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        # FULL SCREEN MODE
        self.showMaximized()
        # NAVBAR
        navbar = QToolBar()
        self.addToolBar(navbar)
        # PREV BUTTON
        prevBtn = QAction('Prev', self)
        prevBtn.triggered.connect(self.browser.back)
        navbar.addAction(prevBtn)
        # NEXT BUTTON
        nextBtn = QAction('Next', self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)
        # REFRESH BUTTON
        refreshBtn = QAction('Refresh', self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)
        # HOME BUTTON
        homeBtn = QAction('Home', self)
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)
        # SEARCH
        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        navbar.addWidget(self.searchBar)

        # if url in searchBar is changed then call updateUrl method
        self.browser.urlChanged.connect(self.updateUrl)

    # navigate back to home page
    def home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    # load required url

    def loadUrl(self):
        url = self.searchBar.text()
        self.browser.setUrl(QUrl(url))
    # update url

    def updateUrl(self, url):
        self.searchBar.setText(url.toString())


MyApp = QApplication(sys.argv)

# set app name
QApplication.setApplicationName('My Web Browser')

# create window
window = Window()

# execute app
MyApp.exec_()
