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
  frame_number = 1

  for i, throw in enumerate(throws):
    if frame_number == 10:
      yield list(zip(range(i, len(throws)), throws[i:]))
      return

    else:
      frame.append((i, throw))

      if throw == 'X' or len(frame) == 2:
        yield frame.copy()
        frame.clear()
        frame_number += 1

def score_frame(throws: str, frame: Frame) -> int:
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
