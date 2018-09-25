from functools import reduce
from operator import add
from typing import Iterator

def score_throw(throw: str) -> int:
  if throw == 'X':
    return 10

  elif throw == '/':
    return 10

  elif throw == '-':
    return 0

  else:
    return int(throw)

def find_strikes(throws: str) -> Iterator[int]:
  for i, throw in enumerate(throws):
    if throw == 'X':
      yield i

def score_throws(throws: str) -> int:
  strikes = find_strikes(throws)

  total = 0

  for strike in strikes:
    total += score_throws(throws[strike + 1: strike + 3])

  total += reduce(add, map(score_throw, throws))

  return total
