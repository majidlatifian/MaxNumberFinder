list=[]
while True:
  a=int(input())
  list.append(a)
  if a == -1:
    break
print(max(list), ' ')