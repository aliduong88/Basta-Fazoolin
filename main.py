class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + " menu available from " + str(self.start_time) + " to " + str(self.end_time)

  def calculate_bill(self,purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill
    
# Brunch Menu
brunch = Menu("Brunch",{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
},11,16)

# Early Bird Menu
early_bird = Menu("Early_Bird",{'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},15,18)

# Dinner Menu
dinner = Menu("Dinner",{'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},17,23)

# Kids Menu
kids = Menu("kids",{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
},11,21)

menus = [brunch, early_bird, dinner, kids]

print(brunch)
print(brunch.calculate_bill(['pancakes','home fries','coffee']))
print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))


class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
   
  def __repr__(self):
    return "The store address is " + self.address

  def available_menus(self,time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

    
flagship_store = Franchise("1232 West End Road",menus)
new_installment = Franchise("12 East Mulberry Street",menus)

print(flagship_store)
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))


class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises  = franchises

basta_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Arepa Menu
arepas_menu = Menu("Take a' Arepa",
  {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
},10,20)

arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])

arepa_business = Business("Take a' Arepa",[arepas_place])

print(arepa_business.franchises[0])
print(arepa_business.franchises[0].menus[0])