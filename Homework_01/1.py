class Car:
    def __init__(self, gas, capacity, gas_per_km, mileage):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = mileage

    def fill(self, liters):
        free_space = self.capacity-self.gas
        if liters > free_space:
            delta = liters-free_space
            liters = liters-delta
            print(f"заполняется полностью + {delta} не вместилось")
        else:
            print(f"Залили {liters} литров")
        self.gas += liters

    def ride(self, distance):
        required_fuel = self.gas_per_km * distance // 100
        real_dist = self.gas // self.gas_per_km * 100.0
        err_dist = ''
        if real_dist < distance:
            delta_dist = distance - real_dist
            self.gas = 0
            err_dist = f"топлива не хватает ещё на {delta_dist} км."
        else:
            self.gas -= required_fuel
            real_dist = distance
        self.mileage += real_dist
        print(f"Проехали {real_dist} км " + err_dist)

    def info(self):
        print(f"Количество бензина в баке: {self.gas} л.\nПробег: {self.mileage} км.")


car1 = Car(10, 50, 8, 1000)
car1.info()
print('=' * 30)

car1.fill(20)
car1.info()
print('=' * 30)

car1.ride(200)
car1.info()
print('=' * 30)

car1.fill(100)
car1.info()
print('=' * 30)

car1.ride(1000)
car1.info()
print('=' * 30)