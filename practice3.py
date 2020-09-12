#if
weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else: 
    print("준비물 필요 없어요.")

temp = int(input("기온은 어때요?"))
if temp >= 30:
    print("너무 더워요, 나가지 마세요.")
elif 10 <= temp and temp <30:
    print("괜찮은 날씨에요")
elif 0 <= temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요, 나가지 마세요")


#for
for waiting in range(5):
    print("대기번호 : {0}" .format(waiting))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다." .format(customer))


#while; 조건이 만족될 때까지 실행 
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요." .format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer = "아이언맨"
index = 1
while True: #무한루프
    print("{0}, 커피가 준비 되었습니다. 호출 {1}회" .format(customer, index))
    index += 1

customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비 되었습니다." .format(customer))
    person = input("이름이 어떻게 되세요?")


#continue & break
absent = [2, 5] #결석
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue #skip할 수 있음
    if student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와" .format(student))
        break #반복문 바로 탈출
    print("{0}, 책을 읽어봐" .format(student))


#한줄 for
#출석번호가 1, 2, 3, 4 > 앞에 100을 붙이기로 함 ex. 101, 102, 103, ...
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)
#학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)
#학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)


#Quiz_5
#50명의 승객과 매칭 기회, 총 탑승 승객 수를 구하는 프로그램
#조건1: 승객별 운행 소요 시간은 5~50분 사이의 난수
#조건2: 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 합니다.
from random import *
count = 0 #총 탑승 승객 수
for i in range(1, 51):
    time = randrange(5, 51) #난수 생성은 for문 안에서!
    if 5 <= time <= 15:
        count += 1
        print("[O] {0}번째 손님 (소요시간: {1}분)" .format(i, time))
    else: 
        print("[ ] {0}번째 손님 (소요시간: {1}분)" .format(i, time))
print("총 탑승 승객: {0}분" .format(count))

