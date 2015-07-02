import tkinter as tk
import random

class ComputerPlayer():
    def __init__(self, start=1, stop=100):
        self.choice = random.randint(start, stop)

    def play(self):
        return self.choice

class RandomNumberGame(object):
    def __init__(self):
        self.game_over = False

    def is_game_over(self):
        return self.game_over

    def start(self, chances = 7):
        self.comp_choice = ComputerPlayer().play()
        # print(self.comp_choice)
        self.chances = chances
        root = tk.Tk()
        self.gui = RandomGUI(root, self.chances)

        self.gui.submit_button.config(command=self.check)
        # self.gui.mainloop()
        root.mainloop()

    def check(self):
        #empty the entry box

        if self.is_game_over():
            return

        try:
            user_guess = int(self.gui.user_choice_entryBox.get())

        except ValueError as e:
            msg = "Invalid input: Enter an Integer Value"
            self.gui.display_message(msg)
            return

        finally:
            self.gui.clear_entryBox()

        if  user_guess == self.comp_choice:
            self.gui.display_message("You Win!! Congratulations!!")
            self.game_over = True
        else:
            self.chances -= 1
            if self.chances:
                self.gui.update_chances_label(self.chances)
                #give hint to the user
                isLess = True if user_guess > self.comp_choice else False
                self.gui.update_hint_label(isLess)
            else:
                self.gui.display_message("You Lose!! Better luck next time!!")
                self.game_over = True


class RandomGUI(tk.Frame):
    def __init__(self, master, chances):
        self.parent = master
        super().__init__(master)
        # self.config(relief=tk.RAISED, borderwidth=10)
        self.parent.title("Number guessing game")
        #next two lines to make full screen
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        self.parent.geometry('%dx%d' %(w,h))

        # self.parent.geometry('400x200+200+200')
        self.buildGUI(chances)
        self.pack(fill=tk.BOTH, expand=True)

    def buildGUI(self, chances):
        #create label to display number of chances left
        self.chances_label = tk.Label(self, font="Times 16 bold", fg="blue")
        self.chances_label.config(text="You have %d chances remaining" %(chances))
        self.chances_label.grid(row=0, sticky=tk.W+tk.E)
        #create the choice label and entry box
        self.user_choice_label = tk.Label(self, text="Enter your choice", fg='red', bg='white', font='Times 16 bold')
        self.user_choice_entryBox = tk.Entry(self, width=5)
        self.user_choice_label.grid(row=1, column=0, padx=2, pady=2)
        self.user_choice_entryBox.grid(row=1, column=1, padx=2, sticky=tk.W+tk.E)


        #create the button to take user input
        self.submit_button = tk.Button(self, text='Submit', bg='white', font='Times 16 bold')
        self.submit_button.grid(row=2, column=1, sticky=tk.E)


    def update_chances_label(self, chances):
        self.chances_label.config(text="You have %d chances remaining" %(chances))

    def display_message(self, msg):
        '''displays a message by updating the label'''
        tk.Label(self, text=msg, font="Times 16 bold", fg='red').grid(row=3)

    def clear_entryBox(self):
        self.user_choice_entryBox.delete(0, tk.END)

    def update_hint_label(self, isLess):
        # print(isLess)
        msg = 'The number is '+ ('lesser' if isLess else 'greater')
        tk.Label(self, text=msg, font="Times 16 bold", fg='red').grid(row=3, sticky=tk.NSEW)

if __name__ == '__main__':
    RandomNumberGame().start()




