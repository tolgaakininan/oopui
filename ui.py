from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.ekran = Tk()
        self.ekran.title("Quiz")
        self.ekran.config(padx=20, pady=20, bg=THEME_COLOR)

        self.skor_label = Label(text=f"Score:{self.score}", fg="white", bg=THEME_COLOR)
        self.skor_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Welcome", width=280, fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        dogru_img = PhotoImage(file="images/true.png")
        self.dogru_butonu = Button(image=dogru_img, highlightthickness=0, command=self.dogru_buton_basildi)
        self.dogru_butonu.grid(row=2, column=0)
        yanlis_img = PhotoImage(file="images/false.png")
        self.yanlis_butonu = Button(image=yanlis_img, highlightthickness=0, command=self.yanlis_buton_basildi)
        self.yanlis_butonu.grid(row=2, column=1)
        self.next_question()
        self.ekran.mainloop()

    def next_question(self):

        self.canvas.config(bg="white")
        self.skor_label.config(text=f"Score:{self.score}")
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question)

    def dogru_buton_basildi(self):
        self.geri_donus_ver(self.quiz.check_answer("True"))

    def yanlis_buton_basildi(self):
        self.geri_donus_ver(self.quiz.check_answer("False"))

    def geri_donus_ver(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score+=1
        else:
            self.canvas.config(bg="red")
        if self.quiz.still_has_questions():
            self.ekran.after(1000,self.next_question)
        else:
            self.canvas.config(bg="white")
            self.yanlis_butonu.destroy()
            self.dogru_butonu.destroy()
            self.canvas.itemconfig(self.question_text, text=f" Test is over.\n Your score is {self.score}/10")