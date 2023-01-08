from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
)

app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        #im kinda stupid so i'm gonna just keep it like that(For Now)
        self.setWindowTitle('Database viewer thingy')
        # Soo for a database app we need a verticaL with a grid layout in it
        layout = QVBoxLayout()
        
        # And then we need a grid layout in the vertical layout
        gridWidget = QWidget()
        gridLayout = QGridLayout()
        gridWidget.setLayout(gridLayout)
        # And then we need a label in the grid layout for the title
        i = 0
        while i < 10:
            j = 0
            while j < 10:
                gridLayout.addWidget(QLineEdit(f"{i}, {j}"), i, j)
                j+=1
            i+=1
        
        
        
        layout.addWidget(gridWidget)
            
        # And then we need a label in the grid

        
        layout.addWidget(QLabel("Database Viewer Thingamabober"))
        layout.addWidget(gridWidget)
        RENDER_WIDGET = QWidget()
        RENDER_WIDGET.setLayout(layout)
        self.setCentralWidget(RENDER_WIDGET)


window = MainWindow()
window.show()

app.exec()
