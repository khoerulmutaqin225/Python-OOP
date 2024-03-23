class Hero:
    
    # private class variabel
    __jumlah = 10
    
    def __init__(self, name):
        self.__name = name
        Hero.__jumlah +=1
    
    # Methode ini hanya berlaku untuk objek    # 
    def getJumlah(self):
        return Hero.__jumlah
    
    
    def getJumlah1():
        return Hero.__jumlah
    
    # methode static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
        
# membuat instance dari Class Hero    
    
sniper = Hero('Spiper')    
print(Hero.getJumlah2())
rikimaru = Hero('rikimaru')    
print(sniper.getJumlah2())
drowranger = Hero('drowranger')    
print(Hero.getJumlah3())