# Boggle

Welcome to the Boggle game!\
This simple word search game challenges you to find as many words as you can on a 4x4 letter grid within a time limit.\
The game features a graphical user interface (GUI) built using the Tkinter library in Python.

![boggleExample](https://github.com/OriDriham/Boggle/assets/145263130/b698d434-c314-4ea1-8406-d8477d008b8e)


# File Descriptions

### boggle.py:
This file contains the main implementation of the Boggle game using Tkinter.\
It includes a GameBoard class for handling the game GUI and a Model class for managing the game state.

### boggle_board_randomizer.py:
This file provides a function to randomize the Boggle board with letters.\
It uses a predefined set of dice faces with letters to create a 4x4 letter grid.

### utils.py:
This file contains utility functions used in the Boggle game.\
It includes functions for loading a dictionary of words, checking the validity of a word path, finding words of a specific length, and identifying neighboring coordinates on the Boggle board.


# Usage

Make sure you have Python installed on your system.\
Run the Boggle game by executing the boggle.py file:

```sh
python boggle.py
```

The game window will appear, allowing you to start playing.


# How to Play

- Click the "Start" button to begin a new round of the game.
- The Boggle board will be filled with random letters, and the timer will start counting down from 3 minutes.
- Click on adjacent letters to form words. Words must be at least three letters long and can be formed by selecting horizontally, vertically, or diagonally adjacent letters.
- Click the "Add Word" button to submit a word.\
If the word is valid (found in the dictionary), your score will increase.
- Keep finding words until the timer reaches 0.
- Click the "Start" button to play another round.


# Game Features

- Real-time countdown timer.
- Score tracking based on word length.
- Randomized Boggle board for each round.
- Dictionary validation for submitted words.


### Enjoy the Boggle game and have fun finding words!
