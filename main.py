from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog
)
import os
import numpy as np
#from .aigenerator import *



app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self,thedata) -> None:
        super().__init__()
        #im kinda stupid so i'm gonna just keep it like that(For Now)
        self.setWindowTitle("Database viewer")
        # Soo for a database app we need a verticaL with a grid layout in it
        layout = QVBoxLayout()
        
        # And then we need a grid layout in the vertical layout
        layout.addWidget(QLabel("Database Viewer"))
        gridWidget = QWidget()
        gridLayout = QGridLayout()
        gridWidget.setLayout(gridLayout)
        # And then we need a label in the grid layout for the title
        i = 0
        while i < thedata.shape[1]:
            j = 0
            while j < thedata.shape[0]:
                gridLayout.addWidget(QLineEdit(f"{thedata[i][j]}"), i, j)
                j+=1
            i+=1
        
        
        
        layout.addWidget(gridWidget)
            
        # And then we need a label in the grid

        
        layout.addWidget(gridWidget)
        RENDER_WIDGET = QWidget()
        RENDER_WIDGET.setLayout(layout)
        self.setCentralWidget(RENDER_WIDGET)


class MainMenu(QMainWindow):

    def openFile(self) -> None:
        fileDialog = QFileDialog()
        fileDialog.setNameFilter(("CSV (*.csv)"))
        fileDialog.setFileMode(QFileDialog.ExistingFile)
        fileDialog.setViewMode(QFileDialog.Detail)
        fileDialog.setLabelText(QFileDialog.Accept, "Open")
        fileDialog.setLabelText(QFileDialog.Reject, "Cancel")
        fileDialog.setWindowTitle("Open File")
        fileDialog.setDirectory(os.getcwd())
        if fileDialog.exec() == QFileDialog.Accepted:
            fileName = fileDialog.selectedFiles()[0]
            print(fileName)
            thedata = np.loadtxt(fileName, delimiter=",", dtype=str)
            self.setVisible(False)
            nextwin = MainWindow(thedata=thedata)
            nextwin.show()


    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Main Menu")
        mainWidget = QWidget()
        mainLayout = QVBoxLayout()
        openFileButton = QPushButton("Open A .csv file")
        openFileButton.clicked.connect(self.openFile)
        mainLayout.addWidget(openFileButton)
        
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)
        # And then we need a label in the grid layout for the title

menu = MainMenu()
menu.show()

# window = MainWindow()
# window.show()

app.exec()