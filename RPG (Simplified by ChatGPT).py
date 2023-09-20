import time

def print_with_delay(text, delay=0.08):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Intro
print("=====================================================")
print("=                     GAME START                    =")
print("=====================================================\n")
print_with_delay("You are currently free falling from the sky.")
print_with_delay("A huge noise echoed from the impact of your fall.")
print_with_delay("*You Fainted*")
print_with_delay(".\n..\n...")
print_with_delay("???: Finally awake. What's your name?")

# Character name
def get_character_name():
    while True:
        name = input("\nEnter Your Name: ")
        if len(name) < 1:
            print("\nPlease enter at least one letter")
        else:
            return name

name = get_character_name()
print_with_delay("\n(NPC): Greetings, " + name + ". My name is '(NPC)'.")
print_with_delay("You fell from a tall cliff but miraculously survived.")

# Check for injuries
print_with_delay("Your body seems to be okay, but are you hurt anywhere?")
response = ""
while response not in ["yes", "Yes", "y", "No", "no", "n"]:
    response = input("\n(Yes/No)\n"+ name +": ")
    if response in ["yes", "Yes", "y", "Y"]:
        print_with_delay("\n(NPC): Let me patch you up.")
    elif response in ["no", "No", "n", "N"]:
        print_with_delay("\n(NPC): You're a tough one!")
    else:
        print("\n*Invalid Answer*")

# Remembering home
home = ""
print_with_delay("Do you remember where you're from?")
response = ""
while response not in ["yes", "Yes", "y", "No", "no", "n"]:
    response = input("\n(Yes/No)\n" + name + ": ")
    if response in ["yes", "Yes", "y", "Y"]:
        print_with_delay("\n(NPC): That's great to hear!")
        print_with_delay("Where are you from?")
        def get_home_name():
            while True:
                home = input("\nEnter Location Name: ")
                if len(home) < 1:
                    print("\n*Please enter at least one letter*")
                else:
                    return home
            
        home = get_home_name()
        print_with_delay("\n(NPC): I'm not familiar with this place called " + home + ".")
    elif response in ["no", "No", "n", "N"]:
        print_with_delay("\n(NPC): Oh. That's too bad.")
    else:
        print("\n*Invalid Answer*")


print_with_delay("How about we head over to the nearest town to see if someone can help you?")

# Chapter 1
print("\n=====================================================")
print("=                     CHAPTER 1                     =")
print("=====================================================\n")
print_with_delay("*You and (NPC) started a journey to the nearest town*")
print_with_delay(".\n..\n...")
print_with_delay("(NPC): We've finally reached our destination!")
print_with_delay("Welcome to the town of '(startingtown_name)'!")
print_with_delay("Let's head over to the Adventurer's Guild. Maybe someone there can help.")
print_with_delay("\n*You and (NPC) entered the building and all eyes were glued on you*")
print_with_delay("\n" + name + ": Why is everyone looking at me?")
print_with_delay("\n(NPC): You are new here. Hence, people are shocked to see a new face.")
print_with_delay("You are also wearing weird clothes which are not commonly found in this town.")
print_with_delay("\n" + name + ": .....")
print_with_delay("\n(NPC): Anyways, let's go to the front desk and ask the receptionist for some information.")
print_with_delay(".\n..\n...")
print_with_delay("\n(guild_receptionist): Welcome to the Adventurer's Guild!")
print_with_delay("My name is '(guild_receptionist)'")
print_with_delay("Would you like to register your name to be a full-fledged adventurer?")
print_with_delay("\n(NPC): Actually, I want to ask some information for my friend here, " + name + ".")
print_with_delay("\n(guild_receptionist): Sure! I'd be more than happy to assist.")

# Player's questions
print_with_delay("So what would you like to know?")
response = ""
any_other_question_asked = False

while response not in ["D", "d"]:
    response = input("\na.) Where am I?\nb.) What is this place?\nc.) Who are you?\nd.) That would be all.\n" + name + ": ")
    if response in ["A", "a"]:
        print_with_delay("\n(guild_receptionist): You are currently in the town of (starting_town_name). Specifically in the Adventurer's Guild.")
        print_with_delay("People come here from various places in order to start an adventure or maybe just sightseeing.")
        print_with_delay("Normally we can distinguish which city they're from, but you look like someone from out of this world just like--.")
        print_with_delay("Oh. Sorry for being frank and rude.")
        print_with_delay("Do you have other questions?")
        any_other_question_asked = True
    elif response in ["B", "b"]:
        print_with_delay("\n(guild_receptionist): This is the Adventurer's Guild.")
        print_with_delay("This is where people come to get quests from clients who have special request which normal people don't have the capabilities to carry out or execute these tasks.")
        print_with_delay("By registering, you can take on these quests or freely adventure the lands.")
        print_with_delay("You can also get fame and prestige for every achievements you accomplish.")
        print_with_delay("Do you have other questions?")
        any_other_question_asked = True
    elif response in ["C", "c"]:
        print_with_delay("\n(guild_receptionist): *giggles*")
        print_with_delay("Again, my name is (guild_receptionist).")
        print_with_delay("I'm here to assist you by answering your questions or anything related to the guild.")
        print_with_delay("Do you have other questions?")
        any_other_question_asked = True
    elif response in ["D", "d"]:
        if any_other_question_asked:
            print_with_delay("\n(guild_receptionist): Okay, I'm glad we're all set!")
        else:
            print("\n*Ask a question first*")
            response = "" 
    else:
        print("\n*Invalid Answer*")

print_with_delay("If you have more questions, you are more than welcome to ask me.")
print_with_delay("Safe travels, Adventurer!")
print_with_delay(".\n..\n...")
print_with_delay("\n(NPC): Well, that's most of the answers we can get.")
print_with_delay("Since you are new to this place, follow me to my home and you can crash there for a couple of days.")
print_with_delay("I'll help you find more answers and information for your questions.")
print_with_delay("We can also discuss about your future agendas.")
print_with_delay("\n*You and (NPC) strode to the direction of (NPC)'s house unadorned*.")
print_with_delay(".\n..\n...")
print_with_delay("\n*Both of you arrived at the destination at dusk*")
print_with_delay("\n(NPC): Welcome to my humble abode!")
print_with_delay("Please make yourself at home.")
print_with_delay("\n" + name + ": Will do. Thanks.")
print_with_delay("\n*You glanced around his home and discover that (NPC) was a former adventurer*")
print_with_delay("\n" + name + ": Hey, (NPC). Did you use to be a member of the Adventurer's Guild?")
print_with_delay("\n(NPC): Ah. I see you found the articles about my previous journeys.")
print_with_delay("I used to be a young adventurer who was wholeheartedly ready to explore the vast world.")
print_with_delay("Until that tragedy striked upon our world...")
print_with_delay("\n" + name + ": .....")
print_with_delay("\n(NPC): Never mind that! How about you? Do you atleast remember what you were doing before you fell of that cliff?")
print_with_delay("\n*You tried to recall your memories but nothing seems to come up*")
print_with_delay("\n" + name + ": I don't think I remember anything about what I was doing there.")
print_with_delay("My mind seems to be in a daze.")
if home:
    print_with_delay("All I remember is I'm from "+ home +".")
print_with_delay("\n(NPC): That's okay. Again I'm here to help you find answers.")
print_with_delay("\n" + name + ": Thanks for all the help, (NPC).")
print_with_delay("\n(NPC): Don't mention it kid!")
print_with_delay("\n*Your stomach suddenly lets out a loud growl*")
print_with_delay("\n" + name + ": Ohhh... That was very embarassing.")
print_with_delay("\n(NPC): *laughs histerically*")
print_with_delay("It seems you've been hungry from all of the trekking and asking questions.")
print_with_delay("Now let me just prepare our dinner so that we can fill our empty stomachs.")
print_with_delay("\n*You and (NPC) had dinner moments later and were stuffed with the delicious meal*")
print_with_delay("\n(NPC): Did you enjoy the meal?")
response = ""
while response not in ["yes", "Yes", "y", "No", "no", "n"]:
    response = input("\n(Yes/No)\n"+ name +": ")
    if response in ["yes", "Yes", "y", "Y"]:
        print_with_delay("\n(NPC): I'm glad you liked it.")
    elif response in ["no", "No", "n", "N"]:
        print_with_delay("\n(NPC): Oh. My bad. I'll do better next time.")
    else:
        print("\n*Invalid Answer*")

print_with_delay("You're quite an honest kid, " + name + ".")
print_with_delay("Honesty. It's a timeless virtue that illuminates the path of trust and fosters genuine connections.")
print_with_delay("Be sure to always stay true to your feelings.")
print_with_delay("\n" + name + ": Thank you, (NPC).")
print_with_delay("\n(NPC): Now let's go to sleep.")
print_with_delay("I need to wake up early in the morning to do my morning tasks.")
print_with_delay("You can also try to explore the town incase something piques your interest.")
print_with_delay("Sweet dreams, kid.")
print_with_delay("\n" + name + ": You too.")
print_with_delay("\n*You fell asleep seconds later*")
print_with_delay(".\n..\n...\n....\n.....")
print_with_delay("\n(NPC): Rise and shine, " + name + "!")
print_with_delay("\n" + name + ": *yawn*")
print_with_delay("Good morning, (NPC).")
print_with_delay("\n(NPC): Seems like you slept wonderfully.")
print_with_delay("I'll be leaving in a bit to do my tasks.")
print_with_delay("Feel free to eat the breakfast I prepared.")
print_with_delay("Don't cause any troubles in town once you go out.")
print_with_delay("\n" + name + ": I understand.")
print_with_delay("\n(NPC): Well, see you soon!")
print_with_delay("\n*(NPC) left and you ate breakfast*")
print_with_delay("\n" + name + ": I still can't remember anything well.")
print_with_delay("Maybe i'll try to explore the town as (NPC) has recommended me to do.")
print_with_delay("I guess ill head to the town's plaza first to find out which places I can visit.")
print_with_delay("\n*You went out and walked through the town*")
print_with_delay(".\n..\n...")
print_with_delay("\n" + name + ": Seems like there's a couple of places I can visit.")
print_with_delay("Where should I go to first?")
# | a. Adventurers Guild | b. Swords and spells workshop | c. Lake |d. Park by the hill | 

# To be continued  
quit()
# *notes* 
# For dot lines try to define it as functions (sc: Prince Magno)
# Check "Program notes.py" to improve program function
# chapter 1: make npc die and make cryptic/glitch text
# text for npc death:
# print("γ̵̰͇̝̹̦́́͛̃͝Ỏ̴̗͓͕̱͖͛̾̆͝υ̶̘̭̳̱̇̈́̇͜͠͝ ̷͎̜̼̈́̑̒͒͊͜͜ƨ̵̻̘̭̳̏̂̏̒͛ͅʜ̷̡͖̲̟͉̓̓͑͘͝O̴̧͈̦̿͐̃͌͆͜ͅυ̴̦͕̘͉̤͊̒̿̔͝ļ̴͎͉̰̄͒̔̎̑͜b̵̡͍͓̯̥͐͌́̀̆'̶̨̛̠̫̝̰̓̈́͛͝v̷̧͔̭̪̋̿͒͆̕ͅƎ̴͔͎̝͚̟͗̓̎͆͒ ̸̧͖̹͓͙̓̍̈́͋͑b̵̡͇̘̩̳̔̾͌̅̚Ḯ̴̫̭̝̼̟̃̔͘̕Ǝ̶̠̰͎̭̰̾̓̐̚͠b̶̡͚̹̅͂́̉͒͜ͅ ̵̡͓͇̤͚̏̾̋͘̕i̶̡̢͈͈̮̔͋͑̐͝И̵̢̩̤̥̩̋̏͋́̈ƨ̷̨̨̺̲̼̈̒̔̑̊Ɉ̵̛̟̙̮̺̘̽͐̾̈ǝ̷̬͙̫̱̘̐̃̒̈́͑À̶̧̡̖̬̰̽̊̾͠b̸̜͈̪͍͇̔́͗͊͐.̶̯͖̲̫͕̒̑̇̈́̚")
# print("ǐ̵̡̩̟̙̝͑̓͂̈́T̵͉̠͉̝̗̈́̽̀̚͝ƨ̴̡͍̟͓̱̐̓́̈́̒ ̷̦̯̰̲̝̃̍̾̽͝ɒ̷͚͕͙̹̱͛͆̄̚̕⅃̷̰̖͚͎̗̈͌̀͗̉ļ̶̮̺͚͕́̾̉͑̓ ̸̖̯͎̟̭̓̂͛͌́γ̸̡̠̩͚̬̾̓̃̅͝O̸̠̫̪̲͐̈̐͆͗͜Ų̴̦̭̠̭̿͗͗̏̈́ɿ̴̢̛̙̘̞͕̅̓͊͘ǝ̷̲̬͓̖̄͂̈́̈́͘ͅ ̷̛̲͙͇̩̻̇̅̓͐ʇ̵̢̤͖̱̪̇̌͒̚͘A̵̢͍̹̺͔̓̀͌͋́ὐ̴̠̳̣̙̬̓̎̋̕l̸̢̨͕̤̔̀͆̓̎ͅṬ̶̦͔͇̜̑͗̂͌̇.̴͚͚͓̬͕͌̉̿̈́̚")
# print("Y̵̠̦͖͎̳̅̽̓̇͝ở̸͖̬̰͖̾̄̚ͅṴ̶̺͇̱̊̊̀̂̃͜ ̶̗͚̜̤̙͒͐̅͘͝ɒ̷͖̦̱͇̃͛̈́̈́͝ͅɿ̴̫̱̫̤̬̈́͌̈́͑̃Ǝ̷̨̡̲̗͖͆̀͗͐͝ ̷̢̬̯̰̱̈́͆̚͝͠n̶͕̞̲̘͇͑̏͐̚͘O̸̡̘̞̣͛̏̍̉͘͜Ɉ̶̛̟̱͖̭̯̀͑̚͠ ̴̨̡̻̳̜̋̄͊͋́ɿ̵̢̦̩͚͇͑̍͆͋̊Ǝ̷̝̻͉̃̏͒̈́̔͜ͅA̶̺̮̤̫̝̒̂̒̉̑⅃̷̭͚̙̖̬̏̇̊̂͝!̶̥͙͕̤̺͒̒͑̀̅!̴͎̝̭̖̭͐̏̔̋̈́!̶͖͉̰͓͇́̉̈́̿̏")