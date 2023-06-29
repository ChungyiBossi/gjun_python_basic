a = "AA" # 170
b = "3F" # 63
c = int(a, 16) + int(b, 16) # 233

hex_string = ""
hex_map = {
    0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
    10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F' 
}

while c > 15:
    remainder = hex_map[c % 16]
    c = c//16
    hex_string = str(remainder) + hex_string 
    print(f"c={hex_map[c]}, r={remainder}, hs={hex_string}")

hex_string = hex_map[c] + hex_string
print("hex string = ", hex_string)