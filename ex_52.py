from sys import exit
import random

def canoe_ride():
	print ""
	print "You regret having to do what you did, but there was little option. You shakenly untie the canoe and get in."
	print "As the your adrenaline lowers, so does the sun, and the sights of that god-awful prision fade from the horizion."
	print "You're unsure of which way to navigate, but you know you have to keep going even though your arms grow tired from rowing over the choppy waters."
	print "Time passes and the waters get rougher, he sky becomes dark and starts to rain. You become nervous as the winds pick up, but you keep rowing. You want nowhere near that prision, but you don't know if you'll ever forget that experience..."
	print "Suddenly, your boat capsizes and you are thrown into the briny deep. The current is too strong for you to ever see the surface again, and slowly everything fades to black..."
	cont = raw_input("Press ENTER to continue...")
	print "."
	cont = raw_input("Press ENTER to continue...")
	print ".."
	cont = raw_input("Press ENTER to continue...")
	print "..."
	print ""
	print "You open your eyes and yawn. You're in your room"
	print "You stretch and quietly observe your surroundings."
	print "You realize it's one of those days again..."
	print "------------------------------------"
	print "     Congratulations, you win!      "
	print "------------------------------------"
	exit(0)

def showdown():
	player_health = 10
	enemy_health = 15
		
	while player_health > 0:
		print "The old man swings at you."
		if random.randint(1,4) == 1:
			print "He connects and deals 1 damage."
			player_health = player_health - 1
		else:
			print "He misses."
		print "You only have one option: ATTACK."
		cont = raw_input("> ").lower()
		
		if "attack" in cont and random.randint(1,2) == 1:
			print "You land a hit and deal 3 damage!"
			enemy_health = enemy_health - 3
		else:
			print "You miss."
		print ""
		print "Your Health: %d" % player_health
		print "Enemy's Health: %d" % enemy_health
		print ""
	
		if player_health == 0:
			death("You can no longer manage to sustain the constant blows to the head, and you lose consciousness, never to wake again...")
	
		if enemy_health == 0:
			print "The old man can no longer manage to sustain your constant punches, and eventually falls to the ground, not breathing."
			cont = raw_input("Press ENTER to continue...")
			canoe_ride()
			
		

def freedom():
	print "You finally see a light coming from outside!"
	print "Your excitement grows as you get closer, and you can sense it from the old man as well."
	print "Breaking through the duct cover, the sun shines on your face as it once did, but you have no time to bask in the light, as you still have to get off this... tropical island??"
	print "The old man interupts your thoughts and explains to you there's winding path to the EAST. What do you do?"
	
	while True:
		cont = raw_input("> ").lower()
	
		if "east" in cont:
			print "As the old prisioner promised, there is a canoe to at the end of a rickity old dock. However you become confused as you realize this canoe can only fit one person."
			print "With an oar in one hand, the old man slowly turns around and says \"I'm sorry, but there's only 2 ways off this island, and I'm taking the canoe!\""
			cont = raw_input("Press ENTER to continue...")
			showdown()
		else:
			print "The old man says: \"There's no time for that!\""

def foreshadow():
	print ""
	print "The man sighs and starts to tell you a incredibly surreal story..."
	print "\"The Controller just conquored this land and built a new arena where people from different realms and realities were pitted against each other.\""
	print "\"Instead of killing us right then and there, the guards transported us to this arena to fight against others for our lives.\""
	print "\"There was 10 rounds, unlike today, I hear. My cellmate fought extravagantly, as did I. By the end of it, we were the only two left.\""
	print "\"The Controller didn't like the outcome, as he and the guards expected us to lose right away, so they matched us against eachother.\""
	print "\"You can guess what happened then...\""
	cont = raw_input("Press ENTER to continue.")
	print "You decide to ask no more."
	freedom()
	
def vent_crawl():
	print ""
	print "After gaining access to the ventilation room, your friend shuts the door behind you and proceeds to bust open a vent."
	print "He rushes you in, and as you start to crawl through, you swear you can feel the fresh air hit your sweaty face."
	print "Your fellow escapee follows you closely telling you which way to turn. Suddenly you start to wonder how, exactly, he knows the route of escape."
	print "Do you ASK him or KEEP GOING?"
	cont = raw_input("> ").lower()
	
	if "ask" in cont:
		print "He replies \"I tried escaping years ago, when this place was still fairly new. I would have made it out, if it wasn't for my coward cellmate...\""
		print "The fellow escapee suddenly goes quiet. Do you ASK him what happened or KEEP GOING?"
		contd = raw_input("> ").lower()
		if "ask" in contd:
			foreshadow()
		elif "keep" and "going" in contd:
			print ""
			print "You decide to leave him to his thoughts and continue your way through the duct system."
			freedom()
		else:
			print ""
			print "For some reason, your thoughts become unclear, so you decide to just keep quiet until you're out."
			freedom()
	elif "keep" and "going" in cont:
		print ""
		print "You decide maybe somethings are best left unsaid and you continue your way through the duct system."
		freedom()
	else:
		print "I don't understand..."
	
def escape_hatch():
	print ""
	print "Your new-found friend takes you to the bottom level and he quickly leads you around a maze of corridors to a locked ventilation access room."
	print "\"Quick, use your keycard!\" He instructs in a hushed, worried tone."
	print "You have only one option: USE CARD. What do you do?"
	cont = raw_input("> ").lower()
	
	if "use" and "card" in cont:
		print "You use the card, and gain access to the room."
		vent_crawl()
	else:
		death ("You could have used the card to gain access to the room but instead, you decide to fool around and you both are caught and beaten to a bloody pulp by 50 guards...")
		

def take_me():
	print ""
	print "You're about to leave the long hall, when the prisioner stops you."
	print "\"Hey!\" He cries. \"I know how to get out of here, take me with you!\""
	print "You talk with the old prisioner a bit and learn there's a secret path to a small canoe, but he only agrees to show you if you take him."
	print "You could choose to TAKE the prisioner, or LEAVE him and find the canoe yourself. What do you do?"
	
	while True:
		cont = raw_input("> ").lower()
		
		if "take" in cont:
			print ""
			print "After some careful thinking, you decide the old man is harmless and open his cell door. He thanks you graciously, but urges you to move on. So you both run to the elevator door."
			global prisioner
			prisioner = 0
			elevator()
		elif "leave" in cont:
			print ""
			print "After some careful thinking, you decide that this old man will only slow you, so you continue on your own. He cries out to you as you leave. You can't make it out but he says something about going up?"
			print "Who knows...."
			global prisioner
			prisioner = 1
			elevator() 
		else:
			print "Haha... what?"


def elevator():
	print "You've made it to the elevator with the guard's keycard in hand!"
	print "You call for it and get in."
	if prisioner == 0:
		print "Your new-found friend stops you before you press any of the buttons."
		print "\"Listen to me, you don't want to go up! There's more guards up there. I know a way out..."
		print "So you decide to let him lead you."
		escape_hatch()
	elif prisioner == 1:
		print "Now you have two options: go UP, or DOWN."
		cont = raw_input("> ").lower()
		
		if "up" in cont:
			death("You press the up button.\nHowever when the door opens, there is another 10 guards like the one you just defeated waiting for you. They instantaneously rush you and you have no chance of escaping their deadly thrashings...")
		elif "down" in cont:
			death("You press the down button.\nHowever when you get to the lower floor, you find no means of escape. Before you can make it back to the elevator, an alarm is sounded and you know what that means.\n Soon enough, you're surrounded by 10 guards like the one you just defeated. They instantaneously rush you and you have no chance of escaping their deadly thrashings...")
				

def leave_hall():
	checkGuard = False
	print ""
	print "Before the shadowy figure can pull out his weapon, you throw yourself at your enemy with the crowbar in your hands. It connects and drops the shadowy figure."
	print "You know what you have to do..."
	print "It's a bloody mess, but you've managed escape the wrath of your enemy by bashing his head in."
	print "From here you can SEARCH the guard, or you can go NORTH. What do you do?"
	
	while True:
		cont = raw_input("> ").lower()
		
		if cont == "north" or cont == "go north":
			if not checkGuard:
				print "Before you leave, something inside of you tells you to SEARCH the guard."
			else:
				take_me()
		elif cont == "search" or cont == "search guard":
			if not checkGuard:
				print "You search the shadowy figure, who doesn't seem so intimidating now that his head as been beaten in, and you find a keycard!"
				print "You can now go NORTH."
				checkGuard = True;
			else:
				print "You've already searched the guard. Time to move on."
		else:
			print "Haha.. what?"	

def long_hall_2():
	print ""
	print "Quickly dodging the punch of this insanely bulky character, you jump back into the sights of an old prisioner who realizes what's going on."
	print "\"Here, Take this!\" He calls out as he pass you a crowbar."
	print "You grab it, and suddenly the shadowy figure stops to pull out his baton."
	print "From here, you can ATTACK or FLEE. What do you do?"
	cont = raw_input("> ").lower()
		
	if "attack" in cont:
		leave_hall()
	else:
		death("You run, but the shadowy figure takes chase. You make it to an elevator door before you realize you need another key to open it. When the shadowy figure catches up to you, he hits you with his weapon before you can even make a move. Everything suddenly goes dark and the rest is unknown...")

def long_hall():
	print ""
	print "You've quietly snuck into what looks like a long hall for a prision block. The ceiling is rather high, compared to your cell and the room is made of some composite material you've never seen before."
	print "Suddenly the shadowy figure appears in front of you!"
	print "\"Hey! What are you doing out here?\" Suddenly he throws a fist at you."
	print "From here you can BLOCK or DODGE. What do you do?"
	cont = raw_input("> ").lower()
	
	if "dodge" in cont:
		long_hall_2() 
	else:
		death("Being the insanely bulky character this shadowy figure turned out to be, your %r does nothing against his powerful punch, and you go flying backwards. Unable to recover from the hefty hit, your enemy gets on top of you and beats you to a bloody pulp until your last breath escapes your punctured lungs...") % cont
	
def jailbreak():
	wire = 0
	key = False
	key2 = False
	print ""
	print "As the guard walked away, you notice he dropped something on the ground, which you now realize is a soft mud, so there was no way for the guard to hear it."
	print "From here, you have a few options. You can %s, %s, or %s. What do you do?" % ("EXAMINE your CHAINS", "LOOK at OBJECT", "do NOTHING")
	
	while True:
		cont = raw_input("> ").lower()
		
		if cont == "examine chains":
			if wire == 0:
				print "Although you can't move or see what's behind you, you start feeling the chains around your wrists."
				print "You can feel something sharp press against you... but you can't tell what it is. You might have to EXAMINE them again."
				wire = 1
			elif wire == 1:
				print "There's a thin peice of wire wrapped around these chains. I wonder if you could PULL on it..."
				wire = 2
			else:
				print "There's nothing else to examine here."
		elif cont == "pull wire":
			if wire == 0 or wire == 1:
				print "How do you know there's a wire? Maybe you should EXAMINE your CHAINS first..."
			elif wire == 2:
				print "By contorting your hands around in different awkward positions, you manage to pull the wire from your chains!"
				print "You now have a 5-foot wire. You can probably USE the wire somehow."
				wire = 3
			else:
				print "Already have the wire"
		elif cont == "look at object" or cont == "look object":
			if not key:
				print "Upon closer inspection, you realize that big brute of a shadowy figure dropped a key!"
				print "Now how are you going to get that key??"
				key2 = True
			elif key:
				print "You now have the key in your hand. What are you going to do with it??"
			else:
				print "I don't know what you're talking about..."
		elif cont == "use wire" or cont == "use wire with key":
			if wire == 3 and key2:
				print "Miraculously, you manage to bend the wire into a hook and reach for the key the shadowy figure dropped!"
				print "You now have the key! You can now UNLOCK yourSELF."
				key = True
			elif wire == 3 and not key2:
				print "With what??"
			elif wire == 1:
				print "You need to PULL the wire from its chains first..."
			else:
				print "What wire?"
		elif "unlock" and "self" in cont:
			if (key):
				print ""
				print "You are able to unlock yourself from your oppressive chains, and use the same key to unlock the cell door!"
				print "Wonderful!"
				long_hall()
			else:
				print "You need to somehow figure out how to do that."
		elif cont == "nothing" or cont == "do nothing":
			print "You should probably try something, lest you waste away in this hell-hole."
		elif "get" in cont:
			print "How are you going to get that?"
		else:
			print "You're going to have to be more specific..."
			
	
def questioned():
	print "\"So, you've finally come to, eh??\" The bulky figure asks with a deep rumbling growl."
	print "From here, you can PLEA for help, choose to get AGGRESSIVE, or say NOTHING."
	
	while True:
		cont = raw_input("> ").lower()
	
		if "nothing" in cont:
			print "In somewhat of a satisfied grunt, the bulky figure walks away saying \"A tough nut to crack, eh?? Maybe they could use someone like you..."
			jailbreak()
		else:
			print ""
			death("The bulky figure lets out a raucous laugh before walking away. Soon, the hours pass, as days to do... Soon starvation creeps in and you grow weaker. Each day your plea's for help becomes weaker, yet no one comes. Eventually you die from starvation...")		

def prision_cell():
	print ""
	print "You're in a dark, damp prision block! ...Or something of that sort."
	print "You can feel the coolness of the air, but something smells rotten in here too."
	print "Your arms in chained behind you and seem connected to the stone wall somehow."
	print "You are sitting, but feet are also chained to the ground. What do you do?"
	cont = raw_input("> ").lower()
	
	if cont or not cont:
		i = 0
		while i < 4:
			print "You struggle around for a bit, hoping to %r but even with all your might, you can't move. Eventually you give up." % cont
			print "What do you do?"
			cont = raw_input("> ").lower()
			i = i + 1
		
		print ""	
		print "Eventually, you hear footsteps and a shadowy, bulky figure stands in your door way..."
		questioned()
	else:
		death("I don't know what you did, but you've gone and messed this up!")
			

def front_door():
	print ""
	print "Skipping breakfast, and a shower, you make your way to your front door."
	print "Suddenly you stop on the threshold of the main entrance to your home."
	print "You sense a evil force lurking behind you, and you swear you can almost hear it breathe down your neck."
	print "From here, you can FIGHT the evil, or RUN from it. What do you do?"
	
	cont = raw_input("> ").lower()
	
	if "fight" in cont:
		print ""
		print "Before you can even lift your arm to throw a punch, the evil force engulfs your entire existence into a realm of darkness."
	elif "run" in cont:
		print ""
		print "Before you can even turn to reach the door knob, the evil force engulfs your entire existence into a realm of darkness."
	else:
		print ""
		print "Before you can even do that, the evil force engulfs your entire existence into a realm of darkness."
		
	print "You stare deep into the black abyss..."
	cont = raw_input("Press ENTER to continue...")
	print "."
	cont = raw_input("Press ENTER to continue...")
	print ".."
	cont = raw_input("Press ENTER to continue...")
	print "..."
	print ""
	print "You have a pounding headache, and your vision is blurry."
	print "Confused andscared you cry out to no one \"Where am I??\""
	print "\"Shaddup!\" Someone hollers from a distance. It echos to and from nowhere. You realize you can't move and you have no idea where you are."
	print "An hour passes (or so it seem) and your vision finally comes back."
	print "You finally become aware of where you are..."
	prision_cell()
		
		
def your_room():
	print "-----"
	print "It's 10am, and you're already an hour late for work."
	print "As you curse to yourself for not setting your alarm the previous night, you quickly grab your clothes and your baseball hat."
	print "From here, you can NORTH. What do you do?"
	
	cont = raw_input("> ").lower()
	
	if "north" in cont:
		front_door()
	else:
		print "You don't really have time for that. You're already an hour late for work."
		bedroom()


def intro():
	print "----------"
	print "You open your eyes and yawn. You're in your room"
	print "You stretch and quietly observe your surroundings."
	print "You realize it's one of those days again..."
	
	cont = raw_input("Press ENTER to continue")
	if cont == "fight":
		showdown()
	elif cont == "escape":
		escape_the_cell()
	else:
		print "------------------------------------"
		print "     Realms and Reality v0.1b       "
		print "------------------------------------"
		your_room()

def death(why):
	print why, "GAME OVER"
	exit(0)

intro()