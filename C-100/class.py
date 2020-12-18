class car(object)
 """
   blueprint for car
 """
 def_init_(self, model, color, comapny, speed_limit):
     self.color = color
     self.company = company
     self.speed_limit = speed_limit
     self.model = model

 def start(self):
     print("started")

 def stop(self):
     print("stopped")

 def accelarate(self):
     print("accelarating...")
     "accelarator functionality here"

 def change_gear(self, gear_type):
     print("gear changed")
     " gear related functionality here"


audi = car("A6", "green", "audi", 80)

print(audi.start())