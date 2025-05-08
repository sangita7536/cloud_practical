def is_safe(assigment,row,col):
  for r in range(n):
    c=assigment[r]
    if c==col or abs(c-col)==abs(r-row):
      return False
  return True

def backtrack(assigment,row,n):
  if row==n:
    print_solution(assigment,n)
    return
  for col in range(n):
    if is_safe(assigment,row,col):
      assigment[row]=col
      backtrack(assigment,row+1,n)
      assigment[row]=-1

def print_solution(assigment,n):
  for row in range(n):
    line=""
    for col in range(n):
      line += " Q" if assigment[row]=col else "."
      print(line)
  print()
    
def n_queen(n):
  assigment=[-1]*n
  backtrack(assigment,0,n)
n_queen(4)
