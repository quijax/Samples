import random
from zellegraphics import *

def randpixel(color1,color2):
    if random.randint(0,1) == 1:
        color = color1
    else:
        color = color2
    return color

def pattern(color1,color2):
	"""draws a box of a certain pattern. 
		color1 is the top cross color. color2 is the other color.
		example: pattern('blue','yellow')"""

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
	boxarray_tl = [(0,0),(4,0),(8,0),(0,4),(6,4),(4,6),(0,8),(8,8)]
	boxarray_br = [(2,2),(6,4),(10,2),(4,6),(10,6),(6,10),(2,10),(10,10)]
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
	vertarray = [(3,0),(4,0),(4,3),(3,3),(3,4),(0,4),(0,3),(1,3),(1,2),(2,2),(2,1),(3,1),(3,0)]
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
	p1.setFill(color2)
	p1.draw(win)

	p2 = Polygon(vertarray2)
	p2.setFill(color2)
	p2.draw(win)
	p2.move(0,6*ps)

	p3 = Polygon(vertarray3)
	p3.setFill(color2)
	p3.draw(win)
	p3.move(6*ps,0)

	p4 = Polygon(vertarray4)
	p4.setFill(color2)
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
    

