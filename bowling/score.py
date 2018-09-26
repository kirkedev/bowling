from typing import Iterator, Tuple, List

def score_throw(throw: str) -> int:
  if throw in ('X', '/'):
    return 10

  elif throw == '-':
    return 0

  else:
    return int(throw)

def split_frames(throws: str) -> Iterator[str]:
  frame = ''
  frame_number = 1

  for i in range(len(throws)):
    if frame_number == 10:
      yield throws[i:]
      return

    else:
      throw = throws[i]
      frame += throw

      if throw == 'X' or len(frame) == 2:
        yield frame
        frame = ''
        frame_number += 1

def score_throws(throws: str) -> int:
  return sum(map(score_throw, throws))

def score_game(throws: str) -> int:
  return sum(map(score_throws, split_frames(throws)))
