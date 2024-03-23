class Hero:
    
    # class variabel
    jumlah = 0
    __privatejumlah = 0
    
    def __init__(self, name, health):
        # instance variabel
        self.name = name
        self.health = health
        
        # variabel instance private
        self.__private = "private"
        #   variabel isntance protected
        self._protected = "protected"
        
        
        
lina = Hero('Lina', 100)
print(lina.__dict__)
print(Hero.__dict__)
print(Hero.__privatejumlah)
        