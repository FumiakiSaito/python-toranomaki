###################################
# 条件分岐
###################################

x = 1
y = 2

if x == 1:
  print("xと1は同じ")

if x == 1 and y == 2:
  print("xと1は同じ かつyは2と同じ")

if x == 1 or y == 3:
  print("xと1は同じ またはyは2と同じ")

if x == 2:
  print("xと2は同じ")
else:
  print("xと2は違う")

if x == 2:
  print("xと2は同じ")
elif x == 3:
  print("xと3は同じ")
else:
  print("xは2でも3でもない")

num = 'a'

if not num.isdigit():
  print("numは数字ではありません")


