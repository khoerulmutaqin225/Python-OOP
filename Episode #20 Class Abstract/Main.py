# Membuat Class Abstract
# abc = abstract base class

# TypeError: Can't instantiate abstract class Button without an implementation for abstract method 'click'
# Abstrack berfungsi agar class tersebut tidak bisa dibuat instance class dan harus membuat child classs
# Abstrack class adalah blue print untuk Child class

from abc import ABC, abstractmethod

# Abstract Class
class Button(ABC):
    
    @abstractmethod
    def click(self):
       pass
        
# Child Class
class PushButton(Button):
    def click(self):
        print("push button click")
    

# Child Class
class RadioButton(Button):
    
    def click(self):
        print("radio button click")



tombol1 = PushButton()
tombol2 = RadioButton()
tombol1.click()
tombol2.click()
# help(tombol1)
