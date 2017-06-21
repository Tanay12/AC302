import random
from Tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.number = random.randint(1, 101)

    def create_widgets(self):
        # create instruction label
        Label(self, text="There is a number between 1 and 100.").grid(row=0, column=0, sticky=W)
        Label(self, text = "Try and guess it in as few attempts as possible!").grid(row = 1, column = 0, sticky = W)
        # creating input for user
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=2,column=1,sticky=W)
        # create the submit button
        Label(self, text="Click Submit!").grid(row=3,column=0,sticky=W)
        Button(self, text='SUBMIT', command=self.run_game).grid(row=3,column=1,sticky=W)
        # create the computer feedback text
        self.text = Text(self, width=75, height=10, wrap=WORD)
        self.text.grid(row=4, column=0, columnspan=4)

    def run_game(self):
        guess = int(self.guess_ent.get())

        if guess != self.number:
            print_text = "You guessed {0}.".format(guess)

            if guess > self.number:
                print_text += " That's too high. Guess lower..."
            elif guess < self.number:
                print_text += " That's too low. Guess higher..."

            self.text.delete(0.0, END)
            self.text.insert(0.0, print_text)

            self.guess_ent.delete(0, END)
        else:
            print_text = "That's the right number! Well done!"
            self.text.delete(0.0, END)
            self.text.insert(0.0, print_text)

root = Tk()
root.title("Guessing Game")
app = Application(root)
root.mainloop()
#
