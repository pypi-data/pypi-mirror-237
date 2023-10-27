import random
import sys
import time


def dice(sides: int = 6):
    return random.randrange(sides) + 1
def scramble(word: str):
  scrambled = ""
  while word:
    position = random.randrange(len(word))
    scrambled += word[position]
    word = word[:position] + word[(position + 1):]

  return scrambled
def type(string = "", delay = 0.06):
  for char in string:
    time.sleep(delay)
    sys.stdout.write(char)
    sys.stdout.flush()

