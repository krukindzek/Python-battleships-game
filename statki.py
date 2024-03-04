import random
import time
import tkinter as tk

comp_board = [['.' for _ in range(11)] for _ in range(11)]
buttons = [[None for _ in range(11)] for _ in range(11)]

def has_ship_or_neighbor(x, y):
    return comp_board[x][y] == 's' or \
           (0 <= x - 1 <= 10 and comp_board[x - 1][y] == 's') or \
           (0 <= x + 1 <= 10 and comp_board[x + 1][y] == 's') or \
           (0 <= y - 1 <= 10 and comp_board[x][y - 1] == 's') or \
           (0 <= y + 1 <= 10 and comp_board[x][y + 1] == 's') or \
           (0 <= x - 1 <= 10 and 0 <= y - 1 <= 10 and comp_board[x - 1][y - 1] == 's') or \
           (0 <= x - 1 <= 10 and 0 <= y + 1 <= 10 and comp_board[x - 1][y + 1] == 's') or \
           (0 <= x + 1 <= 10 and 0 <= y - 1 <= 10 and comp_board[x + 1][y - 1] == 's') or \
           (0 <= x + 1 <= 10 and 0 <= y + 1 <= 10 and comp_board[x + 1][y + 1] == 's')


def create_gui(root):
    for i in range(1, 11):
        for j in range(1, 11):
            value = comp_board[i][j]
            if comp_board[i][j] == 's':
                value = '.'
            btn = tk.Button(root, text=value, width=3, height=1, command=lambda x=i, y=j: on_button_click(x, y))
            btn.grid(row=i, column=j)
            buttons[i][j] = btn

    info_label = tk.Label(root, text="", fg="blue")  # Label to display info
    info_label.grid(row=12, column=1, columnspan=10)

    root.info_label = info_label  # Store info_label as an attribute of the root window

def random_comp_board(number_of_ships):
    random.seed(time.time())
    for i in range(11):
        for j in range(11):
            comp_board[i][j] = '.'
    for _ in range(number_of_ships):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        while has_ship_or_neighbor(x, y):
            x = random.randint(1, 10)
            y = random.randint(1, 10)
        comp_board[x][y] = 's'


def update_gui_buttons():
    for i in range(1, 11):
        for j in range(1, 11):
            value = comp_board[i][j]
            if comp_board[i][j] == 's':
                value = '.'
            btn = buttons[i][j]
            btn.config(text=value)


def on_button_click(x, y):
    global number_of_ships
    if comp_board[x][y] == 's':
        number_of_ships -= 1
        comp_board[x][y] = 'z'
    else:
        if comp_board[x][y] == '.':
            comp_board[x][y] = 'p'
    update_gui_buttons()
    if number_of_ships == 0:
        root.info_label.config(text="Koniec!! Gratulacje!!", fg="green")  # Update info_label with a congratulatory message
        time.sleep(3)
        root.destroy()


def info():
    info_str = "Gra w statki\nAutorzy: Jaroslaw Drzezdzon, Maksymilian Kruk\nData utworzenia: 2024-01-03\nWersja: 1.1"
    root.info_label.config(text=info_str, fg="blue")  # Update info_label with the info message
    time.sleep(3)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Battleship Game")

    number_of_ships = 3
    random_comp_board(number_of_ships)
    create_gui(root)
    info()
    root.mainloop()
