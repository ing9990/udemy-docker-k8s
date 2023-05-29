import random

min = int(input("Enter the min value: "))
max = int(input("Enter the max value: "))

print()

if min >= max:
    print("Invalid value")
else:
    print(random.randint(min, max))
i = int(input("숫자를 입력하세요."))


if str(i)[0] == '-':
  print("음수입니다.")
else if iLen >= 3:
  print("세 자릿수입니다.")
else:
  print("세 자릿수 미만입니다.")
