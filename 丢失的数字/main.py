# def missnumber(nums):
#     nums=sorted(nums)
#     #len(nums)
#     if max(nums)==len(nums):
#         for i in range(len(nums)):
#             if nums[i]!=i:
#                 return i
#     else:
#         return len(nums)
#
# print(missnumber([0,1]))
import PyQt5 as qt
import sys
import ui
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ui.Ui_widget()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())