from functools import reduce
from operator import add
from typing import Iterator, Tuple, List

Throw = Tuple[int, str]
Frame = List[Throw]
Game = Iterator[Frame]

def score_throw(throw: str) -> int:
  if throw == 'X':
    return 10

  elif throw == '/':
    return 10

  elif throw == '-':
    return 0

  else:
    return int(throw)

def split_frames(throws: str) -> Game:
  frame: List[Throw] = list()

  for i, throw in enumerate(throws):
    print(i, throw)
    frame.append((i, throw))

    if throw == 'X' or len(frame) == 2:
      yield frame.copy()
      frame.clear()

def score_throws(throws: str) -> int:
  total = 0

  for frame in split_frames(throws):
    print(frame)
    i, last_throw = frame[-1]

    if last_throw == 'X':
      total += 10 + score_throws(throws[i + 1: i + 3])

    elif last_throw == '/':
      total += 10 + score_throw(throws[i + 1])

    else:
      for i, throw in frame:
        total += score_throw(throw)

  return total
