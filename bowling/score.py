from functools import reduce
from operator import add
from typing import Iterator, Tuple, List

Throw = Tuple[int, str]
Frame = List[Throw]

def score_throw(throw: str) -> int:
  if throw == 'X':
    return 10

  elif throw == '/':
    return 10

  elif throw == '-':
    return 0

  else:
    return int(throw)

def split_frames(throws: str) -> Iterator[Frame]:
  frame: List[Throw] = []

  for i, throw in enumerate(throws):
    frame.append((i, throw))

    if throw == 'X' or len(frame) == 2:
      yield frame.copy()
      frame.clear()

def score_frame(throws: str, frame: Frame) -> int:
  i, last_throw = frame[-1]

  if last_throw == 'X':
    return 10 + score_game(throws[i + 1: i + 3])

  elif last_throw == '/':
    return 10 + score_throw(throws[i + 1])

  else:
    return reduce(add, map(lambda it: score_throw(it[1]), frame))

def score_game(throws: str) -> int:
  return reduce(add, map(lambda it: score_frame(throws, it), split_frames(throws)), 0)
