# -*- coding: utf-8 -*- 
class VendingMachine:

    def __init__(self):
        self.drinks = {
            "포카리": 800,
            "토레타": 1200,
            "코카콜라": 800,
            "웰치스": 1500,
            "2프로": 800,
            "비락식혜": 600,
            "데자와": 700,
            "게토레이": 800,
        }

    def start(self):
        finish = 'doing'
        while finish != 'exit':
            money = int(input("금액을 입력해 주세요 : "))
            self.show_drinks()
            choice = input("음료를 입력해 주세요 : ")
            cnt = int(input("개수를 입력해 주세요"))
            if self.drinks[choice]*int(cnt) > int(money):
                print("현재금액 {}원".format(money))
                print('금액이 {}원 부족합니다'.format(self.drinks[choice]*cnt - money))
                if input('금액추가: go or 종료: exit : ') == 'go':
                    money += int(input('추가할 금액을 입력해 주십시오'))
                else:
                    break

            print("{}가 나왔습니다".format(choice))
            money -= self.drinks[choice]*int(cnt)
            print("계속 하시겠습니까? ")
            finish = input("계속하기 : yes 종료 : exit")

    def show_drinks(self):
        for product, price in self.drinks.items():
            print("{} {}원".format(product,price))


