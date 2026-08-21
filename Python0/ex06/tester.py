from ft_filter import ft_filter


def is_even(n: int) -> bool:
    return n % 2 == 0


def is_allTrue(n: int) -> bool:
    return (True)


print(ft_filter.__doc__)
print(filter.__doc__)
numbers = [1, 2, 3, 4, 5, 6]
print(f"本家：{filter(is_even, numbers)}, {list(filter(is_even, numbers))}\n\
自作：{ft_filter(is_even, numbers)}, {list(ft_filter(is_even, numbers))}")

print("\n")

numbers = [1, 2, 3, 4, 5, 6]
print(f"本家：{filter(is_allTrue, numbers)}, {list(filter(is_allTrue, numbers))}\n\
自作：{ft_filter(is_allTrue, numbers)}, {list(ft_filter(is_allTrue, numbers))}")

print("\n")

fruits = ["apple", "banana", "cherry", "date", "grape"]
fruits_with_a = filter(lambda fruit: 'a' in fruit, fruits)
ft_fruits_with_a = ft_filter(lambda fruit: 'a' in fruit, fruits)
print(f"本家：{fruits_with_a}, {list(fruits_with_a)}\n\
自作：{ft_fruits_with_a}, {list(ft_fruits_with_a)}")
