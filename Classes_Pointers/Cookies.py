class Cookies:
    def __init__(self,color):
        self.color=color
    
    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color=color

cookie_one=Cookies("green")

cookie_two = Cookies('blue')

print('Cookie one is', cookie_one.getColor())
print('Cookie two is', cookie_two.getColor())

cookie_one.setColor('yellow')

print('\nCookie one is now', cookie_one.getColor())
print('Cookie two is still', cookie_two.getColor())

print("cookie one is ",cookie_one.getColor())

cookie_one.setColor("Yellow")

print("cookie one is now",cookie_one.getColor())