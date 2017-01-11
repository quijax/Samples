# Samples
Little programs that do little things. Also testing out git concepts.

######

craft pattern generators use the zellegraphics library to create 2-color patterns with random elements. The original patterns are 10x10 and hard-coded.

######

boring.py is a little adventure game that really doesn't do anything at all. You can 
      'north' : ['go north','head north','north'],
			'south' : ['go south','head south','south'],
			'east' : ['go east','head east','east'],
			'west' : ['go west','head west','west'],
			'left' : ['left','turn left','go left','head left'],
			'right' : ['right','turn right','go right','head right'],
			'up' : ['up','go up','climb up','head up','jump up'],
			'down' : ['down','go down','climb down','head down','jump down'],
			'forward' : ['forward','go forward','go on','go straight','straight'],
			'back' : ['back','go back','go backward','turn back','head back','back up','return'],
			'open' : ['open','open door', 'open the door'],
			'close' : ['close','close door','close the door'],
			'enter' : ['enter','enter room'],
			'exit' : ['exit','exit room'],
			'look' : ['look','look around'],
			'inventory' : ['inventory','look in pocket','look in bag','stuff'],
			'exit' : ['exit']
      
     With parameters (items) you can ['get','drop','use']
     
     But only if they are defined for the specific room you are in. There are only three rooms, one of which is instant death.
     It's not really very much fun.
