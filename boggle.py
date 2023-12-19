import tkinter as tk
import time
import boggle_board_randomizer
import utils

BOARD_SIZE = 4


class GameBoard:
    def __init__(self, root, mod):
        """Initializes a GameBoard instance with the given root (Tkinter root
        window) and a Model instance.
        Configures the layout and design of the game board"""
        self.mod = mod
        root.title("Boggle")
        self.start = 0
        self.timer_1 = 180
        self._job = None
        self.cur_cords = []
        self.words_guessed = "words guessed:"
        self.cur_guess_str = " guess: "
        root.geometry("550x550")
        self.list_of_buttons = []
        self.head = tk.Label(root, text="boggle!", bg="lawn green",
                             font=("Modern", 44, "bold", "italic"))
        self.cur_guess = tk.Label(root, anchor=tk.W, text=self.cur_guess_str,
                                  bg="green yellow",
                                  font=("Modern", 34, "bold", "roman"),
                                  borderwidth=2, relief="sunken")
        self.word_frame = tk.Frame(root, bg='orange', width=100, height=100,
                                   borderwidth=1.5)
        self.timer_label = tk.Label(self.word_frame,
                                    text="time: " + str(self.timer_1),
                                    bg='mint cream',
                                    font=("Courier", 22, "bold", "roman"),
                                    borderwidth=2, relief="groove")
        self.start_button = tk.Button(self.word_frame, text='start',
                                      font=("Courier", 24, 'bold'),
                                      fg='firebrick3', bg='chartreuse2',
                                      bd=10, highlightthickness=2,
                                      highlightcolor="firebrick3",
                                      highlightbackground="chartreuse2",
                                      borderwidth=2, command=self.start_time)
        self.add_word_button = tk.Button(self.word_frame, text='add word',
                                         font=("Courier", 24, 'bold'), bd=10,
                                         highlightthickness=2,
                                         highlightcolor="black",
                                         highlightbackground="deep sky blue",
                                         borderwidth=2, command=self.add_word)
        self.score = tk.Label(self.word_frame,
                              text="score: " + str(mod.score),
                              pady=5, fg='firebrick3',
                              bg='OliveDrab2',
                              bd=10,
                              highlightthickness=4,
                              highlightcolor="firebrick3",
                              highlightbackground="OliveDrab2",
                              borderwidth=4, font=("Courier", 24, "bold"))
        self.word_label = tk.Label(self.word_frame, text=self.words_guessed,
                                   fg='#37d3ff',
                                   bg='#001d26',
                                   bd=10,
                                   highlightthickness=4,
                                   highlightcolor="#37d3ff",
                                   highlightbackground="#37d3ff",
                                   borderwidth=4, font=("Courier", 16))

        self.frame_board = tk.Frame(root, bg='green', width=300, height=300,
                                    borderwidth=1)
        self.pack()
        self.board_create()

    def start_time(self):
        """Starts the game timer and initializes the game board for a new
        round"""
        self.add_word_button["state"] = tk.NORMAL
        self.cur_cords = []
        self.words_guessed = "words guessed:"
        self.word_label["text"] = self.words_guessed
        self.cur_guess_str = " guess: "
        self.cur_guess["text"] = self.cur_guess_str
        self.mod.start_again()
        self.score["text"] = "score: " + str(self.mod.score)
        self.start = time.time()
        self.start_board()
        self.change_time()

    def change_time(self):
        """Updates the game timer during the game - counting from 180 (3 min)
        to 0"""
        #self.start_button.config(state=tk.DISABLED)
        self.timer_1 = 180 - int(time.time() - self.start)
        self.timer_label["text"] = "time: " + str(int(self.timer_1))
        self._job = game_root.after(5, self.change_time)
        self.stop_time()

    def stop_time(self):
        """Stops the game timer when it reaches 0"""
        if self.timer_1 <= 0:
            if self._job is not None:
                game_root.after_cancel(self._job)
                self._job = None
                self.end_board()
                self.start_again()

    def start_again(self):
        """Resets game elements and enables the self.start_button state while
        disabling the self.add_word_button state"""
        self.start_button["state"] = tk.NORMAL
        self.add_word_button["state"] = tk.DISABLED

    def board_create(self):
        """Creates and initializes the buttons on the game board (and adds
        them to a list)"""
        for i in range(0, len(self.mod.board)):
            self.list_of_buttons.append([])
            for j in range(0, len(self.mod.board)):
                self.list_of_buttons[i].append(
                    tk.Button(self.frame_board, width=6, height=4,
                              text=self.mod.board[i][j], relief="solid",
                              font=("Elephant", 30, 'bold'), bd=10,
                              highlightthickness=2,
                              highlightcolor="black",
                              highlightbackground="deep sky blue",
                              borderwidth=2))
                self.list_of_buttons[i][-1].place(relheight=0.5, relwidth=0.6,
                                                  relx=0.3, rely=0.2)
                tk.Grid.columnconfigure(self.frame_board, j, weight=1)
                tk.Grid.rowconfigure(self.frame_board, i, weight=1)
                self.list_of_buttons[i][-1].grid(row=i, column=j,
                                                 sticky="NSEW")

    def start_board(self):
        """Starts a new game board with random letters and enables button
        presses"""
        self.mod.start_board()
        for i in range(0, len(self.mod.board)):
            for j in range(0, len(self.mod.board)):
                self.list_of_buttons[i][j]["text"] = self.mod.board[i][j]
                self.list_of_buttons[i][j]["command"] = lambda x=i, y=j: \
                    self.press_letter(x, y)
                self.list_of_buttons[i][j]["state"] = tk.NORMAL

    def end_board(self):
        """Ends the current game board by disabling button presses (setting
        the command to None)"""
        for i in range(0, len(self.mod.board)):
            for j in range(0, len(self.mod.board)):
                self.list_of_buttons[i][j]["text"] = self.mod.board[i][j]
                self.list_of_buttons[i][j]["state"] = tk.DISABLED

    def end_not_neighbors(self, neighbors):
        """Disables the option to choose buttons that are not neighbors of the
        last selected button"""
        for i in range(0, len(self.mod.board)):
            for j in range(0, len(self.mod.board)):
                if (i, j) not in neighbors or (i, j) in self.cur_cords:
                    self.list_of_buttons[i][j]["state"] = tk.DISABLED

    def start_all(self):
        """starts a board with the option to press the buttons,
        and without choosing randomly new letters"""
        for i in range(0, len(self.mod.board)):
            for j in range(0, len(self.mod.board)):
                if (i, j) not in self.cur_cords:
                    self.list_of_buttons[i][j]["state"] = tk.NORMAL

    def press_letter(self, i, j):
        """Updates the current neighbors
        and display the current choice (letter) in the 'guess:' label"""
        if self.timer_1 > 0:
            self.cur_cords.append((i, j))
            self.cur_guess_str += self.mod.board[i][j]
            self.cur_guess["text"] = self.cur_guess_str
            self.start_all()
            neighbors = utils.neighbors(self.mod.board, i, j)
            self.end_not_neighbors(neighbors)
        else:
            self.end_board()

    def add_word(self):
        """
        preforms to action of adding a word the player chose. if the word is
        in the dictionary, the word will be added and the score will be raised
        """
        word = self.mod.check_path(self.cur_cords)
        self.cur_guess_str = " guess: "
        self.cur_guess["text"] = self.cur_guess_str
        if word:
            self.words_guessed += f"\n {word}"
            self.word_label["text"] = self.words_guessed
            self.mod.raise_score(len(word))
            self.score["text"] = "score: " + str(self.mod.score)
        self.cur_cords = []
        self.start_all()

    def pack(self):
        """Packs and organizes all the widgets in the Tkinter window"""
        self.head.pack(fill=tk.X)
        self.cur_guess.pack(fill=tk.X)
        self.word_frame.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        self.timer_label.pack(fill=tk.BOTH)
        self.start_button.pack(fill=tk.BOTH)
        self.score.pack(fill=tk.BOTH, expand=0)
        self.add_word_button.pack(fill=tk.BOTH, expand=0)
        self.word_label.pack(fill=tk.BOTH, expand=0)
        self.frame_board.pack(expand=1, fill=tk.BOTH)


class Model:
    def __init__(self):
        """Initializes a Model instance with an empty list of guessed words, a
        score of 0, a dictionary of words from a file, and an empty board"""
        self.guess_words = []
        self.score = 0
        self.word_dict = utils.load_words_dict('boggle_dict.txt')
        self.board = [['?' for _ in range(BOARD_SIZE)] for _ in
                      range(BOARD_SIZE)]

    def start_again(self):
        """
        sets self.guess_words and self.score back to default
        """
        self.guess_words = []
        self.score = 0

    def start_board(self):
        """sets the board with new random letters"""
        self.board = boggle_board_randomizer.randomize_board()

    def end_board(self):
        """sets the board with '?' as letters"""
        self.board = [['?' for _ in range(BOARD_SIZE)] for _ in
                      range(BOARD_SIZE)]

    def raise_score(self, n):
        """raises the score according to the chosen word"""
        # raise self.score + n^2
        self.score += n ** 2

    def check_path(self, path):
        """checks if a path is valid. if yes - returns the word, else - None"""
        word = utils.is_valid_path(self.board, path,
                                        self.word_dict.keys())
        if word:
            if not self.word_dict[word]:
                return None
            else:

                self.word_dict[word] = False
                return word
        return


if __name__ == "__main__":
    model = Model()
    game_root = tk.Tk()
    game_root["bd"] = 1.3
    G = GameBoard(game_root, model)
    game_root.mainloop()
    game_root.quit()
