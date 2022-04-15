#합계, 최대, 최소 과제 (+ 문제 풀이)
nums=[35,10,30,20,40,90,45]
print(nums)

sum = 0;
for i in nums :
  sum = sum + i
print('합계 : ', end = '')
print(sum)

max = 0
for j in nums :
  if j > max :
    max = j
print('최대 : ', end = '')
print(max)

min = 1000
for k in nums :
  if k < min :
    min = k
print('최소 : ', end = '')
print(min)

ave = 0
sum_a = 0
c = 0
for l in nums :
  sum_a = sum_a + l
  c = c + 1
ave = sum_a / c
print('평균 : ', end = '')
print(ave)