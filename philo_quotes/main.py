from tkinter import *
import requests

def get_quote():
    response = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
    response.raise_for_status()
    data = response.json()
    quote = data["quoteText"]
    canvas.itemconfig(quote_text, text=quote)

def set_background_image():
    global background_img
    background_img = PhotoImage(file=filedialog.askopenfilename())
    canvas.create_image(150, 207, image=background_img)

def set_kanye_image():
    global kanye_img
    kanye_img = PhotoImage(file=filedialog.askopenfilename())
    kanye_button.config(image=kanye_img)

window = Tk()
window.title("Philosopher Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Philosopher Quote Goes HERE", width=250, font=("Garamond", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="freud_bg.png")
kanye_button = Button(image=kanye_img, bd=0, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()