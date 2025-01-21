import os
def cont():
	cont = input("press enter to continue.....")
	
def scene1(name): # pre-battle script
	print(f"\nBip bop!")
	print(f"System : \"A wild {name} has appeared!\"")
	print(f"System : \"Also, you are the only person who can see this system text :)\"\nHave Fun!\n")
	cont()
	print(f"\nYou find yourself lying on such comfy ground")
	print(f"You sweep your hands around as you try to wake up")
	print(f"But there are too many tiny sharp things, and that's hurt")
	print(f"In the next split second, you can feel that your back begins to stiff")
	print(f"{name} : \"....................\"\n")
	cont()
	print(f"\nYour intuition suddenly kicks in")
	print(f"Something is wrong and yet has to be found")
	print(f"So, you gently move your eyelid, attempting to open your eyes")
	print(f"And then finally...\n")
	cont()
	print(f"\n{name} : \"Ahh..\"")
	print(f"The bright sunlight meets your eyes as you awake")
	print(f"The breeze air around warms you as you breathe")
	print(f"In no time, unknown living trees already filled your vision corner")
	print(f"Except, they are not dense enough and let you peek out the shy sky above\n")
	cont()
	print(f"\nDespite those welcoming vibes that you got")
	print(f"You still feel somewhat awkwardly unfamiliar with your surrounding")
	print(f"Those big trunks that grows immensely tall..")
	print(f"Weird looking birds who loves to dance around its huge branch..")
	print(f"And below that, those grassy ground that now you're standing at")
	print(f"Well, except the ground and rocky soil beneath your feet, \nthings are truly different from any place that you ever know\n")
	cont()
	print(f"\n{name} : \"In the name of the most deadliest fart on this land..\"")
	print(f"{name} : \"I swear, I've never been in this place before!\"")
	print(f"Still standing on the same spot, you slowly turn your head \nand watch anything that got caught within your eyes very carefully")
	print(f"{name} : \"What is this place..?\"")
	print(f"{name} : \"How did I ended up here?\"")
	print(f"All and all. More and more questions stacking up inside your mind, yet none of them got answered\n")
	cont()
	print(f"\n{name} : \"This place does look like a deep forest, doesn't it..?\"")
	print(f"The wind still blows once in a while, bringing up such cozy humid but not enough to wet your skin")
	print(f"Somehow, your brain still working just fine as you attempt to pull out as many answers as you could")
	print(f"You lay down your arm, trying to touch the grass below")
	print(f"{name} : \"Hmm.. Feels like normal grass to me. But there's no grasshoper though... Just yet.\"")
	print(f"Those grass surely are not that thick and they aren't too tall neither")
	print(f"You try to shut your eyes, sharpen your ears. And start hearing such bizzare song from weird birds above")
	print(f"{name} : \"Nope, nope. Never heard that song before. I don't think its from Owl City..\"")
	print(f"{name} : \".....Nor Taylor Swift.\"\n")
	cont()
	print(f"\nAs you try to listen once more.. very carefully")
	print(f"Suddenly.....")
	print(f"??? : \"GRRAAAAAAWWWWL!\"")
	print(f"..................................")
	print(f"You hear a growling sound from distance")
	print(f"Caught in surprise, You open your eyes instantly")
	print(f"{name} : \"Huh? This one doesn't sound like a song at all..\"")
	print(f"The wind blows stronger than before, and it spreads such chilling touch along the way")
	print(f"Weird Birds : \"CRAAAAAAK! CRAAAAAK!\", the werid birds above are cracking, tries to fly away and scattered in panic")
	print(f"Your intuition ticks again, followed by your adrenaline")
	print(f"{name} : \"Uh-huh.. This doesn't sounds good..\"")
	print(f"Your fear starts to grow and so does your heartbeat..")
	print(f"??? : \"PURRRRRRRHHHH...\"")
	print(f"You hear another puring sound... and its closer")
	print(f"You can feel your blood pumping even faster, and now your feets are also trembling!\n")
	cont()
	
# battling phase, currently, attacks only
def battle1(mc, target):
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
			print(f"\nGame Over! {mc.name} died!\n")
			battling = False
			print(f"How unfortunate, eh?\n")
			quit()
		cont()

# battle scene1, main event 1 battle phase. A modified encounter function
def encounter1(mc, target):
	'''
	"Battle scene 1, main game event. Non-skippable, cannot run away nor abort. Healing only available for once."
	'''
	global running_status
	global playing_status
	global battling
	heal_count = 0
	print(f"\nA wild {target.name} has been spotted!")
	while True:
		print(f"\n{mc.name} sees a wild {target.name} is standing still!")
		print(f"What are you going to do?")
		print(f"\n[1] Attack!\n[2] Run!\n[3] Heal Up")
		answer = input("\n")
		if answer == "1":
			battling = True
			battle1(mc, target)
			if target.alive == False or mc.alive == False:
				break
		elif answer == "2":
			print(f"\n{name} decided to run away!")
			playing_status = False
			quit()
		elif answer == "3":
			if heal_count < 1:
				print(f"\n{mc.name} has decided to heal up!")
				mc.heal(10)
				print(f"{mc.name} current HP is : {mc.hp}!\n")
				heal_count += 1
				continue
			else:
				print(f"\nCannot heal anymore!")
				continue
		else:
			print(f"\n{mc.name} has comitted suicide")
			print("See you in your eternal nightmare!\n")
			running_status = False
			quit()



def scene1_over(name): # post battle script
	print(f"\nSystem :\"Congratulations! You just won your first battle!!\"")
	print(f"{name} : \"Yeah, thank you.. so much..\"")
	print(f"{name} : \"That was the best surprise present I have ever got\"")
	print(f"{name} : \"And I thought I will be eaten alive..\"")
	print(f"You finally defeated your fear and now you have also killed the wolf")
	print(f"Exhausted, you decided to lay down a bit. Trying to catch your breath\n")
	cont()
