from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QComboBox, QStyleFactory, QTextEdit
import sqlite3
from PyQt5.QtGui import QFont, QPixmap, QCursor, QTextCharFormat
import datetime
import random
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget, QLabel, QApplication)
from PyQt5.QtCore import QDate

connection = sqlite3.connect("my_progect.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_allrecipe (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                          col_name TEXT,
                                                          col_ingredient TEXT,
                                                          col_quantity INT,
                                                          col_cook TEXT,
                                                          col_persones INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_menuess (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                       col_data TEXT,
                                                       col_time TEXT,
                                                       col_dish TEXT,
                                                       col_plates INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_advices (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                          col_advices TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_ingredientes (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                               col_ingredients TEXT,
                                                               col_calories INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_categories (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                              col_category TEXT,
                                                              col_recipes TEXT)''')

# cursor.execute('''INSERT INTO tab_advices(col_advices) VALUES ("Не запивайте пищу. Лучше выпейте стакан воды до еды!")''')
# connection.commit()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)
        self.setFixedSize(800, 800)
        self.setWindowTitle("Меню на неделю")
        # self.cursor_pix = QPixmap('Cursor.png')
        # self.current_cursor = QCursor(self.cursor_pix)
        # self.setCursor(self.current_cursor)

        self.label2 = QLabel(self)
        self.label2.setToolTip("Меню на текущую дату")
        self.label2.setGeometry(0, 24, 280, 30)
        self.label2_style = "border: 3px solid green; color:green; background-color:black"
        self.label2.setStyleSheet(self.label2_style)
        self.label2.setText("         ЗАВТРАК:")
        self.label2.setFont(QFont('Fixedsys'))

        self.textEdit1 = QTextEdit(self)
        self.textEdit1.setGeometry(0, 52, 280, 200)
        self.textEdit1_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit1.setStyleSheet(self.textEdit1_style)
        self.textEdit1.setFont(QFont('Fixedsys'))

        self.label3 = QLabel(self)
        self.label3.setToolTip("Меню на текущую дату")
        self.label3.setGeometry(0, 247, 280, 30)
        self.label3_style = "border: 3px solid green; color:green; background-color:black"
        self.label3.setStyleSheet(self.label3_style)
        self.label3.setText("           ОБЕД:")
        self.label3.setFont(QFont('Fixedsys'))

        self.textEdit2 = QTextEdit(self)
        self.textEdit2.setGeometry(0, 275, 280, 250)
        self.textEdit2_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit2.setStyleSheet(self.textEdit2_style)
        self.textEdit2.setFont(QFont('Fixedsys'))

        self.label4 = QLabel(self)
        self.label4.setToolTip("Меню на текущую дату")
        self.label4.setGeometry(0, 523, 280, 30)
        self.label4_style = "border: 3px solid green; color:green; background-color:black"
        self.label4.setStyleSheet(self.label4_style)
        self.label4.setText("           УЖИН:")
        self.label4.setFont(QFont('Fixedsys'))

        self.textEdit3 = QTextEdit(self)
        self.textEdit3.setGeometry(0, 545, 280, 255)
        self.textEdit3_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit3.setStyleSheet(self.textEdit3_style)
        self.textEdit3.setFont(QFont('Fixedsys'))

        pixmap2 = QPixmap("advice_label.jpg")
        self.lbl2 = QLabel(self)
        self.lbl2.setPixmap(pixmap2)
        self.lbl2.setGeometry(280, 10, 520, 400)

        pixmap = QPixmap("og_og_1458682072217628152.jpg")
        self.lbl = QLabel(self)
        self.lbl.setPixmap(pixmap)
        self.lbl.setGeometry(280, 325, 520, 520)

        self.textEdit4 = QTextEdit(self)
        self.textEdit4.setGeometry(350, 150, 377, 100)
        self.textEdit4_style = "border: 0px solid green; color:green; background-color:black"
        self.textEdit4.setStyleSheet(self.textEdit4_style)
        self.textEdit4.setFont(QFont('Fixedsys'))
        self.number = random.randint(1, 15)                                                                              #Набить побольше советов, посмотреть сколько их и тут выставить количество!
        cursor.execute('''SELECT col_advices FROM tab_advices WHERE id=?''', (self.number,))
        q = cursor.fetchall()
        self.advice = q[0][0]
        self.textEdit4.setPlainText(self.advice)

        self.label1 = QLabel(self)
        self.label1.setGeometry(0, 770, 280, 30)
        self.label1_style = "border: 3px solid green; color:green; background-color:black"
        self.label1.setStyleSheet(self.label1_style)
        self.current_date = str(datetime.date.today())
        self.label1.setText(f"Текущая дата: {self.current_date}")
        self.label1.setFont(QFont('Fixedsys'))

        a = self.current_date.split("-")
        b = [int(i) for i in a]
        y = [str(m) for m in b]
        self.data_formated = ", ".join(y)
        cursor.execute('''SELECT col_time, col_dish, col_plates FROM tab_menuess WHERE col_data=?''', (self.data_formated, ))
        table_all1 = cursor.fetchall()
        for i in table_all1:
            if i[0] == 'ЗАВТРАК':
                self.new_line1 = i[1] + " - " + str(i[2]) + " ПЕРСОН"
                self.textEdit1.append(self.new_line1)
            elif i[0] == 'ОБЕД':
                self.new_line2 = i[1] + " - " + str(i[2]) + " ПЕРСОН"
                self.textEdit2.append(self.new_line2)
            elif i[0] == 'УЖИН':
                self.new_line3 = i[1] + " - " + str(i[2]) + " ПЕРСОН"
                self.textEdit3.append(self.new_line3)

        menuBar = self.menuBar()
        self.file_menu = menuBar.addMenu("Меню")
        self.file_menu2 = menuBar.addMenu("Список покупок")
        self.file_menu3 = menuBar.addMenu("Мои рецепты")
        self.file_menu4 = menuBar.addMenu("Ингридиенты")
        self.file_menu5 = menuBar.addMenu("Калории")
        menuBar.setStyleSheet("""QMenuBar { border: 0px solid green; background-color: green; color: black; }""")
        menuBar.setFont(QFont('Fixedsys'))


        file_action1 = QtWidgets.QWidgetAction(self.file_menu)
        l1 = QtWidgets.QLabel("Посмотреть меню")
        l1.setStyleSheet("QLabel"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "background-color : white;"
                             "}")
        l1.setFont(QFont('Fixedsys'))
        file_action1.setDefaultWidget(l1)

        file_action2 = QtWidgets.QWidgetAction(self.file_menu)
        l2 = QtWidgets.QLabel("Составить меню")
        l2.setStyleSheet("QLabel"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "background-color : white;"
                             "}")
        l2.setFont(QFont('Fixedsys'))
        file_action2.setDefaultWidget(l2)

        file_action3 = QtWidgets.QWidgetAction(self.file_menu)
        l3 = QtWidgets.QLabel("Изменить меню")
        l3.setStyleSheet("QLabel"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "background-color : white;"
                             "}")
        l3.setFont(QFont('Fixedsys'))
        file_action3.setDefaultWidget(l3)

        file_action4 = QtWidgets.QWidgetAction(self.file_menu2)
        l4 = QtWidgets.QLabel("Создать список покупок")
        l4.setStyleSheet("QLabel"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "background-color : white;"
                             "}")
        l4.setFont(QFont('Fixedsys'))
        file_action4.setDefaultWidget(l4)

        file_action5 = QtWidgets.QWidgetAction(self.file_menu3)
        l5 = QtWidgets.QLabel("Создать новый рецепт")
        l5.setStyleSheet("QLabel"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "background-color : white;"
                             "}")
        l5.setFont(QFont('Fixedsys'))
        file_action5.setDefaultWidget(l5)

        file_action6 = QtWidgets.QWidgetAction(self.file_menu3)
        l6 = QtWidgets.QLabel("Отредактировать рецепт")
        l6.setStyleSheet("QLabel"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "background-color : white;"
                             "}")
        l6.setFont(QFont('Fixedsys'))
        file_action6.setDefaultWidget(l6)

        file_action7 = QtWidgets.QWidgetAction(self.file_menu3)
        l7 = QtWidgets.QLabel("Удалить рецепт")
        l7.setStyleSheet("QLabel"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "background-color : white;"
                             "}")
        l7.setFont(QFont('Fixedsys'))
        file_action7.setDefaultWidget(l7)

        file_action9 = QtWidgets.QWidgetAction(self.file_menu3)
        l9 = QtWidgets.QLabel("Посмотреть рецепт")
        l9.setStyleSheet("QLabel"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "background-color : white;"
                             "}")
        l9.setFont(QFont('Fixedsys'))
        file_action9.setDefaultWidget(l9)

        file_action8 = QtWidgets.QWidgetAction(self.file_menu4)
        l8 = QtWidgets.QLabel("Удалить ингридиент")
        l8.setStyleSheet("QLabel"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "background-color : white;"
                             "}")
        l8.setFont(QFont('Fixedsys'))
        file_action8.setDefaultWidget(l8)

        file_action10 = QtWidgets.QWidgetAction(self.file_menu4)
        l10 = QtWidgets.QLabel("Редактировать ингридиент")
        l10.setStyleSheet("QLabel"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "background-color : white;"
                             "}")
        l10.setFont(QFont('Fixedsys'))
        file_action10.setDefaultWidget(l10)

        file_action11 = QtWidgets.QWidgetAction(self.file_menu5)
        l11 = QtWidgets.QLabel("Калорийность меню")
        l11.setStyleSheet("QLabel"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "background-color : white;"
                             "}")
        l11.setFont(QFont('Fixedsys'))
        file_action11.setDefaultWidget(l11)

        file_action12 = QtWidgets.QWidgetAction(self.file_menu3)
        l12 = QtWidgets.QLabel("Что приготовить?")
        l12.setStyleSheet("QLabel"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "background-color : white;"
                             "}")
        l12.setFont(QFont('Fixedsys'))
        file_action12.setDefaultWidget(l12)

        self.file_menu.addAction(file_action1)
        self.file_menu.addAction(file_action2)
        self.file_menu.addAction(file_action3)
        self.file_menu2.addAction(file_action4)
        self.file_menu3.addAction(file_action9)
        self.file_menu3.addAction(file_action5)
        self.file_menu3.addAction(file_action6)
        self.file_menu3.addAction(file_action7)
        self.file_menu3.addAction(file_action12)
        self.file_menu4.addAction(file_action8)
        self.file_menu4.addAction(file_action10)
        self.file_menu5.addAction(file_action11)

        file_action1.triggered.connect(self.func_act1)
        file_action2.triggered.connect(self.func_act2)
        file_action3.triggered.connect(self.func_act3)
        file_action4.triggered.connect(self.func_act4)
        file_action5.triggered.connect(self.func_act5)
        file_action6.triggered.connect(self.func_act6)
        file_action7.triggered.connect(self.func_act7)
        file_action8.triggered.connect(self.func_act8)
        file_action9.triggered.connect(self.func_act9)
        file_action10.triggered.connect(self.func_act10)
        file_action11.triggered.connect(self.func_act11)
        file_action12.triggered.connect(self.func_act12)


    def func_act1(self):
        self.calendar2 = Calendar2()
        self.calendar2.show()

    def func_act2(self):
        self.calendar = Calendar()
        self.calendar.show()

    def func_act3(self):
        self.calendar3 = Calendar3()
        self.calendar3.show()

    def func_act4(self):
        self.calendar_for_list = CalendarForList()
        self.calendar_for_list.show()

    def func_act5(self):
        self.new_recipe = SubMenu_new_recipe()
        self.new_recipe.show()

    def func_act6(self):
        self.change_recipe = SubMenu_change_recipe()
        self.change_recipe.show()

    def func_act7(self):
        self.delete_recipe = SubMenu_delete_recipe()
        self.delete_recipe.show()

    def func_act8(self):
        self.delete_ingridient = SubMenu_delete_ingridient()
        self.delete_ingridient.show()

    def func_act9(self):
        self.look_recipe = SubMenuLookRecipe()
        self.look_recipe.show()

    def func_act10(self):
        self.change_ingridient = SubMenuChangeIngridient()
        self.change_ingridient.show()

    def func_act11(self):
        self.calendar_for_calories = CalendarForCalories()
        self.calendar_for_calories.show()

    def func_act12(self):
        self.what_to_cook = SubmenuWhatToCook()
        self.what_to_cook.show()


class SubMenu_look_menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(280, 800)
        self.setWindowTitle("Посмотреть меню")

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        cursor.execute('''SELECT col_time, col_dish, col_plates FROM tab_menuess WHERE col_data=?''', (precize_date2, ))
        table_all = cursor.fetchall()

        self.label2 = QLabel(self)
        self.label2.setGeometry(0, 0, 280, 30)
        self.label2_style = "border: 3px solid green; color:green; background-color:black"
        self.label2.setStyleSheet(self.label2_style)
        self.label2.setText("         ЗАВТРАК:")
        self.label2.setFont(QFont('Fixedsys'))

        self.textEdit1 = QTextEdit(self)
        self.textEdit1.setGeometry(0, 27, 280, 200)
        self.textEdit1_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit1.setStyleSheet(self.textEdit1_style)
        self.textEdit1.setFont(QFont('Fixedsys'))

        self.label3 = QLabel(self)
        self.label3.setGeometry(0, 225, 280, 30)
        self.label3_style = "border: 3px solid green; color:green; background-color:black"
        self.label3.setStyleSheet(self.label3_style)
        self.label3.setText("         ОБЕД:")
        self.label3.setFont(QFont('Fixedsys'))

        self.textEdit2 = QTextEdit(self)
        self.textEdit2.setGeometry(0, 253, 280, 280)
        self.textEdit2_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit2.setStyleSheet(self.textEdit2_style)
        self.textEdit2.setFont(QFont('Fixedsys'))

        self.label4 = QLabel(self)
        self.label4.setGeometry(0, 497, 280, 30)
        self.label4_style = "border: 3px solid green; color:green; background-color:black"
        self.label4.setStyleSheet(self.label4_style)
        self.label4.setText("           УЖИН:")
        self.label4.setFont(QFont('Fixedsys'))

        self.textEdit3 = QTextEdit(self)
        self.textEdit3.setGeometry(0, 520, 280, 280)
        self.textEdit3_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit3.setStyleSheet(self.textEdit3_style)
        self.textEdit3.setFont(QFont('Fixedsys'))

        for i in table_all:
            if i[0] == 'ЗАВТРАК':
                self.new_line1 = i[1] + " - " + str(i[2]) + " ПЕРСОН"
                self.textEdit1.append(self.new_line1)
            elif i[0] == 'ОБЕД':
                self.new_line2 = i[1] + " - " + str(i[2]) + " ПЕРСОН"
                self.textEdit2.append(self.new_line2)
            elif i[0] == 'УЖИН':
                self.new_line3 = i[1] + " - " + str(i[2]) + " ПЕРСОН"
                self.textEdit3.append(self.new_line3)

        self.label1 = QLabel(self)
        self.label1.setGeometry(0, 770, 280, 30)
        self.label1_style = "border: 3px solid green; color:green; background-color:black"
        self.label1.setStyleSheet(self.label1_style)
        self.current_date = str(datetime.date.today())
        self.label1.setText(f"Меню на дату: {precize_date2}")
        self.label1.setFont(QFont('Fixedsys'))

class Calendar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(False)
        self.cal.setHorizontalHeaderFormat(QCalendarWidget.NoHorizontalHeader)
        self.cal.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.cal.setStyleSheet("color:green; background-color:black;")
        self.cal.setFont(QFont('Fixedsys'))
        self.cal.move(20, 20)
        self.cal.setToolTip("На подчеркнутые даты меню составлено")
        self.cal.clicked[QDate].connect(self.showDate)
        self.setGeometry(300, 300, 290, 220)
        self.setWindowTitle('Calendar')
        cursor.execute('''SELECT col_data FROM tab_menuess''')
        filled_dates_dirty = cursor.fetchall()
        filled_dates = {1}
        for dates in filled_dates_dirty:
            filled_dates.add(dates[0])
        filled_dates.remove(1)
        for every_date in filled_dates:
            format = QTextCharFormat()
            #format.setFont(QFont('Arial', 14))
            format.setUnderlineStyle(QTextCharFormat.SingleUnderline)
            #format.setForeground(QtCore.Qt.white) делает белым
            date = QDate.fromString(every_date, "yyyy, M, d")
            self.cal.setDateTextFormat(date, format)

        self.label1 = QLabel(self)
        self.label1.setGeometry(100, 170, 120, 30)
        self.label1_style = "border: 0px solid green; color:green; background-color:black"
        self.label1.setStyleSheet(self.label1_style)
        self.label1.setText("ВЫБЕРИТЕ ДАТУ")
        self.label1.setFont(QFont('Fixedsys'))


    def showDate(self):
        cursor.execute('''SELECT col_data FROM tab_menuess''')
        filled_dates_dirty = cursor.fetchall()
        filled_dates = {1}
        for dates in filled_dates_dirty:
            filled_dates.add(dates[0])
        filled_dates.remove(1)
        self.date = self.cal.selectedDate()
        self.precize_date = str(self.date)
        global precize_date2
        if len(self.precize_date) == 31:
            precize_date2 = self.precize_date[19:30]
        elif len(self.precize_date) == 30:
            precize_date2 = self.precize_date[19:29]
        if precize_date2 in filled_dates:
            self.warning_menu =SubMenuWarning1()
            self.warning_menu.show()
            self.close()
        else:
            self.create_menu = SubMenu_create_menu()
            self.create_menu.show()
            self.close()

class SubMenuWarning1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(350, 100)
        self.setWindowTitle("Предупреждение")

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        self.label1 = QLabel(self)
        self.label1.setGeometry(13, 10, 320, 30)
        self.label1_style = "border: 0px solid green; color:green; background-color:black"
        self.label1.setStyleSheet(self.label1_style)
        self.label1.setText(f"Меню на дату {precize_date2} уже составлено.")
        self.label1.setFont(QFont('Fixedsys'))

        self.btn1 = QPushButton("ДРУГАЯ ДАТА", self)
        self.btn1.setGeometry(10, 50, 150, 30)
        self.btn1.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn1.setFont(QFont('Fixedsys'))

        self.btn2 = QPushButton("ИЗМЕНИТЬ МЕНЮ", self)
        self.btn2.setGeometry(180, 50, 150, 30)
        self.btn2.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn2.setFont(QFont('Fixedsys'))

        self.btn1.clicked.connect(self.btn1_func)
        self.btn2.clicked.connect(self.btn2_func)

    def btn1_func(self):
        self.calendar = Calendar()
        self.calendar.show()
        self.close()

    def btn2_func(self):
        self.change_menu = SubMenu_change_menu()
        self.change_menu.show()
        self.close()

class SubMenu_create_menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 800)
        self.setWindowTitle("Создать меню")

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        self.label1 = QLabel(self)
        self.label1.setGeometry(0, 0, 320, 30)
        self.label1_style = "border: 3px solid green; color:green; background-color:black"
        self.label1.setStyleSheet(self.label1_style)
        self.label1.setText("         ЗАВТРАК:")
        self.label1.setFont(QFont('Fixedsys'))

        self.textEdit1 = QTextEdit(self)
        self.textEdit1_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit1.setFont(QFont('Fixedsys'))
        self.textEdit1.setStyleSheet(self.textEdit1_style)
        self.textEdit1.setGeometry(0, 27, 320, 200)

        self.label2 = QLabel(self)
        self.label2.setGeometry(0, 222, 320, 30)
        self.label2_style = "border: 3px solid green; color:green; background-color:black"
        self.label2.setStyleSheet(self.label2_style)
        self.label2.setText("           ОБЕД:")
        self.label2.setFont(QFont('Fixedsys'))

        self.textEdit2 = QTextEdit(self)
        self.textEdit2.setGeometry(0, 250, 320, 250)
        self.textEdit2_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit2.setStyleSheet(self.textEdit2_style)
        self.textEdit2.setFont(QFont('Fixedsys'))

        self.label3 = QLabel(self)
        self.label3.setGeometry(0, 497, 320, 30)
        self.label3_style = "border: 3px solid green; color:green; background-color:black"
        self.label3.setStyleSheet(self.label3_style)
        self.label3.setText("           УЖИН:")
        self.label3.setFont(QFont('Fixedsys'))

        self.textEdit3 = QTextEdit(self)
        self.textEdit3.setGeometry(0, 520, 320, 280)
        self.textEdit3_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit3.setStyleSheet(self.textEdit3_style)
        self.textEdit3.setFont(QFont('Fixedsys'))

        self.combo1 = QComboBox(self)
        self.combo1.addItems(["Выберите блюдо"])
        self.combo1.move(350, 40)
        self.combo1.setStyleSheet("QComboBox"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;min-width: 150px;"
                             "}"
                             "QComboBox::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.combo1.setFont(QFont('Fixedsys'))
        cursor.execute('''SELECT col_name FROM tab_allrecipe ORDER BY col_name''')
        dirty_row = cursor.fetchall()
        clean_row = sorted(set(dirty_row), key=lambda d: dirty_row.index(d))
        for element in clean_row:
            self.combo1.addItems([element[0]])

        self.line1 = QLineEdit(self)
        self.line1.move(550, 40)
        self.line1_style = "border: 0px solid green; color:black; background-color:green;"
        self.line1.setStyleSheet(self.line1_style)
        self.line1.setFont(QFont('Fixedsys'))

        self.label1_1 = QLabel(self)
        self.label1_1.setGeometry(667, 38, 80, 20)
        self.label1_1_style = "border: 0px solid green; color:green; background-color:black"
        self.label1_1.setStyleSheet(self.label1_1_style)
        self.label1_1.setText("   ПЕРСОН")
        self.label1_1.setFont(QFont('Fixedsys'))

        self.btn1 = QPushButton(">>> ДОБАВИТЬ", self)
        self.btn1.setGeometry(430, 180, 250, 30)
        self.btn1.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn1.setFont(QFont('Fixedsys'))

        self.label_warning1 = QLabel(self)
        self.label_warning1.setGeometry(480, 100, 180, 20)
        self.label_warning1_style = "border: 0px solid green; color:green; background-color:black"
        self.label_warning1.setStyleSheet(self.label_warning1_style)
        self.label_warning1.setFont(QFont('Fixedsys'))

        self.label1_1_1 = QLabel(self)
        self.label1_1_1.setGeometry(320, 222, 500, 3)
        self.label1_1_1_style = "border: 0px solid green; color:green; background-color:green"
        self.label1_1_1.setStyleSheet(self.label1_1_1_style)
        self.label1_1_1.setFont(QFont('Fixedsys'))

        self.combo2 = QComboBox(self)
        self.combo2.addItems(["Выберите блюдо"])
        self.combo2.move(350, 280)
        self.combo2.setStyleSheet("QComboBox"
                                  "{"
                                  "border: 0px solid green;color:black; background-color:green;min-width: 150px;"
                                  "}"
                                  "QComboBox::hover"
                                  "{"
                                  "background-color : white;"
                                  "}")
        self.combo2.setFont(QFont('Fixedsys'))
        cursor.execute('''SELECT col_name FROM tab_allrecipe ORDER BY col_name''')
        dirty_row2 = cursor.fetchall()
        clean_row2 = sorted(set(dirty_row2), key=lambda d: dirty_row2.index(d))
        for element in clean_row2:
            self.combo2.addItems([element[0]])

        self.line2 = QLineEdit(self)
        self.line2.move(550, 280)
        self.line2_style = "border: 0px solid green; color:black; background-color:green;"
        self.line2.setStyleSheet(self.line2_style)
        self.line2.setFont(QFont('Fixedsys'))

        self.label2_2 = QLabel(self)
        self.label2_2.setGeometry(665, 274, 100, 30)
        self.label2_2_style = "border: 0px solid green; color:green; background-color:black"
        self.label2_2.setStyleSheet(self.label2_2_style)
        self.label2_2.setText("   ПЕРСОН")
        self.label2_2.setFont(QFont('Fixedsys'))

        self.label_warning2 = QLabel(self)
        self.label_warning2.setGeometry(480, 370, 180, 20)
        self.label_warning2_style = "border: 0px solid green; color:green; background-color:black"
        self.label_warning2.setStyleSheet(self.label_warning2_style)
        self.label_warning2.setFont(QFont('Fixedsys'))

        self.label2_2_2 = QLabel(self)
        self.label2_2_2.setGeometry(320, 497, 500, 3)
        self.label2_2_2_style = "border: 0px solid green; color:green; background-color:green"
        self.label2_2_2.setStyleSheet(self.label2_2_2_style)
        self.label2_2_2.setFont(QFont('Fixedsys'))

        self.btn2 = QPushButton(">>> ДОБАВИТЬ", self)
        self.btn2.setGeometry(430, 455, 250, 30)
        self.btn2.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn2.setFont(QFont('Fixedsys'))

        self.combo3 = QComboBox(self)
        self.combo3.addItems(["Выберите блюдо"])
        self.combo3.move(350, 540)
        self.combo3.setStyleSheet("QComboBox"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;min-width: 150px;"
                             "}"
                             "QComboBox::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.combo3.setFont(QFont('Fixedsys'))
        cursor.execute('''SELECT col_name FROM tab_allrecipe ORDER BY col_name''')
        dirty_row3 = cursor.fetchall()
        clean_row3 = sorted(set(dirty_row3), key=lambda d: dirty_row3.index(d))
        for element in clean_row3:
            self.combo3.addItems([element[0]])

        self.line3 = QLineEdit(self)
        self.line3.move(550, 540)
        self.line3_style = "border: 0px solid green; color:black; background-color:green;"
        self.line3.setStyleSheet(self.line3_style)
        self.line3.setFont(QFont('Fixedsys'))

        self.label3_3 = QLabel(self)
        self.label3_3.setGeometry(665, 534, 100, 30)
        self.label3_3_style = "border: 0px solid green; color:green; background-color:black"
        self.label3_3.setStyleSheet(self.label3_3_style)
        self.label3_3.setText("   ПЕРСОН")
        self.label3_3.setFont(QFont('Fixedsys'))

        self.label_warning3 = QLabel(self)
        self.label_warning3.setGeometry(480, 610, 180, 20)
        self.label_warning3_style = "border: 0px solid green; color:green; background-color:black"
        self.label_warning3.setStyleSheet(self.label_warning3_style)
        self.label_warning3.setFont(QFont('Fixedsys'))

        self.btn3 = QPushButton(">>> ДОБАВИТЬ", self)
        self.btn3.setGeometry(430, 700, 250, 30)
        self.btn3.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn3.setFont(QFont('Fixedsys'))

        self.btn4 = QPushButton("МЕНЮ НА ДАТУ >>>", self)
        self.btn4.setGeometry(350, 750, 150, 30)
        self.btn4_style = "border: 0px solid green; color:black; background-color:green"
        self.btn4.setStyleSheet(self.btn4_style)
        self.btn4.setFont(QFont('Fixedsys'))

        self.label_data_and_error = QLabel(self)
        self.label_data_and_error.setGeometry(507, 750, 100, 30)
        self.label_data_and_error_style = "border: 0px solid green; color:green; background-color:black"
        self.label_data_and_error.setStyleSheet(self.label_data_and_error_style)
        self.label_data_and_error.setText(precize_date2)
        self.label_data_and_error.setFont(QFont('Fixedsys'))

        self.btn5 = QPushButton(">>> СОХРАНИТЬ", self)
        self.btn5.setGeometry(665, 750, 120, 30)
        self.btn5.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn5.setFont(QFont('Fixedsys'))

        self.btn1.clicked.connect(self.btn1_func)
        self.btn2.clicked.connect(self.btn2_func)
        self.btn3.clicked.connect(self.btn3_func)
        self.btn5.clicked.connect(self.btn5_func)

    def btn1_func(self):
        self.dish1 = self.combo1.currentText()
        self.persones_inputed1 = self.line1.text()
        if self.persones_inputed1.isdigit():
            self.persones_inputed_ok1 = self.persones_inputed1
        else:
            self.persones_inputed_ok1 = "ОШИБКА"
        self.new_line1 = self.dish1 + " - " + self.persones_inputed_ok1 + " ПЕРСОН"
        self.textEdit1.append(self.new_line1)
        self.combo1.setCurrentIndex(0)
        self.label_warning1.setText(" ")

    def btn2_func(self):
        self.dish2 = self.combo2.currentText()
        self.persones_inputed2 = self.line2.text()
        if self.persones_inputed2.isdigit():
            self.persones_inputed_ok2 = self.persones_inputed2
        else:
            self.persones_inputed_ok2 = "ОШИБКА"
        self.new_line2 = self.dish2 + " - " + self.persones_inputed_ok2 + " ПЕРСОН"
        self.textEdit2.append(self.new_line2)
        self.combo2.setCurrentIndex(0)
        self.label_warning2.setText(" ")

    def btn3_func(self):
        self.dish3 = self.combo3.currentText()
        self.persones_inputed3 = self.line3.text()
        if self.persones_inputed3.isdigit():
            self.persones_inputed_ok3 = self.persones_inputed3
        else:
            self.persones_inputed_ok3 = "ОШИБКА"
        self.new_line3 = self.dish3 + " - " + self.persones_inputed_ok3 + " ПЕРСОН"
        self.textEdit3.append(self.new_line3)
        self.combo3.setCurrentIndex(0)
        self.label_warning3.setText(" ")

    def btn5_func(self):
        self.final_line1 = self.textEdit1.toPlainText()
        self.final_line2 = self.textEdit2.toPlainText()
        self.final_line3 = self.textEdit3.toPlainText()
        if "ОШИБКА" in self.final_line1 or "Выберите блюдо" in self.final_line1:
            self.label_warning1.setText("<<< Возникла ошибка")
        elif "ОШИБКА" in self.final_line2 or "Выберите блюдо" in self.final_line2:
            self.label_warning2.setText("<<< Возникла ошибка")
        elif "ОШИБКА" in self.final_line3 or "Выберите блюдо" in self.final_line3:
            self.label_warning3.setText("<<< Возникла ошибка")
        else:
            self.final_line1 = self.textEdit1.toPlainText()
            self.final_array_dirt = self.final_line1.split("\n")
            self.final_array1_1 = []
            for i in self.final_array_dirt:
                if i:
                    i = i.replace(" ПЕРСОН", "")
                    ind = i.split(" - ")
                    ind.insert(0, "ЗАВТРАК")
                    ind.insert(0, precize_date2)
                    self.final_array1_1.append(ind)
                else:
                    pass
            for some_ind in self.final_array1_1:
                cursor.execute('''INSERT INTO tab_menuess(col_data, col_time, col_dish, col_plates) VALUES (?, ?, ?, ?)''', (some_ind[0], some_ind[1], some_ind[2], some_ind[3]))
                connection.commit()
            self.final_line2 = self.textEdit2.toPlainText()
            self.final_array_dirt2 = self.final_line2.split("\n")
            self.final_array2_2 = []
            for u in self.final_array_dirt2:
                if u:
                    u = u.replace(" ПЕРСОН", "")
                    indu = u.split(" - ")
                    indu.insert(0, "ОБЕД")
                    indu.insert(0, precize_date2)
                    self.final_array2_2.append(indu)
                else:
                    pass
            for some_indi in self.final_array2_2:
                cursor.execute('''INSERT INTO tab_menuess(col_data, col_time, col_dish, col_plates) VALUES (?, ?, ?, ?)''', (some_indi[0], some_indi[1], some_indi[2], some_indi[3]))
                connection.commit()
            self.final_line3 = self.textEdit3.toPlainText()
            self.final_array_dirt3 = self.final_line3.split("\n")
            self.final_array3_3 = []
            for c in self.final_array_dirt3:
                if c:
                    c = c.replace(" ПЕРСОН", "")
                    indi = c.split(" - ")
                    indi.insert(0, "УЖИН")
                    indi.insert(0, precize_date2)
                    self.final_array3_3.append(indi)
                else:
                    pass
            for some_indic in self.final_array3_3:
                cursor.execute('''INSERT INTO tab_menuess(col_data, col_time, col_dish, col_plates) VALUES (?, ?, ?, ?)''', (some_indic[0], some_indic[1], some_indic[2], some_indic[3]))
                connection.commit()
            self.close()

class Calendar3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # palette = QtGui.QPalette()
        # palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        # self.setPalette(palette)
        #
        # self.cal = QCalendarWidget(self)
        # self.cal.setGridVisible(False)
        # self.cal.setStyleSheet("color:green; background-color:black;")
        # self.cal.setFont(QFont('Fixedsys'))
        # self.cal.move(20, 20)
        # self.cal.clicked[QDate].connect(self.showDate)
        # self.setGeometry(300, 300, 320, 250)
        # self.setWindowTitle('Calendar')

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(False)
        self.cal.setHorizontalHeaderFormat(QCalendarWidget.NoHorizontalHeader)
        self.cal.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.cal.setStyleSheet("color:green; background-color:black;")
        self.cal.setFont(QFont('Fixedsys'))
        self.cal.move(20, 20)
        self.cal.setToolTip("На подчеркнутые даты меню составлено")
        self.cal.clicked[QDate].connect(self.showDate)
        self.setGeometry(300, 300, 290, 220)
        self.setWindowTitle('Calendar')
        cursor.execute('''SELECT col_data FROM tab_menuess''')
        filled_dates_dirty = cursor.fetchall()
        filled_dates = {1}
        for dates in filled_dates_dirty:
            filled_dates.add(dates[0])
        filled_dates.remove(1)
        for every_date in filled_dates:
            format = QTextCharFormat()
            #format.setFont(QFont('Arial', 14))
            format.setUnderlineStyle(QTextCharFormat.SingleUnderline)
            #format.setForeground(QtCore.Qt.white) делает белым
            date = QDate.fromString(every_date, "yyyy, M, d")
            self.cal.setDateTextFormat(date, format)

        self.label1 = QLabel(self)
        self.label1.setGeometry(100, 170, 120, 20)
        self.label1_style = "border: 0px solid green; color:green; background-color:black"
        self.label1.setStyleSheet(self.label1_style)
        self.label1.setText("ВЫБЕРИТЕ ДАТУ")
        self.label1.setFont(QFont('Fixedsys'))


    def showDate(self):
        self.date = self.cal.selectedDate()
        self.precize_date = str(self.date)
        global precize_date2
        if len(self.precize_date) == 31:
            precize_date2 = self.precize_date[19:30]
        elif len(self.precize_date) == 30:
            precize_date2 = self.precize_date[19:29]
        self.change_menu = SubMenu_change_menu()
        self.change_menu.show()
        self.close()

class SubMenu_change_menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 800)
        self.setWindowTitle("Изменить меню")

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        cursor.execute('''SELECT col_time, col_dish, col_plates FROM tab_menuess WHERE col_data=?''', (precize_date2, ))
        table_all = cursor.fetchall()

        self.label1 = QLabel(self)
        self.label1.setGeometry(0, 0, 320, 30)
        self.label1_style = "border: 3px solid green; color:green; background-color:black"
        self.label1.setStyleSheet(self.label1_style)
        self.label1.setText("         ЗАВТРАК:")
        self.label1.setFont(QFont('Fixedsys'))

        self.textEdit1 = QTextEdit(self)
        self.textEdit1_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit1.setFont(QFont('Fixedsys'))
        self.textEdit1.setStyleSheet(self.textEdit1_style)
        self.textEdit1.setGeometry(0, 27, 320, 200)

        self.label2 = QLabel(self)
        self.label2.setGeometry(0, 222, 320, 30)
        self.label2_style = "border: 3px solid green; color:green; background-color:black"
        self.label2.setStyleSheet(self.label2_style)
        self.label2.setText("           ОБЕД:")
        self.label2.setFont(QFont('Fixedsys'))

        self.textEdit2 = QTextEdit(self)
        self.textEdit2.setGeometry(0, 250, 320, 250)
        self.textEdit2_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit2.setStyleSheet(self.textEdit2_style)
        self.textEdit2.setFont(QFont('Fixedsys'))

        self.label3 = QLabel(self)
        self.label3.setGeometry(0, 497, 320, 30)
        self.label3_style = "border: 3px solid green; color:green; background-color:black"
        self.label3.setStyleSheet(self.label3_style)
        self.label3.setText("           УЖИН:")
        self.label3.setFont(QFont('Fixedsys'))

        self.textEdit3 = QTextEdit(self)
        self.textEdit3.setGeometry(0, 520, 320, 280)
        self.textEdit3_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit3.setStyleSheet(self.textEdit3_style)
        self.textEdit3.setFont(QFont('Fixedsys'))

        self.combo1 = QComboBox(self)
        self.combo1.addItems(["Выберите блюдо"])
        self.combo1.move(350, 30)
        self.combo1.setStyleSheet("QComboBox"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;min-width: 150px;"
                             "}"
                             "QComboBox::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.combo1.setFont(QFont('Fixedsys'))
        cursor.execute('''SELECT col_name FROM tab_allrecipe ORDER BY col_name''')
        dirty_row = cursor.fetchall()
        clean_row = sorted(set(dirty_row), key=lambda d: dirty_row.index(d))
        for element in clean_row:
            self.combo1.addItems([element[0]])

        self.line1 = QLineEdit(self)
        self.line1.move(550, 30)
        self.line1_style = "border: 0px solid green; color:black; background-color:green;"
        self.line1.setStyleSheet(self.line1_style)
        self.line1.setFont(QFont('Fixedsys'))

        self.label1_1 = QLabel(self)
        self.label1_1.setGeometry(665, 24, 100, 30)
        self.label1_1_style = "border: 0px solid green; color:green; background-color:black"
        self.label1_1.setStyleSheet(self.label1_1_style)
        self.label1_1.setText("   ПЕРСОН")
        self.label1_1.setFont(QFont('Fixedsys'))

        self.btn1 = QPushButton("ДОБАВИТЬ", self)
        self.btn1.setGeometry(550, 80, 100, 30)
        self.btn1.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn1.setFont(QFont('Fixedsys'))

        self.combo2 = QComboBox(self)
        self.combo2.addItems(["Выберите блюдо"])
        self.combo2.move(350, 280)
        self.combo2.setStyleSheet("QComboBox"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;min-width: 150px;"
                             "}"
                             "QComboBox::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.combo2.setFont(QFont('Fixedsys'))
        cursor.execute('''SELECT col_name FROM tab_allrecipe ORDER BY col_name''')
        dirty_row2 = cursor.fetchall()
        clean_row2 = sorted(set(dirty_row2), key=lambda d: dirty_row2.index(d))
        for element in clean_row2:
            self.combo2.addItems([element[0]])

        self.line2 = QLineEdit(self)
        self.line2.move(550, 280)
        self.line2_style = "border: 0px solid green; color:black; background-color:green;"
        self.line2.setStyleSheet(self.line2_style)
        self.line2.setFont(QFont('Fixedsys'))

        self.label2_2 = QLabel(self)
        self.label2_2.setGeometry(665, 274, 100, 30)
        self.label2_2_style = "border: 0px solid green; color:green; background-color:black"
        self.label2_2.setStyleSheet(self.label2_2_style)
        self.label2_2.setText("   ПЕРСОН")
        self.label2_2.setFont(QFont('Fixedsys'))

        self.btn2 = QPushButton("ДОБАВИТЬ", self)
        self.btn2.setGeometry(550, 330, 100, 30)
        self.btn2.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn2.setFont(QFont('Fixedsys'))

        self.combo3 = QComboBox(self)
        self.combo3.addItems(["Выберите блюдо"])
        self.combo3.move(350, 590)
        self.combo3.setStyleSheet("QComboBox"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;min-width: 150px;"
                             "}"
                             "QComboBox::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.combo3.setFont(QFont('Fixedsys'))
        cursor.execute('''SELECT col_name FROM tab_allrecipe ORDER BY col_name''')
        dirty_row3 = cursor.fetchall()
        clean_row3 = sorted(set(dirty_row3), key=lambda d: dirty_row3.index(d))
        for element in clean_row3:
            self.combo3.addItems([element[0]])

        self.line3 = QLineEdit(self)
        self.line3.move(550, 590)
        self.line3_style = "border: 0px solid green; color:black; background-color:green;"
        self.line3.setStyleSheet(self.line3_style)
        self.line3.setFont(QFont('Fixedsys'))

        self.label3_3 = QLabel(self)
        self.label3_3.setGeometry(665, 584, 100, 30)
        self.label3_3_style = "border: 0px solid green; color:green; background-color:black"
        self.label3_3.setStyleSheet(self.label3_3_style)
        self.label3_3.setText("   ПЕРСОН")
        self.label3_3.setFont(QFont('Fixedsys'))

        self.btn3 = QPushButton("ДОБАВИТЬ", self)
        self.btn3.setGeometry(550, 640, 100, 30)
        self.btn3.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn3.setFont(QFont('Fixedsys'))

        self.btn4 = QPushButton("МЕНЮ НА ДАТУ", self)
        self.btn4.setGeometry(350, 750, 150, 30)
        self.btn4_style = "border: 0px solid green; color:black; background-color:green"
        self.btn4.setStyleSheet(self.btn4_style)
        self.btn4.setFont(QFont('Fixedsys'))

        self.label_data_and_error = QLabel(self)
        self.label_data_and_error.setGeometry(507, 750, 100, 30)
        self.label_data_and_error_style = "border: 0px solid green; color:green; background-color:black"
        self.label_data_and_error.setStyleSheet(self.label_data_and_error_style)
        self.label_data_and_error.setText(precize_date2)
        self.label_data_and_error.setFont(QFont('Fixedsys'))

        self.btn5 = QPushButton(">>> СОХРАНИТЬ", self)
        self.btn5.setGeometry(665, 750, 120, 30)
        self.btn5.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn5.setFont(QFont('Fixedsys'))

        self.btn1.clicked.connect(self.btn1_func)
        self.btn2.clicked.connect(self.btn2_func)
        self.btn3.clicked.connect(self.btn3_func)
        self.btn5.clicked.connect(self.btn5_func)

        for i in table_all:
            if i[0] == 'ЗАВТРАК':
                self.new_line1 = i[1] + " - " + str(i[2]) + " ПЕРСОН"
                self.textEdit1.append(self.new_line1)
            elif i[0] == 'ОБЕД':
                self.new_line2 = i[1] + " - " + str(i[2]) + " ПЕРСОН"
                self.textEdit2.append(self.new_line2)
            elif i[0] == 'УЖИН':
                self.new_line3 = i[1] + " - " + str(i[2]) + " ПЕРСОН"
                self.textEdit3.append(self.new_line3)

    def btn1_func(self):
        self.dish1 = self.combo1.currentText()
        self.persones_inputed1 = self.line1.text()
        if self.persones_inputed1.isdigit():
            self.persones_inputed_ok1 = self.persones_inputed1
        else:
            self.persones_inputed_ok1 = "ОШИБКА"
        self.new_line1 = self.dish1 + " - " + self.persones_inputed_ok1 + " ПЕРСОН"
        self.textEdit1.append(self.new_line1)
        self.combo1.setCurrentIndex(0)

    def btn2_func(self):
        self.dish2 = self.combo2.currentText()
        self.persones_inputed2 = self.line2.text()
        if self.persones_inputed2.isdigit():
            self.persones_inputed_ok2 = self.persones_inputed2
        else:
            self.persones_inputed_ok2 = "ОШИБКА"
        self.new_line2 = self.dish2 + " - " + self.persones_inputed_ok2 + " ПЕРСОН"
        self.textEdit2.append(self.new_line2)
        self.combo2.setCurrentIndex(0)

    def btn3_func(self):
        self.dish3 = self.combo3.currentText()
        self.persones_inputed3 = self.line3.text()
        if self.persones_inputed3.isdigit():
            self.persones_inputed_ok3 = self.persones_inputed3
        else:
            self.persones_inputed_ok3 = "ОШИБКА"
        self.new_line3 = self.dish3 + " - " + self.persones_inputed_ok3 + " ПЕРСОН"
        self.textEdit3.append(self.new_line3)
        self.combo3.setCurrentIndex(0)

    def btn5_func(self):
        cursor.execute('''DELETE FROM tab_menuess WHERE col_data=?''', (precize_date2,))
        connection.commit()

        self.final_line1 = self.textEdit1.toPlainText()
        self.final_array_dirt = self.final_line1.split("\n")
        self.final_array1_1 = []
        for i in self.final_array_dirt:
            if i:
                i = i.replace(" ПЕРСОН", "")
                ind = i.split(" - ")
                ind.insert(0, "ЗАВТРАК")
                ind.insert(0, precize_date2)
                self.final_array1_1.append(ind)
            else:
                pass
        for some_ind in self.final_array1_1:
            cursor.execute('''INSERT INTO tab_menuess(col_data, col_time, col_dish, col_plates) VALUES (?, ?, ?, ?)''', (some_ind[0], some_ind[1], some_ind[2], some_ind[3]))
            connection.commit()
        self.final_line2 = self.textEdit2.toPlainText()
        self.final_array_dirt2 = self.final_line2.split("\n")
        self.final_array2_2 = []
        for u in self.final_array_dirt2:
            if u:
                u = u.replace(" ПЕРСОН", "")
                indu = u.split(" - ")
                indu.insert(0, "ОБЕД")
                indu.insert(0, precize_date2)
                self.final_array2_2.append(indu)
            else:
                pass
        for some_indi in self.final_array2_2:
            cursor.execute('''INSERT INTO tab_menuess(col_data, col_time, col_dish, col_plates) VALUES (?, ?, ?, ?)''', (some_indi[0], some_indi[1], some_indi[2], some_indi[3]))
            connection.commit()
        self.final_line3 = self.textEdit3.toPlainText()
        self.final_array_dirt3 = self.final_line3.split("\n")
        self.final_array3_3 = []
        for c in self.final_array_dirt3:
            if c:
                c = c.replace(" ПЕРСОН", "")
                indi = c.split(" - ")
                indi.insert(0, "УЖИН")
                indi.insert(0, precize_date2)
                self.final_array3_3.append(indi)
            else:
                pass
        for some_indic in self.final_array3_3:
            cursor.execute('''INSERT INTO tab_menuess(col_data, col_time, col_dish, col_plates) VALUES (?, ?, ?, ?)''', (some_indic[0], some_indic[1], some_indic[2], some_indic[3]))
            connection.commit()
        self.close()


class Calendar2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # palette = QtGui.QPalette()
        # palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        # self.setPalette(palette)
        #
        # self.cal = QCalendarWidget(self)
        # self.cal.setGridVisible(False)
        # self.cal.setStyleSheet("color:green; background-color:black;")
        # self.cal.setFont(QFont('Fixedsys'))
        # self.cal.move(20, 20)
        # self.cal.clicked[QDate].connect(self.showDate)
        # self.setGeometry(300, 300, 320, 250)
        # self.setWindowTitle('Calendar')


        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(False)
        self.cal.setHorizontalHeaderFormat(QCalendarWidget.NoHorizontalHeader)
        self.cal.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.cal.setStyleSheet("color:green; background-color:black;")
        self.cal.setFont(QFont('Fixedsys'))
        self.cal.move(20, 20)
        self.cal.setToolTip("На подчеркнутые даты меню составлено")
        self.cal.clicked[QDate].connect(self.showDate)
        self.setGeometry(300, 300, 290, 220)
        self.setWindowTitle('Calendar')
        cursor.execute('''SELECT col_data FROM tab_menuess''')
        filled_dates_dirty = cursor.fetchall()
        filled_dates = {1}
        for dates in filled_dates_dirty:
            filled_dates.add(dates[0])
        filled_dates.remove(1)
        for every_date in filled_dates:
            format = QTextCharFormat()
            #format.setFont(QFont('Arial', 14))
            format.setUnderlineStyle(QTextCharFormat.SingleUnderline)
            #format.setForeground(QtCore.Qt.white) делает белым
            date = QDate.fromString(every_date, "yyyy, M, d")
            self.cal.setDateTextFormat(date, format)

        self.label1 = QLabel(self)
        self.label1.setGeometry(100, 170, 120, 20)
        self.label1_style = "border: 0px solid green; color:green; background-color:black"
        self.label1.setStyleSheet(self.label1_style)
        self.label1.setText("ВЫБЕРИТЕ ДАТУ")
        self.label1.setFont(QFont('Fixedsys'))

    def showDate(self):
        self.date = self.cal.selectedDate()
        self.precize_date = str(self.date)
        global precize_date2
        if len(self.precize_date) == 31:
            precize_date2= self.precize_date[19:30]
        elif len(self.precize_date) == 30:
            precize_date2 = self.precize_date[19:29]
        self.look_menu = SubMenu_look_menu()
        self.look_menu.show()
        self.close()

class SubMenu_achats(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 600)
        self.setWindowTitle("Список покупок")

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        self.textEdit_annotation = QTextEdit(self)
        self.textEdit_annotation.setGeometry(0, 0, 300, 550)
        self.textEdit_annotation_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit_annotation.setStyleSheet(self.textEdit_annotation_style)
        self.textEdit_annotation.setFont(QFont('Fixedsys'))
        self.dirty_allmenu = []
        for some_date in dates_list:
            cursor.execute('''SELECT col_dish, col_plates FROM tab_menuess WHERE col_data=?''', (some_date,))
            from_menu = cursor.fetchall()
            self.dirty_allmenu.extend(from_menu)
        self.dirty_achats_list = []
        for every_position in self.dirty_allmenu:
            self.dirty_achats = []
            cursor.execute('''SELECT col_ingredient, col_quantity, col_persones FROM tab_allrecipe WHERE col_name=?''', (every_position[0],))
            from_recipe = cursor.fetchall()
            for every_ingridient in from_recipe:
                self.dirty_achats.append(every_ingridient[0])
                self.number = every_ingridient[1]*every_position[1]/every_ingridient[2]
                self.dirty_achats.append(self.number)
            self.dirty_achats_list.append(self.dirty_achats)
        self.achats_list = []
        for qwerty in self.dirty_achats_list:
            temp = []
            for i in range(0, len(qwerty), 2):
                temp.append(qwerty[i])
                temp.append(qwerty[i+1])
                self.achats_list.append(temp)
                temp = []
        self.achats_list.sort(key = lambda x: x[0])
        self.achats_list_string = self.achats_list[0][0]
        start_weight = self.achats_list[0][1]
        for index in range(1, len(self.achats_list)+1):
            try:
                if self.achats_list[index][0]==self.achats_list[index-1][0]:
                    start_weight += self.achats_list[index][1]
                else:
                    self.achats_list_string += " - "
                    self.achats_list_string += str(int(start_weight))
                    self.achats_list_string += "  граммов\n"
                    self.textEdit_annotation.append(self.achats_list_string)
                    start_weight = self.achats_list[index][1]
                    self.achats_list_string = self.achats_list[index][0]
            except Exception as E:
                self.achats_list_string += " - "
                self.achats_list_string += str(int(start_weight))
                self.achats_list_string += "  граммов\n"
                self.textEdit_annotation.append(self.achats_list_string)


        self.btn_save_and_quit = QPushButton(">>> ВЫГРУЗИТЬ ТЕКСТ", self)
        #self.btn_save_and_quit.setToolTip("Файл будет создан на рабочем столе")
        self.btn_save_and_quit.setGeometry(5, 560, 290, 30)
        self.btn_save_and_quit.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn_save_and_quit.setFont(QFont('Fixedsys'))

        self.btn_save_and_quit.clicked.connect(self.btn_save_and_quit_func)


    def btn_save_and_quit_func(self):
        self.list_of_ashats = self.textEdit_annotation.toPlainText()
        f = open(str(dates_list), "w")
        f.write(self.list_of_ashats)
        f.close()
        self.close()

class SubMenu_new_recipe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(720, 600)
        self.setWindowTitle("Создать новый рецепт")

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        self.combo_ingredients = QComboBox(self)
        self.combo_ingredients.addItems(["ВЫБЕРИТЕ ИНГРИДИЕНТ"])
        cursor.execute('''SELECT col_ingredients FROM tab_ingredientes ORDER BY col_ingredients''')
        x = cursor.fetchall()
        for i in x:
            self.combo_ingredients.addItems([i[0]])
        self.combo_ingredients.move(10, 10)
        self.combo_ingredients.setStyleSheet("QComboBox"
                                  "{"
                                  "border: 0px solid green;color:black; background-color:green;min-width: 260px;"
                                  "}"
                                  "QComboBox::hover"
                                  "{"
                                  "background-color : white;"
                                  "}")
        self.combo_ingredients.setFont(QFont('Fixedsys'))

        self.line_ingredient = QLineEdit(self)
        self.line_ingredient.setToolTip("Не нашли новый ингридиент? Создайте новый!\nПотом он появится в нашей базе)")
        self.line_ingredient.move(10, 30)
        self.line_ingredient.setText("ИЛИ ВВЕДИТЕ НОВЫЙ ИНГРИДИЕНТ")
        self.line_ingredient_style = "border: 0px solid green; color:black; background-color:green; min-width: 278 px;"
        self.line_ingredient.setStyleSheet(self.line_ingredient_style)
        self.line_ingredient.setFont(QFont('Fixedsys'))

        self.line_quantity = QLineEdit(self)
        self.line_quantity.setToolTip("Количество указывайте в граммах, только число")
        self.line_quantity.move(10, 50)
        self.line_quantity.setText("ТУТ ВВЕДИТЕ ЕГО КОЛИЧЕСТВО")
        self.line_quantity_style = "border: 0px solid green; color:black; background-color:green; min-width: 278 px;"
        self.line_quantity.setStyleSheet(self.line_quantity_style)
        self.line_quantity.setFont(QFont('Fixedsys'))

        self.btn_enter_ingredient = QPushButton(">>> ВВЕСТИ ИНГРИДИЕНТ", self)
        self.btn_enter_ingredient.setGeometry(10, 85, 200, 25)
        self.btn_enter_ingredient.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn_enter_ingredient.setFont(QFont('Fixedsys'))

        self.line_recipe_name = QLineEdit(self)
        self.line_recipe_name.setToolTip("Потом это название поможет вам быстро отыскать нужное блюдо")
        self.line_recipe_name.move(310, 10)
        self.line_recipe_name.setText("ВВЕДИТЕ НАЗВАНИЕ БЛЮДА")
        self.line_recipe_name_style = "border: 0px solid green; color:black; background-color:green; min-width: 278 px;"
        self.line_recipe_name.setStyleSheet(self.line_recipe_name_style)
        self.line_recipe_name.setFont(QFont('Fixedsys'))

        self.combo_cathegory = QComboBox(self)
        self.combo_cathegory.addItems(["ВЫБЕРИТЕ КАТЕГОРИЮ"])
        cursor.execute('''SELECT col_category FROM tab_categories ORDER BY col_category''')
        x = cursor.fetchall()
        self.new_row = set(x)
        for i in self.new_row:
            self.combo_cathegory.addItems([i[0]])
        self.combo_cathegory.move(310, 30)
        self.combo_cathegory.setStyleSheet("QComboBox"
                                             "{"
                                             "border: 0px solid green;color:black; background-color:green;min-width: 260px;"
                                             "}"
                                             "QComboBox::hover"
                                             "{"
                                             "background-color : white;"
                                             "}")
        self.combo_cathegory.setFont(QFont('Fixedsys'))

        self.line_recipe_cathegory = QLineEdit(self)
        self.line_recipe_cathegory.setToolTip("Например: вегетарианское, праздничное, и т.д.")
        self.line_recipe_cathegory.move(310, 50)
        self.line_recipe_cathegory_style = "border: 0px solid green; color:black; background-color:green; min-width: 278 px;"
        self.line_recipe_cathegory.setText("ИЛИ ДОБАВЬТЕ НОВУЮ КАТЕГОРИЮ")
        self.line_recipe_cathegory.setStyleSheet(self.line_recipe_cathegory_style)
        self.line_recipe_cathegory.setFont(QFont('Fixedsys'))

        self.line_dishes = QLineEdit(self)
        self.line_dishes.setToolTip("Укажите, на сколько человек расчитано блюдо")
        self.line_dishes.move(310, 70)
        self.line_dishes_style = "border: 0px solid green; color:black; background-color:green; min-width: 278 px;"
        self.line_dishes.setText("КОЛИЧЕСТВО ПЕРСОН")
        self.line_dishes.setStyleSheet(self.line_dishes_style)
        self.line_dishes.setFont(QFont('Fixedsys'))

        self.btn_save_and_quit = QPushButton(">>> СОХРАНИТЬ И ВЫЙТИ", self)
        self.btn_save_and_quit.setGeometry(10, 520, 690, 60)
        self.btn_save_and_quit.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn_save_and_quit.setFont(QFont('Fixedsys'))

        self.textEdit_ingredients = QTextEdit(self)
        self.textEdit_ingredients.setToolTip("Тут отображаются ингридиенты для блюда\nи их количество. Если ошиблись, исправьте)")
        self.textEdit_ingredients.setGeometry(10, 120, 280, 380)
        self.textEdit_ingredients_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit_ingredients.setStyleSheet(self.textEdit_ingredients_style)
        self.textEdit_ingredients.setFont(QFont('Fixedsys'))

        self.textEdit_annotation = QTextEdit(self)
        self.textEdit_annotation.setToolTip(
            "Тут введите описание рецепта. Смешать, сварить, и т.д.")
        self.textEdit_annotation.setGeometry(310, 120, 390, 380)
        self.textEdit_annotation_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit_annotation.setStyleSheet(self.textEdit_annotation_style)
        self.textEdit_annotation.setFont(QFont('Fixedsys'))

        self.btn_enter_ingredient.clicked.connect(self.btn_enter_ingredient_func)
        self.btn_save_and_quit.clicked.connect(self.btn_save_and_quit_func)

    def btn_enter_ingredient_func(self):
        self.new_ingredient = self.line_ingredient.text()
        if self.new_ingredient == "ИЛИ ВВЕДИТЕ НОВЫЙ ИНГРИДИЕНТ" and self.combo_ingredients.currentText() == "ВЫБЕРИТЕ ИНГРИДИЕНТ":
            self.inp_ingredient = "ОШИБКА"
        elif self.new_ingredient == "ИЛИ ВВЕДИТЕ НОВЫЙ ИНГРИДИЕНТ":
            self.inp_ingredient = str(self.combo_ingredients.currentText())
        elif self.new_ingredient != "ИЛИ ВВЕДИТЕ НОВЫЙ ИНГРИДИЕНТ":
            self.inp_ingredient = self.new_ingredient
        self.quantity = self.line_quantity.text()
        if self.quantity.isdigit():
            self.quantity_ok = self.quantity
        else:
            self.quantity_ok = "ОШИБКА"
        self.final_string = self.inp_ingredient + " - " + self.quantity_ok + " гр."
        self.textEdit_ingredients.append(self.final_string)
        if self.new_ingredient != "ИЛИ ВВЕДИТЕ НОВЫЙ ИНГРИДИЕНТ":
            cursor.execute('''INSERT INTO tab_ingredientes(col_ingredients) VALUES (?)''', (self.new_ingredient,))
            connection.commit()
        else:
            pass
        self.line_ingredient.setText("ИЛИ ВВЕДИТЕ НОВЫЙ ИНГРИДИЕНТ")
        self.line_quantity.setText("ТУТ ВВЕДИТЕ ЕГО КОЛИЧЕСТВО")
        self.combo_ingredients.setCurrentIndex(0)

    def btn_save_and_quit_func(self):
        self.recipe_category = self.line_recipe_cathegory.text()
        self.recipe_name = self.line_recipe_name.text()
        self.final_recipe = self.textEdit_ingredients.toPlainText()
        self.how_to_cook = self.textEdit_annotation.toPlainText()
        self.persones_quantity = int(self.line_dishes.text())
        self.recipe_list = []
        r = self.final_recipe.split("\n")
        for z in r:
            z = z.replace(" гр.", "")
            self.recipe_list.append(z.split(" - "))
        for ingr in self.recipe_list:
            ingr[1] = int(ingr[1])
            cursor.execute(
                '''INSERT INTO tab_allrecipe (col_name, col_ingredient, col_quantity, col_cook, col_persones) VALUES (?, ?, ?, ?, ?)''',
                (self.recipe_name, ingr[0], ingr[1], self.how_to_cook, self.persones_quantity,))
            connection.commit()
        if self.recipe_category != "ВВЕДИТЕ КАТЕГОРИЮ БЛЮДА":
            cursor.execute('''INSERT INTO tab_categories (col_category, col_recipes) VALUES (?, ?)''', (self.recipe_category, self.recipe_name,))
            connection.commit()
        elif self.combo_cathegory.currentText() != "ВЫБЕРИТЕ КАТЕГОРИЮ":
            cursor.execute('''INSERT INTO tab_categories (col_category, col_recipes) VALUES (?, ?)''', (self.combo_cathegory.currentText(), self.recipe_name,))
            connection.commit()
        else:
            pass
        self.close()

class SubMenu_change_recipe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(720, 630)
        self.setWindowTitle("Отредактировать рецепт")

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        self.combo_list_of_recipes = QComboBox(self)
        self.combo_list_of_recipes.addItems(["Выберите рецепт"])
        cursor.execute('''SELECT col_name FROM tab_allrecipe ORDER BY col_name''')
        x = cursor.fetchall()
        self.temporary_array = []
        for i in x:
            self.temporary_array.append([i[0]])
        for y in range(0, len(self.temporary_array)):
            if self.temporary_array[y] == self.temporary_array[y - 1]:
                pass
            else:
                self.combo_list_of_recipes.addItems(self.temporary_array[y])
        self.combo_list_of_recipes.move(10, 20)
        self.combo_list_of_recipes.setStyleSheet("QComboBox"
                                           "{"
                                           "border: 0px solid green;color:black; background-color:green;min-width: 180px;"
                                           "}"
                                           "QComboBox::hover"
                                           "{"
                                           "background-color : white;"
                                           "}")
        self.combo_list_of_recipes.setFont(QFont('Fixedsys'))

        self.line = QLineEdit(self)
        self.line.move(10, 60)
        self.line_style = "border: 0px solid green; color:black; background-color:green; min-width: 198px;"
        self.line.setStyleSheet(self.line_style)
        self.line.setFont(QFont('Fixedsys'))

        self.line2 = QLineEdit(self)
        self.line2.move(130, 120)
        self.line2_style = "border: 0px solid green; color:black; background-color:green; min-width: 180px;"
        self.line2.setStyleSheet(self.line2_style)
        self.line2.setFont(QFont('Fixedsys'))

        self.line3 = QLineEdit(self)
        self.line3.move(440, 120)
        self.line3_style = "border: 0px solid green; color:black; background-color:green; min-width: 30px;"
        self.line3.setStyleSheet(self.line3_style)
        self.line3.setFont(QFont('Fixedsys'))

        self.label2 = QLabel(self)
        self.label2.setGeometry(10, 120, 100, 15)
        self.label2_style = "border: 0px solid green; color:green; background-color:black"
        self.label2.setStyleSheet(self.label2_style)
        self.label2.setText("КАТЕГОРИЯ ->")
        self.label2.setFont(QFont('Fixedsys'))

        self.label3 = QLabel(self)
        self.label3.setGeometry(600, 120, 80, 15)
        self.label3_style = "border: 0px solid green; color:green; background-color:black"
        self.label3.setStyleSheet(self.label3_style)
        self.label3.setText("<- ПЕРСОН")
        self.label3.setFont(QFont('Fixedsys'))

        self.btn_enter_recipe = QPushButton(">>> ВЫБРАТЬ РЕЦЕПТ И \nНАЧАТЬ РЕДАКТИРОВАНИЕ", self)
        self.btn_enter_recipe.setGeometry(300, 20, 350, 60)
        self.btn_enter_recipe.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn_enter_recipe.setFont(QFont('Fixedsys'))

        self.textEdit_ingredients = QTextEdit(self)
        self.textEdit_ingredients.setGeometry(10, 150, 280, 380)
        self.textEdit_ingredients_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit_ingredients.setStyleSheet(self.textEdit_ingredients_style)
        self.textEdit_ingredients.setFont(QFont('Fixedsys'))

        self.textEdit_annotation = QTextEdit(self)
        self.textEdit_annotation.setGeometry(310, 150, 390, 380)
        self.textEdit_annotation_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit_annotation.setStyleSheet(self.textEdit_annotation_style)
        self.textEdit_annotation.setFont(QFont('Fixedsys'))

        self.btn_change_and_quit = QPushButton(">>> СОХРАНИТЬ И ВЫЙТИ", self)
        self.btn_change_and_quit.setGeometry(10, 550, 690, 60)
        self.btn_change_and_quit.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn_change_and_quit.setFont(QFont('Fixedsys'))

        self.btn_enter_recipe.clicked.connect(self.btn_enter_recipe_func)
        self.btn_change_and_quit.clicked.connect(self.btn_change_and_quit_func)

    def btn_enter_recipe_func(self):
        self.recipe_chosen_name = str(self.combo_list_of_recipes.currentText())
        cursor.execute('''SELECT * FROM tab_allrecipe WHERE col_name=?''', (self.recipe_chosen_name, ))
        recipe = cursor.fetchall()
        self.recipe_string = ''
        for i in recipe:
            self.line.setText(i[1])
            self.recipe_string += (i[2])
            self.recipe_string += " - "
            self.recipe_string += str(i[3])
            self.recipe_string += " гр.\n"
            self.textEdit_ingredients.setText(self.recipe_string)
            self.textEdit_annotation.setPlainText(i[4])
            self.line3.setText(str(i[5]))
        cursor.execute('''SELECT col_category FROM tab_categories WHERE col_recipes=?''', (self.recipe_chosen_name, ))
        cathegory = cursor.fetchall()
        try:
            self.line2.setText(cathegory[0][0])
        except Exception as e:
            pass

    def btn_change_and_quit_func(self):
        cursor.execute('''DELETE FROM tab_allrecipe WHERE col_name=?''', (self.recipe_chosen_name,))
        connection.commit()
        self.recipe_name = self.line.text()
        self.final_recipe = self.textEdit_ingredients.toPlainText()
        self.how_to_cook = self.textEdit_annotation.toPlainText()
        self.recipe_list_dirty = self.final_recipe.split()
        self.kategory_name = self.line2.text()
        self.quantity_of_persones = self.line4.text()
        self.recipe_list = []
        r = self.final_recipe.split("\n")
        for z in r:
            if z:
                z = z.replace(" гр.", "")
                self.recipe_list.append(z.split(" - "))
        for ingr in self.recipe_list:
            ingr[1] = int(ingr[1])
            cursor.execute(
                '''INSERT INTO tab_allrecipe (col_name, col_ingredient, col_quantity, col_cook, col_persones) VALUES (?, ?, ?, ?, ?)''',
                (self.recipe_name, ingr[0], ingr[1], self.how_to_cook, self.quantity_of_persones,))
            connection.commit()

        cursor.execute('''DELETE FROM tab_categories WHERE col_recipes=?''', (self.recipe_chosen_name,))
        connection.commit()
        if self.kategory_name:
            cursor.execute('''INSERT INTO tab_categories (col_category, col_recipes) VALUES (?, ?)''', (self.kategory_name, self.recipe_name,))
            connection.commit()
        else:
            pass
        self.close()

class SubMenu_delete_recipe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(600, 400)
        self.setWindowTitle("Удалить рецепт")

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.darkGreen)
        self.setPalette(palette)

        self.combo_list_of_recipes = QComboBox(self)
        self.combo_list_of_recipes.addItems(["Выберите рецепт"])
        cursor.execute('''SELECT col_name FROM tab_allrecipe ORDER BY col_name''')
        x = cursor.fetchall()
        self.temporary_array = []
        for i in x:
            self.temporary_array.append([i[0]])
        for y in range(len(self.temporary_array)):
            if self.temporary_array[y] == self.temporary_array[y-1]:
                pass
            else:
                self.combo_list_of_recipes.addItems(self.temporary_array[y])
        self.combo_list_of_recipes.move(10, 10)
        self.combo_list_of_recipes.setStyleSheet("QComboBox"
                                                 "{"
                                                 "border: 0px solid green;color:green; background-color:black;min-width: 180px;"
                                                 "}"
                                                 "QComboBox::hover"
                                                 "{"
                                                 "color:black;background-color : white;"
                                                 "}")
        self.combo_list_of_recipes.setFont(QFont('Fixedsys'))

        self.textEdit_ingridients = QTextEdit(self)
        self.textEdit_ingridients.setGeometry(10, 50, 280, 340)
        self.textEdit_ingridients_style = "border: 0px solid green; color:green; background-color:black"
        self.textEdit_ingridients.setStyleSheet(self.textEdit_ingridients_style)
        self.textEdit_ingridients.setFont(QFont('Fixedsys'))

        self.textEdit_annotation = QTextEdit(self)
        self.textEdit_annotation.setGeometry(300, 50, 290, 340)
        self.textEdit_annotation_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit_annotation.setStyleSheet(self.textEdit_annotation_style)
        self.textEdit_annotation.setFont(QFont('Fixedsys'))

        self.btn_load = QPushButton("ВЫБРАТЬ\nРЕЦЕПТ", self)
        self.btn_load.setGeometry(250, 10, 140, 35)
        self.btn_load.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:green; background-color:black;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "color:black; background-color : white;"
                             "}")
        self.btn_load.setFont(QFont('Fixedsys'))

        self.btn_delete = QPushButton("УДАЛИТЬ\nИ ВЫЙТИ", self)
        self.btn_delete.setGeometry(420, 10, 140, 35)
        self.btn_delete.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:green; background-color:black;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "color:black; background-color : white;"
                             "}")
        self.btn_delete.setFont(QFont('Fixedsys'))

        self.btn_load.clicked.connect(self.btn_load_func)
        self.btn_delete.clicked.connect(self.btn_delete_func)

    def btn_load_func(self):
        self.recipe_chosen_name = str(self.combo_list_of_recipes.currentText())
        cursor.execute('''SELECT * FROM tab_allrecipe WHERE col_name=?''', (self.recipe_chosen_name,))
        recipe = cursor.fetchall()
        self.recipe_string = ''
        for i in recipe:
            self.recipe_string += (i[2])
            self.recipe_string += " - "
            self.recipe_string += str(i[3])
            self.recipe_string += " гр.\n"
            self.textEdit_ingridients.setText(self.recipe_string)
            self.textEdit_annotation.setText(i[4])

    def btn_delete_func(self):
        try:
            cursor.execute('''DELETE FROM tab_allrecipe WHERE col_name=?''', (self.recipe_chosen_name,))
            connection.commit()
            cursor.execute('''DELETE FROM tab_categories WHERE col_recipes=?''', (self.recipe_chosen_name,))
            connection.commit()
            self.close()
        except Exception as e:
            pass


class SubMenu_delete_ingridient(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(370, 47)
        self.setWindowTitle("Удалить ингридиент")

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        self.combo_ingredients = QComboBox(self)
        self.combo_ingredients.addItems(["Выберите ингридиент"])
        cursor.execute('''SELECT col_ingredients FROM tab_ingredientes ORDER BY col_ingredients''')
        x = cursor.fetchall()
        for i in x:
            self.combo_ingredients.addItems([i[0]])
        self.combo_ingredients.move(10, 10)
        self.combo_ingredients.setStyleSheet("QComboBox"
                                           "{"
                                           "border: 0px solid green;color:black; background-color:green;min-width: 160px;"
                                           "}"
                                           "QComboBox::hover"
                                           "{"
                                           "background-color : white;"
                                           "}")
        self.combo_ingredients.setToolTip("При удалении ингридиент останется\nв уже созданных с ним рецептах.")
        self.combo_ingredients.setFont(QFont('Fixedsys'))

        self.btn_delete = QPushButton(">>> УДАЛИТЬ И ВЫЙТИ", self)
        self.btn_delete.setGeometry(200, 10, 160, 20)
        self.btn_delete.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn_delete.setFont(QFont('Fixedsys'))
        self.btn_delete.clicked.connect(self.btn_delete_func)

    def btn_delete_func(self):
        self.ingridient_chosen_name = str(self.combo_ingredients.currentText())
        cursor.execute('''DELETE FROM tab_ingredientes WHERE col_ingredients=?''', (self.ingridient_chosen_name,))
        connection.commit()
        self.close()

class SubMenuLookRecipe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(698, 450)
        self.setWindowTitle("Посмотреть рецепт")

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        self.textEdit_ingridients = QTextEdit(self)
        self.textEdit_ingridients.setGeometry(0, 0, 300, 300)
        self.textEdit_ingridients_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit_ingridients.setStyleSheet(self.textEdit_ingridients_style)
        self.textEdit_ingridients.setFont(QFont('Fixedsys'))

        self.textEdit_annotation = QTextEdit(self)
        self.textEdit_annotation.setGeometry(298, 0, 400, 300)
        self.textEdit_annotation_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit_annotation.setStyleSheet(self.textEdit_annotation_style)
        self.textEdit_annotation.setFont(QFont('Fixedsys'))

        self.calories_and_persones_label = QLabel(self)
        self.calories_and_persones_label.setGeometry(10, 315, 500, 20)
        self.calories_and_persones_label.setStyleSheet("border: 0px solid green; color:green; background-color:black")
        self.calories_and_persones_label.setFont(QFont('Fixedsys'))


        self.btn_load_filter = QPushButton(">>> ПРИМЕНИТЬ ФИЛЬТР", self)
        self.btn_load_filter.setGeometry(50, 400, 200, 35)
        self.btn_load_filter.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn_load_filter.setFont(QFont('Fixedsys'))
        self.btn_load_filter.clicked.connect(self.btn_load_filter_func)

        self.btn_look_recipe = QPushButton(">>> ПОСМОТРЕТЬ РЕЦЕПТ", self)
        self.btn_look_recipe.setGeometry(400, 400, 200, 35)
        self.btn_look_recipe.setStyleSheet("QPushButton"
                             "{"
                             "border: 0px solid green;color:black; background-color:green;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "}")
        self.btn_look_recipe.setFont(QFont('Fixedsys'))
        self.btn_look_recipe.clicked.connect(self.btn_look_recipe_func)

        self.combo_categories = QComboBox(self)
        self.combo_categories.addItems(["Все категории"])
        cursor.execute('''SELECT col_category FROM tab_categories''')
        x = cursor.fetchall()
        categories = []
        for v in x:
            categories.append(v[0])
        final_categories = set(categories)
        final_categories_list = sorted(list(final_categories))
        for b in final_categories_list:
            self.combo_categories.addItems([b])
        self.combo_categories.move(50, 350)
        self.combo_categories.setStyleSheet("QComboBox"
                                           "{"
                                           "border: 0px solid green;color:black; background-color:green;min-width: 185px;"
                                           "}"
                                           "QComboBox::hover"
                                           "{"
                                           "background-color : white;"
                                           "}")
        self.combo_categories.setFont(QFont('Fixedsys'))

        self.combo_recipes = QComboBox(self)
        self.combo_recipes.addItems(["Выберите рецепт"])
        cursor.execute('''SELECT col_name FROM tab_allrecipe''')
        recepty = cursor.fetchall()
        vse_recepty = []
        for i in recepty:
            vse_recepty.append(i[0])
        vse_recepty_clean = set(vse_recepty)
        vse_recepty_list = sorted(list(vse_recepty_clean))
        for each_recipe in vse_recepty_list:
            self.combo_recipes.addItems([each_recipe])
        self.combo_recipes.move(400, 350)
        self.combo_recipes_style = "border: 0px solid green; color:black; background-color:green; min-width: 185px;"
        self.combo_recipes.setStyleSheet(self.combo_recipes_style)
        self.combo_recipes.setFont(QFont('Fixedsys'))

    def btn_load_filter_func(self):
        if self.combo_categories.currentText() != "Все категории":
            self.combo_recipes.clear()
            self.combo_recipes.addItems(["Выберите рецепт"])
            chosen_category = self.combo_categories.currentText()
            cursor.execute('''SELECT col_recipes FROM tab_categories WHERE col_category=?''', (chosen_category, ))
            necessary_recipes = cursor.fetchall()
            for each_necessary_recipe in necessary_recipes:
                self.combo_recipes.addItems([each_necessary_recipe[0]])
        else:
            self.combo_recipes.clear()
            self.combo_recipes.addItems(["Выберите рецепт"])
            cursor.execute('''SELECT col_name FROM tab_allrecipe''')
            recepty = cursor.fetchall()
            vse_recepty = []
            for i in recepty:
                vse_recepty.append(i[0])
            vse_recepty_clean = set(vse_recepty)
            vse_recepty_list = sorted(list(vse_recepty_clean))
            for each_recipe in vse_recepty_list:
                self.combo_recipes.addItems([each_recipe])

    def btn_look_recipe_func(self):
        try:
            self.textEdit_ingridients.clear()
            self.textEdit_annotation.clear()
            chosen_recipe = self.combo_recipes.currentText()
            cursor.execute('''SELECT col_ingredient, col_quantity, col_cook, col_persones FROM tab_allrecipe WHERE col_name=?''', (chosen_recipe, ))
            recept = cursor.fetchall()
            string_to_wiew = ""
            calories = 0
            for component in recept:
                string_to_wiew += component[0]
                string_to_wiew += " - "
                string_to_wiew += str(component[1])
                string_to_wiew += " грамм"
                string_to_wiew += "\n"
                cursor.execute('''SELECT col_calories FROM tab_ingredientes WHERE col_ingredients=?''', (component[0], ))
                every_calory = cursor.fetchall()
                try:
                    calories =+ every_calory[0][0]
                except Exception as E:
                    calories = "???"
            self.textEdit_ingridients.append(string_to_wiew)
            self.textEdit_annotation.setPlainText(component[2])
            self.calories_and_persones_label.setText(f"Блюдо расчитано на {recept[0][3]} персон. В одной порции - {calories} калорий.")
        except Exception as E:
            pass

class CalendarForList(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(False)
        self.cal.setHorizontalHeaderFormat(QCalendarWidget.NoHorizontalHeader)
        self.cal.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.cal.setStyleSheet("color:green; background-color:black;")
        self.cal.setFont(QFont('Fixedsys'))
        self.cal.move(20, 20)
        self.cal.setToolTip("На подчеркнутые даты меню составлено")
        self.cal.clicked[QDate].connect(self.showDate)
        self.setGeometry(300, 300, 290, 570)
        self.setWindowTitle('Calendar')
        cursor.execute('''SELECT col_data FROM tab_menuess''')
        filled_dates_dirty = cursor.fetchall()
        self.filled_dates = {1}
        for dates in filled_dates_dirty:
            self.filled_dates.add(dates[0])
        self.filled_dates.remove(1)
        for every_date in self.filled_dates:
            format = QTextCharFormat()
            #format.setFont(QFont('Arial', 14))
            format.setUnderlineStyle(QTextCharFormat.SingleUnderline)
            #format.setForeground(QtCore.Qt.white) делает белым
            date = QDate.fromString(every_date, "yyyy, M, d")
            self.cal.setDateTextFormat(date, format)

        self.textEdit_dates = QTextEdit(self)
        self.textEdit_dates.setGeometry(20, 200, 250, 300)
        self.textEdit_dates_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit_dates.setStyleSheet(self.textEdit_dates_style)
        self.textEdit_dates.setFont(QFont('Fixedsys'))

        self.btn_save_and_quit = QPushButton(">>> ВЫГРУЗИТЬ СПИСОК ПОКУПОК", self)
        self.btn_save_and_quit.setGeometry(20, 520, 250, 35)
        self.btn_save_and_quit.setStyleSheet("QPushButton"
                                       "{"
                                       "border: 0px solid green;color:black; background-color:green;"
                                       "}"
                                       "QPushButton::hover"
                                       "{"
                                       "background-color : white;"
                                       "}")
        self.btn_save_and_quit.setFont(QFont('Fixedsys'))
        self.btn_save_and_quit.clicked.connect(self.btn_save_and_quit_func)

    def showDate(self):
        self.date = self.cal.selectedDate()
        self.precize_date = str(self.date)
        if len(self.precize_date) == 31:
            self.precize_date_oneofselected = self.precize_date[19:30]
        elif len(self.precize_date) == 30:
            self.precize_date_oneofselected = self.precize_date[19:29]
        self.textEdit_dates.append(self.precize_date_oneofselected)

    def btn_save_and_quit_func(self):
        self.dates_string = self.textEdit_dates.toPlainText()
        global dates_list
        dates_list = self.dates_string.split("\n")
        c = list(set(dates_list) & self.filled_dates)
        if c:
            self.achats = SubMenu_achats()
            self.achats.show()
            self.close()
        else:
            self.aware = SubMenu_aware()
            self.aware.show()

class SubMenu_aware(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(200, 100)
        self.setWindowTitle("Ничего не получилось(")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        self.label = QLabel(self)
        self.label.setGeometry(15, 0, 200, 100)
        self.label_style = "border: 0px solid green; color:green; background-color:black"
        self.label.setStyleSheet(self.label_style)
        self.label.setText("На выбранную вами\nдату не создано меню!")
        self.label.setFont(QFont('Fixedsys'))

class SubMenuChangeIngridient(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 120)
        self.setWindowTitle("Редактировать ингридиент")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        self.label = QLabel(self)
        self.label.setGeometry(200, 7, 180, 30)
        self.label_style = "border: 0px solid green; color:green; background-color:black"
        self.label.setStyleSheet(self.label_style)
        self.label.setText("НАЗВАНИЕ ИНГРИДИЕНТА:")
        self.label.setFont(QFont('Fixedsys'))

        self.label2 = QLabel(self)
        self.label2.setGeometry(200, 55, 180, 30)
        self.label2_style = "border: 0px solid green; color:green; background-color:black"
        self.label2.setStyleSheet(self.label2_style)
        self.label2.setText("КАЛОРИЙ В 100 ГР.:")
        self.label2.setFont(QFont('Fixedsys'))

        self.combo_ingredients = QComboBox(self)
        self.combo_ingredients.addItems(["Выберите ингридиент"])
        cursor.execute('''SELECT col_ingredients FROM tab_ingredientes ORDER BY col_ingredients''')
        x = cursor.fetchall()
        for i in x:
            self.combo_ingredients.addItems([i[0]])
        self.combo_ingredients.move(10, 15)
        self.combo_ingredients.setStyleSheet("QComboBox"
                                           "{"
                                           "border: 0px solid green;color:black; background-color:green;min-width: 160px;"
                                           "}"
                                           "QComboBox::hover"
                                           "{"
                                           "background-color : white;"
                                           "}")
        self.combo_ingredients.setToolTip("При удалении ингридиент останется\nв уже созданных с ним рецептах.")
        self.combo_ingredients.setFont(QFont('Fixedsys'))
        self.combo_ingredients.activated[str].connect(self.combo_func)

        self.btn_save_and_quit = QPushButton(">>> СОХРАНИТЬ И ВЫЙТИ", self)
        self.btn_save_and_quit.setGeometry(10, 55, 175, 45)
        self.btn_save_and_quit.setStyleSheet("QPushButton"
                                       "{"
                                       "border: 0px solid green;color:black; background-color:green;"
                                       "}"
                                       "QPushButton::hover"
                                       "{"
                                       "background-color : white;"
                                       "}")
        self.btn_save_and_quit.setFont(QFont('Fixedsys'))
        self.btn_save_and_quit.clicked.connect(self.btn_save_and_quit_func)

        self.line = QLineEdit(self)
        self.line.move(200, 30)
        self.line_style = "border: 0px solid green; color:black; background-color:green; min-width: 180px;"
        self.line.setStyleSheet(self.line_style)
        self.line.setFont(QFont('Fixedsys'))

        self.line2 = QLineEdit(self)
        self.line2.move(200, 80)
        self.line2_style = "border: 0px solid green; color:black; background-color:green; min-width: 180px;"
        self.line2.setStyleSheet(self.line2_style)
        self.line2.setFont(QFont('Fixedsys'))

    def combo_func(self):
        self.chosen_ingridient = self.combo_ingredients.currentText()
        self.line.setText(self.chosen_ingridient)
        cursor.execute('''SELECT col_calories FROM tab_ingredientes WHERE col_ingredients=?''', (self.chosen_ingridient, ))
        all_about_ingridient = cursor.fetchall()
        try:
            self.line2.setText(str(all_about_ingridient[0][0]))
        except Exception as E:
            pass

    def btn_save_and_quit_func(self):
        self.chosen_ingridient = self.combo_ingredients.currentText()
        self.new_calories = self.line2.text()
        self.new_ingridient_name = self.line.text()
        cursor.execute('''DELETE FROM tab_ingredientes WHERE col_ingredients=?''',
                       (self.chosen_ingridient,))
        connection.commit()
        cursor.execute('''INSERT INTO tab_ingredientes(col_ingredients, col_calories) VALUES (?, ?)''', (self.new_ingridient_name, self.new_calories, ))
        connection.commit()
        self.close()

class CalendarForCalories(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(False)
        self.cal.setHorizontalHeaderFormat(QCalendarWidget.NoHorizontalHeader)
        self.cal.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.cal.setStyleSheet("color:green; background-color:black;")
        self.cal.setFont(QFont('Fixedsys'))
        self.cal.move(20, 20)
        self.cal.setToolTip("На подчеркнутые даты меню составлено")
        self.cal.clicked[QDate].connect(self.showDate)
        self.setGeometry(300, 300, 290, 300)
        self.setWindowTitle('Calendar')
        cursor.execute('''SELECT col_data FROM tab_menuess''')
        filled_dates_dirty = cursor.fetchall()
        self.filled_dates = {1}
        for dates in filled_dates_dirty:
            self.filled_dates.add(dates[0])
        self.filled_dates.remove(1)
        for every_date in self.filled_dates:
            format = QTextCharFormat()
            format.setUnderlineStyle(QTextCharFormat.SingleUnderline)
            date = QDate.fromString(every_date, "yyyy, M, d")
            self.cal.setDateTextFormat(date, format)

    def showDate(self):
        self.date = self.cal.selectedDate()
        self.precize_date = str(self.date)
        global precize_date_oneofselected
        if len(self.precize_date) == 31:
            precize_date_oneofselected = self.precize_date[19:30]
        elif len(self.precize_date) == 30:
            precize_date_oneofselected = self.precize_date[19:29]
        if precize_date_oneofselected in self.filled_dates:
            self.calories_from_menu = SubMenuCaloriesFromMenu()
            self.calories_from_menu.show()
            self.close()
        else:
            self.beware = SubMenu_beware()
            self.beware.show()

class SubMenuCaloriesFromMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(280, 800)
        self.setWindowTitle("Посмотреть меню")

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        cursor.execute('''SELECT col_time, col_dish, col_plates FROM tab_menuess WHERE col_data=?''', (precize_date_oneofselected, ))
        table_all = cursor.fetchall()

        self.label2 = QLabel(self)
        self.label2.setGeometry(0, 0, 280, 30)
        self.label2_style = "border: 3px solid green; color:green; background-color:black"
        self.label2.setStyleSheet(self.label2_style)
        self.label2.setText("ЗАВТРАК:")
        self.label2.setFont(QFont('Fixedsys'))

        self.textEdit1 = QTextEdit(self)
        self.textEdit1.setGeometry(0, 27, 280, 200)
        self.textEdit1_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit1.setStyleSheet(self.textEdit1_style)
        self.textEdit1.setFont(QFont('Fixedsys'))

        self.label3 = QLabel(self)
        self.label3.setGeometry(0, 225, 280, 30)
        self.label3_style = "border: 3px solid green; color:green; background-color:black"
        self.label3.setStyleSheet(self.label3_style)
        self.label3.setText("ОБЕД:")
        self.label3.setFont(QFont('Fixedsys'))

        self.textEdit2 = QTextEdit(self)
        self.textEdit2.setGeometry(0, 253, 280, 280)
        self.textEdit2_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit2.setStyleSheet(self.textEdit2_style)
        self.textEdit2.setFont(QFont('Fixedsys'))

        self.label4 = QLabel(self)
        self.label4.setGeometry(0, 497, 280, 30)
        self.label4_style = "border: 3px solid green; color:green; background-color:black"
        self.label4.setStyleSheet(self.label4_style)
        self.label4.setText("УЖИН:")
        self.label4.setFont(QFont('Fixedsys'))

        self.textEdit3 = QTextEdit(self)
        self.textEdit3.setGeometry(0, 520, 280, 280)
        self.textEdit3_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit3.setStyleSheet(self.textEdit3_style)
        self.textEdit3.setFont(QFont('Fixedsys'))

        self.petit_dejener_calories = 0
        self.dejener_calories = 0
        self.diner_calories = 0
        for i in table_all:
            if i[0] == 'ЗАВТРАК':
                cursor.execute('''SELECT col_ingredient, col_quantity, col_persones FROM tab_allrecipe WHERE col_name=?''',
                               (i[1],))
                all_from_recipe = cursor.fetchall()
                self.calories = 0
                for each_ingridient in all_from_recipe:
                    exact_quantity = each_ingridient[1]/each_ingridient[2]
                    cursor.execute(
                        '''SELECT col_calories FROM tab_ingredientes WHERE col_ingredients=?''',
                        (each_ingridient[0],))
                    calorage = cursor.fetchall()
                    try:
                        exact_calories = exact_quantity * calorage[0][0]/100
                        self.calories += exact_calories
                        self.petit_dejener_calories += exact_calories
                    except Exception as E:
                        self.calories = "???"
                        #self.petit_dejener_calories = "???"
                self.new_line1 = i[1] + " - " + str(self.calories) + " КАЛОРИЙ"
                self.textEdit1.append(self.new_line1)
            elif i[0] == 'ОБЕД':
                cursor.execute('''SELECT col_ingredient, col_quantity, col_persones FROM tab_allrecipe WHERE col_name=?''',
                               (i[1],))
                all_from_recipe2 = cursor.fetchall()
                self.calories2 = 0
                for each_ingridient2 in all_from_recipe2:
                    exact_quantity2 = each_ingridient2[1]/each_ingridient2[2]
                    cursor.execute(
                        '''SELECT col_calories FROM tab_ingredientes WHERE col_ingredients=?''',
                        (each_ingridient2[0],))
                    calorage2 = cursor.fetchall()
                    try:
                        exact_calories2 = exact_quantity2 * calorage2[0][0]/100
                        self.calories2 += exact_calories2
                        self.dejener_calories += exact_calories2
                    except Exception as E:
                        self.calories2 = "???"
                        #self.dejener_calories = "???"
                self.new_line2 = i[1] + " - " + str(self.calories2) + " КАЛОРИЙ"
                self.textEdit2.append(self.new_line2)
            elif i[0] == 'УЖИН':
                cursor.execute('''SELECT col_ingredient, col_quantity, col_persones FROM tab_allrecipe WHERE col_name=?''',
                               (i[1],))
                all_from_recipe3 = cursor.fetchall()
                self.calories3 = 0
                for each_ingridient3 in all_from_recipe3:
                    exact_quantity3 = each_ingridient3[1] / each_ingridient3[2]
                    cursor.execute(
                        '''SELECT col_calories FROM tab_ingredientes WHERE col_ingredients=?''',
                        (each_ingridient3[0],))
                    calorage3 = cursor.fetchall()
                    try:
                        exact_calories3 = exact_quantity3 * calorage3[0][0] / 100
                        self.calories3 += exact_calories3
                        self.diner_calories += exact_calories3
                    except Exception as E:
                        self.calories3 = "???"
                        #self.diner_calories = "???"
                self.new_line3 = i[1] + " - " + str(self.calories3) + " КАЛОРИЙ"
                self.textEdit3.append(self.new_line3)
        # if type(self.petit_dejener_calories) is int:
        #     self.petit_dejener_calories = round(self.petit_dejener_calories)
        # else:
        #     pass
        # if type(self.dejener_calories) is int:
        #     self.dejener_calories = round(self.dejener_calories)
        # else:
        #     pass
        # if type(self.diner_calories) is int:
        #     self.diner_calories = round(self.diner_calories)
        # else:
        #     pass
        self.label2.setText(f"ЗАВТРАК: {round(self.petit_dejener_calories)} КАЛОРИЙ")
        self.label3.setText(f"ОБЕД: {round(self.dejener_calories)} КАЛОРИЙ")
        self.label4.setText(f"УЖИН: {round(self.diner_calories)} КАЛОРИЙ")

        self.label1 = QLabel(self)
        self.label1.setGeometry(0, 770, 280, 30)
        self.label1_style = "border: 3px solid green; color:green; background-color:black"
        self.label1.setStyleSheet(self.label1_style)
        self.current_date = str(datetime.date.today())
        self.label1.setText(f"Меню на дату: {precize_date_oneofselected}")
        self.label1.setFont(QFont('Fixedsys'))

class SubMenu_beware(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(240, 120)
        self.setWindowTitle("Внимание")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        self.label = QLabel(self)
        self.label.setGeometry(10, 7, 222, 30)
        self.label_style = "border: 0px solid green; color:green; background-color:black"
        self.label.setStyleSheet(self.label_style)
        self.label.setText("На эту дату меню не создано.")
        self.label.setFont(QFont('Fixedsys'))

        self.btn_save_and_quit = QPushButton(">>> ВЫБРАТЬ ДРУГУЮ ДАТУ", self)
        self.btn_save_and_quit.setGeometry(10, 55, 220, 30)
        self.btn_save_and_quit.setStyleSheet("QPushButton"
                                       "{"
                                       "border: 0px solid green;color:black; background-color:green;"
                                       "}"
                                       "QPushButton::hover"
                                       "{"
                                       "background-color : white;"
                                       "}")
        self.btn_save_and_quit.setFont(QFont('Fixedsys'))
        self.btn_save_and_quit.clicked.connect(self.btn_save_and_quit_func)

    def btn_save_and_quit_func(self):
        self.close()

class SubmenuWhatToCook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(600, 500)
        self.setWindowTitle("Что бы приготовить?")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        self.combo_ingredients = QComboBox(self)
        self.combo_ingredients.addItems(["ВЫБЕРИТЕ ИНГРИДИЕНТ"])
        cursor.execute('''SELECT col_ingredients FROM tab_ingredientes ORDER BY col_ingredients''')
        x = cursor.fetchall()
        for i in x:
            self.combo_ingredients.addItems([i[0]])
        self.combo_ingredients.move(10, 10)
        self.combo_ingredients.setStyleSheet("QComboBox"
                                         "{"
                                         "border: 0px solid green;color:black; background-color:green;min-width: 260px;"
                                         "}"
                                         "QComboBox::hover"
                                         "{"
                                         "background-color : white;"
                                         "}")
        self.combo_ingredients.setFont(QFont('Fixedsys'))
        self.combo_ingredients.activated[str].connect(self.combo_func)

        self.textEdit_ingridients = QTextEdit(self)
        self.textEdit_ingridients.setGeometry(10, 40, 277, 300)
        self.textEdit_ingridients_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit_ingridients.setStyleSheet(self.textEdit_ingridients_style)
        self.textEdit_ingridients.setFont(QFont('Fixedsys'))

        self.btn_save_and_quit = QPushButton(">>> КАЖЕТСЯ, ВСЕ...", self)
        self.btn_save_and_quit.setGeometry(25, 350, 250, 30)
        self.btn_save_and_quit.setStyleSheet("QPushButton"
                                       "{"
                                       "border: 0px solid green;color:black; background-color:green;"
                                       "}"
                                       "QPushButton::hover"
                                       "{"
                                       "background-color : white;"
                                       "}")
        self.btn_save_and_quit.setFont(QFont('Fixedsys'))
        self.btn_save_and_quit.clicked.connect(self.btn_save_and_quit_func)

        self.textEdit_advice = QTextEdit(self)
        self.textEdit_advice.setGeometry(300, 10, 280, 372)
        self.textEdit_advice_style = "border: 3px solid green; color:green; background-color:black"
        self.textEdit_advice.setStyleSheet(self.textEdit_advice_style)
        self.textEdit_advice.setFont(QFont('Fixedsys'))

        self.label4 = QLabel(self)
        self.label4.setGeometry(10, 405, 570, 80)
        self.label4_style = "border: 0px solid green; color:green; background-color:black"
        self.label4.setStyleSheet(self.label4_style)
        self.label4.setText("В холодильнике завалялись какие-то продукты, а вы не знаете,\nчто из этого приготовить? Постараемся вам помочь! Введите все,\nчто есть и нажмите кнопку!")
        self.label4.setFont(QFont('Fixedsys'))

    def combo_func(self):
        self.chosen_ingridient = self.combo_ingredients.currentText()
        self.textEdit_ingridients.append(self.chosen_ingridient)
        self.combo_ingredients.setCurrentIndex(0)

    def btn_save_and_quit_func(self):
        self.textEdit_advice.clear()
        all_in_fridge = self.textEdit_ingridients.toPlainText()
        dirty_list_in_fridge = set(all_in_fridge.split("\n"))
        cursor.execute('''SELECT col_name, col_ingredient FROM tab_allrecipe''')
        dirty_list_inrecipe = cursor.fetchall()
        temp_set = {dirty_list_inrecipe[0][1]}
        percentage = 0
        for i in range(len(dirty_list_inrecipe)+1):
            try:
                if dirty_list_inrecipe[i+1][0] == dirty_list_inrecipe[i][0]:
                    temp_set.add(dirty_list_inrecipe[i+1][1])
                else:
                    union = dirty_list_in_fridge.intersection(temp_set)
                    if len(union) == len(temp_set):
                        self.textEdit_advice.append(f"Приготовьте {dirty_list_inrecipe[i][0]}! У вас обязательно получится!")
                    elif len(union) >= (len(dirty_list_in_fridge)/10*8):
                        self.textEdit_advice.append(
                            f"Возможно, получится {dirty_list_inrecipe[i][0]}, но это не точно.")
                    temp_set = {dirty_list_inrecipe[i+1][1]}
            except Exception as E:
                if len(union) == len(temp_set):
                    self.textEdit_advice.append(
                        f"Приготовьте {dirty_list_inrecipe[i-1][0]}! У вас обязательно получится!")
                elif len(union) >= (len(dirty_list_in_fridge) / 10 * 8):
                    self.textEdit_advice.append(
                        f"Возможно, получится {dirty_list_inrecipe[i-1][0]}, но это не точно.")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    ex = Main()
    ex.show()
    sys.exit(app.exec_())