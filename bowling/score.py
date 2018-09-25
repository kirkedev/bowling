def score_throw(throw: str) -> int:
  if throw == 'X':
    return 10

  elif throw == '/':
    return 10

  else:
    return int(throw)
