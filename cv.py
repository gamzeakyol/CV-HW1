#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 17:36:07 2018

@author: gamzeakyol
"""

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program creates a submenu.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, qApp


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):         
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        
        #impMenu1 = QMenu('Open Input', self)
        #impMenu2 = QMenu('Open Target', self)
        #impMenu3 = QMenu('Exit', self)
        
        #fileMenu.addMenu(impMenu1)
        #fileMenu.addMenu(impMenu2)
        #fileMenu.addMenu(impMenu3)
        
        
        impAct1 = QAction('Open Input', self)
        impAct2 = QAction('Open Target', self)
        impAct3 = QAction('Exit', self)

        fileMenu.addAction(impAct1)
        fileMenu.addAction(impAct2)
        fileMenu.addAction(impAct3)

        
        eqAct = QAction('Equalize Histogram', self)
        eqAct.setShortcut('Ctrl+Q')
        eqAct.triggered.connect(qApp.quit)
        
        self.toolbar = self.addToolBar('Equalize Histogram')
        self.toolbar.addAction(eqAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Histogram Equalization')    
        self.show()
        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
