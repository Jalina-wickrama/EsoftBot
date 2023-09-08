from tkinter import *

from numpy import size
from chat import get_response, bot_name

BG_GRAY = "#ABB2B9"
BG_BLUE = "#3383FF"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Courier 12"
FONT_BOLD = "Courier 12 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
    
    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=400, height=600, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg="#FF334C", fg=TEXT_COLOR,
                           text="Welcome To Esoft", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg="#353535", fg="#fff",
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=1, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_COLOR, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#fff", fg="#202020", font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

         # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_BLUE,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()