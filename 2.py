def power(b, e):
    return b if e == 1 else b * power(b, e - 1)
    
b = int(input("Число: "))
e = int(input("Степінь: "))
print(f"{b}^{e} = {power(b, e)}")
