# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game in Python. Practice string manipulation, loops, conditionals, user input, and random selection while creating a playable Hangman game.

## 📝 Tasks

### 🛠️ Create the Game Setup

#### Description

Create the starting logic for a Hangman game that randomly chooses a hidden word from a predefined list and prepares the game state.

#### Requirements

Completed program should:

- Store at least five possible words in a predefined list.
- Randomly select one word when the game starts.
- Track the letters guessed by the player.
- Set a clear number of incorrect guesses the player is allowed to make.


### 🛠️ Implement Guessing and Game Flow

#### Description

Use a loop to accept letter guesses, show the player's progress, and end the game when the word is guessed or no attempts remain.

#### Requirements

Completed program should:

- Accept one letter guess at a time from the player.
- Display the hidden word using underscores for letters that have not been guessed.
- Reduce the remaining attempts when the player guesses an incorrect letter.
- End with a win message when the player reveals the entire word.
- End with a lose message and reveal the word when the player runs out of attempts.
