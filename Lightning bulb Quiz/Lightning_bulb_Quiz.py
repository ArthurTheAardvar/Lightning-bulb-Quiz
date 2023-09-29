import random

gameover = False

class lightbulb:
    def __init__(self):
        self.On = False
        self.Off = True
        self.Burnt = False
        self.r = random.randrange(0,255)
        self.g = random.randrange(0,255)
        self.b = random.randrange(0,255)

#I just merged the burnt out and whether it was on or off, cuz it makes more sense #Mo code
    def burntout(self):
        num = random.randrange(0,100)
        print(num)
        if num >= 5:
            print("The lightbulb is not burnt and the rgb is", self.r, self.g, self.b)

            choice = input("Do you want the light on or off? ")

            if choice == "on":
                print("The light is on now")
                self.On = True
                self.Off = False
            elif choice == "off":
                print("The light is off now")
                self.On = False
                self.Off = False
        else:
            print("lightbulb burnt out")
            self.Burnt = False
            self.Off = False
           

    

light = lightbulb()
light2 = lightbulb()
light3 = lightbulb()


light.burntout()
light2.burntout()
light3.burntout()