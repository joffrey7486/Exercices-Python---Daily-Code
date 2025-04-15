import random

# Créer un tableau de nombre unique aléatoire
def create_unique_random_array(size, max_val=100):
    return random.sample(range(max_val), size)



# Retrouve l'index de l'élément dans le tableau
def find_index(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return None  

arr = create_unique_random_array(10, 10)
my_number = random.randint(1, 10)
index = find_index(arr, my_number)

print("Begin")

print("My array: {}".format(arr))

print("My number : {}".format(my_number))

print("My index : {}".format(index))