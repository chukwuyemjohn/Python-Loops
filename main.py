students = ['Joel','Harry','Ben']
for name in students:
  print("hi Mr",name)
# ===============

print(range(10))
print(list(range(10)))
print(list(range(3,9)))
print(list(range(3,12,2)))

# ==================

for i in range(1, 6):
  for j in range(i):
    print(i, end=" ")
  print()
# ===================
for i in range(1,10):
  if i == 3:
    continue
  print(i)
# ===================

'''
For in Loop
'''
students = ['Bob', 'Adriana', 'Felix']

for x in students:
    print("hi", x)

# ==========================

print(range(10))
print(list(range(10)))
print(list(range(3, 6)))
print(list(range(3, 12, 3)))

# ==========================

for x in range(1, 6, 2):
    print(x * 2)

# ==========================

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
# ==========================
'''
While Loop
'''

i = 1
while i < 10:
    print(i)
    i += 1

# ==========================
# break statements

i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# ==========================
# continue statements

i = 1
while i < 5:
    i += 1
    if i == 4:
        continue
    print(i)

# ==========================

for i in range(1, 10):
    if i == 3:
      break
    print(i)