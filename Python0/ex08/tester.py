from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


print("========普通 range(333) =======")
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()


print("========始まりと終わりを指定 range(0, 1) =======")
for elem in ft_tqdm(range(0, 1)):
    sleep(0.005)
print()
for elem in tqdm(range(0, 1)):
    sleep(0.005)
print()


print("========途中で始まる range(10, 20) =======")
for elem in ft_tqdm(range(10, 20)):
    sleep(0.005)
print()
for elem in tqdm(range(10, 20)):
    sleep(0.005)
print()


print("========始まりと終わりが同じ range(20, 20) =======")
for elem in ft_tqdm(range(20, 20)):
    sleep(0.005)
print()
for elem in tqdm(range(20, 20)):
    sleep(0.005)
print()


print("========始まりの方が少ない range(10, 20)/range(-10, 0) =======")
for elem in ft_tqdm(range(10, 20)):
    sleep(0.005)
print()
for elem in tqdm(range(10, 20)):
    sleep(0.005)
print()

for elem in ft_tqdm(range(-10, 0)):
    sleep(0.005)
print()
for elem in tqdm(range(-10, 0)):
    sleep(0.005)
print()
