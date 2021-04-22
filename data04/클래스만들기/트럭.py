class Truck:

    weight = None
    company = None

    def move(self):
        print(self.weight +'톤의 짐을 실어나르다.')
    def own(self):
        print(self.company + '회사 소속의 트럭입니다.')

    def __str__(self):
        return self.weight + ',' + self.company

if __name__ == '__main__':
    truck1 = Truck()
    truck1.weight = str(1)
    truck1.company = "mega"

    print(truck1)
    print(truck1.weight)
    print(truck1.company)
    truck1.move()
    truck1.own()