import random
from zellegraphics import *

def randpixel(color1,color2):
    if random.randint(0,1) == 1:
        color = color1
    else:
        color = color2
    return color

def pattern5(color1,color2):
	"""draws a box of a certain pattern. 
		color1 is the top cross color. color2 is the other color."""
	ps = 20
	win = GraphWin("box", 10*ps, 10*ps)

	for x in range(10):
		for y in range(10):
			color = randpixel(color1,color2)
			tl = Point(x*ps,y*ps)
			br = Point((x+1)*ps,(y+1)*ps)
			p = Rectangle(tl,br)
			p.setFill(color)
			p.draw(win)

#let's draw the color1 boxes on top
	boxarray_tl = [(0,0),(4,0),(8,0),(3,3),(6,3),(0,4),(8,4),(3,6),(6,6),(0,8),(4,8),(8,8)]
	boxarray_br = [(2,2),(6,2),(10,2),(4,4),(7,4),(2,6),(10,6),(4,7),(7,7),(2,10),(6,10),(10,10)]
	for q in range(len(boxarray_tl)):
		tl_x = boxarray_tl[q][0]*ps
		tl_y = boxarray_tl[q][1]*ps
		tl = Point(tl_x,tl_y)
		br_x = boxarray_br[q][0]*ps
		br_y = boxarray_br[q][1]*ps
		br = Point(br_x,br_y)
		p = Rectangle(tl,br)
		p.setFill(color1)
		p.draw(win)

#Now the color2 boxes (which are harder)
	boxarray_tl = [(2,0),(6,0),(0,2),(8,2),(0,6),(8,6),(2,8),(6,8)]
	boxarray_br = [(4,2),(8,2),(2,4),(10,4),(2,8),(10,8),(4,10),(8,10)]
	for q in range(len(boxarray_tl)):
		tl_x = boxarray_tl[q][0]*ps
		tl_y = boxarray_tl[q][1]*ps
		tl = Point(tl_x,tl_y)
		br_x = boxarray_br[q][0]*ps
		br_y = boxarray_br[q][1]*ps
		br = Point(br_x,br_y)
		p = Rectangle(tl,br)
		p.setFill(color2)
		p.draw(win)

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
    

