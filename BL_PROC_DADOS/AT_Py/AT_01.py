def square_range(start, stop, step=1):
  """
  Liste os quadrados

  Args:
    start: nº inicial da sequência gerada pela função range
    stop: nº onde a sequência gerada pela função range para (não incluído na sequência)
    step: diferença entre números consecutivos na sequência (c/ valor padrão 1)
  
  """

  if stop is None:
    stop = start
    start = 0

  return [x**2 for x in range(start, stop, step)]

print(square_range(1, 6, 2))