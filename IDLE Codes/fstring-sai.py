'''
Author: Saikumar Srinivas
Filename: fstring-sai.py
Purpose: Coin Counter
'''

# f-string exercises
# x, y, z variables for the exercise
x = 27
y = 3.14159
z = 'pi'

# 10 different exercises of increasing complexity

# #1
s = f'{x} is a whole number'
print(f"#1 ...\n{s}")

# #2
s = f'{x} is {type(x)}'
print(f"#2 ...\n{s}")

# #3
q = f"{z} to 6 digits is {y:.5f}"
print(f"#3 ...\n{q}")

# #4
q = f"{z} to 3 digits is {y:.2f}"
print(f"#4 ...\n{q}")

# #5
r = f"{z} to 4 digits is {y:.3f}"
print(f"#5 ...\n{r}")

# #6
r = f"{x:^10} {y:^10} {z:^10}"
print(f"#6 ...\n{r}")

# #7
r = f"{'x':^10}{'y':^10}{'z':^10}\n{x:^10}{y:^10}{z:^10}\n"
print(f"#7 ...\n{r}")

# #8
q = f"${x:.2f}{'':<4}${y:.2f}{'':<5}"
print(f"#8 ...\n{q}")

# #9
q = f"{'':^2}${x:.2f}{'':^4}${y:.2f}{'':^3}"
print(f"#9 ...\n{q}")

# #10
s = f"{'':^1}${x:7.2f}{'':^2}${y:7.2f}{'':^1}"
print(f"#10 ...\n{s}")
