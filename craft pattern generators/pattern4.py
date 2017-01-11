import random
from zellegraphics import *

def randpixel(goal_color,color2,percent):
    #percent is how much the algorithm favors the goal_color, it is an int from 0 to 100
    if random.randint(0,100) >= percent:
        color = color2
    else:
        color = goal_color
    return color

def drawpixel(win, color, ps, x, y):
        tl = Point(x*ps,y*ps)
        br = Point((x+1)*ps,(y+1)*ps)
        p = Rectangle(tl,br)
        p.setFill(color)
        p.draw(win)

def pattern4(cross_color,goal_color,other_color):
    #other_color is the non-goal color
    ps = 20
    win = GraphWin("box", 10*ps, 15*ps)
    
    for x in range(10):
        for y in range(1):
            color = randpixel(goal_color,other_color,25)
            drawpixel(win, color, ps, x, y)
        for y in range(1,5):
            color = randpixel(goal_color,other_color,40)
            drawpixel(win, color, ps, x, y)
        for y in range(5,9):
            color = randpixel(goal_color,other_color,60)
            drawpixel(win, color, ps, x, y)
        for y in range(9,10):
            color = randpixel(goal_color,other_color,75)
            drawpixel(win, color, ps, x, y)
        for y in range(10,11):
            color = randpixel(goal_color,other_color,85)
            drawpixel(win, color, ps, x, y)
        for y in range(11,12):
            color = randpixel(goal_color,other_color,93)
            drawpixel(win, color, ps, x, y)
        for y in range(12,15):
            color = goal_color
            drawpixel(win, color, ps, x, y)

    if cross_color == goal_color:
        #let's draw the cross_color boxes on top
        boxarray_tl = [(0,0),(4,0),(8,0),(3,3),(6,3),(0,4),(7,4),(4,6),(0,8),(8,8)]
        boxarray_br = [(2,2),(6,4),(10,2),(4,7),(7,7),(3,6),(10,6),(6,10),(2,10),(10,10)]
        for q in range(len(boxarray_tl)):
            tl_x = boxarray_tl[q][0]*ps
            tl_y = boxarray_tl[q][1]*ps
            tl = Point(tl_x,tl_y)
            br_x = boxarray_br[q][0]*ps
            br_y = boxarray_br[q][1]*ps
            br = Point(br_x,br_y)
            p = Rectangle(tl,br)
            p.setFill(cross_color)
            p.draw(win)
        
    else: #goal_color is the background color
        #Draw the bg_color boxes (which are harder)
        bg_color = goal_color #I've been changing the variable names too much

        #Center box
        cp1 = Point(4*ps,4*ps)
        cp2 = Point(6*ps,6*ps)
        cp = Rectangle(cp1,cp2)
        cp.setFill(bg_color)
        cp.draw(win)

        #Ears
        vertarray = [(2,0),(4,0),(4,3),(3,3),(3,4),(0,4),(0,2),(2,2)]
        vertarray1 = []
        vertarray2 = []
        vertarray3 = []
        vertarray4 = []
        for v in vertarray:
            vert_x = v[0]*ps
            vert_y = v[1]*ps
            vertex1 = Point(vert_x,vert_y)
            vertarray1.append(vertex1)
            vertex2 = Point(vert_x,4*ps-vert_y)
            vertarray2.append(vertex2)
            vertex3 = Point(4*ps-vert_x,vert_y)
            vertarray3.append(vertex3)
            vertex4 = Point(4*ps-vert_x,4*ps-vert_y)
            vertarray4.append(vertex4)
            
        p1 = Polygon(vertarray1)
        p1.setFill(bg_color)
        p1.draw(win)

        p2 = Polygon(vertarray2)
        p2.setFill(bg_color)
        p2.draw(win)
        p2.move(0,6*ps)

        p3 = Polygon(vertarray3)
        p3.setFill(bg_color)
        p3.draw(win)
        p3.move(6*ps,0)

        p4 = Polygon(vertarray4)
        p4.setFill(bg_color)
        p4.draw(win)
        p4.move(6*ps,6*ps)

#Lets put some grid lines in
    for x in range(11):
        point1 = Point(x*ps,0)
        point2 = Point(x*ps,10*ps)
        y_line = Line(point1,point2)
        y_line.draw(win)
        point3 = Point(0,x*ps)
        point4 = Point(10*ps,x*ps)
        x_line = Line(point3,point4)
        x_line.draw(win)
    


