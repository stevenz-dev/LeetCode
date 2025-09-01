import curses
import time

def main(stdscr):
    # 隐藏光标
    curses.curs_set(0)
    
    # 清空屏幕
    stdscr.clear()

    # 定义箭头字符
    arrow = "↑"

    for i in range(5):
        # 在屏幕上的新位置写入箭头
        stdscr.addstr(0, i, arrow)

        # 刷新屏幕以显示新的箭头
        stdscr.refresh()

        # 每秒移动一次
        time.sleep(1)

        # 清除旧箭头
        stdscr.addstr(0, i, "  ")

    # 等待用户按键，以便看到箭头移动的最终位置
    stdscr.getkey()

# 使用 curses.wrapper() 初始化 curses 环境，并调用 main() 函数
curses.wrapper(main)
