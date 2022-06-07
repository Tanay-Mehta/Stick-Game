import tkinter as tk
from tkinter import messagebox
import random as rd

window = tk.Tk()
counter = 0
number = 51
def one_player():
    counter = 0
    b11.grid_forget()
    b22.grid_forget()
    def hard():
        b11_.grid_forget()
        b22_.grid_forget()
        def check_won():
            if number == 1:
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                messagebox.showinfo(title="you lost", message="computer wins")
        def com1():
            global number
            number -= 4
            l1.config(text=number)
            check_won()

        def b1_pressed():
            global number
            number -= 1
            l1.config(text=number)
            window.after(1000, com1)

        def com2():
            global number
            number -= 3
            l1.config(text=number)
            check_won()


        def b2_pressed():
            global number
            number -= 2
            l1.config(text=number)
            window.after(1000, com2)

        def com3():
            global number
            number -= 2
            l1.config(text=number)
            check_won()

        def b3_pressed():
            global number
            number -= 3
            l1.config(text=number)
            window.after(1000, com3)

        def com4():
            global number
            number -= 1
            l1.config(text=number)
            check_won()

        def b4_pressed():
            global number
            number -= 4
            l1.config(text=number)
            window.after(1000, com4)

        l1 = tk.Label(text=51, font=("arial", 50))

        b1 = tk.Button(text="1", font=("arial", 20), command=b1_pressed)
        b2 = tk.Button(text="2", font=("arial", 20), command=b2_pressed)
        b3 = tk.Button(text="3", font=("arial", 20), command=b3_pressed)
        b4 = tk.Button(text="4", font=("arial", 20), command=b4_pressed)

        l1.grid(column=1, columnspan=4, row=1)
        b1.grid(column=1, row=2)
        b2.grid(column=2, row=2)
        b3.grid(column=3, row=2)
        b4.grid(column=4, row=2)
    def easy():
        b11_.grid_forget()
        b22_.grid_forget()
        def check_if_game_over():
            global number, count
            if number == 1:
                if counter % 2 != 0:
                    messagebox.showinfo(title="Congratulations", message="computer wins")
                else:
                    messagebox.showinfo(title="Congratulations", message="user 1 wins")
            elif number < 1:
                if counter % 2 != 0:
                    messagebox.showinfo(title="Congratulations", message="user 1 wins")
                else:
                    messagebox.showinfo(title="Congratulations", message="computer wins")
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
                return False
            else:
                return True

        def com_num_fun(count=counter):
            global number
            com_num = rd.randint(1, 4)
            number -= com_num
            l1.config(text=number)
            count += 1
            check_if_game_over()


        def b1_pressed(count=counter):
            global number
            number -= 1
            count += 1
            b1.config(state="disabled")
            b2.config(state="disabled")
            b3.config(state="disabled")
            b4.config(state="disabled")
            check = check_if_game_over()
            if check:
                window.after(1000, com_num_fun)
            else:
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")

        def b2_pressed(count=counter):
            global number
            number -= 2
            l1.config(text=number)
            count += 1
            check = check_if_game_over()
            if check:
                window.after(1000, com_num_fun)
            else:
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")

        def b3_pressed(count = counter):
            global number
            number -= 3
            l1.config(text=number)
            count += 1
            check = check_if_game_over()
            if check:
                window.after(1000, com_num_fun)
            else:
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
        def b4_pressed(count = counter):
            global number
            number -= 4
            l1.config(text=number)
            count += 1
            check = check_if_game_over()
            if check:
                window.after(1000, com_num_fun)
            else:
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")
        l1 = tk.Label(text=51, font=("arial", 50))

        b1 = tk.Button(text="1", font=("arial", 20), command=b1_pressed)
        b2 = tk.Button(text="2", font=("arial", 20), command=b2_pressed)
        b3 = tk.Button(text="3", font=("arial", 20), command=b3_pressed)
        b4 = tk.Button(text="4", font=("arial", 20), command=b4_pressed)

        l1.grid(column=1, columnspan=4, row=1)
        b1.grid(column=1, row=2)
        b2.grid(column=2, row=2)
        b3.grid(column=3, row=2)
        b4.grid(column=4, row=2)

    b11_ = tk.Button(text="hard", font=("arial", 20), command=hard)
    b22_ = tk.Button(text="easy", font=("arial", 20), command=easy)
    b11_.grid(column=3, row=1)
    b22_.grid(column=3, row=2)


def two_players():
    b11.grid_forget()
    b22.grid_forget()
    def easy():
        def check_if_game_over():
            if number == 1:
                if counter%2 == 0:
                    messagebox.showinfo(title="Congratulations", message="user 2 wins")
                else:
                    messagebox.showinfo(title="Congratulations", message="user 1 wins")
            elif number < 1:
                if counter%2 == 0:
                    messagebox.showinfo(title="Congratulations", message="user 1 wins")
                else:
                    messagebox.showinfo(title="Congratulations", message="user 2 wins")
                b1.config(state="disabled")
                b2.config(state="disabled")
                b3.config(state="disabled")
                b4.config(state="disabled")


        def b1_pressed():
            global number, counter
            number -= 1
            counter += 1
            check_if_game_over()
            l1.config(text=number)

        def b2_pressed():
            global number, counter
            number -= 2
            counter += 1
            l1.config(text=number)
            check_if_game_over()
        def b3_pressed():
            global number, counter
            number -= 3
            counter += 1
            l1.config(text=number)
            check_if_game_over()
        def b4_pressed():
            global number, counter
            number -= 4
            counter += 1
            l1.config(text=number)
            check_if_game_over()


        l1 = tk.Label(text=number, font=("arial", 50))

        b1 = tk.Button(text="1", font=("arial", 20), command=b1_pressed)
        b2 = tk.Button(text="2", font=("arial", 20), command=b2_pressed)
        b3 = tk.Button(text="3", font=("arial", 20), command=b3_pressed)
        b4 = tk.Button(text="4", font=("arial", 20), command=b4_pressed)

        l1.grid(column=1, columnspan=4, row=1)
        b1.grid(column=1, row=2)
        b2.grid(column=2, row=2)
        b3.grid(column=3, row=2)
        b4.grid(column=4, row=2)
b11 = tk.Button(text="two players", font=("arial", 20), command=two_players)
b22 = tk.Button(text="single player", font=("arial", 20), command=one_player)
b11.grid(column=1, row=1)
b22.grid(column=1, row=2)
window.mainloop()