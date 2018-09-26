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

def score_frame(throws: str, frame: str) -> int:
  throw, *_ = frame

  if throw[1] == 'X':
    i = throw[0]
    return 10 + score_game(throws[i + 1: i + 3])

  _, throw, *_ = frame

  if throw[1] == '/':
    i = throw[0]
    return 10 + score_throw(throws[i + 1])

  else:
    return sum(map(lambda it: score_throw(it[1]), frame))

def score_game(throws: str) -> int:
  return sum(map(lambda it: score_frame(throws, it), split_frames(throws)))
