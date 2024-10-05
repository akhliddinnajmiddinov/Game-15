from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color: rgb(255, 213, 84);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_game()

    def start_game(self):
        MainWindow.resize(400, 400)

        # self.winbtn = QtWidgets.QPushButton(self.centralwidget)
        # self.winbtn.setGeometry(QtCore.QRect(0, 400, 400, 20))
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # font.setBold(True)
        # font.setWeight(75)
        # self.winbtn.setFont(font)
        # self.winbtn.setStyleSheet("background-color: rgb(255, 168, 47);\n"
        #                   "border-color: rgb(0, 0, 0);")
        # self.winbtn = btn
        # self.winbtn.hide()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def getInvCount(self, arr):
        N=4
        arr1=[]
        for y in arr:
            for x in y:
                arr1.append(x)
        arr=arr1
        inv_count = 0
        for i in range(N * N - 1):
            for j in range(i + 1,N * N):
                # count pairs(arr[i], arr[j]) such that
                # i < j and arr[i] > arr[j]
                if (arr[j] and arr[i] and arr[i] > arr[j]):
                    inv_count+=1
             
         
        return inv_count
     
     
    # find Position of blank from bottom
    def findXPosition(self, puzzle):
        N=4
        # start from bottom-right corner of matrix
        for i in range(N - 1,-1,-1):
            for j in range(N - 1,-1,-1):
                if (puzzle[i][j] == 0):
                    return N - i
     
     
    # This function returns true if given
    # instance of N*N - 1 puzzle is solvable
    def isSolvable(self, puzzle):
        N=4
        # Count inversions in given puzzle
        invCount = self.getInvCount(puzzle)
     
        # If grid is odd, return true if inversion
        # count is even.
        if (N & 1):
            return ~(invCount & 1)
     
        else:    # grid is even
            pos = self.findXPosition(puzzle)
            if (pos & 1):
                return ~(invCount & 1)
            else:
                return invCount & 1
     

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        labels = [i for i in range(16)]
        random.shuffle(labels)
        while not self.isSolvable([labels[:4], labels[4:8], labels[8:12], labels[12:]]):
            random.shuffle(labels)
        
        
        self.table = []
        for i in range(4):
            row = []
            for j in range(4):
                if labels[i*4+j] == 0:
                    row.append(None)
                    continue
                btn = QtWidgets.QPushButton(self.centralwidget)
                btn.setGeometry(QtCore.QRect(j * 100, i * 100, 100, 100))
                font = QtGui.QFont()
                font.setPointSize(40)
                font.setBold(True)
                font.setWeight(75)
                btn.setFont(font)
                btn.setStyleSheet("background-color: rgb(255, 168, 47);\n"
                                  "border-color: rgb(0, 0, 0);")
                row.append(btn)
            self.table.append(row)

        for i in range(16):
            if labels[i] != 0:
                self.table[i//4][i%4].setText(_translate("MainWindow", str(labels[i])))
        # self.winbtn.setText(_translate("MainWindow", "Reply"))

        # self.print_all_cells()
        self.addFunctions()

    def addFunctions(self):
        try:
            self.table[0][0].clicked.disconnect()
        except:
            pass

        try:
            self.table[0][1].clicked.disconnect()
        except:
            pass

        try:
            self.table[0][2].clicked.disconnect()
        except:
            pass

        try:
            self.table[0][3].clicked.disconnect()
        except:
            pass

        try:
            self.table[1][0].clicked.disconnect()
        except:
            pass

        try:
            self.table[1][1].clicked.disconnect()
        except:
            pass

        try:
            self.table[1][2].clicked.disconnect()
        except:
            pass

        try:
            self.table[1][3].clicked.disconnect()
        except:
            pass

        try:
            self.table[2][0].clicked.disconnect()
        except:
            pass

        try:
            self.table[2][1].clicked.disconnect()
        except:
            pass

        try:
            self.table[2][2].clicked.disconnect()
        except:
            pass

        try:
            self.table[2][3].clicked.disconnect()
        except:
            pass

        try:
            self.table[3][0].clicked.disconnect()
        except:
            pass

        try:
            self.table[3][1].clicked.disconnect()
        except:
            pass

        try:
            self.table[3][2].clicked.disconnect()
        except:
            pass

        try:
            self.table[3][3].clicked.disconnect()
        except:
            pass

        if (self.table[0][0] != None):
            self.table[0][0].clicked.connect(self.cell00)
        if (self.table[0][1] != None):
            self.table[0][1].clicked.connect(self.cell01)
        if (self.table[0][2] != None):
            self.table[0][2].clicked.connect(self.cell02)
        if (self.table[0][3] != None):
            self.table[0][3].clicked.connect(self.cell03)
        if (self.table[1][0] != None):
            self.table[1][0].clicked.connect(self.cell10)
        if (self.table[1][1] != None):
            self.table[1][1].clicked.connect(self.cell11)
        if (self.table[1][2] != None):
            self.table[1][2].clicked.connect(self.cell12)
        if (self.table[1][3] != None):
            self.table[1][3].clicked.connect(self.cell13)
        if self.table[2][0] != None:
            self.table[2][0].clicked.connect(self.cell20)
        if self.table[2][1] != None:
            self.table[2][1].clicked.connect(self.cell21)
        if (self.table[2][2] != None):
            self.table[2][2].clicked.connect(self.cell22)
        if (self.table[2][3] != None):
            self.table[2][3].clicked.connect(self.cell23)
        if (self.table[3][0] != None):
            self.table[3][0].clicked.connect(self.cell30)
        if (self.table[3][1] != None):
            self.table[3][1].clicked.connect(self.cell31)
        if (self.table[3][2] != None):
            self.table[3][2].clicked.connect(self.cell32)
        if (self.table[3][3] != None):
            self.table[3][3].clicked.connect(self.cell33)
        # self.show_win()

    def show_win(self):
        print("YUTDINGIZ!!!")

    def check(self):
        if self.table[3][3] != None:
            return False

        for i in range(4):
            for j in range(4):
                if i == j == 3:
                    continue
                if self.table[i][j].text() != str(i * 4 + j + 1):
                    return False
        return True

    def print_all_cells(self):
        for i in range(4):
            for j in range(4):
                print(f"{i}{j} = ", self.table[i][j])


    def right_move(self, row, left_col, right_col):
        for i in range(right_col, left_col - 1, -1):
            self.table[row][i].setGeometry(QtCore.QRect((i + 1) * 100, row * 100, 100, 100))
            self.table[row][i + 1] = self.table[row][i]
        self.table[row][left_col] = None
        # self.print_all_cells()
        self.addFunctions()
        if self.check():
            self.show_win()

    def left_move(self, row, left_col, right_col):
        for i in range(left_col, right_col + 1):
            self.table[row][i].setGeometry(QtCore.QRect((i - 1) * 100, row * 100, 100, 100))
            self.table[row][i - 1] = self.table[row][i]
        self.table[row][right_col] = None
        # self.print_all_cells()
        self.addFunctions()
        if self.check():
            self.show_win()


    def up_move(self, col, top_row, bottom_row):
        for i in range(top_row, bottom_row + 1):
            self.table[i][col].setGeometry(QtCore.QRect(col * 100, (i - 1) * 100, 100, 100))
            self.table[i - 1][col] = self.table[i][col]
        self.table[bottom_row][col] = None
        # self.print_all_cells()
        self.addFunctions()
        if self.check():
            self.show_win()

    def bottom_move(self, col, top_row, bottom_row):
        for i in range(bottom_row, top_row - 1, -1):
            self.table[i][col].setGeometry(QtCore.QRect(col * 100, (i + 1) * 100, 100, 100))
            self.table[i + 1][col] = self.table[i][col]
        self.table[top_row][col] = None
        # self.print_all_cells()
        self.addFunctions()
        if self.check():
            self.show_win()

    def cell00(self):
        for i in range(1, 4):
            if self.table[0][i] == None:
                self.right_move(0, 0, i - 1)
                break

        for i in range(1, 4):
            if self.table[i][0] == None:
                self.bottom_move(0, 0, i - 1)
                break

    def cell01(self):
        for i in range(2, 4):
            if self.table[0][i] == None:
                self.right_move(0, 1, i - 1)
                break

        for i in range(1):
            if self.table[0][i] == None:
                self.left_move(0, i + 1, 1)
                break

        for i in range(1, 4):
            if self.table[i][1] == None:
                self.bottom_move(1, 0, i - 1)
                break

    def cell02(self):
        for i in range(3, 4):
            if self.table[0][i] == None:
                self.right_move(0, 2, i - 1)
                break

        for i in range(2):
            if self.table[0][i] == None:
                self.left_move(0, i + 1, 2)
                break

        for i in range(1, 4):
            if self.table[i][2] == None:
                self.bottom_move(2, 0, i - 1)
                break

    def cell03(self):
        for i in range(3):
            if self.table[0][i] == None:
                self.left_move(0, i + 1, 3)
                break

        for i in range(1, 4):
            if self.table[i][3] == None:
                self.bottom_move(3, 0, i - 1)
                break

    def cell10(self):
        for i in range(1, 4):
            if self.table[1][i] == None:
                self.right_move(1, 0, i - 1)
                break

        for i in range(1):
            if self.table[i][0] == None:
                self.up_move(0, i + 1, 1)
                break

        for i in range(2, 4):
            if self.table[i][0] == None:
                self.bottom_move(0, 1, i - 1)
                break

    def cell11(self):
        # self.print_all_cells()
        for i in range(2, 4):
            if self.table[1][i] == None:
                self.right_move(1, 1, i - 1)
                break

        for i in range(1):
            if self.table[1][i] == None:
                self.left_move(1, i + 1, 1)
                break

        for i in range(1):
            if self.table[i][1] == None:
                self.up_move(1, i + 1, 1)
                break

        for i in range(2, 4):
            if self.table[i][1] == None:
                self.bottom_move(1, 1, i - 1)
                break

    def cell12(self):
        for i in range(3, 4):
            if self.table[1][i] == None:
                self.right_move(1, 2, i - 1)
                break

        for i in range(2):
            if self.table[1][i] == None:
                self.left_move(1, i + 1, 2)
                break

        for i in range(1):
            if self.table[i][2] == None:
                self.up_move(2, i + 1, 1)
                break

        for i in range(2, 4):
            if self.table[i][2] == None:
                self.bottom_move(2, 1, i - 1)
                break

    def cell13(self):
        for i in range(3):
            if self.table[1][i] == None:
                self.left_move(1, i + 1, 3)
                break

        for i in range(1):
            if self.table[i][3] == None:
                self.up_move(3, i + 1, 1)
                break

        for i in range(2, 4):
            if self.table[i][3] == None:
                self.bottom_move(3, 1, i - 1)
                break

    def cell20(self):
        for i in range(1, 4):
            if self.table[2][i] == None:
                self.right_move(2, 0, i - 1)
                break

        for i in range(2):
            if self.table[i][0] == None:
                self.up_move(0, i + 1, 2)
                break

        for i in range(3, 4):
            if self.table[i][0] == None:
                self.bottom_move(0, 2, i - 1)
                break

    def cell21(self):
        for i in range(2, 4):
            if self.table[2][i] == None:
                self.right_move(2, 1, i - 1)
                break

        for i in range(1):
            if self.table[2][i] == None:
                self.left_move(2, i + 1, 1)
                break

        for i in range(2):
            if self.table[i][1] == None:
                self.up_move(1, i + 1, 2)
                break

        for i in range(3, 4):
            if self.table[i][1] == None:
                self.bottom_move(1, 2, i - 1)
                break

    def cell22(self):
        for i in range(3, 4):
            if self.table[2][i] == None:
                self.right_move(2, 2, i - 1)
                break

        for i in range(2):
            if self.table[2][i] == None:
                self.left_move(2, i + 1, 2)
                break

        for i in range(2):
            if self.table[i][2] == None:
                self.up_move(2, i + 1, 2)
                break

        for i in range(3, 4):
            if self.table[i][2] == None:
                self.bottom_move(2, 2, i - 1)
                break

    def cell23(self):
        for i in range(3):
            if self.table[2][i] == None:
                self.left_move(2, i + 1, 3)
                break

        for i in range(2):
            if self.table[i][3] == None:
                self.up_move(3, i + 1, 2)
                break

        for i in range(3, 4):
            if self.table[i][3] == None:
                self.bottom_move(3, 2, i - 1)
                break

    def cell30(self):
        for i in range(1, 4):
            if self.table[3][i] == None:
                self.right_move(3, 0, i - 1)
                break

        for i in range(3):
            if self.table[i][0] == None:
                self.up_move(0, i + 1, 3)
                break

    def cell31(self):
        for i in range(2, 4):
            if self.table[3][i] == None:
                self.right_move(3, 1, i - 1)
                break

        for i in range(1):
            if self.table[3][i] == None:
                self.left_move(3, i + 1, 1)
                break

        for i in range(3):
            if self.table[i][1] == None:
                self.up_move(1, i + 1, 3)
                break
    def cell32(self):
        for i in range(3, 4):
            if self.table[3][i] == None:
                self.right_move(3, 2, i - 1)
                break

        for i in range(2):
            if self.table[3][i] == None:
                self.left_move(3, i + 1, 2)
                break

        for i in range(3):
            if self.table[i][2] == None:
                self.up_move(2, i + 1, 3)
                break

        for i in range(3, 4):
            if self.table[i][2] == None:
                self.bottom_move(2, 3, i - 1)
                break

    def cell33(self):
        for i in range(3):
            if self.table[3][i] == None:
                self.left_move(3, i + 1, 3)
                break

        for i in range(3):
            if self.table[i][3] == None:
                self.up_move(3, i + 1, 3)
                break





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
