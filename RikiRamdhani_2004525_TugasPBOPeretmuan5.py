class Negara:
    def intro (self):
        print("Di dunia terdapat banyak negara-negara di dalamnya")

    def IbuKota(self):
        print("Di setiap negara memiliki Ibu Kota ")

    
class Indonesia(Negara):
   def IbuKota(self):
        print("Ibu Kota negara Indonesia ialah Jakarta ")
    

class Malaysia(Negara):
     def IbuKota(self):
        print("Ibu Kota negara Malaysia ialah Kuala Lumpur  ")
    

obj_Negara = Negara()
obj_Indonesia = Indonesia()
obj_Malaysia = Malaysia()

obj_Indonesia.intro()
obj_Indonesia.IbuKota()

print("\n")

obj_Malaysia.intro()
obj_Malaysia.IbuKota()