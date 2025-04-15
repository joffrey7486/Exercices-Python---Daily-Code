# Retrouve l'index de l'élément dans le tableau
def find_index(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return None  

print(find_index([13, 18, 25, 2, 8, 10], 10))