# a =   11 => 3
# b =  101 => 5
# s = 1000 => 8

# e = 12 => 18
# f = 2A => 42
# e = 3C => 60
# 0, 1, 2 ,3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F -> hex

a = "1010" # 10
b = "1011" # 11
c = int(a, 2) + int(b, 2) # 21 10101

# 100
binary_string = ""

while c > 1:
    remainder = c % 2
    c = c//2
    binary_string = str(remainder) + binary_string 
    print(f"c={c}, r={remainder}, bs={binary_string}")

binary_string = str(c) + binary_string
print("binary string: ", binary_string)