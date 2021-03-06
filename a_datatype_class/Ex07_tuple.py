"""
#----------------------------------------------------------
[튜플 자료형]
    1- 리스트와 유사하지만 튜플은 값을 변경 못한다.
    2- 각 값에 대해 인덱스가 부여
    3- 변경 불가능 (*****)
    4- 소괄호 () 사용
"""

# (1) 튜플 생성
print('------------------- 1. 튜플 생성-----------------')
t = (1, 2, 3)  # list = [1, 2, 3]
print(t)
print(t[0])

t2 = 1, 2, 3  # 되도록 사용하지 말 것
print(t2[-1])

# 빈 튜플 생성
t3 = ()
print(t3)
t4 = tuple()
print(t4)

# (2) 튜플은 요소를 변경하거나 삭제 안됨
# t[1] = 0;  # 블럭이 생기면서 실행 안됨
# del t[1]   # 에러 발생
print('------------------- 2 -----------------')
t = (1, 2, 3)
# t[1] = 0 변경 불가능
# del t[1] 삭제 불가능
del t  # 당연히 튜플 자체는 삭제 가능하다

# (3) 하나의 요소를 가진 튜플
print('------------------- 3 -----------------')
# ************
t2 = ('one',)  # 요소가 하나라면 우선순위 괄호로 취급함. 그렇기에 뒤에 콤마를 붙여야 한다.
print(t2)
print(t2[0])
print(type(t2))

t4 = tuple('one')
print(t4)
print(t4[0])
print(type(t4))

# (4) 인덱싱과 연산자 - 리스트와 동일
print('------------------- 4 -----------------')
t1 = (1, )
t2 = (5, 6, 7)
print(t1 + t2)
print(t2 * 2)
print(t2[-1])
print(t2[1:])

# (5) 튜플 요소 풀기
print('-' * 50)
t5 = (1, 2, 3)
a, b, c = t5
print(a+b+c)

# (6) 튜플과 리스트 형변환
print('-' * 50)
my_list = ['a', 'b', 'c']
my_tuple = ('z', 'y', 'x')
print(tuple(my_list)) # 튜플 형변환
print(list(my_tuple)) # 리스트 형변환

your_tuple = tuple(my_list)
print(type(your_tuple))