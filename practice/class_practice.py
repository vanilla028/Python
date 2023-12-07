class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            print(f"The {self.year} {self.make} {self.model}'s engine is now running.")
            self.is_running = True
        else:
            print("The engine is already running.")

    def stop_engine(self):
        if self.is_running:
            print(f"The {self.year} {self.make} {self.model}'s engine is now stopped.")
            self.is_running = False
        else:
            print("The engine is already stopped.")

# 객체 생성
my_car = Car(make="Toyota", model="Camry", year=2022, color="Blue")

# 객체의 속성에 접근
print(f"My car is a {my_car.year} {my_car.make} {my_car.model} in {my_car.color} color.")

# 객체의 메서드 호출
my_car.start_engine()
my_car.stop_engine()
my_car.start_engine()
