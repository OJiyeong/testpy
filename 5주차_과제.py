print('문제 1 (김다은)')
str = '   Class Java'
print(str)
str_new = str.strip()
str_py = str_new[: 6] + 'Python'
print(str_py)
print('7번째 문자 : ' + str_py[6] + '\n')

print('문제 2 (곽지은)')
menu = '스테이크 pizza 파스타 콜라'
print(menu)
print('1) 문자열의 문자 갯수는?', end = ' > ')
print(len(menu))
print('2) 맨 마지막 문자를 출력하시오.', end = ' > ')
print(menu[len(menu)-1])
print('3) 영어와 한글을 구별하여 출력하시오.', end = ' > ')
menu_eng = ''
menu_kor = ''
for x in menu :
    if x >= 'a' and x <= 'z' :
        menu_eng = menu_eng + x;
    else :
        menu_kor = menu_kor + x;
print('영어 : ' + menu_eng, end = ', ')
print('한글 : ' + menu_kor + '\n')