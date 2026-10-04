print("Hello, World!")

x = 5
y = 10
a = 1.5
b = [1, 2, 3]
d = (4, 5, 6)
c = {"key1": 4.8, "num2": 5.2, "char": "This is a string"}
c["char"] = "This is a new string"
c["num2"] = "New value for num2"
c["new_key"] = "This is a new key-value pair"
c["key1"] = "this is a key field"
#b[3] = 5  # This will raise an error because the index is out of range
b.append(4)  # This will add 4 to the end of the list
# d[1] = 10  # This will raise an error because tuples are immutable
z = x + y
print("The sum of", x, "and", y, "is", z)
print(b[2])
print(type(z))
print(type(a))
print(type(b))
print(a,b)
print(type(c))
print(type(d))
print(c["char"])
print(c["num2"])
print(c)
print(d[1])