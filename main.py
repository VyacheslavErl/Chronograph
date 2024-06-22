import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QFontDatabase
from CalendarWidget import CalendarWidget

class CalendarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chronograph")
        self.setFixedSize(300, 200)
        
        QFontDatabase.addApplicationFont(":/fonts/JetBrainsMono-Bold.ttf")
        
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        
        self.date_label = QLabel(self)
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.calendar = CalendarWidget(self)
        self.calendar.selectionChanged.connect(self.update_date_label)
        
        layout.addWidget(self.date_label)
        layout.addWidget(self.calendar)
        
        self.setCentralWidget(central_widget)
        
        self.update_date_label()

        with open("style.qss", "r") as f:
            self.setStyleSheet(f.read())
    
    def update_date_label(self):
        selected_date = self.calendar.selectedDate()
        self.date_label.setText(selected_date.toString("yyyy MMMM"))
        
def main():
    app = QApplication(sys.argv)
    win = CalendarWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
