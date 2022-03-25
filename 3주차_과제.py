data = [32, 14, 55, 23, 12, 67, 44]
print(data)
print('')

#1) 30 이상 출력
print('1. 30 이상 : ', end = '')
for x in data :
    if x >= 30 :
        print(x, end = ' ')
print('\n')

#2) 40 보다 크고 50 미만 출력
print('2. 40 보다 크고 50 미만 : ', end = '')
for x in data :
    if x > 40 and x < 50 :
        print(x, end = ' ')
print('\n')

#3) 20 보다 작거나 50 이상 출력
print('3. 20 보다 작거나 50 이상 : ', end = '')
for x in data :
    if x < 20 or x >= 50 :
        print(x, end = ' ')
print('\n')

#4) 홀수값 출력
print('4. 홀수 : ', end = '')
for x in data :
    if x % 2 != 0 :
        print(x, end = ' ')
print('\n')


#5) 30 이상 갯수
i = 0
for x in data :
    if x >= 30 :
        i = i + 1
print('5. 30 이상 : ' + str(i))
print('')

