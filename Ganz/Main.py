from tkinter import *
from diceClass import Dice

root = Tk()
root.title('Ganz Schon Clever!')
root.iconbitmap('dice.ico')
root.geometry('1200x900')

activeDice = dict()

#diceButtons = [yDieButton, bDieButton, gDieButton, oDieButton, pDieButton, wDieButton]

computerTurn = False
yCount = IntVar()
bCount = IntVar()
gCount = IntVar()
oCount = IntVar()
pCount = IntVar()
wCount = IntVar()
pickedCount = IntVar()
pickedCount.set(0)


#Locks the chosen dice, only allows to roll button active
def pickDie(chosenDie):
    activeDice[chosenDie].dieButtonText.set('Locked')
    activeDice[chosenDie].dieButton['state'] = 'disabled'
    lockLower(activeDice[chosenDie].value)
    activeDice[chosenDie].lock = True

    for key in activeDice:
        activeDice[key].dieButton['state'] = 'disabled'

    pickedCount.set(pickedCount.get() + 1)
    if pickedCount.get() >= 3:
        rollButtonText.set("Next\nRound")
        rollButton.configure(command=rollAll)
        pickedCount.set(0)

    rollButton['state'] = 'normal'

#function to check the validity of choosing a die value
def check(dieColor, dieValue):

#####THIS NEEDS FINISHED
    if dieColor == "Y":
        pass
    elif dieColor == "B":
        if (activeDice[dieColor].value + activeDice["W"].value) in activeDice[dieColor].checkVal:
            activeDice[dieColor].dieButton.configure(command=lambda: selectDie("B", activeDice[dieColor].count))
            activeDice[dieColor].dieButtonText.set('Select')
        else:
            activeDice[dieColor].dieButton.configure(command=lambda: pickDie(dieColor))
            activeDice[dieColor].dieButtonText.set('Can\'t score')

    elif dieColor == "G":
        if dieValue >= activeDice["G"].checkVal[gCount.get()]:
            activeDice[dieColor].dieButton.configure(command=lambda: selectDie("G", activeDice[dieColor].count))
            activeDice[dieColor].dieButtonText.set('Select')
        else:
            activeDice[dieColor].dieButton.configure(command=lambda: pickDie(dieColor))
            activeDice[dieColor].dieButtonText.set('Can\'t score')

    elif dieColor == "O":
        if oCount.get() > 10:
            activeDice[dieColor].dieButton.configure(command=lambda: pickDie(dieColor))
            activeDice[dieColor].dieButtonText.set('Can\'t score')
        else:
            activeDice[dieColor].dieButton.configure(command=lambda: selectDie("O", activeDice[dieColor].count))
            activeDice[dieColor].dieButtonText.set('Select')

    elif dieColor == "P":
        if pCount.get() > 10 or activeDice[dieColor].checkVal >= activeDice[dieColor].value:
            activeDice[dieColor].dieButton.configure(command=lambda: pickDie(dieColor))
            activeDice[dieColor].dieButtonText.set('Can\'t score')
        else:
            activeDice[dieColor].dieButton.configure(command=lambda: selectDie("P", activeDice[dieColor].count))
            activeDice[dieColor].dieButtonText.set('Select')


#Lock buttons function
def lockLower(checkNum):
    for i in activeDice:
        if activeDice[i].lock is False and activeDice[i].value < checkNum:
            activeDice[i].dieButton['state'] = 'disabled'
            activeDice[i].dieButtonText.set("Locked")
            activeDice[i].lock = True

###Button Functions #############################################

#Roll for new Round
def rollAll():
    for key in activeDice:
        activeDice[key].lock = False
        activeDice[key].value = activeDice[key].roll()
        activeDice[key].dieButton['state'] = 'normal'
        activeDice[key].dieButtonText.set("Select")
        activeDice[key].dieLabelText.set(str(activeDice[key].value))
        check(key, activeDice[key].value)

    rollButton.configure(state='disabled', command=rollActive)
    rollButtonText.set("Roll")



#Roll all active Dice
def rollActive():
    rollButtonText.set("Roll")
    for key in activeDice:
        if activeDice[key].lock is False:
            activeDice[key].value = activeDice[key].roll()
            activeDice[key].dieButton['state'] = 'normal'
            check(key, activeDice[key].value)

        activeDice[key].dieLabelText.set(str(activeDice[key].value))

    rollButton['state'] = 'disabled'

def selectDie(chosenDie, position):

    if chosenDie == "Y":
        pass

    #NOT FINISHED WITH B SELECTION
    elif chosenDie == "B":
        activeDice[chosenDie].currentScore = activeDice[chosenDie.score[position.get()]]

    elif chosenDie == "G":
        Label(gFrame, text=str(activeDice["G"].value)).grid(row=1, column=position.get(), ipadx=5, padx=5)
        activeDice[chosenDie].currentScore = activeDice[chosenDie].score[position.get()]

    elif chosenDie == "O":
        Label(oFrame, text=str(activeDice["O"].value * oVal[position.get()])).grid(row=1, column=position.get(), ipadx=5, padx=5)
        activeDice[chosenDie].currentScore += (activeDice["O"].value * oVal[position.get()])

    elif chosenDie == "P":
        Label(pFrame, text=str(activeDice["P"].value)).grid(row=1, column=position.get(), ipadx=5, padx=5)
        activeDice[chosenDie].currentScore += activeDice[chosenDie].value
        activeDice[chosenDie].checkVal = activeDice[chosenDie].value
        if activeDice[chosenDie].checkVal == 6:
            activeDice[chosenDie].checkVal = 0

    else:
        pass

    activeDice[chosenDie].count.set(activeDice[chosenDie].count.get() + 1)
    pickDie(chosenDie)

    #elif computerTurn == False:
    #    computerTurn = True
    #
    #else:
    #    computerTurn = False


yValues = [[3, 6, 5, "X"], [2, 1, 'X', 5], [1, 'X', 2, 4], ['X', 3, 4, 6]]
bValues = [["", 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
gValues = ["≥1", "≥2", "≥3", "≥4", "≥5", "≥1", "≥2", "≥3", "≥4", "≥5", "≥6"]
oValues = ["", "", "", "x2", "", "", "x2", "", "x2", "", "x3"]
pValues = ["", "", "", "", "", "", "", "", "", "", ""]

gVal = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5]
oVal = [1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 3]

#create frames for each die
diceFrame = LabelFrame(root, text="Dice Frame")
yFrame = LabelFrame(root, text="Yframe", padx=50, pady=50, bg="yellow")
bFrame = LabelFrame(root, text="Bframe", padx=50, pady=50, bg="blue")
gFrame = LabelFrame(root, text="Gframe", padx=50, pady=50, bg="green")
oFrame = LabelFrame(root, text="Oframe", padx=50, pady=50, bg="orange")
pFrame = LabelFrame(root, text="pValues", padx=50, pady=50, bg="pink")

#space the frames
diceFrame.grid(row=1, column=0, columnspan=2)
yFrame.grid(row=4, column=0, pady=10)
bFrame.grid(row=4, column=1, pady=10)
gFrame.grid(row=5, column=0, columnspan=2)
oFrame.grid(row=6, column=0, columnspan=2)
pFrame.grid(row=7, column=0, columnspan=2)

#Create Dice Button Lables
yDieButtonText = StringVar()
bDieButtonText = StringVar()
gDieButtonText = StringVar()
oDieButtonText = StringVar()
pDieButtonText = StringVar()
wDieButtonText = StringVar()
rollButtonText = StringVar()
yDieButtonText.set("Select")
bDieButtonText.set("Select")
gDieButtonText.set("Select")
oDieButtonText.set("Select")
pDieButtonText.set("Select")
wDieButtonText.set("Select")
rollButtonText.set("Roll")

#Create Buttons for dice
yDieButton = Button(diceFrame, textvariable=yDieButtonText, command=lambda: (selectDie("Y", activeDice["Y"].count)))
bDieButton = Button(diceFrame, textvariable=bDieButtonText, command=lambda: (selectDie("B", activeDice["B"].count)))
gDieButton = Button(diceFrame, textvariable=gDieButtonText, command=lambda: (selectDie("G", activeDice["G"].count)))
oDieButton = Button(diceFrame, textvariable=oDieButtonText, command=lambda: (selectDie("O", activeDice["O"].count)))
pDieButton = Button(diceFrame, textvariable=pDieButtonText, command=lambda: (selectDie("P", activeDice["P"].count)))
wDieButton = Button(diceFrame, textvariable=wDieButtonText, command=lambda: (selectDie("W", activeDice["W"].count)))

yDieButton.grid(row=2, column=0)
bDieButton.grid(row=2, column=1)
gDieButton.grid(row=2, column=2)
oDieButton.grid(row=2, column=3)
pDieButton.grid(row=2, column=4)
wDieButton.grid(row=2, column=5)

#Create label values to update for Dice
yDieValue = StringVar()
bDieValue = StringVar()
gDieValue = StringVar()
oDieValue = StringVar()
pDieValue = StringVar()
wDieValue = StringVar()

#Create Labels to display Dice Value for now
yDie = Label(diceFrame, textvariable=yDieValue)
bDie = Label(diceFrame, textvariable=bDieValue)
gDie = Label(diceFrame, textvariable=gDieValue)
oDie = Label(diceFrame, textvariable=oDieValue)
pDie = Label(diceFrame, textvariable=pDieValue)
wDie = Label(diceFrame, textvariable=wDieValue)

yDie.grid(row=1, column=0)
bDie.grid(row=1, column=1)
gDie.grid(row=1, column=2)
oDie.grid(row=1, column=3)
pDie.grid(row=1, column=4)
wDie.grid(row=1, column=5)

#List variables to create Die class objects
#Store fox count in white score value
#Combine dice Button Variables for creating die class
diceList = ["Yellow", "Blue", "Green", "Orange", "Pink", "White"]
diceScore = [0,
             [1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56],
             [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66],
             0,
             0,
             0]
diceBonus = [['bx', 'o4', 'gx', 'fox', '+1'],
             ['o5', 'yx', 'fox', 'rr', 'gx', 'p6', '+1'],
             [None, None, None, '+1', None, 'bx', 'fox', None, 'p6', 'rr', None],
             [None, None, 'rr', None, 'yx', '+1', None, 'fox', None, 'p6', None],
             [None, None, 'rr', 'bx', '+1', 'yx', 'fox', 'rr', 'gx', 'o6', '+1'],
             None]
diceCheck = [[3, 6, 5, 2, 1, 5, 1, 2, 4, 3, 4, 6],
             {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12},
             [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6],
             None,
             0,
             None]
diceButtons = [yDieButton, bDieButton, gDieButton, oDieButton, pDieButton, wDieButton]
diceButtonText = [yDieButtonText, bDieButtonText, gDieButtonText, oDieButtonText, pDieButtonText, wDieButtonText]
diceLabels = [yDie, bDie, gDie, oDie, pDie, wDie]
diceLabelText = [yDieValue, bDieValue, gDieValue, oDieValue, pDieValue, wDieValue]
diceCounts = [yCount, bCount, gCount, oCount, pCount, wCount]

#Build dictionary of class object to make single variable to pull everything from
for i in range(len(diceList)):
    activeDice[diceList[i][0]] = Dice(diceList[i], diceScore[i], diceButtons[i], diceButtonText[i], diceLabels[i], diceLabelText[i], diceCheck[i], diceCounts[i])

#Display initial values set initial counts to 0
for key in activeDice:
    activeDice[key].dieLabelText.set(str(activeDice[key].value))

#Create Roll Button
rollButton = Button(diceFrame, textvariable=rollButtonText, command=rollActive, state=DISABLED)
rollButton.grid(row=1, column=6)

for i in range(len(yValues)):
    col = 0
    for value in yValues[i]:
        yButton = Button(yFrame, text=str(value)).grid(row=i, column=col)
        col += 1

for i in range(len(bValues)):
    col = 0
    for value in bValues[i]:
        bButton = Button(bFrame, text=str(value)).grid(row=i, column=col)
        col += 1
col = 0
for i in gValues:
    gButton = Button(gFrame, text=str(i)).grid(row=0, column=col, padx=20, ipadx=10, ipady=10)
    col += 1

col = 0
for i in oValues:
    oButton = Button(oFrame, text=str(i)).grid(row=0, column=col)
    col += 1

col = 0
for i in pValues:
    pButton = Button(pFrame, text=str(i)).grid(row=0, column=col)
    col += 1

root.mainloop()
