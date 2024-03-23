from abc import ABC, abstractmethod

# Abstract Class
class Button(ABC):
    
    def __init__(self, set_Link):
        self.link = set_Link
    
    @abstractmethod
    def click(self):
       pass
   
    @property   
    @abstractmethod
    def link(self):
        pass
        
# Child Class
class PushButton(Button):
    def click(self):
        # kita tau self.link adalah getter setter dari line 23 - 34
        print("Go To: {}".format(self.link))
    
    # getter
    @Button.link.getter 
    def link(self):
        return self.__link
    
    # Setter
    # @Button.link.setter (button tidak perlu ditambahkan karena sudah di define di getter)
    @link.setter
    def link(self, input):
        self.__link = input

# tombol1 adalah instance class
tombol1 = PushButton("www.kelasterbuka.id")
tombol1.click()
