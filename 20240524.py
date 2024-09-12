# # import tkinter as tk
# # window = tk.Tk()
# #
# # def SavePoint(event):
# #     global x,y
# #     x = event.x
# #     y = event.y
# #
# # def Draw(event):
# #     canvas.create_line(x,y,event.x,event.y,fill="red")
# #     SavePoint(event)
# # canvas = tk.Canvas(window,width=600,height=400,bg="white")
# # canvas.pack()
# #
# # canvas.bind("<Button-1>",SavePoint)
# # canvas.bind("<B1-Motion>",Draw)
# # window.mainloop()
#
# import tkinter as tk
# window = tk.Tk()
#
# def SavePoint(event):
#     global x,y
#     x = event.x
#     y = event.y
#
# def Draw(event):
#     canvas.create_rectangle(x,y,event.x,event.y,fill="red")
#     SavePoint(event)
# canvas = tk.Canvas(window,width=600,height=400,bg="white")
# canvas.pack()
#
# canvas.bind("<Button-1>",SavePoint)
# canvas.bind("<ButtonRelease-1>",Draw)
# window.mainloop()

import random
import tkinter as tk
from tkinter import messagebox

# Ball 클래스 생성 : player, ball(들) 생성 시 사용
class Ball:
    def __init__(self, canvas, color, x, y, r, speed_x, speed_y):
        self.canvas = canvas
        self.color = color                      # 색깔
        self.x = x                              # 중심 좌표
        self.y = y
        self.r = r                              # 반지름
        self.speed_x = speed_x                  # 속도
        self.speed_y = speed_y
        self.id = canvas.create_oval(x - r, y - r, x + r, y + r, fill=color)

    def Move(self):
        # 현재 속도(speed_x, speed_y)에 따라 이동한다.
        self.canvas.move(self.id, self.speed_x, self.speed_y)
        self.canvas.update()
        # 공의 현재 위치를 얻는다. (왼쪽-위 꼭지점의 좌표가 반환됨)
        (x1, y1, x2, y2) = self.canvas.coords(self.id)
        # 공의 위치를 갱신한다.
        self.x, self.y = x1 + self.r, y1 + self.r  # 나중에 필요한 경우 사용

    def CheckCollisionWall(self):
        # 왼쪽 또는 오른쪽 경계를 넘으면 x 속도의 부호를 반전시킨다.
        collision = False                          # 벽과의 충돌 여부
        if self.x - self.r <= 0 or self.x + self.r >= self.canvas.winfo_width():
            self.speed_x = -self.speed_x
            collision = True
        # 위 또는 아래 경계를 넘으면 y 속도의 부호를 반전시킨다.
        if self.y - self.r <= 0 or self.y + self.r >= self.canvas.winfo_height():
            self.speed_y = -self.speed_y
            collision = True
        return collision
    def CheckCollisionBall(self,ball):
        distance = ((self.x -ball.x)**2 +(self.y-ball.y)**2)**(1/2)
        if distance <= self.r +ball.r:
            return True
        else:
            return False
    def SetSpeed(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
window = tk.Tk()
canvas = tk.Canvas(window, width = 800, height = 400, background="white")
canvas.pack(expand = 1, fill = tk.BOTH)

# player 생성
player = Ball(canvas, "green", 400, 200, 25, 10, 0)
window.bind("<Up>", lambda event: player.SetSpeed(0, -10)) # 방향키 => 속도 변경
window.bind("<Down>", lambda event: player.SetSpeed(0, 10))
window.bind("<Left>", lambda event: player.SetSpeed(-10, 0))
window.bind("<Right>", lambda event: player.SetSpeed(10, 0))

# ball들 생성
balls = []
for i in range(5):
    balls.append(Ball(canvas, "red", 100, 100, 25,
                      random.randint(1, 10), random.randint(1, 10)))
# 주기적으로 이동
def Move():
    player.Move()               # player 이동
    if player.CheckCollisionWall():
        messagebox.showinfo("정보창", "플레이어가 벽에 부딪혔습니다.\n프로그램을 종료합니다.")
        window.quit()               # 프로그램 종료

    for ball in balls:              # ball들 이동
        ball.Move()
        ball.CheckCollisionWall()
        if player.CheckCollisionBall(ball):
            messagebox.showinfo("정보창","플레이어가")
            window.quit()
    canvas.after(30, Move)          # 0.03초 후 다시 Move 함수 실행

Move()                              # Move 함수 실행
window.mainloop()
