import string

chars = []
with open('input5.test.txt') as f:
  while True:
    c = f.read(1)
    if not c or c == '\n':
      print("End of file")
      break
    inverter = c
    if c.isupper():
      inverter = c.lower()
    if c.islower():
      inverter = c.upper()
    if chars and chars[-1] == inverter:
      del chars[-1] 
    else:
      chars.append(c)
    #print(''.join(chars))
f.closed

each = dict({})
for a in list(string.ascii_lowercase):
  local = []
  for c in chars:
    if not c or c == '\n':
      print("End of file")
      break
    if c.lower() == a:
      continue
    inverter = c
    if c.isupper():
      inverter = c.lower()
    if c.islower():
      inverter = c.upper()
    if local and local[-1] == inverter:
      del local[-1] 
    else:
      local.append(c)
    #print(''.join(chars))
  each[a] = len(local)

#print(chars)
print(''.join(chars))
print(len(chars))
print(each)