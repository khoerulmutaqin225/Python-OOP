class Team:
    def setTeam(self,team):
        self.team = team

    def showTeam(self):
        print(self.team)
        
class Tipe_Hero:
    # pass
    def setTipe(self,tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)
        

class Hero(Team,Tipe_Hero):
    
    def __init__(self,name, health):
        self.name = name
        self.health = health

Ucup = Hero('Ucup',100)
Ucup.setTeam('Merah')
Ucup.setTipe('Cundang')

Ucup.showTeam()
Ucup.showTipe()
