from itertools import accumulate
from typing import Iterator, Tuple, List

def score_throw(throw: str) -> int:
  if throw in ('X', '/'):
    return 10

  elif throw == '-':
    return 0

  else:
    return int(throw)

def is_spare(frame: str) -> int:
  return frame[1] == '/'

def is_strike(frame: str) -> int:
  return frame[0] == 'X'

def split_frames(throws: str) -> Iterator[str]:
  frame_number = 1
  i = 0

  while i < len(throws):
    if frame_number == 10:
      yield throws[i:]
      return

    else:
      end = i + 2
      frame = throws[i:end]

      if is_strike(frame):
        yield frame + throws[end: end + 1]

      else:
        if is_spare(frame):
          yield frame + throws[end: end + 1]
        else:
          yield frame

        i += 1

      frame_number += 1
      i += 1

def score_throws(throws: str) -> int:
  return sum(map(score_throw, throws))

def score_frame(frame: str) -> int:
  if is_strike(frame):
    return 10 + score_throws(frame[1:])

  if is_spare(frame):
    return 10 + score_throws(frame[2])

  else:
    return score_throws(frame)

def score_game(throws: str) -> Iterator[int]:
  return accumulate(map(score_frame, split_frames(throws)))
