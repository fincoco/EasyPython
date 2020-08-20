# 참/거짓(boolean)
print(5>10)
print(True)
print(not True)

#변수
animal = "강아지"
name = "펭도리"
age = 4
hobby = "산책"
is_adult = age >= 3

#int, boolean 변수는 str으로 변환 후 연산 가능
print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) +"살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

#Quiz_1_sol1
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

#Quiz_1_sol2
station = ["사당", "신도림", "인천공항"]
for i in range(len(station)):
    print(station[i] + "행 열차가 들어오고 있습니다.")

#연산자
number = 2 + 3 + 4
number = number + 2
number += 2
print(number)

#숫자 처리 함수
print(abs(-5)) 
print(pow(4, 2)) #4^2
print(max(5, 12))
print(min(5, 13))
print(round(4.5555, 2))

from math import *
print(floor(4.99)) #내림, 4
print(ceil(3.14)) #올림, 4
print(sqrt(16)) #제곱근, 4

#랜덤 함수
from random import *
print(random()) #0.0~1.0 미만 임의의 값 생성
print(random() * 10) 
print(int(random() * 10))
print(int(random() * 10) + 1)

print(randrange(1, 45)) #1 ~ 45 미만의 임의의 값 생성
print(randint(1, 45)) #1 ~45 이하의 임의의 값 생성

#Quiz_2
from random import randint
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

#문자열
sentence = '나는 소녀입니다'
print(sentence)
sentence2 = "나는 소년입니다"
print(sentence2)

#슬라이싱
jumin = "990120-1233456"
print("성별 : " + jumin[7])
print("연도 : " + jumin[0:2])
print("뒤 7자리 : " + jumin[-7:])

#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python.replace("Python", "Java"))

index = python.index("n") #처음에 등장한 값만
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) #False인 경우 -1 반환
print(python.index("Jave")) #에러값 

print(python.count("n"))

#문자열 포맷
print("a" + "b")
print("a", "b")

#방법1
print("나는 %d살입니다." % 20) #%d 정수, %f 소수
print("나는 %s을 좋아해요" % "파이썬") #%s 문자열
print("Apple은 %c로 시작해요." % "A") #%c 한글자만 가져오기
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

#방법2
print("나는 {}살 입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))

#방법4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
