class Mangga:
    
    # Magic methode
    def __init__(self, name,jumlah):
        self.name = name
        self.jumlah = jumlah

    def __repr__(self):
        return"Debug - Mangga: {} dengan jumlah: {}".format(self.name,self.jumlah)

    def __str__(self):
        return"Mangga: {} dengan jumlah: {}".format(self.name,self.jumlah)
    
    def __add__(self, objek):
        return self.jumlah + objek.jumlah
    
belanja1 = Mangga("Arumanis", 10)
belanja2 = Mangga("Mana Lagi", 20)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)