import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QHBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QGroupBox, QAction, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import Qt
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import random
import cv2

from histogram import histogram, histogram_match, cdf, lookup_table


##########################################
## Do not forget to delete "return NotImplementedError"
## while implementing a function
########################################

class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()

        self.title = 'Histogram Equalization'

        self.inputLoaded = False
        self.targetLoaded = False

        self.initUI()

    def initUI(self):
        # Write GUI initialization code
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')


        self.groupBox1 = QGroupBox(self)
        self.groupBox2 = QGroupBox(self)
        self.groupBox3 = QGroupBox(self)

        self.groupBox1.setTitle("Input")
        self.groupBox1.resize(500, 1000)
        self.groupBox1.move(100, 50)

        self.groupBox2.setTitle("Target")
        self.groupBox2.resize(500, 1000)
        self.groupBox2.move(700, 50)

        self.groupBox3.setTitle("Output")
        self.groupBox3.resize(500, 1000)
        self.groupBox3.move(1300, 50)

        mainLayout = QHBoxLayout(self)
        mainLayout.addStretch(1)

        mainLayout.addWidget(self.groupBox1)
        mainLayout.addWidget(self.groupBox2)
        mainLayout.addWidget(self.groupBox3)


        impAct1 = QAction('Open Input', self)
        impAct1.triggered.connect(self.openInputImage)
        impAct2 = QAction('Open Target', self)
        impAct2.triggered.connect(self.openTargetImage)
        impAct3 = QAction('Exit', self)
        impAct3.setShortcut('Ctrl+Q')
        impAct3.triggered.connect(self.quitProgram)

        fileMenu.addAction(impAct1)
        fileMenu.addAction(impAct2)
        fileMenu.addAction(impAct3)

        eqAct = QAction('Equalize Histogram', self)
        eqAct.triggered.connect(self.histogramButtonClicked)

        self.toolbar = self.addToolBar('Equalize Histogram')
        self.toolbar.addAction(eqAct)

        self.setWindowTitle('Histogram Equalization')

        self.setLayout(mainLayout)

        self.show()



    def openInputImage(self):
        # This function is called when the user clicks File->Input Image.

        # The image
        #The QLabel where we can display an Image
        self.label = QLabel(self)
        self.boxLayout = QVBoxLayout(self.groupBox1)
        self.boxLayout.addWidget(self.label)

        self.imagePath, _ = QFileDialog.getOpenFileName(self, 'OpenFile')
        self.pixmap = QPixmap(self.imagePath)
        self.label.setPixmap(self.pixmap)


        #Histogram of image
        self.histimage = cv2.imread(self.imagePath)
        self.hist1 = histogram(self.histimage)


        self.canvas0 = FigureCanvas(Figure(figsize=(5, 3)))
        self.canvas1 = FigureCanvas(Figure(figsize=(5, 3)))
        self.canvas2 = FigureCanvas(Figure(figsize=(5, 3)))

        self.boxLayout.addWidget(self.canvas0)
        self.boxLayout.addWidget(self.canvas1)
        self.boxLayout.addWidget(self.canvas2)

        self.canvas0_plot = self.canvas0.figure.subplots()
        self.canvas0_plot.axes.bar(range(0, 256), self.hist1[:, 2], color="red")
        self.canvas0.draw()

        self.canvas1_plot = self.canvas1.figure.subplots()
        self.canvas1_plot.axes.bar(range(0, 256), self.hist1[:, 1], color="green")
        self.canvas1.draw()

        self.canvas2_plot = self.canvas2.figure.subplots()
        self.canvas2_plot.axes.bar(range(0, 256), self.hist1[:, 0], color="blue")
        self.canvas2.draw()

        self.label.setAlignment(Qt.AlignCenter)

        self.inputLoaded = True


    def openTargetImage(self):
        # This function is called when the user clicks File->Target Image.

        # The QLabel where we can display an Image
        self.label2 = QLabel(self)
        self.boxLayout2 = QVBoxLayout(self.groupBox2)
        self.boxLayout2.addWidget(self.label2)


        # The image
        self.imagePath2, _ = QFileDialog.getOpenFileName(self, 'OpenFile')
        self.pixmap2 = QPixmap(self.imagePath2)
        self.label2.setPixmap(self.pixmap2)

        # Histogram of image
        self.histimage2 = cv2.imread(self.imagePath2)
        self.hist2 = histogram(self.histimage2)

        self.canvas3 = FigureCanvas(Figure(figsize=(5, 3)))
        self.canvas4 = FigureCanvas(Figure(figsize=(5, 3)))
        self.canvas5 = FigureCanvas(Figure(figsize=(5, 3)))

        self.boxLayout2.addWidget(self.canvas3)
        self.boxLayout2.addWidget(self.canvas4)
        self.boxLayout2.addWidget(self.canvas5)

        self.canvas3_plot = self.canvas3.figure.subplots()
        self.canvas3_plot.axes.bar(range(0, 256), self.hist2[:, 2], color="red")
        self.canvas3.draw()

        self.canvas4_plot = self.canvas4.figure.subplots()
        self.canvas4_plot.axes.bar(range(0, 256), self.hist2[:, 1], color="green")
        self.canvas4.draw()

        self.canvas5_plot = self.canvas5.figure.subplots()
        self.canvas5_plot.axes.bar(range(0, 256), self.hist2[:, 0], color="blue")
        self.canvas5.draw()


        self.label2.setAlignment(Qt.AlignCenter)

        self.targetLoaded = True



    def histogramButtonClicked(self):

        if not self.inputLoaded and not self.targetLoaded:
            # Error: "First load input and target images" in MessageBox
            QMessageBox.about(self, "Error", "First load input and target images")

        elif not self.inputLoaded:
            # Error: "Load input image" in MessageBox
            QMessageBox.about(self, "Error", "Load input image")

        elif not self.targetLoaded:
            # Error: "Load target image" in MessageBox
            QMessageBox.about(self, "Error", "Load target image")

        else:
            self.label3 = QLabel(self)
            self.boxLayout3 = QVBoxLayout(self.groupBox3)
            self.boxLayout3.addWidget(self.label3)

            self.label3.setAlignment(Qt.AlignCenter)

            # The image
            self.image1 = cv2.imread(self.imagePath)
            self.image2 = cv2.imread(self.imagePath2)

            self.h1 = histogram(self.image1)
            self.h2 = histogram(self.image2)

            c1_0 = cdf(self.h1[:, 0])
            c2_0 = cdf(self.h2[:, 0])

            c1_1 = cdf(self.h1[:, 1])
            c2_1 = cdf(self.h2[:, 1])

            c1_2 = cdf(self.h1[:, 2])
            c2_2 = cdf(self.h2[:, 2])

            LUT0 = lookup_table(c1_0, c2_0)
            LUT1 = lookup_table(c1_1, c2_1)
            LUT2 = lookup_table(c1_2, c2_2)

            out_im0 = histogram_match(LUT0, self.image1, 0)
            out_im1 = histogram_match(LUT1, self.image1, 1)
            out_im2 = histogram_match(LUT2, self.image1, 2)

            self.out_im = np.dstack((out_im0, out_im1, out_im2))
            self.out_im = np.divide(self.out_im, 255)


            self.output_image = self.out_im[..., ::-1]

            self.output_image = np.array(self.output_image)

            self.output_image = QImage(self.output_image.data, self.output_image.shape[1], self.output_image.shape[0], self.output_image.strides[0], QImage.Format_RGB32)

            self.pixmap3 = QPixmap.fromImage(self.output_image)
            self.pixmap3 = QPixmap(self.pixmap3)
            self.label3.setPixmap(self.pixmap3)

            self.label3.show()


    def quitProgram(self):

        return QApplication.exit(0)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
