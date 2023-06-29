string_chinese = "這是一個字串"
string_chinese = "這不是一個字串吧?"
print(string_chinese)

# 底下再說明數值的使用方法
number_1 = 12
number_2 = 5
print(number_1 + number_2)
print(number_1, "+", number_2, "=", number_1 + number_2)
print(number_1, "-", number_2, "=", number_1 - number_2)
print(number_1, "*", number_2, "=", number_1 * number_2)
print(number_1, "/", number_2, "=", number_1 / number_2)
print(number_1, "//", number_2, "=", number_1 // number_2)
print(number_1, "%", number_2, "=", number_1 % number_2)

import math
number_3 = -2.648
print(number_3, "的Abs(絕對值): ", abs(number_3))
print(number_1, number_2, number_3, "的最大值:", max(number_1, number_2, number_3))
print(number_1, number_2, number_3, "的最小值:", min(number_1, number_2, number_3))
print(number_3, "的四捨五入是: ", round(number_3))
print(number_3, "的絕對值的方根是: ", math.sqrt(abs(number_3)))
print(number_3, "的絕對值取自然對數是: ", math.log(abs(number_3)))
print(number_3, "的絕對值取二的對數是: ", math.log2(abs(number_3)))
print(number_3, "的5次方: ", pow(number_3, 5))
print(number_3, "的5次方: ", number_3 ** 5)
print("自然數的", number_3, "次方", math.exp(number_3))
print("2的", number_3, "次方", math.exp2(number_3))


a = b = c = 50
c = 40
print(a, b, c)
c = a + b # c = 100
a = c + b # a = 150
b = a + c # b = 250
print(a, b, c)

