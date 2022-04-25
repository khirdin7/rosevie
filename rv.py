from turtle import*
bgcolor("black")
pensize(1)
speed(0)
def rosevie():
 for i in range(300):
     for colours in ["green","red","white","cyan"]:
         color(colours)
         circle(190-i,90)
         left(90)
         circle(190-i,90)
         left(18)
rosevie()
mainloop()
