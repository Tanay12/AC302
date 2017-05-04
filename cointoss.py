from Tkinter import *
import random

def calculate():
    count = 0
    heads = 0
    tails = 0

    times = theEntry.get()
    times = int(times)

    if times > 100000:
        outputHeads.set("Sorry! Number too high...")
    elif times < 0:
        outputHeads.set("Don't put in negative values!")
    else:
        while count < times:
            rand = random.randint(1,2)
            # Checks if head or tail #
            if rand == 1:
                heads += 1
            else:
                tails += 1

            count += 1

            # Basic formula for calculating percentage #
            percentage = (float(heads) / count) * 100

            # Output statements #
            outputHeads.set("Heads = " + str(heads))
            outputTails.set("Tails = " + str(tails))
            outputPerc.set("Percentage heads = " + str(percentage) + "%")

            userInput = theEntry.get()

# Basic window configuration #
app = Tk()
app.geometry("300x200")
app.title("Coin Toss Simulator")

# Instructions text #r
welcomeText = IntVar()
welcomeText.set("How many coin tosses?")
welcome = Label(app, textvariable=welcomeText)
welcome.pack()

# User input #
theEntry = Entry(app)
theEntry.pack()

# Button #
button1 = Button(app, text="Simulate!", command=calculate)
button1.pack()

# Output Labels #
outputHeads = IntVar()
outputHeads.set("")
outputHeadsLabel = Label(app, textvariable=outputHeads)
outputHeadsLabel.pack()

outputTails = IntVar()
outputTails.set("")
outputTailsLabel = Label(app, textvariable=outputTails)
outputTailsLabel.pack()

outputPerc = IntVar()
outputPerc.set("")
outputPercLabel = Label(app, textvariable=outputPerc)
outputPercLabel.pack()

app.mainloop()
