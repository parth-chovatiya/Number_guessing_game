from tkinter import *
from random import *
from tkinter.font import Font
from tkinter import messagebox

# def get_detail():
#     answer.delete(1.0, END)
#     f_number = int(first_number.get())
#     s_number = int(second_number.get())
#     try:
#         random_number = randint(f_number, s_number)
#         print(random_number)
#         if int(entry_user.get()) == random_number:
#             answer.insert(INSERT, "Congratulation, You Win")
#         else:
#             answer.insert(INSERT, "Better Luck, Next Time")
#     except:
#         answer.insert(INSERT, "Please, \nEnter large number compare to " + str(f_number))

random_number = 0


# def yes_prompt():
#     ans_yes_no = messagebox.askyesno("Enter Yes or No", "Yes or No")
#     print(ans_yes_no)
#     if ans_yes_no:
#         print(random_number.get())


root = Tk()
root.title("Random Number Generator Game")
root.geometry("415x400")


def get_detail():
    answer.delete(1.0, END)
    f_number = int(first_number.get())
    s_number = int(second_number.get())
    if s_number >= f_number:
        global random_number
        random_number = randint(f_number, s_number)
        print(random_number)
        if int(entry_user.get())>=f_number and int(entry_user.get())<=s_number:
            if random_number == int(entry_user.get()):
                answer.insert(INSERT, "Congratulation, You Win")
            else:
                answer.insert(INSERT, "Better Luck, Next Time")
        else:
            answer.insert(INSERT, "Enter valid number")
    else:
        answer.insert(INSERT, "Please, \nEnter large number compare to " + str(f_number))


def yes_prompt():
    ans_yes_no = messagebox.askyesno("Do you want to show answer?", "Yes or No")
    print(ans_yes_no)
    if ans_yes_no:
        answer_label = Label(bottom_frame, text="Answer = " + str(random_number))
        answer_label.pack()
    


my_font = Font(family="bazooka", size=14, weight="bold")

top_frame = Frame(root, pady=10)

label_1 = Label(top_frame, text="Choose number between ", font=my_font)
label_1.pack(side=LEFT)

first_number = Entry(top_frame, width=4)
first_number.pack(side=LEFT)

label_2 = Label(top_frame, text=" to ", font=my_font)
label_2.pack(side=LEFT)

second_number = Entry(top_frame, width=4)
second_number.pack(side=LEFT)

label_3 = Label(top_frame, text=" : ", font=my_font)
label_3.pack(side=LEFT)

entry_user = Entry(top_frame, width=4)
entry_user.pack(side=LEFT)

top_frame.pack(side=TOP)

middle_frame = Frame(root)
enter_button = Button(middle_frame, text="Enter", command=get_detail)
enter_button.pack()
middle_frame.pack()


bottom_frame = Frame(root, pady=10)

answer = Text(bottom_frame, width=35, height=5, wrap=WORD)
answer.pack()


label_ask = Label(bottom_frame, text="Do you want to show answer ? :: ")
label_ask.pack()

button_yes = Button(bottom_frame, text="Yes", command=yes_prompt)
button_yes.pack()


bottom_frame.pack()


root.mainloop()
