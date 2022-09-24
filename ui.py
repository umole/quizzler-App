from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.score_number = 0
        self.score_label = Label(text=f"Score: {self.score_number}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        false_png = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_png, command=self.is_false)
        self.false_button.grid(column=0, row=2)

        true_png = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_png, command=self.is_true)
        self.true_button.config(highlightthickness=0)
        self.true_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the game!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)



    # def interface(self):
    #     score_label = Label(text=f"Score: ")
    #     score_label.grid(column=1, row=0)
    #
    #     canvas = Canvas(width=300, height=250, background="white")
    #     canvas.create_text(text="", font=("Arial", 20, "italic"))
    #     canvas.grid(column=0, row=1, columnspan=2)
    #
    #     false_png = PhotoImage(file="./images/false.png")
    #     false_button = Button(image=false_png)
    #     false_button.grid(column=0, row=2)
    #
    #     true_png = PhotoImage(file="./images/true.png")
    #     true_button = Button(image=true_png)
    #     true_button.grid(column=1, row=2)


