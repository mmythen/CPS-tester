from tkinter import *
from tkmacosx import Button
from threading import Timer


# asking for initial input
timeSet = input("For how many second would you like to test cps? ")
timeSet = int(timeSet)


#functions for adding click, pressing the button, and computing cps
#add click
clicks = 0
buffer = False

def addClick():
    global clicks
    clicks += 1

#pressing button
testActive = False

def runTest():
    #accessing all global variables for use
    global testActive
    global clicks
    global buffer

    if buffer == False:
        if testActive == False:
            clicks = 0
            runCpsTimer()
            testActive = True
            textBox.destroy()
            timeButton.destroy()
            
        else:
            addClick()


#computing cps
finalCps = 0

def totalCps():

    #outputting total cps
    global finalCps
    global clicks
    finalCps = clicks/timeSet
    finalCps = str(finalCps)
    print("Your Clicks/Second is: " + finalCps)

    #resesting for next cps test
    global testActive
    global buffer
    testActive = False
    buffer = True
    runBufferTimer()


# timer functions and stupid buffer function
def runCpsTimer():
    cpsTimer = Timer(timeSet, totalCps)
    cpsTimer.start()
    newButton.config(text="keep going!", bg='green', highlightbackground='green')

def runBufferTimer():
    global buffer
    bufferTimer = Timer(2, setBufferFalse)
    bufferTimer.start()
    newButton.config(text="please wait!", bg='red')

def setBufferFalse():
    #stupid
    #buffer 
    global buffer
    buffer = False

    #new display
    global textBox
    global timeButton
    newButton.config(text=f"Your CPS was {finalCps}!", bg='white')

    textBox = Entry(width = 50)
    textBox.focus_set()
    textBox.pack()
    timeButton = Button(text='change time limit', width=450, height = 25, command=changeTime)
    timeButton.pack()



def changeTime():
    global textBox
    global timeSet
    timeSet = int(textBox.get())
    textBox.delete(0, END)


#creating window
window = Tk()
window.geometry = ("800x800")
label = Label(text="whats up....")
newButton = Button(text="click here to start test!", width=500, height=200, fg='black', bg='white', command=runTest)

#packing items into window
label.pack()
newButton.pack(pady=15, padx=15)






#runs window
window.mainloop()
