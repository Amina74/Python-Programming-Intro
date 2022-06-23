price = float(input("price :"))
payment = float(input("payment :"))
change = int(payment) - int(price)

print("change :", int(change))
a =change / 1000
print("1000kr bills :", int(a))
b = change % 1000
c = b / 500
print("500kr  bills :", int(c))
d = b % 500
e = d / 200
print("200kr  bills :", int(e))
f = d % 200
g = f / 100
print("100kr  bills :", int(g))
h = f % 100
i = h / 50
print("50kr   bills :", int(i))
j = h % 50
k = j / 20
print("20kr   bills :", int(k))
l = j % 20
m = l / 10
print("10kr   coins :", int(m))
n = l % 10
o = n / 5
print("5kr    coins :", int(o))
p = n % 5
q = p / 2
print("2kr    coins :", int(q))
r = p % 2
s = r / 1
print("1kr    coins :", int(s))
