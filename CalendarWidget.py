from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QColor, QPainter, QPen
from PyQt6.QtWidgets import QCalendarWidget, QApplication, QTableView

class CalendarWidget(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGridVisible(False)
        self.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.NoHorizontalHeader)
        self.setSelectedDate(QDate.currentDate())
        self.setNavigationBarVisible(False)

        self.setFocusPolicy(Qt.FocusPolicy.NoFocus) 
        view = self.findChild(QTableView)
        if view:
            view.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        for dayOff in (Qt.DayOfWeek.Saturday, Qt.DayOfWeek.Sunday):
            format = self.weekdayTextFormat(dayOff)
            format.setForeground(QColor("#CAD3F5"))
            self.setWeekdayTextFormat(dayOff, format)
        self.clicked.connect(self.copyDateToClipboard)

    def paintCell(self, painter, rect, date):
        if not date.month() == self.selectedDate().month():
            painter.save()
            painter.setPen(QPen(QColor("#939ab7")))
            painter.drawText(rect, int(Qt.AlignmentFlag.AlignCenter), str(date.day()))
            painter.restore()
        else:
            if date == self.selectedDate():
                painter.save()
                painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                painter.setPen(QPen(QColor("#24273A")))
                painter.setBrush(QColor("#B7BDF8"))
                painter.drawRoundedRect(rect.adjusted(2, 2, -2, -2), 10, 10)
                painter.drawText(rect, int(Qt.AlignmentFlag.AlignCenter), str(date.day()))
                painter.restore()
            else:
                super().paintCell(painter, rect, date)

    def copyDateToClipboard(self):
        selected_date = self.selectedDate()
        clipboard_text = selected_date.toString("dd.MM.yyyy")
        QApplication.clipboard().setText(clipboard_text)
