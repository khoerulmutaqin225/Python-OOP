class Hero: #Template
    pass

hero1 = Hero()  #Objeck / instance (instantiane)
hero2 = Hero()  #Objeck / instance (instantiane)
hero3 = Hero()  #Objeck / instance (instantiane)

hero1.name = "sniiper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 100

hero3.name = "ucup"
hero3.health = 400


print(hero1.__dict__)
print(hero1.name)
print(hero1)