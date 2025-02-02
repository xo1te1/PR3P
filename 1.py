def km_miles(km):
    return km * 0.621371

km = float(input("Введіть відстань у км: "))
miles = km_miles(km)
print(f"{km} км = {miles} миль")