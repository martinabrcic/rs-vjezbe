import math

class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return round(2 * self.r * math.pi, 3)
    
    def povrsina(self):
        return round(self.r ** 2 * math.pi, 3)
    
krug = Krug(8)
print(krug.opseg())
print(krug.povrsina())