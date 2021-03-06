# -*-coding:Utf-8 -*

import time
import sys
import re

from threading import *

from clientClass import *

displayLock = RLock()
gameStarted = False
myTurn = False
command = ""
Fin=False

def isValidCommand(c):
    """Check if a command is valid"""
    x = re.match("^[sSoOnNeEmMpP][0-9sSoOnNeE]*$", c.upper())
    return x != None
    
def getUserInput():
    global gameStarted
    global myTurn
    global command
    global Fin

    while not Fin:
        ############################################### DEBUG A LA CON ##################################################
        with displayLock:
            if not gameStarted:
                print("If there are more than 2 players, enter C to start the game: ", end="", flush=True)
            elif myTurn:
                print("It's your turn, please make a move: ", end="", flush=True)
            else:
                print("It isn't your turn yet, please wait", end="", flush=True)

        msg = input()

        if not gameStarted:     # if the game hasn't started yet => send command immediately to server
            client.send(msg)
        elif myTurn:            # if it's my turn then check if input is valid
            if (isValidCommand(msg)):
                command = msg
                # wait for command to be handled by other thread
                # why don't we handle/send the command here ? : because we can still have remaining move in the pipe
                # so we don't need to take other additional input
                while command != "":
                    time.sleep(0.001)
        else:
            pass

def getServerResponse():
    global gameStarted
    global myTurn
    global command
    global Fin

    gameStarted = False
    while True:
        ############################################### DEBUG A LA CON ##################################################
        #print("Pif")
        msg = client.receive()
        ############################################### DEBUG A LA CON ##################################################
        #print("J'ai recu cette daube du serveur :",msg)
        if msg == "START":
            #print("Paf")
            print("Game started !")
            gameStarted = True
            myTurn = False
        elif msg == "TURN":
            myTurn = True
            #print("Pof")
            # make my move
            print("It's your turn, please make a move")
            if len(client.remainingMove) > 0:       # if there is some move in stock then move it
                client.move()
            else:                                   # else wait till having a valid input then move it
                while command == "":
                    time.sleep(0.001)
                client.addMove(command)
                client.move()
                print("moved ! now set command to empty to continue")
                myTurn = False
                command = ""
        elif not msg == "":
            #print("Puf")
            if not gameStarted:
                with displayLock:
                    print()
                    print(">> SERVER : {0}".format(msg))
                    print("Still waiting for your command...")
            else:
                myTurn = False
                with displayLock:
                    print()
                    print(msg)
                    #print("Puiff")           
        else:
            print("Partie gagnee par un robot")
            Fin=True
            return

# Connect to server
client = Client("localhost", 20123)
while True:
    try:
        client.connect()
        break
    except:
        print("ERROR : Cannot connect to server. Will try in 5 seconds")
        for i in range(5):
            print(". ", end="", flush=True)
            time.sleep(1)
        print()

# Get welcome message from server
print(client.receive())

# Start 2 threads : one to get user's input, other to communicate with server
getUserInputThread = Thread(target=getUserInput)
getServerResponseThread = Thread(target=getServerResponse)

getServerResponseThread.start()
getUserInputThread.start()

# wait till the end of the game
getServerResponseThread.join()

client.close()