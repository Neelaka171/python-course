import random
import my_module

random_int = random.randint(11,111)
print(random_int)

print(my_module.my_fav_number)

random_number_1_11 = random.random() *10
print(random_number_1_11)

rand_float = random.uniform(1,10)
print(rand_float)

random_heads_or_tail = random.randint(0,1)

if random_heads_or_tail == 0:
    print("head")
else:
    print("tail")