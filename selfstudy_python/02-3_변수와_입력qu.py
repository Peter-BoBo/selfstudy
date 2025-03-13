#변수 만들기/사용하기

# pi = 3.14159265
# r = 10
# print (pi)
# print (r)

# print("원주율=", pi)
# print("반지름=", r)
# print("원의 둘레=", 2* pi *r)
# print("원의 넓이=", pi * r * r)

#사용자 입력: input()

# 입력을 받습니다
# string = input("입력> ")

# # # 출력합니다
# print("자료:", string)
# print("자료형:", type(string))


# 입력받고 더하기
string = input("입력> ")

# 출력합니다
print("입력 + 100:", string + 100)

string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("숫자 자료:", int_a + int_b)
