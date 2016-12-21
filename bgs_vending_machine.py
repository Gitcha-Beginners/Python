# python 3.5.2
# -*- coding: utf-8 -*-


class VendingMachine(object):
    def __init__(self):
        # Initialize

        self.beverage_list = {1: {'name': 'Coke', 'price': 300},
                              2: {'name': 'Sprite', 'price': 200},
                              3: {'name': 'Coco-pam', 'price': 200},
                              4: {'name': 'Gatorade', 'price': 300},
                              5: {'name': 'Red-bull', 'price': 200}
                              }

        self.beverage_name = None
        self.beverage_price = None
        self.coin = None
        self.beverage_name = None
        self.power = 1

        print('Machine is ready !!')

    def beverage_out(self, option):

        self.beverage_name = self.beverage_list[option]['name']
        self.beverage_price = self.beverage_list[option]['price']

        if self.coin <= self.beverage_price:
            self.power = 0

        self.coin -= self.beverage_price

        print(self.beverage_name + " is out")
        print('exchange is ', self.coin, ' won')

    def start_machine(self):
        self.coin = int(input('Insert the coin : '))

        while self.power:
            option = int(input('1. Coke  2. Sprite  3. Coco-pam  4. Gatorade  5. Red-bull  6. Exit'))
            if option == 6:
                print(self.coin, 'won is out')
                break
            self.beverage_out(option)


if __name__ == '__main__':
    vending_machine = VendingMachine()
    vending_machine.start_machine()
