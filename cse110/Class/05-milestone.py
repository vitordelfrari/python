print("""
                        WELCOME TO THE ADVENTURE GAME!

    Your castle is invaded by enemies from another kingdom. 
    They want an really old but important dagger of an ancient king from your family. 
    This dagger is in a vault in the great library. But you're in your room, two floors up. 
    Do you FLEE away on your Dragon or try to SAVE the dagger?
        """)

while True:
    a = input("Type your choice: FLEE or SAVE? ")
    if a.upper().strip() == "FLEE":
        print("""
    You climb on your dragon and see many invaders who, seeing you fleeing, shoot many arrows in your direction that hit the dragon's wings, forcing you to descend into a forest. You don't have much time. Will you WALK and try to find help or will you HIDE? .
    """)

        while True:   
            b = input("Type your choice: WALK or HIDE? ")
            
            if b.upper() == "WALK":
                print("""
    You walk a long time and find a big river, that seens to be good to drink and get fish to eat and a cave where you can protect you and your dragon.
    You can WAIT safe with your dragon in the forest and wait for someone save you, or you can try to find HELP to save your family.
    """)      

                while True:   
                    c = input("Type your choice: WAIT or HELP? ")
                    if c.upper() == "WAIT":
                        print("""
    You stay in the forest for a long time, living in peace. When your dragon recover, you fly back to your castle, but all you found was ruins. 
    """)
                        break
                    elif c.upper() == "HELP":
                        print("""
    You found a king and his servents hunting by that trail. He made an oath to your father to protect and serve him and promessed to help you rescuing then.
    """)
                        break
                    else:
                        continue
                break
            elif(b.upper() == "HIDE"):
                print("""
    You find a huge cave, big enough for you and you dragon, but you hear a strange noise. 
    Will you run BACK to where you where or SEE where this noise come from?""")  
              
                while True:
                    c2 = input("Type your choice: BACK or SEE? ")
                    if c2.upper() == "BACK":
                        print("""
    You run back to the place you were, but the enemies where waiting for you there. They killed your dragon and captured you.""")
                        break
                    elif c2.upper() == "SEE":
                        print("""
    You walk in search of that noise, but realize that you are walking in circles inside the cave. The cave is cursed and those who enter cannot leave. Until now... """)
                        break
                    else:
                        continue
                break
            else:
                continue
        break 

    elif a.upper().strip() =="SAVE":
        print("""
    you manage a plan to leave your room without no one knowing. You can use a SECRET path to go down or use the WINDOWS. 
    """)

        while True:   
            b2 = input("Type your choice: SECRET or WINDOW? ")
            
            if b2.upper() == "SECRET":
                print("""
    You go down the long stairs but on the way you end up meeting your family members. They ask you to go with then and ESCAPE the castle, but you want to RESCUE the dagger.
    """)      

                while True:   
                    c3 = input("Type your choice: ESCAPE or RESCUE? ")
                    if c3.upper() == "ESCAPE":
                        print("""
        You and your family continue downhill until you reach a small river, where you board a boat and escape the castle.""")
                        break
                    elif c3.upper() == "RESCUE":
                        print("""
        You enter the library but soon as you open the vault, the dagger wasn't there. Your enemies show up quickly as they hear you but you could still find another place to hide.""")
                        break
                    else:
                        continue
                break
            elif(b2.upper() == "WINDOW"):
                print("""
    You climb down to the library but when your almost there, you slips and can only hold on a few meters from the ground.
    You can now go UP to the library, ENTER the castle right there, or try to FIND your family again outside the castle.?""")  
              
                while True:
                    c4 = input("Type your choice: UP, ENTER or FIND? ")
                    if c4.upper() == "UP":
                        print("""
    You now start climbing to the library and when you get there, you found the vault open and nothing is there. 
    The enemies are already leaving the castle and you hide to wait then leave.""")
                        break
                    elif c4.upper() == "ENTER":
                        print(""" 
    You enter in the throne room, but you hear the enemies and hide behind the throne.
    While there you find the Hand of the King, walking out with the leader of the enemies. 
    You can't hear what they say, but they are all leaving the castle toghether.        
     """)
                        break
                    elif c4.upper() == "FIND":
                        print(""" 
    You run the fast as you can to try to find your family but when you get there, they have already leave in the boat. 
    For your luck, the let another one for you, so you get in and escape from there too.        
     """)
                    else:
                        continue
                break
            else:
                continue
        break 

    else:
        continue