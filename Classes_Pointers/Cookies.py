class Cookies:
    def __init__(self,color):
        self.color=color
    
    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color=color

cookie_one=Cookies("green")class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())

print("cookie one is ",cookie_one.getColor())

cookie_one.setColor("Yellow")

print("cookie one is now",cookie_one.getColor())