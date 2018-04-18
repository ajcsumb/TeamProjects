####################################################################################################################
# CST-205		Final Project: Final Adventure Game
# Luis Corea, Dominique Babaian, Christian Gutierrez, Alfred De La Costa, Gabriel Quan Juarez
# 4/17/2018
####################################################################################################################

####################################################################################################################
# Strategy Adevnture Game Details:
#		Title: Pugs, Corgis, and Dragons, a dog's tale.
#		Plot: The player is a dog knight of the order of Pugs who has been requested by the League of Divine Pug Masters
#		      to investigate a cavern that has been said to be occupied by a rentless man eating dragon. The player
#		      must nagivate through the chambers of this cavern to determine where the Dragon is and then the player
#		      has to make the decision of what to do when meeting the dragon. Does the player try to slay the dragon,
#		      reason with the dragon, or do something else?
#		Main Characters: Pug Knight (Player), dragon (boss)...
#		Features: 7 explorable areas, NPC's, items, and a final battle
#		Explorable Areas:	The Cavern Entrance, The Howler Room (west of entrance), Room of Bones (east of entrance), 
#                                        The Whisker Lounge (north of entrance), Dragon's Chamber (north of whisker lounge),
#				Szechuan Sauce Kitchen (east of whisker lounge), The Lair of the Cats (west of whisker lounge), and a secret room.
#
#		Goal of Final:Construct each room and nagivation. Print a description of the room. Give the user directions of
#			   where they are allowed to move next, and ask the user where they would like to go. Added in audio
#                                 and visuals to convey fantasy. Implement "item in inventory" feature.
#
#		OOP Methodolgy:
#			Main function: Will initiate the start of the game, the end of the game, and call the functions to keep it running.
#			BuildWorld(): This will build the map, add the NPC's, and add the items to the rooms.
#			BuildNPCs(): This will build all of the NPC's and their traits.
#			BuildItems(): Build all of the items and their traits.
#			BuildRoom(): Build all of the rooms and their descriptions.
#			Navigation(): Use user input to determine where the user is going to go next.
#                             
####################################################################################################################

#Global variables
maxRooms = 8
tries = 2
inv = [] #To fill item inventory
npcs = [] #To fill the list of NPCs, keeps track of NPCs visited

###########################################################################################################

#MediaPath: Call this function to set the media path for images and sound files:
def setPath():
  setMediaPath()

################################
#      Sounds Functions	#
################################

#Plays a door opening sound
def doorOpenSnd():
  sound = makeSound("door-open.wav")
  return (sound)
  
#Plays a door closing sound
def doorCloseSnd():
  sound = makeSound("door-close.wav")
  return (sound)
  
#Plays a walking sound
def walkingSnd():
  sound = makeSound("walking.wav")
  return (sound)

#Plays a sound when player gets an item
def itemSnd():
  sound = makeSound("item.wav")
  return (sound)
  
#Plays the battle music
def battleSnd():
  sound = makeSound("battle.wav")
  return sound

#Plays the boss-battle sound
def bossBattleSnd():
  sound = makeSound("boss-battle.wav")
  return sound

#Plays background music
def backgroundSnd():
  sound = makeSound("background.wav")
  return sound

#Plays game over sound
def gameOverSnd():
  sound = makeSound("game-over.wav")
  return sound
  
#Plays win sound
def winSnd():
  sound = makeSound("win.wav")
  return sound

#Plays dragon encounter sound
def dragonEncounterSnd():
  sound = makeSound("dragon-encounter.wav")
  return sound
  
#musicPlayer class
class musicPlayer():
  #Attributes:
  
  #Sound - Holds the sound file, we are playing or stopping. Gets initialized and assigned in start.
  
  #Methods
  #start(soundFile)
  def start(self, soundFile):
    self.sound = soundFile
    play(self.sound)
    
  def blockingStart(self, soundFile):
    self.blockSound = soundFile
    blockingPlay(self.blockSound)
    
  #stop (soundFile)
  def stop(self):
    stopPlaying(self.sound)
    
  def stopBGSnd(self, soundFile):
    self.stopSound = soundFile
    stopPlaying(self.stopSound)
    
  def stopItemSnd(self, soundFile):
    self.stopsound = soundFile
    stopPlaying(self.stopsound)

player = musicPlayer() 
##################################################################################################################################
#  Edits green screen photos #
##############################
def chromaKeyGreen(source, background, background2):
  for x in range(0, getWidth(source)): #loops through the original image
    for y in range(0,getHeight(source)):
      OG_pixel_color = getColor(getPixel(source, x, y))
      if distance(OG_pixel_color, green) < 200.0: #checks for the distance between the current pixel and predefined color green
        OG_pixel = getPixel(source, x, y)
        BG_pixel_color = getColor(getPixel(background, x, y)) #grabs pixel color at x and y from bg image
        setColor(OG_pixel, BG_pixel_color) #sets the corresponding bg pixel color to the original image's same pixel location
  for x in range(0, getWidth(source)): #loops through the original image
    for y in range(0, getHeight(source)):
      OG_pixel_color = getColor(getPixel(source, x, y))
      if distance(OG_pixel_color, green) < 200.0: #checks for the distance between the current pixel and predefined color green
        OG_pixel = getPixel(source, x, y)
        BG_pixel_color = getColor(getPixel(background2, x, y)) #grabs pixel color at x and y from bg image
        setColor(OG_pixel, BG_pixel_color) #sets the corresponding bg pixel color to the original image's same pixel location
  repaint(source)
  return source
#######################################################################################################################################  

#Buildroom(): Builds all the rooms and places descriptions in each one
def buildRoom(num):
  #Build the entrance and return it.
      #All rooms will have the following format:
      #	Title
      #	Description
  player.blockingStart(walkingSnd())
  player.blockingStart(doorOpenSnd())
  
  if num == 0:
    entrance = """\n\t\tThe Cavern Entrance
         \tThe beginning of the dog's perilous tale.
         \tGood to see you young padawan. Which path will you choose to to claim victory and fulfill your destiny? 
         \tTake your time, don't miss a thing. You may proceed to the West, East, or continue North. 
         \tWhich direction shall you choose?"""
    print entrance
  	
  elif num == 1:
  #NE
    howlerRoom = """\n\t\tThe Howler Room
         \tYou can hear howling coming from the room, as you walk in, it gets lounder and louder!
         \tIt's now at the point where you are barely able to widthstand it. As you try to cover your ears,
         \tYou look to the right you see a baby wolf crying in the corner of the room...
         \tYou see no path available to continue down but a door to the north and east.\n"""
    print howlerRoom
    
  elif num == 2:
  #NW
    roomOfBones = '''\n\t\tThe Bone Room
          \tSkeletons litter the room and a grinding noise comes from beneath your feet as you step onto the bones. 
          \tTo the left you see a throne of bones with a skeleton sitting in it.
          \tThere is a door to the nNorth or fall back to the entrance in the west.\n'''
    print roomOfBones
    
  elif num == 3:
   	#NESW
    CatnipLounge = '''\n\t\tThe Whisker Lounge
   \tYou continue walking down and past through a door. 
   \tThere are remnants of what appear to be sofas in the room and the smell of danger fills the room.
   \tAn ominous feeling begins to build within as the surrounding doors loom over you.\n'''
    print CatnipLounge
  elif num == 4:
   	#SE,W is hidden
   CatsLair = '''\n\t\tThe Lair of the Cats
   \tYou walked into a lair. You see portraits decorating the wall. 
   \tA state of a once prominent feline sits on the wall in front of a bookcase. 
   \tThere is a door to the south and to the east.\n'''
   print CatsLair
      
  elif num == 5:
   	#SW
   CheeseBurgerRoom = '''\n\t\tSzechuan Sauce Kitchen
   \tYou enter the room and the smell of cheeseburgers plagues your nostrils.
   \tThis must have been the kitchen at a time before the dragon had come here.
   \tYou spot a door to the south and to the west.\n'''
   print CheeseBurgerRoom
  elif num == 6:
   #S
   DragonsChamber = '''\n\t\tThe Dragon's Chamber
   \tYou have entered the chamber. The door shuts behind you, as the torches light the room.
   \tA Dragon sits in the corner of the room eyeing you. It's now or never...\n'''
   print DragonsChamber
  else:
      #E
    Secret = '''\n\t\tThe Secret Room
   \tAs you enter the room you come across five weary scholars. 
   \tWhat could they possibly have to offer?\n'''
    print Secret
  player.blockingStart(doorCloseSnd())
#Input check for User's choice to move
#Pass in the room number and returns a direction the user choose
def IOCheck(room, name):
	##Acceptable inputs for rooms
  acceptedControls = """\tAccepted Controls: n for North, e for East, s for South, w for West, 
  		  \tu to use an item, c to see the controls, exit to quit the game"""
  #allControls = ["n", "e", "w", "s", "u", "c" "exit"]
  allDirections = ["n", "e", "s", "w"]
  
  ent =    ["n", "e", "w"]
  howl =   ["n", "e"]
  bone =   ["n", "w"]
  catnip = ["n", "e", "s", "w"]
  lair =   ["e", "s", "w"]
  cheese = ["s", "w"]
  dragon = ["s"]
  secret = ["e"]
  
  seeControls = ["c"]
  useItem = ["u"] #alternate input
	##Check which room we use
  if room == 0:
    inputCheck = ent
    altCheck = useItem
  elif room == 1:
    inputCheck = howl
    altCheck = useItem
  elif room == 2:
    inputCheck = bone
    altCheck = useItem
  elif room == 3:
    inputCheck = catnip
    altCheck = useItem
  elif room == 4:
    inputCheck = lair
    altCheck = useItem
  elif room == 5:
    inputCheck = cheese
    altCheck = useItem
  elif room == 6:
    inputCheck = dragon
    altCheck = useItem
  else:
    inputCheck = secret
    altCheck = useItem
  

  ##Checks User Input for correct Input
  direction = requestString("Please enter a direction or action you wish to commence in.")
  direction = direction.lower()
  #If the user entered exit return false
  if direction == "exit":
    #TODO: We might change this later.
    showInformation("We're sad to see you go so soon, %s. We hope you enjoyed playing Pugs, Corgis, and Dragons: A Dog's Tale!" % name)
    player.stop()
    sys.exit()
  elif direction in altCheck:
    itemDependency(inv, room, tries, name)
  elif direction in seeControls:
    showInformation(acceptedControls)
    IOCheck(room, name)
  ##Checks to make sure it is an acceptable direction
  #First If set does directional check
  #Nested If checks for direction acceptable for the room
  #nested Else then asks for repeated input if not acceptable
  while len(direction) != 1 or direction.isalpha() == False or direction not in allDirections:
    direction = requestString("Please enter a valid key.")
  while direction in allDirections:
    if direction == allDirections[0]: #N
      if direction in inputCheck:
        return direction
      else:
        direction = requestString("Please enter which direction you wish to take as you cannot go north from this room.")
        while direction not in allDirections:
        	direction = requestString("Please enter which direction you wish to take as you cannot go nNorth from this room.")
    elif direction == allDirections[1]: #E
      if direction in inputCheck:
        return direction
      else:
        direction = requestString("Please enter which direction you wish to take as you cannot go east from this room.")
        while direction not in allDirections:
          direction = requestString("Please enter which direction you wish to take as you cannot go east from this room.")
    elif direction == allDirections[2]: #S
      if direction in inputCheck:
        return direction
      else:
        direction = requestString("Please enter which direction you wish to take as you cannot go south from this room.")
        while direction not in allDirections:
          direction = requestString("Please enter which direction you wish to take as you cannot go south from this room.")
    else:
      if direction in inputCheck:
      	return direction
      else:                             #W
        direction = requestString("Please enter which direction you wish to take as you cannot go west from this room.")
        while (direction not in allDirections):
          direction = requestString("Please enter which direction you wish to take as you cannot go west from this room.")
  
#Navigation(userInput, room) - Gabriel:
def navigation(room, name):
  #Get userInput into local variable to manipulate it.
  if room == 6: #Dragon's Chamber
  #Battle function
    player.stop()
    player.stopBGSnd(backgroundSnd())
    player.blockingStart(dragonEncounterSnd())
    chromaKeyGreen(makePicture("16 Fighting Pug.jpg"), makePicture("17 Dragon.jpg"), makePicture("2 Background.jpg"))
    showInformation("The dragon has spotted you. This is your crowning moment, %s! Prepare to fight!" % name)
    player.stop()
    player.start(bossBattleSnd())
    print "Item Inventory"
    print ", ".join(inv) #display inventory
    itemDependency(inv, room, tries, name)
    player.stop()
    sys.exit()
  direction = IOCheck(room, name)
  
  #To determine where the user can go.
  if room == 0: #user can only go left, right, and forward
    #If the user enters anything other than l, r, or f
    if direction == "n":
      return 3
    elif direction == "e":
      return 2
    elif direction == "w":
      return 1  
    
  elif room == 1: #user can only go forward and back
    if direction == "n":
      return 4
    elif direction == "e":
      return 0

  elif room == 2: #user can only go forward and back
    if direction == "n":
      return 5
    elif direction == "w":
      return 0

  elif room == 3: #user can go any direction
    if direction == "n":
      return 6
    elif direction == "e":
      return 5
    elif direction == "s":
      return 0
    elif direction == "w":
      return 4  
      
  elif room == 4: #user can only go back and right
    if direction == "e":
      return 3
    elif direction == "s":
      return 1

  elif room == 5: #user can only go left
    if direction == "s":
      return 2
    elif direction == "w":
      return 3

  elif room == 6: #user can only go back
    if direction == "s":
      return 3
  else:
    if direction == "e":
      return 4
      
#NPC supporting functions
def npcRecord(record, npc):
  while npc not in record:
    record.append(npc)
  return record

def dialogue(num):
  yesOrNo = ["yes", "no"]
  dialogue = requestString("Do you wish to speak to the NPC or has a cat got your tongue? Yes or no?")
  dialogue = dialogue.lower()
  while dialogue not in yesOrNo or dialogue not in yesOrNo:
    dialogue = requestString("Do you wish to speak to the NPC or has a cat got your tongue? Yes or no?")
    dialogue = dialogue.lower()
  if dialogue == yesOrNo[0]: #if yes
    buildNPC(num)
  else: #if no
    return

#Main buildNPC() function    
def buildNPC(num):
  if num == 0:
    return
  elif num == 1:
    chromaKeyGreen(makePicture("6 Pug.jpg"), makePicture("10 Enemy1.jpg"), makePicture("2 Background.jpg"))
    room1NPC = """Hello, my name is Warwick. I am far too full to finish this bacon I have leftover. 
Here, you can have the delicious strip but in exchange you must go clean up the mess I left after my meal. You'll know its my leftovers when you can smell the fish-rat souffle. Thanks!"""
    npcRecord(npcs, "warwick")
    showInformation(room1NPC)
    checkItems(num, inv)
  elif num == 2: 
    chromaKeyGreen(makePicture("6 Pug.jpg"), makePicture("11 Enemy2.jpg"), makePicture("2 Background.jpg"))
    room2NPC = """Purrfect. You arrived just in time as I hunted this rat. 
Unfortunately, it is infected with the plague and I already used up eight of my lives. 
Be a good dog and dispose of it and you can have the precious jewel that adorns my domain."""
    npcRecord(npcs, "garfield")
    showInformation(room2NPC)
    checkItems(num, inv)
  elif num == 3:
    chromaKeyGreen(makePicture("6 Pug.jpg"), makePicture("12 Enemy3.jpg"), makePicture("2 Background.jpg"))
    room3NPC = """Yikes! You caught me, the one and only Hamburglar. 
I was trying to eat the cat's fish filets since the Szechuan Sauce Kitchen is full with junk.
If you can clean it, I don't have to resort to stealing anymore. 
I'll even make you a deal by letting you keep what you find!"""
    npcRecord(npcs, "hamburglar")
    showInformation(room3NPC)
    checkItems(num, inv)
  elif num == 4:
    chromaKeyGreen(makePicture("6 Pug.jpg"), makePicture("6 Pug.jpg"), makePicture("2 Background.jpg"))
    showInformation("Looks like there's no one here to talk to.")
  elif num == 5:
    chromaKeyGreen(makePicture("6 Pug.jpg"), makePicture("22 Enemy 5.jpg"), makePicture("2 Background.jpg"))
    room5NPC = """Gosh darnit, that Hamburglar... Did he scam you into doing his chores? 
I'm sorry for the terrible customer service you must be having. 
Let me make it up to you. When you've been in the burger industry as long as I've been, you know a thing or two.
There's a special toy if you figure out the secret of the empty happy meal box!"""
    npcRecord(npcs, "ronald")
    showInformation(room5NPC)
    checkItems(num, inv)
  elif num == 6:
    return
  else:
    chromaKeyGreen(makePicture("6 Pug.jpg"), makePicture("13 Enemy4.jpg"), makePicture("2 Background.jpg"))
    room7NPC = """Congratulations! Welcome to Team Architech's secret room. This is a realm in between reality and dreams. 
If you made it this far, kudos to you for supporting a small indie company such as ourselves. 
We're rooting for you every step of the way!"""
    npcRecord(npcs, "sandman")
    showInformation(room7NPC)
    checkItems(num, inv)
    
#Item supporting functions
#Appends item to global list
def itemInventory(inventory, item):
  while item not in inventory:
    inventory.append(item)
  return inventory

#Main buildItems() function
def buildItems(roomNum):
  
  #Initializing all items to empty strings
  bacon = ""
  deadRat = ""
  fishBones = ""
  fireJewel = ""
  mightyMuzzle = ""
  iceSpear = ""
  emptyRoom = ""
  
  player.blockingStart(itemSnd())
  #player.stopItemSnd(itemSnd())
  if roomNum == 0:
    print "There are no items in this room."
  elif roomNum == 1: #howlerRoom
    bacon = """You found some bacon! Looks like this could be used to compliment a meal.
Item added to your inventory."""
    #Add the item to the inventory list
    itemInventory(inv, "bacon")
    showInformation(bacon)
  elif roomNum == 2: #roomOfBones. Find two items in a box.
    DRandFB = """You found two items! A dead rat and some fish bones.
Items added to your inventory."""
    #Add the items to the inventory list
    itemInventory(inv, "dead rat")
    itemInventory(inv, "fish bones")
    showInformation(DRandFB)
  elif roomNum == 3: #Cat's Lounge
    fireJewel = """You found the Fire Jewel! This legendary gem is said to possess supernatural powers. Its beauty radiates and cultivates attention from all those who stare into it.
Item added to your inventory."""
    #Add the items to the inventory list
    itemInventory(inv, "fire jewel")
    showInformation(fireJewel)
  elif roomNum == 4: #Cat's Lair
    emptyRoom = "It doesn't look like there are any useful items here."
    print emptyRoom
  elif roomNum == 5: #CheeseBurgerRoom
    #Get the Ice Spear. Used to kill the dragon and win the game 
    iceSpear = """Looks like you found the Ice Spear! The Ice Spear is the ultimate weapon to use against an enemy. When used correctly, you will be able to effortlessly slay any dragon.
Item added to your inventory."""
    #Add the items to the inventory list
    itemInventory(inv, "ice spear")
    showInformation(iceSpear)
  elif roomNum == 6: #Dragon's Chamber
    emptyRoom = """\t\tAlthough there are some pretty cool artifacts in here, you wouldn't want to
                take anything away from the dragon."""
    print emptyRoom
  elif roomNum == 7: #Architech's secret room
    emptyRoom = "This is a neat room, but it doesn't look like there are any useful items here."
    print emptyRoom
  
#Battle function
def itemDependency(inventory, room, tries, name): #Pass the inventory list to this function
  iceSpear = "ice spear"
  if room == 6:
    if len(inventory) == 0: #If nothing in inventory, user loses game
      chromaKeyGreen(makePicture("7 Dead Pug.jpg"), makePicture("17 Dragon.jpg"), makePicture("2 Background.jpg"))
      player.stop()
      player.start(gameOverSnd())
      showInformation("""Oh, no. Unfortunately, you met the dragon with no items at your disposal. You tried to run but couldn't make it out in time.
Looks like the dragon will be having Pup Soup for dinner! Better luck next time. Game over.""")
      player.stop()
      sys.exit()
    userInput = requestString("Which item would you like to use?")
    userInput = userInput.lower()
    if userInput not in inventory:
      if userInput == "exit": #If input is "exit", quit program
        showInformation("We're sad to see you go so soon, %s. We hope you enjoyed playing Pugs, Corgis, and Dragons: A Dog's Tale!" % name)
        player.stop()
        sys.exit()
      while userInput not in inventory:
        showInformation("This item is not in your inventory. Please enter a valid item.")
        itemDependency(inventory, room, tries, name)
    elif userInput in inventory:
      while userInput != iceSpear and tries > 0: #User has three tries to win
          showInformation("The item had no effect! Try using another item. You have " + str(tries) + " tries remaining. Use them wisely.")
          tries -= 1 #Declared globally, decreases by one each try
          itemDependency(inventory, room, tries, name)
      if userInput == iceSpear: #win condition
        chromaKeyGreen(makePicture("6 Pug.jpg"), makePicture("14 Dead Enemy.jpg"), makePicture("2 Background.jpg"))
        player.stop()
        player.start(winSnd())
        showInformation("You have used the Ice Spear! The dragon is at your mercy and you have saved the nation. Congratulations, %s!" % name)
        player.stop()
        sys.exit()
      else:  #lose condition
        chromaKeyGreen(makePicture("7 Dead Pug.jpg"), makePicture("17 Dragon.jpg"), makePicture("2 Background.jpg"))
        player.stop()
        player.start(gameOverSnd())
        showInformation("Oh no! The dragon has taken you captive! You have failed your mission. Better luck next time, %s. Game over." % name)
        player.stop()
        sys.exit()
  else: #If user inputs "u" in any other room
    showInformation("You can't use an item in this room.")
    IOCheck(room, name)

def checkItems(num, inventory): #Checks to see if room has been visited
  
  sword = "sword"
  bacon = "bacon"
  DRandFB = "dead rat and fish bones"
  fireJewel = "fire jewel"
  iceSpear = "ice spear"
  
  if len(inventory) == 0:
    buildItems(num)
  elif len(inventory) > 0:
    if num == 0:
      checkItemsResult(num, sword, inventory)
    elif num == 1:
      checkItemsResult(num, bacon, inventory)
    elif num == 2:
      checkItemsResult(num, DRandFB, inventory)
    elif num == 3:
      checkItemsResult(num, fireJewel, inventory)
    elif num == 5:
      checkItemsResult(num, iceSpear, inventory)
      
def checkItemsResult(num, item, inventory): #Send resultant info to checkItems
  DRandFB = "dead rat and fish bones"
  if item == DRandFB:
      showInformation("Recall that you have already collected the %s from this room." % item)
  if item not in inventory and item != DRandFB:
    buildItems(num)
  elif item in inventory:
    showInformation("Recall that you have already collected the %s from this room." % item)
    




###############################################################################################################################################################
print "Please select a media path"
setPath()
player = musicPlayer()

#Main() - The main part of the program that runs the controls the programs flow
def main():
  player.start(backgroundSnd())
  #Header displayed in the console
  gameHeader = """\tPugs, Corgis, and Dragons: A Dog's Tale\n"""
  
  #Displayed in information dialog
  title = """Welcome to Pugs, Corgis, and Dragons: A Dog's Tale!
What is your desired character name?"""
  name = requestString(title)
  
  #Info dialog
  welcomeMessage = """\tGreetings, %s! Pugs, Corgis, and Dragons: A Dog's Tale is
A text-based adventure game about pugs, corgis, and well, you guessed it, dragons!
Don't worry about controls or anything like that. The game will help guide you.
If you type exit, you can quit the game...but hopefully you won't and you will finish it!
Thanks for playing!""" % name
  
  #Info dialog
  plot = """\tYou are a dog knight of the Order of the Pugs. You have been requested by the League of Divine Pug Masters.
  	\tYou are needed to investigate a cavern that is said to be guarded by a relentless dog-eating dragon! 
          \tYou must navigate your way through the cavern to determine how to defeat the dragon! 
          \tBeware! Not everything may appear as it seems! You will meet new characters along the way and obtain items to use in your quest. 
          \tPay close attention to how you talk to people, for they may show you things you can't see..."""
  
  #Main console
  controls = "\tControls: n (north), s (south), e (east), w (west), \n\tu (use item), c (view controls), exit to quit the game."
  
  #To keep track of the player location. Set to 0 to start.
  playerLocation = 0
  #Display the welcome message:
  
  chromaKeyGreen(makePicture("1 Welcome.jpg"), makePicture("1 Welcome.jpg"), makePicture("1 Welcome.jpg"))
  showInformation(welcomeMessage)
  #Display the plot:
  showInformation(plot)
  
  #Print the header and controls in console:
  print(gameHeader)
  print(controls)
  
  #Control the game
  #Print which room they are in:
  while True:
    if playerLocation == 0: 
      buildRoom(playerLocation)
      playerLocation = navigation(playerLocation, name)
    elif playerLocation == 6: 
      buildRoom(playerLocation)
      playerLocation = navigation(playerLocation, name)
    else:
     buildRoom(playerLocation)
     dialogue(playerLocation)
     playerLocation = navigation(playerLocation, name)

#Calling main to initiate game upon program load
main()

  