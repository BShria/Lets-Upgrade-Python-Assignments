# print the key with the maximum value in a dictionary

marks = {
  'Shria': 91,
  'Sam': 81,
  'Ani': 88,
  'Arko': 93,
  'Shan': 76
}

ans = max(marks, key = marks.get)
print(ans)

