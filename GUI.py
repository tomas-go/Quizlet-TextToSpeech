import tkinter as tk

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title("Quizlet Text To Speech App")    # Title for window

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

user_input = tk.Entry(frame, font=40)
user_input.place(relwidth=0.65, relheight=1)

submit_button = tk.Button(frame, text="Go", font="40")
submit_button.place(relx=0.7, relheight=1, relwidth=0.3)

# root.mainloop()