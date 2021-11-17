class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def my_location(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")


loc1 = Location("Tomas", "Portugal")
loc1.my_location()

loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
loc2.my_location()
loc3.my_location()
your_loc = Location("Your_Name", "Your_Country")
your_loc.my_location()
