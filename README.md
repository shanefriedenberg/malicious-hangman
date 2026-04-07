# Malicious Hangman

A version of hangman where the computer cheats. It doesn't pick a word at the start. Instead it keeps a set of every word that's still possible given the player's guesses, and after each guess it shrinks that set as little as it can. The result is the computer is basically always playing the worst possible word for you, but it's still a real word.

Written in Python for a Data Structures class at the University of Denver.

## How it works

The dictionary gets loaded into a set, filtered by word length. On each guess, the `select_new_word` function goes through the candidate set and removes any word containing a guessed letter, but only if that still leaves words behind. Once the set can't shrink any more without going empty, the game finally commits to one of the remaining words and the player actually has to guess the letters in it.

The interesting part is that the computer doesn't have a real word until it's forced to pick one.

## Running it

You need Python 3 and a word list saved as `Dictionary.txt` in the same folder (one word per line).

```
python friedenberg_COMP1353_Project4_hangmanp2.py
```

It will ask for a word length and how many guesses you want, then start the game.

## Files

- `friedenberg_COMP1353_Project4_hangmanp2.py` - the game (has both regular and malicious mode)
- `Dictionary.txt` - bring your own word list
