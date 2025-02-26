class BMW:
    def speed(self):
        print("The speed of BMW: 191 MPH")
    
    def horsepower(self):
        print("The horsepower of BMW: 550 hp")
        
    def layout(self):
        print("layout of BMW: front-engine, rear-wheel drive")

class Ferrari:
    def speed(self):
        print("The speed of Ferrari: 217 MPH")
    
    def horsepower(self):
        print("The horsepower of Ferrari: 880 hp")
        
    def layout(self):
        print("layout of Ferrari: Rear mid-engine, all-wheel-drive")
        
bmw= BMW()
ferrari = Ferrari()

for car in (bmw, ferrari):
    car.speed()
    car.horsepower()
    car.layout()
    print()