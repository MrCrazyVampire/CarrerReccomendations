# # gui.py
# import tkinter as tk
# from tkinter import ttk
# from ttkthemes import ThemedStyle
# from project02 import career

# class QuestionnaireApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Questionnaire")

#         # Set window dimensions to cover the entire screen
#         screen_width = self.master.winfo_screenwidth()
#         screen_height = self.master.winfo_screenheight()
#         self.master.geometry(f"{screen_width}x{screen_height}+0+0")

#         self.questions = [
#             "Does it often happen that the solution you have found is different from the solutions of everyone else?",
#             "Can you recall a situation where you successfully conveyed a complex idea to someone with different background knowledge, ensuring their understanding?",
#             "When faced with a challenging problem, do you systematically break it down into smaller components to analyze each part rather than working at it as a whole?",
#             "Do you find it easy to work with numbers and statistics rather than words?",
#             "Is it easier for you to learn about many skills rather than focusing and improving on one?",
#             "Are you consistent in performing routine tasks, ensuring accuracy and reliability in your work?"
#         ]

#         self.current_question_index = 0
#         self.responses = []

#         # Calculate font size based on screen height
#         font_size = int(screen_height / 20)

#         # Set initial x and y coordinates for the question label
#         initial_x = 0
#         initial_y = 100

#         self.question_label = tk.Label(self.master, text=self.questions[self.current_question_index], wraplength=screen_width - 20, font=('Arial', font_size))
#         self.question_label.place(x=initial_x, y=initial_y)

#         self.style = ThemedStyle(self.master)
#         self.style.set_theme("equilux")

#         self.style.configure('TButton', padding=10, font=('Arial', 14), relief='flat', foreground='white', background='#4CAF50')

#         self.yes_button = ttk.Button(self.master, text="Yes", command=lambda: self.answer_question(1))
#         self.yes_button.pack(side=tk.LEFT, pady=10)

#         self.no_button = ttk.Button(self.master, text="No", command=lambda: self.answer_question(0))
#         self.no_button.pack(side=tk.LEFT, pady=10)

#         self.maybe_button = ttk.Button(self.master, text="Maybe", command=lambda: self.answer_question(0.5))
#         self.maybe_button.pack(side=tk.LEFT, pady=10)

#     def answer_question(self, response):
#         self.responses.append(response)
#         self.current_question_index += 1

#         if self.current_question_index < len(self.questions):
#             self.question_label.config(text=self.questions[self.current_question_index])
#         else:
#             self.display_results()

#     def display_results(self):
#         self.question_label.config(text="Questionnaire Completed!")
#         self.yes_button.destroy()
#         self.no_button.destroy()
#         self.maybe_button.destroy()

#         # Display career recommendation
#         input_vector = self.responses
#         recommended_career = career(input_vector)
#         recommendation_label = tk.Label(self.master, text=f"Recommended Career: {recommended_career}", font=('Arial', 36))
#         recommendation_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = QuestionnaireApp(root)
#     root.mainloop()
# gui.py
# gui.py
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from project02 import career

class QuestionnaireApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Questionnaire")

        # Set window dimensions to cover the entire screen
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        self.master.geometry(f"{screen_width}x{screen_height}+0+0")
        self.master.configure(bg='#222831')
        self.questions = [
            "Does it often happen that the solution you have found is different from the solutions of everyone else?",
            "Can you recall a situation where you successfully conveyed a complex idea to someone with different background knowledge, ensuring their understanding?",
            "When faced with a challenging problem, do you systematically break it down into smaller components to analyze each part rather than working at it as a whole?",
            "Do you find it easy to work with numbers and statistics rather than words?",
            "Is it easier for you to learn about many skills rather than focusing and improving on one?",
            "Are you consistent in performing routine tasks, ensuring accuracy and reliability in your work?"
        ]

        self.current_question_index = 0
        self.responses = []

        # Calculate font size based on screen height
        font_size = int(screen_height / 20)

        # Set initial x and y coordinates for the question label
        initial_x = 20
        initial_y = 100

        self.question_label = tk.Label(self.master, text=self.questions[self.current_question_index], wraplength=screen_width - 20, font=('Arial', font_size), bg='#222831', fg='#EEEEEE')
        self.question_label.place(x=initial_x, y=initial_y)

        self.style = ThemedStyle(self.master)
        self.style.set_theme("equilux")

        self.style.configure('TButton', padding=10, font=('Arial', 14), relief='flat', foreground='#00ADB5', background='#222831', bordercolor='#EEEEEE')

        self.yes_button = ttk.Button(self.master, text="Yes", command=lambda: self.answer_question(1), style='TButton')
        self.yes_button.pack(side=tk.LEFT, pady=10)

        self.no_button = ttk.Button(self.master, text="No", command=lambda: self.answer_question(0), style='TButton')
        self.no_button.pack(side=tk.LEFT, pady=10)

        self.maybe_button = ttk.Button(self.master, text="Maybe", command=lambda: self.answer_question(0.5), style='TButton')
        self.maybe_button.pack(side=tk.LEFT, pady=10)

    def answer_question(self, response):
        self.responses.append(response)
        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question_index])
        else:
            self.display_results()

    def display_results(self):
        self.question_label.config(text="Questionnaire Completed!")
        self.yes_button.destroy()
        self.no_button.destroy()
        self.maybe_button.destroy()

        # Display career recommendation
        input_vector = self.responses
        recommended_career = career(input_vector)
        recommendation_label = tk.Label(self.master, text=f"Recommended Career: {recommended_career}", font=('Arial', 36), bg='#222831', fg='#EEEEEE')
        recommendation_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuestionnaireApp(root)
    root.mainloop()

