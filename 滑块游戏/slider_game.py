import sys
import random
from enum import IntEnum
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QGridLayout, QMessageBox
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import Qt

# 用枚举类表示方向
class Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Slider(QWidget):
    """ 滑块游戏主体 """
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.zero_row = 0
        self.zero_column = 0
        self.gltMain = QGridLayout()

        self.initUI()

    # 窗口的搭建
    def initUI(self):
        # 滑块间隔
        self.gltMain.setSpacing(10)

        self.onInit()

        # 布局
        self.setLayout(self.gltMain)
        # 窗口的宽和高
        self.setFixedSize(800, 800)
        # 标题
        self.setWindowTitle('Slider come on')
        # 背景色
        self.setStyleSheet("background-color:purple;")
        self.show()

    # 初始化布局
    def onInit(self):
        # 随机数据的产生

        # 产生顺序数组
        self.numbers = list(range(1, 16))
        self.numbers.append(0)
        # 将数字添加到二维数组
        for row in range(4):
            self.blocks.append([])
            for column in range(4):
                temp = self.numbers[row*4 + column]

                if temp == 0:
                    self.zero_row = row
                    self.zero_column = column
                self.blocks[row].append(temp)
        # 打乱数组
        for i in range(500):
            random_num = random.randint(0, 3)
            self.move(Direction(random_num))

        # 将数字转换成滑块添加到布局
        self.updatePanel()

    # 按键检测
    # 重写 QWidget 的 keyPressEvent 事件句柄
    def keyPressEvent(self, event):
        # 检测按键按下之后是否是"↑↓←→"或"WSAD",并作出相应的移动
        key = event.key()
        if(key == Qt.Key_Up or key == Qt.Key_W):
            self.move(Direction.UP)
        if(key == Qt.Key_Down or key == Qt.Key_S):
            self.move(Direction.DOWN)
        if(key == Qt.Key_Left or key == Qt.Key_A):
            self.move(Direction.LEFT)
        if(key == Qt.Key_Right or key == Qt.Key_D):
            self.move(Direction.RIGHT)
        # 更新布局
        self.updatePanel()
        # 检测是否完成
        if self.checkResult():
            # 弹出提示框，如果点击"ok"，则重新开始
            if QMessageBox.Ok == QMessageBox.information(self, 'The result', 'You are so great'):
                # 重新开始
                self.onInit()

    # 滑块移动
    def move(self, direction):
        if(direction == Direction.UP): # 上
            if self.zero_row != 3:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row + 1][self.zero_column]
                self.blocks[self.zero_row + 1][self.zero_column] = 0
                self.zero_row += 1
        if(direction == Direction.DOWN): # 下
            if self.zero_row != 0:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row - 1][self.zero_column]
                self.blocks[self.zero_row - 1][self.zero_column] = 0
                self.zero_row -= 1
        if(direction == Direction.LEFT): # 左
            if self.zero_column != 3:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column + 1]
                self.blocks[self.zero_row][self.zero_column + 1] = 0
                self.zero_column += 1
        if(direction == Direction.RIGHT): # 右
            if self.zero_column != 0:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column - 1]
                self.blocks[self.zero_row][self.zero_column - 1] = 0
                self.zero_column -= 1

    # 将数字滑块添加到布局
    def updatePanel(self):
        for row in range(4):
            for column in range(4):
                self.gltMain.addWidget(Block(self.blocks[row][column]), row, column)

        self.setLayout(self.gltMain)

    # 检测是否完成
    def checkResult(self):
        # 首先检测右下角是否为0
        if self.blocks[3][3] != 0:
            return False

        # 然后检测数字是否对应
        for row in range(4):
            for column in range(4):
                if self.blocks[row][column] != row*4 + column + 1:
                    return False
        return True

class Block(QLabel):
    """ 数字方块 """

    def __init__(self, number):
        super().__init__()

        self.number = number
        self.setFixedSize(80, 80)

        # 字体
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.setFont(font)

        # 字体颜色
        pa = QPalette()
        pa.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(pa)

        # 文字位置
        self.setAlignment(Qt.AlignCenter)

        # 背景颜色\圆角和文本内容
        if self.number == 0:
            self.setStyleSheet("background-color:white;border-radius:10px;")
        else:
            self.setStyleSheet("background-color:red;border-radius:10px;")
            self.setText(str(self.number))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    slider_game = Slider()
    sys.exit(app.exec_())