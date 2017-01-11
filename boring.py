#This is an adventure-style game: let's call it "Boring Game."

from sys import exit
#from random import randint
global prompt
prompt = 'ahem: '

#Limited inputs
#First, a dictionary where keys are possible actions and entries are lists of synonyms
input_dict = {
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
			'exit' : ['exit'],
			#the next entry is special. it is a list of actions that require parameters
			#Usually items. As such, they are more brittle than other actions.
			'param_actions' : ['get','drop','use']
			}			

#We will need to interact with inventory
#inventories are dicts of items and counts
#should items be objects? That way they can have a description and a count
class Inventory(object):
	"""Some functions to work with our inventory structure"""
	
	def __init__(self, inventory = {}):
		self._inventory = inventory
		
	#a check to see if an item exists (and count > 0)
	def has_item(self,item):
		try:
			count = self._inventory.get(item)
			if count > 0:
				return True
			else:
				return False
		except KeyError:
			return False
	
	#returns the count of an item - is this necessary?
	def how_many(self,item):
		if self.has_item(item):
			return self._inventory[item]
		else:
			return 0
	
	#add dictionary entry or up count
	def add_item(self,item):
		try:
			self._inventory[item] += 1
		except KeyError:
			self._inventory[item] = 1
			
	#reduce count, but not below zero
	def drop_item(self, item):
		if self.has_item(item):
			self._inventory[item] -= 1
		else:
			raise KeyError
	
	#What is a useful list? ['count item','count item']
	def list_items(self):
		items = []
		for kc in self._inventory.items():
			key, count = kc
			if count > 0:
				out_item = str(count) + ' ' + key
				items.append(out_item)
		if len(items) > 0:
			return items
		else:
			raise KeyError

#We will need scenes (nodes?)
	#scenes have entry points and events
		#scenes may have items
		#events may need to check on items
	#scenes must also interact with the player, at least the player's inventory
	#special scenes are start, win, and death
class Scene(object):
	"""A scene is a space which has doors, events, and items"""
	
	def __init__(self):
		self.items = Inventory({})
		self.description = "This is a scene."
		#flags for events - a dictionary of Booleans
		self.flags = {'first' : True}
		
	def play_event(self,player):
		"""What happens when you enter a room - events are defined here?
		This function is called by Game engine only"""
		if self.flags['first'] is True:
			print "You have entered a scene."
			self.flags['first'] = False
		else:
			print "You have entered a scene. You have been here before."
	
	#define available player actions for the room. actions should match input_dict keys
	#all scenes can interact with inventory items. other actions will be scene specific
	#all actions must have only one variable - the player object
	#all actions must return a flag - True if you want to run play_event again or if you want
	#to change scenes
	def look(self,player):
		#this will be a general description and a list of items.
		print self.description
		try:
			items = self.items.list_items()
			print "There are items here:"
			for i in items:
				print i
		except:
			print "There are no items here."
		
	def exit(self,player):
		#at some point, we may have some saving capability. For now, we are just breaking out.'
		print "Goodbye!"
		exit(1)
		
	def back(self,player):
		#this goes back one scene
		player.scene_stack.pop()
		player.scene_flag = True
	
	#Inventory actions require the player object so we can futz with the player's inventory
	def inventory(self,player):
		"""lets the player see what is in their inventory"""
		try:
			stuff = player.items.list_items()
			print "You have:"
			for s in stuff:
				print s
		except KeyError:
			print "You have no items."
	
	def get(self,player,item):
		#this may be confusing. The player is getting, so the scene is dropping
		try:
			self.items.drop_item(item)
			player.items.add_item(item)
			print "You got a %s." % item
		except KeyError:
			raise Exception('NoItem')
		
	def drop(self,player,item):
		#this may be confusing. The player is dropping, so the scene is getting
		try:
			player.items.drop_item(item)
			self.items.add_item(item)
			print "You dropped a %s." % item
		except KeyError:
			raise Exception('NoItem')
		
	#This is a dummy 'use' to define the exception
	def use(self,player,item):
		#use must be defined for each item
		if item == 'lint':
			#If an item is used up, drop it so it disappears
			player.items.drop_item(item)
			print "Use that lint!"
			count = player.items.how_many(item)
			if count >= 1:
				print "You have %d %s left." % (count, item)
			else:
				print "You used up your %s." % item
		elif item == 'key':
			print "You use your key."
		else:
			raise Exception("Item has no defined use.")
			
class Death(object):
	"""Death is a special scene/event that has only one action: back up"""
	def __init__(self):
		self.description = "You are dead."
	
	def play_event(self,player):
		print self.description
		print "Would you like to try again?"
		choice = raw_input(prompt)
		if choice == 'yes':
			player.scene_stack.pop()
			player.scene_flag = True
		else:
			print "Better luck next time!"
			exit(1)

class Win(object):
	"""Win is a special scene/event that has no actions"""
	def __init__(self):
		self.description = "You win!"
		
	def play_event(self,player):	
		print self.description
		exit(1)

#Specific Scenes
class Opening(Scene):
	"""The first scene, sets the stage."""
	def __init__(self):
		start_inventory = {'key':1}
		self.items=Inventory(start_inventory)
		self.description = "You are at the beginning. There is a door to the north and a corridor to the east."
		self.flags = {'first' : True, 'door_locked' : True}
	
	#overwrite the actions that are scene specific
	def use(self,player,item):
		#use must be defined for each item
		if item == 'key':
			print "You have unlocked the door."
			self.flags['door_locked'] = False
		else:
			raise Exception("Item has no defined use.")
	
	def back(self,player):
		print "You can't back up."
		
	def play_event(self,player):
		"""What happens when you enter a room - events are defined here?
		This function is called by Game engine only"""
		if self.flags['first'] is True:
			print "It begins."
			print "There is a door on the north wall and a corridor to the east."
			self.flags['first'] = False
		else:
			print "You are back at the beginning."
			
	def north(self,player):
		if self.flags['door_locked'] is True:
			print "The door is locked."
		else:
			print "Through that door is death."
			player.scene_stack.append('death')
			player.scene_flag = True
			
	def east(self,player):
		player.scene_stack.append('corridor')
		player.scene_flag = True
		
class Corridor(Scene):
	def __init__(self):
		self.items=Inventory({})
		self.description = "This is a corridor. It runs east-west."
		self.flags = {'first' : True}
	
	def play_event(self,player):
		if self.flags['first'] is True:
			print "This is a long corridor, running east-west."
			self.flags['first'] = False
		else:
			print "You have entered a corridor. You have been here before."
	
	def look(self,player):
		#description will depend on where you entered the corridor
		print self.description
		if player.scene_stack[-2] == 'opening':
			print "You are facing east. There is a room there."
		else:
			print "You are facing west. That way is the beginning."
		try:
			items = self.items.list_items()
			print "There are items here:"
			for i in items:
				print i
		except:
			print "There are no items here."	
	
	def forward(self,player):
		#description will depend on where you entered the corridor
		if player.scene_stack[-2] == 'opening':
			player.scene_stack.append('room')
			player.scene_flag = True
		else:
			player.scene_stack.append('opening')
			player.scene_flag = True
	
	def east(self,player):
		player.scene_stack.append('room')
		player.scene_flag = True
		
	def west(self,player):
		player.scene_stack.append('opening')
		player.scene_flag = True
		
	def use(self,player,item):
		#use must be defined for each item
			raise Exception("Item has no defined use.")
			
class Room(Scene):
	def __init__(self):
		self.items=Inventory({'gold':5})
		self.description = "This is a room."
		self.flags = {'first' : True}
		
	def look(self,player):
		#description will depend on where you entered the corridor
		print self.description
		if player.scene_stack[-2] == 'corridor':
			print "You are facing east. There is a door there."
		else:
			print "You are facing west. That way is the corridor."
		try:
			items = self.items.list_items()
			print "There are items here:"
			for i in items:
				print i
		except:
			print "There are no items here."
	
	def play_event(self,player):
		if self.flags['first'] is True:
			if player.scene_stack[-2] == 'corridor':
				print "This is a little room with some gold in it. Take some. There is a door to the east."
			else:
				print "This is a little room with some gold in it. There is a door to the west."
			self.flags['first'] = False
		else:
			print "This is a little room. You have been here before."
	
	def east(self,player):
		if player.items.has_item('gold') is True:
			print "That way is the end."
			player.scene_stack.append('win')
			player.scene_flag = True
		else:
			print "You should really get some gold."
			
	def west(self,player):
		player.scene_stack.append('corridor')
		player.scene_flag = True
		
	def use(self,player,item):
		#use must be defined for each item
			raise Exception("Item has no defined use.")
			
class Player(object):
	"""The player has these attributes: 'items' is an Inventory object, 'name' is a string, 
	'scene_stack' is a list of scene objects"""
	def __init__(self,first_scene,scene_dict):
		start_inventory = {'lint':3,'key':0,'house':1,'food':0}
		self.items = Inventory(start_inventory)
		self.name = 'Bob'
		self.scene_stack=[first_scene]
		self.scene_dict = scene_dict
		#This flag tells us whether to run play_event on the last scene in scene_stack
		self.scene_flag = True
		
class Game(object):
	"""The engine that directs the player through the game. 
	It needs to be able to take inputs, call up scenes, manage the player's items.
	"""
	
	def __init__(self, input_dict, scene_dict):	
		self.first_scene = 'opening'		
		#We're doing this stuff up here so that we only do the pop once per instance
		self.input_dict = input_dict
		#We are going to take an item out of the input_dict - the special entry that 
		#lists actions that require parameters
		self.param_actions = self.input_dict.pop('param_actions')
		self.scene_dict = scene_dict
	
	#Asks for and interprets a single input, iterates until it gets something it understands
	#It understands only those phrases in the input_dict, defined at the top.
	#item inputs have a different format: 'action item'
	#we need to strip the item and return them separately...
	def take_input(self):
		#static information
		values = self.input_dict.values()
		keys = self.input_dict.keys()
		param = None
		action = None
		
		#iteration
		while action is None:
			player_input = raw_input(prompt)

			for v in values:
				if player_input in v:
					for k in keys:
						if player_input in self.input_dict[k]:
							action = k
							return (action, param)
				else:
					#We're going to check for those special actions now
					#These actions are brittle. they must be in the form 'action param'
					#we may want to strip off leading 'the' and 'a', but I'll worry about that later
					try:
						first,rest = player_input.split(' ', 1)
					except ValueError:
						first = player_input
						rest = None
						
					if first in self.param_actions:
						action = first	
						param = rest
						return (action, param)
							
			print "I don't understand you."	
				
	#turn an input into an action, depends on what scene you're in
	def take_action(self,scene,player,action_param):
		"""Action_param is a tuple. The first element is a string, action, and the 
		second element is a parameter, default None. We want 
		to see if the action is defined in the scene and run it if it is.
		"""
		action, param = action_param
		
		#build a string and then execute it using exec
		if param is None:
			action_string = 'scene.'+action+'(player)'					
			try:
				exec action_string
			except AttributeError:
				print "You can't do that here."
			except TypeError:
				print "%s what?" % action
		#we know what to do with parameters! We defined it below:
		else:
			self.item_action(scene,player,action,param)

			
	#I'm going to separate out the item actions for now
	def item_action(self,scene,player,action,item):
		"""I'm going to have to hard code item actions because we need to keep 
		track of player inventory as well as scene inventory.
		"""
		if action == 'get':
			try:
				scene.get(player,item)
			except Exception:
				print "There is no %s here." % item
				
		elif action == 'drop':
			try:
				scene.drop(player,item)
			except Exception:
				print "You don't have a %s to drop." % item
				
		elif action == 'use':
			if player.items.has_item(item):
				try:
					scene.use(player,item)
				except AttributeError:
					print "You can't do that."
				except Exception:
					print "You can't use %s here." % item
					
			else:
				print "You don't have a %s to use." % item
		else:
			print "You want to what with what?"
			
	#We're going to put some things together now
	def play(self):
		s = self.first_scene
		p = Player(s,self.scene_dict)
		
		print "Welcome to Boring Game!"
		print "What is your name?"
		name = raw_input(prompt)
		p.name = name
		print "Hello %s!" % p.name
		
		#This is an infinite loop. Sorry!
		while True:
			current_scene_key = p.scene_stack[-1]
			current_scene = p.scene_dict[current_scene_key]
			p.scene_flag = False
	
			#set the scene - instantiate if you have to
			try:
				current_scene.play_event(p)
			except Exception as error:
				print "There was an Exception: %r" % error
				exit(1)
				
			print "What do you want to do?"
			while p.scene_flag is False:
				input = self.take_input()
				try:
					self.take_action(current_scene,p,input)
				except:
					exit(1)

#and now to run it
#We're going to instantiate all the scenes:
opening = Opening()
corridor = Corridor()
death = Death()
win = Win()
room = Room()
scene_dict = {'win' : win, 'opening' : opening, 'corridor' : corridor, 'death' : death,
				'room' : room,}

g = Game(input_dict,scene_dict)
g.play()
