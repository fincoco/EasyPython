#파일 만들어서 편집
score_file = open("score.txt", "w", encoding="utf8") #쓰기 목적으로 열기
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close() #항상 닫아주기!

#내용 추가하기
score_file = open("score.txt", "a", encoding="utf8") #append
score_file.write("과학 : 80") #줄바꿈이 따로 적용되지 않음. write()에서는
score_file.write("\n코딩 : 100")
score_file.close()


#파일 읽기
#파일 전체 읽기
score_file = open("score.txt", "r", encoding="utf8") #read
print(score_file.read()) 
score_file.close()

#한줄씩 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

#줄 수를 모를 때
score_file = open("score.txt", "r", encoding="utf8")
while True: #무한루프
    line = score_file.readline()
    if not line: #라인이 더이상 없을 때
        break 
    print(line, end="")
score_file.close()

#리스트에 각 줄 넣기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()


#pickle, 데이터를 파일 형태로 저장하기
import pickle
profile_file = open("profile.pickle", "wb") #wb 쓰기 바이너리, 인코딩 필요없음/파일 형태를 피클로
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 profile_file에 저장
profile_file.close()

#피클 데이터 가져오기
profile_file = open("profile.pickle", "rb") #rb 읽기 바이너리
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()


#with
import pickle
with open("profile.pickle", "rb") as profile_file: #따로 닫을 필요 없음
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


#Quiz_7
#당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력 되어야 합니다.

# - X 주차 주간보고 - 
# 부서 : 
# 이름 :
# 업무 요약 : 

#1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
for week in range(1, 11):
    with open(str(week)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("-{0} 주차 주간보고 -" .format(week), )
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")







