class vehicle:
    def start(self):
        print("vehicle")


class car(vehicle):
    def end(self):
        print("car")
c1=car()
c1.start()
c1.end()