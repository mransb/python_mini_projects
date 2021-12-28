import tkinter as tt
import time
class BouncingBall:
    def __init__(self):
        frame=tt.Tk()
        frame.title("Bouncing Ball")
        DP=tt.Canvas(frame,width="500",height="400",bg="seashell2")
        MB1=DP.create_oval(10,10,30,30,fill="pink")
        MB2=DP.create_oval(10,10,50,50,fill="green")
        MB3=DP.create_oval(10,10,40,40,fill="yellow")
        MB4=DP.create_oval(10,10,60,60,fill="red")
        DP.pack()
        x1_speed=2
        y1_speed=2
        x2_speed=3
        y2_speed=3
        x3_speed=4
        y3_speed=4
        x4_speed=5
        y4_speed=5
        while True:
            DP.move(MB1,x1_speed,y1_speed)
            DP.move(MB2,x2_speed,y2_speed)
            DP.move(MB3,x3_speed,y3_speed)
            DP.move(MB4,x4_speed,y4_speed)
            mycoords1=DP.coords(MB1)
            mycoords2=DP.coords(MB2)
            mycoords3=DP.coords(MB3)
            mycoords4=DP.coords(MB4)
            if mycoords1[2]>500 or mycoords1[0]<0:
                x1_speed=-x1_speed
            if mycoords1[3]>=400 or mycoords1[1]<0:
                y1_speed=-y1_speed
            if mycoords2[2]>500 or mycoords2[0]<0:
                x2_speed=-x2_speed
            if mycoords2[3]>=400 or mycoords2[1]<0:
                y2_speed=-y2_speed
            if mycoords3[2]>500 or mycoords3[0]<0:
                x3_speed=-x3_speed
            if mycoords3[3]>=400 or mycoords3[1]<0:
                y3_speed=-y3_speed
            if mycoords4[2]>500 or mycoords4[0]<0:
                x4_speed=-x4_speed
            if mycoords4[3]>=400 or mycoords4[1]<0:
                y4_speed=-y4_speed
            DP.update()
            time.sleep(0.02)
        
BouncingBall()
