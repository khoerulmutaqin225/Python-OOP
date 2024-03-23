# Methode adalah blok kode yang berfungsi melakukan tugas tertentu
class Hero:
    # Class variabel
    jumlah_hero = 0
    
    def __init__(self, inputName, inputHealth, inputAttack, inptArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack
        self.armor = inptArmor
        Hero.jumlah_hero += 1
        # Increment class variable when create a new object
        
    # void function, methode tanpa return , tanpa argumen
    def siapa(self):
        print('namaku adalah ' + self.name)
        
    # methode dengan argument
    def healthUp(self, up):
        self.health += up

    # methode dengan return
    def getHealth(self):
        return self.health
        
hero1 =Hero('Sniper', 100,10,5)
hero2 =Hero('Sniper', 100,2,10)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())