import random
import os
from scenes import *
from characters import *

# global variables
running_status = True
playing_status = False
battling = False
name = ""

# this x variable below is used to count on something later, especially when battling (i.e. turn count, limited heal count, etc)
x = 0

# in_wilderness is one kind to check whether random encounter loop should be performed or not
in_wilderness = False

# quick continue message / breakpoint on each sequence of text or story


# welcome game interface
def welcome():
	global name
	global playing_status
	print(f"Welcome!")
	print(f"Please input your stinky name!")
	foo = input()
	name = foo
	print(f"\nAlright, good luck {name}! Sorry, no chance to change your name or anything ;D\n")
	playing_status = True
	cont()
			
# respawn all enemies or update
def respawn_enemies():
	global enemies
	global x
	enemy1 = Character("Wolf", 14, 3)
	enemy2 = Character("Coyote", 15, 2)
	enemy3 = Character("Lion", 18, 4)
	enemy4 = Character("Hyena", 18, 2)
	enemy5 = Character("Cheetah", 16, 4)
	enemies = [enemy1, enemy2, enemy3, enemy4, enemy5]
	x = len(enemies) - 1
		
# battling phase, currently, attacks only
def battle(mc, target):
	global battling
	while battling == True:
		os.system("clear") # not a necessity. if things break, just comment this line
		print(f"Battle Begins!")
		mc.attacks(target)
		target.alive
		if target.alive == False:
			print(f"{target.name} is dead!")
			print(f"{mc.name} wins!")
			print(f"{mc.name}'s HP left : {mc.hp}")
			battling = False
			break
		target.attacks(mc)
		mc.alive
		if mc.alive == False:
			print(f"\nGame Over! {mc.name} died!")
			battling = False
			print(f"See you in your eternal nightmare!\n")
			quit()
		cont()
			
# normal random encounter
def encounter(mc, target):
	global running_status
	global playing_status
	global battling
	print(f"\nA wild {target.name} has been spotted!")
	while True:
		print(f"\n{mc.name} sees a wild {target.name} is standing still!")
		print(f"What are you going to do?")
		print(f"\n[1] Attack!\n[2] Run!\n[3] Heal Up")
		answer = input("\n")
		if answer == "1":
			battling = True
			break
		elif answer == "2":
			print(f"\n{name} decided to run away!")
			playing_status = False
			quit()
		elif answer == "3":
			print(f"\n{mc.name} has decided to heal up!")
			mc.heal(10)
			print(f"{mc.name} current HP is : {mc.hp}!\n")
			continue
		else:
			print(f"\n{mc.name} has comitted suicide")
			print("See you in your eternal nightmare!\n")
			running_status = False
			quit()
			

# main game loop event
while running_status == True:
	welcome()
	player = Character(name, 20, 4) #current basic stats on character creation
	respawn_enemies()
	scene1(player.name)
	foo = enemy1
	encounter1(player, foo)
	if player.alive == True: # this if-else statement is untested!
		scene1_over(player.name)
		while playing_status == True: # this while function is working for random encounter, and it is working perfectly
			respawn_enemies()
			y = random.randint(0,x)
			foo1 = enemies[y]
			encounter(player, foo1)
			battle(player, foo1)
	else:
		playing_status = False
		running_status = False
		quit()