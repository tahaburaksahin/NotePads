
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = 0
except ImportError:
    import tkinter.ttk as ttk

    py3 = 1

import notepad_support


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    root.resizable(False, False)
    top = Notepads_managment(root)
    notepad_support.init(root, top)
    root.mainloop()


w = None


def create_Notepads_managment(root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Notepads_managment(w)
    notepad_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Notepads_managment():
    global w
    w.destroy()
    w = None


class Notepads_managment:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
        top is the toplevel containing window."""
        _bgcolor = "#d9d9d9"  # X11 color: 'gray85'
        _fgcolor = "#000000"  # X11 color: 'black'
        _compcolor = "#d9d9d9"  # X11 color: 'gray85'
        _ana1color = "#d9d9d9"  # X11 color: 'gray85'
        _ana2color = "#d9d9d9"  # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use("winnative")
        self.style.configure(".", background=_bgcolor)
        self.style.configure(".", foreground=_fgcolor)
        self.style.configure(".", font="TkDefaultFont")
        self.style.map(
            ".", background=[("selected", _compcolor), ("active", _ana2color)]
        )

        top.geometry("600x450")
        top.title("Notepads managment")
        top.configure(highlightcolor="black")

        self.style.configure("TNotebook.Tab", background=_bgcolor)
        self.style.configure("TNotebook.Tab", foreground=_fgcolor)
        self.style.map(
            "TNotebook.Tab",
            background=[("selected", _compcolor), ("active", _ana2color)],
        )
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.02, rely=0.02, relheight=0.85, relwidth=0.97)
        self.TNotebook1.configure(width=582)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(
            0,
            text="Add",
            compound="none",
            underline="-1",
        )
        self.TNotebook1_t1 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(
            1,
            text="Display",
            compound="none",
            underline="-1",
        )
        self.TNotebook1_t2 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(
            2,
            text="Create",
            compound="none",
            underline="-1",
        )

        self.inputNotice = Text(self.TNotebook1_t0)
        self.inputNotice.place(relx=0.02, rely=0.28, relheight=0.64, relwidth=0.68)
        self.inputNotice.configure(background="white")
        self.inputNotice.configure(font="TkTextFont")
        self.inputNotice.configure(selectbackground="#c4c4c4")
        self.inputNotice.configure(width=396)
        self.inputNotice.configure(wrap=WORD)

        self.inputTitle = Entry(self.TNotebook1_t0)
        self.inputTitle.place(relx=0.09, rely=0.08, height=20, relwidth=0.6)
        self.inputTitle.configure(background="white")
        self.inputTitle.configure(font="TkFixedFont")
        self.inputTitle.configure(selectbackground="#c4c4c4")

        self.Label1 = Label(self.TNotebook1_t0)
        self.Label1.place(relx=0.02, rely=0.08, height=18, width=29)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text="""Title""")

        self.Label2 = Label(self.TNotebook1_t0)
        self.Label2.place(relx=0.02, rely=0.22, height=18, width=46)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text="""Notice:""")

        self.Button2 = Button(self.TNotebook1_t0)
        self.Button2.place(relx=0.74, rely=0.28, height=26, width=50)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(text="""Add""")
        self.Button2.bind("<Button-1>", lambda e: notepad_support.add_button(e))

        self.Button3 = Button(self.TNotebook1_t0)
        self.Button3.place(relx=0.74, rely=0.39, height=26, width=56)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(text="""Clear""")
        self.Button3.bind("<Button-1>", lambda e: notepad_support.clear_button(e))

        self.outputNotice = Text(self.TNotebook1_t1)
        self.outputNotice.place(relx=0.02, rely=0.19, relheight=0.76, relwidth=0.6)
        self.outputNotice.configure(background="white")
        self.outputNotice.configure(font="TkTextFont")
        self.outputNotice.configure(selectbackground="#c4c4c4")
        self.outputNotice.configure(width=346)
        self.outputNotice.configure(wrap=WORD)

        self.inputSearchTitle = Entry(self.TNotebook1_t1)
        self.inputSearchTitle.place(relx=0.09, rely=0.08, height=20, relwidth=0.51)
        self.inputSearchTitle.configure(background="white")
        self.inputSearchTitle.configure(font="TkFixedFont")
        self.inputSearchTitle.configure(selectbackground="#c4c4c4")

        self.Label3 = Label(self.TNotebook1_t1)
        self.Label3.place(relx=0.02, rely=0.08, height=18, width=29)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text="""Title""")

        self.Button4 = Button(self.TNotebook1_t1)
        self.Button4.place(relx=0.69, rely=0.33, height=26, width=54)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(text="""Next""")
        self.Button4.bind("<Button-1>", lambda e: notepad_support.next_button(e))

        self.Button5 = Button(self.TNotebook1_t1)
        self.Button5.place(relx=0.69, rely=0.44, height=26, width=55)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(text="""Back""")
        self.Button5.bind("<Button-1>", lambda e: notepad_support.back_button(e))

        self.Button7 = Button(self.TNotebook1_t1)
        self.Button7.place(relx=0.69, rely=0.22, height=26, width=68)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(text="""Search""")
        self.Button7.bind("<Button-1>", lambda e: notepad_support.search_button(e))

        self.Button8 = Button(self.TNotebook1_t1)
        self.Button8.place(relx=0.69, rely=0.56, height=26, width=64)
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(text="""Delete""")
        self.Button8.bind("<Button-1>", lambda e: notepad_support.delete_button(e))

        self.Label4 = Label(self.TNotebook1_t2)
        self.Label4.place(relx=0.09, rely=0.14, height=18, width=259)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(text="""For creating a new notepads managment.""")

        self.Button6 = Button(self.TNotebook1_t2)
        self.Button6.place(relx=0.22, rely=0.25, height=26, width=69)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(text="""Create""")
        self.Button6.bind("<Button-1>", lambda e: notepad_support.create_button(e))

        self.Button1 = Button(top)
        self.Button1.place(relx=0.4, rely=0.91, height=26, width=117)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text="""Exit""")
        self.Button1.bind("<Button-1>", lambda e: notepad_support.exit_button(e))

        self.errorOutput = Label(top)
        self.errorOutput.place(relx=0.03, rely=0.91, height=18, width=206)
        self.errorOutput.configure(activebackground="#f9f9f9")


if __name__ == "__main__":
    vp_start_gui()
