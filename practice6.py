#클래스
#마린: 공격유닛, 군인, 총
name = "마린"
hp = 40
damage = 5
print("{} 유닛이 생성되었습니다." .format(name))
print("체력 {0}, 공격력 {1}\n" .format(hp, damage))

#탱크: 공격유닛, 탱크, 포, 일반모드/시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35
print("{} 유닛이 생성되었습니다." .format(tank_name))
print("체력 {0}, 공격력 {1}\n" .format(tank_hp, tank_damage))


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

#붕어빵 틀 같은 클래스! 변수와 함수의 집합
class Unit:
    def __init__(self, name, hp, speed): #기본 생성 함수, 필요한 것들을 모두 넣어야 함
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다." .format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}: {1} 방향으로 이동합니다. [속도 {2}]" .format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다" .format(self.name))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)  
tank = Unit("탱크", 40, 5)  

#멤버 변수, 클래스 내에서 정의된 변수
#생성된 유닛의 멤버변수를 외부에서 사용 가능
#레이스: 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력: {1}" .format(wraith1.name, wraith1.damage)) 

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True #clocking이라는 변수는 원래 없지만, 객채에 외부에서 변수 추가 가능(해당 객체에만 적용)
if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다." .format(wraith2.name))

#메소드와 상속
class AttackUnit(Unit): #공격유닛(자식클래스)은 일반유닛(부모클래스) 클래스의 변수를 상속
    def __init__(self, name, hp, speed, damage): #기본 생성 함수, 필요한 것들을 모두 넣어야 함
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location): #location은 메소드에서 전달받은 인자 사용하는 것
        print("{0}: {1} 방향을 적군을 공격합니다. [공격력 {2}]" .format(self.name, location, self.damage))
   
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    def stimpack(self)):
        if self.hp > 10:
            self.hp -= 10
            print("{0}: 스팀팩을 사용합니다. (HP 10감소)" .format(self.name))
        else:
            print("{0}: 체력이 부족하여 스팀팩을 사용하지 않습니다." .format(self.name))
    

#파이어뱃: 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시") #self는 넣을 필요 없음
firebat1.damaged(25)
firebat1.damaged(20)
firebat1.damaged(10)

#다중 상속(부모 클래스가 2 이상)
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0}: {1} 방향으로 날아갑니다. [속도 {2}]" .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): #, 로 구분하면 됨
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #self 꼭 쓸 것! speed는 0으로 일괄 처리
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

#연산자 오버로딩
vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시") #move라는 같은 이름의 함수 재정의(같은 이름으로 사용 가능)

#pass
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") #init함수 내에서 인자 없어도 그냥 pass

#super
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0) #speed를 0으로 생각하고 고정
        super().__init__(name, hp, 0) 
        #self 없이 상속 초기화 가능/대신 다중 상속시 앞에서 상속하는 부모 클래스만 인식하게 됨.
        self.location = location


#스타크래프트 전반전 문제는 유튜브로!

#Quiz_8
#코드 활용하여 부동산 프로그램 작성

class House:
    def __init__(self, location, htype, deal, price, year):
        self.location = location
        self.htype = htype
        self.deal = deal
        self.price = price
        self.year = year

    def show_detail(self):
        print(self.location, self.htype, self.deal, self.price, self.year)

houses = []
house1  = House("강남", "아파트", "매매" ,"10억","2010년")
house2  = House("마포", "오피스텔", "전세", "5억", "2007년")
house3  = House("송파", "빌라", "월세", "500/50", "2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다" .format(len(houses)))
for house in houses:
    house.show_detail()
