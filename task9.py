a = [90,85,70,75,80]
average = sum(a) / len(a)
print(average)
grade = 0
if average in range(91,101):
    print('A+')
if average in range(81,91):
    print('A')
if average in range(71,81):
    print('B')
if average in range(61,71):
    print('C')
if average in range(51,61):
    print('D')
if average == 50 or average < 50:
    print('F')
