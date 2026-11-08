ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# your code here
# list 可変性
ft_list.append("World!")

# tuple 不変性
ft_tuple = ft_tuple[:1] + ("Japan!", )

# set 順序 set型は順序を持たない仕様になっているので、出力順は不規則。
ft_set.remove("tutu!")
ft_set.add("Tokyo!")

# dict 一意性
ft_dict["Hello"] = "42Tokyo!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
