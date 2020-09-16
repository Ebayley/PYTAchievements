
a = True
while a:

    def fifthChoice():
        c5 = input("Choose A or B.\n")
        if c4 == 'A':
            print("You don't run and you don't make it in time.\nYou're not allowed to enter the classroom.\n\nBAD ENDING...")
            a = False
        elif c4 == 'B':
            print("You run and you don't make it in time.\nBut you're only five minutes late. You're allowed to enter the classroom.\n\nDECENT ENDING...")
            a = False
        else:
            print('\n(Let op! het moeten hoofdletters zijn.\n)')
            fifthChoice() 
            
    def fourthChoice():
        c4 = input("Choose A or B.\n")
        if c4 == 'A':
            print("\nYou walk to school at a brisk pace. You get close to school, you realise you're not going to make it at this pace.\nA.You're not going to run, you won't make it anyway.\nB. You run, you might still make it!\n")
            fifthChoice()
        elif c4 == 'B':
            print("\nYou take the metro, but its late!\nYou arrive late and aren't allowed to enter the classroom, too bad!\n\nBAD ENDING...")
            a = False
        else:
            print('\n(Let op! het moeten hoofdletters zijn.\n)')
            fourthChoice() 
    
    def thirdChoice():
        c3 = input("Choose A or B.\n")
        if c3 == 'A':
            print("\nYou run and barely make it, you arrive at Amsterdam Sloterdijk in time to catch the bus.\nYou arrive at school on time.\nYou enter the classroom and are marked as present.\n\nGOOD ENDING!!!")
            a = False
        elif c3 == 'B':
            print("\nYou don't run and miss the train, you wait for the next train and arrive at Amsterdam Sloterdijk.\nYou missed the bus, you have to get to school a different way.\nA. Walk to school instead.\nB. Take the metro instead.\n")
            fourthChoice()
        else:
            print('\n(Let op! het moeten hoofdletters zijn.\n)')
            thirdChoice() 
    
    def secondChoice():
        c2 = input("Choose A or B.\n")
        if c2 == 'A':
            print("\nYou skip breakfast and run out of the house, you manage to catch the bus right on time.\nYou arrive at the station Haarlem in time. You also catch the right train.\nYou arrive at Amsterdam Sloterdijk in time to catch the bus and arrive at school on time.\nYou enter the classroom and are marked as present.\n\nGOOD ENDING!!!")
            a = False
        elif c2 == 'B':
            print("\nBreakfast is the most important meal of the day! You don't skip it and miss the bus.\nYou have to take the next bus and you arrive at the station late. If you run you might still catch the right train.\nA. Run to catch the train.\nB. Don't run. You can always take the metro instead of the bus when you arrive,\nor even walk instead.\n")
            thirdChoice()
        else:
            print('\n(Let op! het moeten hoofdletters zijn.\n)')
            secondChoice() 

    
    def firstChoice():
        c1 = input("Choose A or B.\n")
        if c1 == 'B':
            print("\nYou wake up on time, as a result you leave the house on time.\nYou catch the right bus.\nYou arrive at the station Haarlem in time. You also catch the right train.\nYou arrive at Amsterdam Sloterdijk in time to catch the bus and arrive at school on time.\nYou enter the classroom and are marked as present.\n\nGOOD ENDING!!!")
            a = False
        elif c1 == 'A':
            print("\nYou sleep in, by the time you wake up you're almost late.\n")
            print("A. Skip breakfast to safe time.\nB. Don't skip breakfast.\n")
            secondChoice()
        else: 
            print('\n(Let op! het moeten hoofdletters zijn.\n)')
            firstChoice()

    print("Hello you! let's play a game of choices.\n")
    print("You have to get to school, your route is as follows:\nFirst you walk to the bus and go to station Haarlem.\nFrom there you take the train to Amsterdam Sloterdijk. Then you take the bus to school.\nIf you take this route and leave on time, you'll arrive at school on time.\n")
    print("You hear you alarm buzzing, but you're very tired.\nWhat harm can it do to sleep in a little?\n\nA. Press the snooze button and sleep in.\nB. Wake up, you set the alarm for a reason.\n")
    firstChoice()
    break




