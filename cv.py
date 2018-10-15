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
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, qApp, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):         
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
              
        impAct1 = QAction('Open Input', self)
        impAct1.triggered.connect(self.openImage) 
        impAct2 = QAction('Open Target', self)
        impAct2.triggered.connect(self.openImage) 
        impAct3 = QAction('Exit', self)
        impAct3.setShortcut('Ctrl+Q')
        impAct3.triggered.connect(qApp.quit)      
        
        fileMenu.addAction(impAct1)
        fileMenu.addAction(impAct2)
        fileMenu.addAction(impAct3)

        
        eqAct = QAction('Equalize Histogram', self)
        #eqAct.setShortcut('Ctrl+Q')
        #eqAct.triggered.connect(qApp.quit)
        
        self.toolbar = self.addToolBar('Equalize Histogram')
        self.toolbar.addAction(eqAct)
        
        lbl1 = QLabel('Input', self)
        lbl1.move(100, 50)
        
        lbl2 = QLabel('Target', self)
        lbl2.move(700, 50)
        
        lbl3 = QLabel('Result', self)
        lbl3.move(1300, 50)
                     

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Histogram Equalization')    
        self.show()
        
    def openImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(pixmap)
        self.resize(pixmap.size())
        self.adjustSize()
        
        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
