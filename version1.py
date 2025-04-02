#quiz wiht data visulisation

from tkinter import *
from tkinter import messagebox

#dictionairy of questions and answers
qa = {"what is the highest moutain from sea level?": ["Mount Everest", "Mount Kilimanjaro", "Mount Cook", "Mount Fuji",0],
    "Which element has the chemical symbol Na?": ["magnesium", "sodium", "hydrogen", "sulfer",1],
    "what is the largest ocean?": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean",0],
    "which planet is closest to the sun?": ["earth", "jupiter", "venus", "mercury",3],
    "what is the largest country in the world": ["Russia", "Canada", "China", "USA",0],}

root = Tk()
root.title("Quiz")
root.geometry("500x700")

#quiz information
questions = list(qa.keys())
answers = list(qa.values())
question_number = 0
score = 0
answer_buttons = []


#obtaining user information
def submit():
    if ename.get() == "" or eage.get() == "":
        messagebox.showerror("Error", "Please enter a name")
    else:#removes the details from the quiz
        name.grid_forget()
        ename.grid_forget()
        yl.grid_forget()
        eyl.grid_forget()
        age.grid_forget()
        eage.grid_forget()
        submit_button.grid_forget()
        label.grid_forget()
        #printing user information for testing (delete code later)
        print(f"name: {ename.get()}\nyear levl: {eyl.get()}\nage: {eage.get()}")
        #running the main quiz
        butoon()
        ask_question()






#quiz
def ask_question():
    #asking the questions and asigning the answers
    #changes the question label to the current question
    question_label.config(text=questions[question_number])
    print(answer_buttons)
    for i, btn in enumerate(answer_buttons):
        btn.config(text=answers[question_number][i], command=lambda i=i: check_answer(i))

#check answer function
def check_answer(choice):
    global question_number, score

    correct_number = answers[question_number][4]  # Correct answer index
    if choice == correct_number:
        score += 1

    question_number += 1
    if question_number < len(questions):
        ask_question()
    else:
        messagebox.showinfo("Quiz Completed", f"Name: {ename.get()}\nYear levl: {eyl.get()}\nAge: {eage.get()}\nYour score: {score}/{len(questions)}")
        root.quit()

def butoon():   
    for i in range(4):
        btn = Button(root, text='', width=15)
        btn.grid(row=1,column=i)
        print(btn)
        answer_buttons.append(btn)

#creates the label for the question
question_label = Label(root, text="", font=("Arial", 14))
question_label.grid(row=0, column=0,columnspan=4)
#entering details
label = Label( text='Please enter your details', )
label.grid(row=0, column=0, columnspan=2,sticky='w')
name = Label( text='name')
name.grid(row=1, column=0)
ename = Entry()
ename.grid(row=1, column=1)

yl = Label( text='year level')
yl.grid(row=2, column=0)
eyl = Entry()
eyl.grid(row=2, column=1)

age = Label( text='age')
age.grid(row=3, column=0)
eage = Entry()
eage.grid(row=3, column=1)

submit_button=Button(root,text="submit",command=submit)
submit_button.grid(row=4, column=0,columnspan=3)



root.mainloop()












