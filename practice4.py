#함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account() #호출을 해야 실행됨

#전달값과 반환값
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다." .format(balance+money))
    return balance+money
balance = 0
balance = deposit(balance, 1000) #입금이 완료되었습니다~
print(balance) #1000

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다." .format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다." .format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100 #수수료 100원
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다." .format(commission, balance))


#기본값
def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" .format(name, age, main_lang))
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")
#같은 학교, 학년, 반, 수업인 경우; 기본값 설정
def profile(name, age=17, main_lang="파이썬"): #따로 값을 주지 않으면 기본값으로 출력
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" .format(name, age, main_lang))
profile("유재석", 20)
profile("김태호")


#키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(name = "유재석", main_lang = "파이썬", age = 20) #함수와 변수 순서 달라도 키워드로 호출 가능


#가변 인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이: {1}\t" .format(name, age), end=" ") #end=" "는 줄바꿈하지 않는 설정
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

def profile(name, age, *language): #*을 통해 가변인자 설정 가능
    print("이름: {0}\t나이: {1}\t" .format(name, age), end=" ") 
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")


#지역변수와 전역변수
gun = 10 #전역변수
def checkpoint(soldiers): #경계근무
    gun = 20 #지역변수
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}" .format(gun))
print("전체 총: {0}" .format(gun))
checkpoint(2)
print("남은 총: {0}" .format(gun))

gun = 10 
def checkpoint(soldiers): #경계근무
    global gun #전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}" .format(gun))
print("전체 총: {0}" .format(gun))
checkpoint(2)
print("남은 총: {0}" .format(gun))

gun = 10
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}" .format(gun))
    return gun
print("전체 총: {0}" .format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총: {0}" .format(gun))


#Quiz_6
#표준 체중 구하는 프로그램
#남자: 키 * 키 * 22/여자: 키 * 키 * 21
#조건1: 표준 체중은 별도의 함수 내에서 계산. 함수명(std_weight), 전달값(키: heigt/성별: gender)
#조건2: 표준 체중은 소수점 둘째자리까지 표시

def std_weight(height, gender):
    if gender == "여자":
        return height * height * 21
    else:
        return height * height * 22

height = 175
gender = "남자"
weight = round(std_weight(height/100, gender), 2)
print("키 {0}cm {1}의 표준체중은 {2}kg 입니다." .format(height, gender, weight))



#표준 입출력
print("Python", "Java", sep = "")
print("Python", "Java", sep = " vs ")

print("Python", "Java", sep = ",", end = "?") #문장의 끝부분을 ?로 바꾸기(기본은 줄바꿈)
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file = sys.stdout) #표준출력
print("Python", "Java", file = sys.stderr) #에러처리

scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items(): #튜플로 생성
    print(subject, score) 
    print(subject.ljust(8), str(score).rjust(4), sep = ":") #문자에 대해 왼쪽 정렬, 오른쪽 정렬

#은행 대기순번표 001, 002, 003, ....
for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3)) #전체 크기를 3으로 보고, 값이 없으면 빈 공간을 0으로 채우기

#표준입력
answer = input("아무 값이나 입력하세요: ") #입력된 값은 str 
print("입력하신 값은 " + answer + "입니다.")


#다양한 출력 포맷
#빈 자리는 빈 공간으로 두고, 오른쪽 정렬, 총 10자리 확보
print("{0: >10}" .format(500)) #>오른쪽 정렬
#양수일 땐 +, 음수일 땐 -
print("{0: >+10}" .format(500)) 
print("{0: >+10}" .format(-200)) 
#왼쪽 정렬하고, 빈칸을 _로 채우기
print("{0:_<+10}" .format(500)) 
#3자리 마다 , 찍기
print("{0:,}" .format(1000000000)) 
#3자리 마다 , 찍기, +-부호 붙이기
print("{0:+,}" .format(1000000000)) 
print("{0:+,}" .format(-1000000000)) 
#3자리 마다 , 찍기, 부호 붙이고 자릿수 확보, 빈 자리는 ^ 표시채우기
print("{0:^<+20}" .format(1000000000)) 
#소수점 출력
print("{0:f}" .format(5/3))
#소수점 특정 자리까지 표시
print("{0:.2f}" .format(5/3))