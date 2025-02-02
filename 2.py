def power(с,s):
    return c if s == 1 else c * power(c, s - 1)
    
c = int(input("Число: "))
s = int(input("Степінь: "))
print(f"{c}^{s} = {power(c, s)}")
