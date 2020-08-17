import tkinter as tk

_WIDTH = 800
_HEIGHT = 450
_TITLE = "Dragon Killer"


def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width = _WIDTH, height = _HEIGHT)
    canvas.configure(background="black")
    canvas.pack()
    root.title(_TITLE)
    root.mainloop()


if __name__ == "__main__":
    main()

