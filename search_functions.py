import random
from time import time


"""
Bubble sorts a list of objects based on their lexicographical order.
"""
def bubble_sort(arr):
    n = len(arr)    
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
 
            if arr[j].car_brand > arr[j + 1].car_brand:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
    return arr


"""
Insertion sorts a list of objects based on their lexicographical order.
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >=0 and key.car_brand < arr[j].car_brand:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


"""
Selection sorts a list of objects based on their lexicographical order.
"""

def selection_sort(arr):  
    n = len(arr)  
      
    for i in range(n-1):  
        minIndex = i  
          
        for j in range(i+1, n):  
            if arr[j].car_brand < arr[minIndex].car_brand:  
                minIndex = j  
                  
        arr[i], arr[minIndex] = arr[minIndex], arr[i]  
          
    return arr 





class Car:
    def __init__(self, car_brand: str = None):
        if car_brand is None:
            self.assign_random_brand()
        else:
            self.car_brand = car_brand


    def __repr__(self) -> str:
        return self.car_brand


    def assign_random_brand(self):
        brands = ["Volvo",
                  
                  
                  "Volkswagen",
                  "Audi",
                  "Opel",
                  "Peugeot",
                  "Jeep",
                  "Renault",
                  "Citroen",
                  "Fiat",
                  "Tesla",
                  "Chrysler",
                  "Kia",
                  "Mitsubishi",
                  "Subaru",
                  "Mercedes"]
        new_car = random.choice(brands)
        self.car_brand = new_car
        

if __name__ == "__main__":


    one_thousand_car_objects = []
    two_thousand_car_objects = []
    four_thousand_car_objects = []
    eight_thousand_car_objects = []

    for i in range(1,8000+1):
        car = Car()
        if i <= 1000:
            one_thousand_car_objects.append(car)
        if i <= 2000:
            two_thousand_car_objects.append(car)
        if i <= 4000:
            four_thousand_car_objects.append(car)
        if i <= 8000:
            eight_thousand_car_objects.append(car)
    
    print(len(one_thousand_car_objects))
    print(len(two_thousand_car_objects))
    print(len(four_thousand_car_objects))
    print(len(eight_thousand_car_objects))


# Testing time complexity of Selection sort        

    start = time()
    one_thousand_sorted = selection_sort(one_thousand_car_objects)
    end = time()
    print(f"Sorted in {end-start} seconds.")

    start = time()
    two_thousand_sorted = selection_sort(two_thousand_car_objects)
    end = time()
    print(f"Sorted in {end-start} seconds.")

    start = time()
    four_thousand_sorted = selection_sort(four_thousand_car_objects)
    end = time()
    print(f"Sorted in {end-start} seconds.")

    start = time()
    eight_thousand_sorted = selection_sort(eight_thousand_car_objects)
    end = time()
    print(f"Sorted in {end-start} seconds.")





# Testing time complexity of Bubble sort        

start = time()
one_thousand_sorted = bubble_sort(one_thousand_car_objects)
end = time()
print(f"Sorted in {end-start} seconds.")

start = time()
two_thousand_sorted = bubble_sort(two_thousand_car_objects)
end = time()
print(f"Sorted in {end-start} seconds.")

start = time()
four_thousand_sorted = bubble_sort(four_thousand_car_objects)
end = time()
print(f"Sorted in {end-start} seconds.")

start = time()
eight_thousand_sorted = bubble_sort(eight_thousand_car_objects)
end = time()
print(f"Sorted in {end-start} seconds.")







# Testing time complexity of insertion sort        

start = time()
one_thousand_sorted = insertion_sort(one_thousand_car_objects)
end = time()
print(f"Sorted in {end-start} seconds.")

start = time()
two_thousand_sorted = insertion_sort(two_thousand_car_objects)
end = time()
print(f"Sorted in {end-start} seconds.")

start = time()
four_thousand_sorted = insertion_sort(four_thousand_car_objects)
end = time()
print(f"Sorted in {end-start} seconds.")

start = time()
eight_thousand_sorted = insertion_sort(eight_thousand_car_objects)
end = time()
print(f"Sorted in {end-start} seconds.")


"""

(In the middle)

Selection sort results:

Sorted in 0.12629199028015137 seconds.
Sorted in 0.49656009674072266 seconds.
Sorted in 1.940688133239746 seconds.
Sorted in 7.7049009799957275 seconds.

(Slowest)

Bubble sort results:

Sorted in 0.21045303344726562 seconds.
Sorted in 0.8142571449279785 seconds.
Sorted in 3.197427272796631 seconds.
Sorted in 12.98838496208191 seconds.


(Fastest)

Insertion sort results:

Sorted in 0.09642386436462402 seconds.
Sorted in 0.363736629486084 seconds.
Sorted in 1.4472520351409912 seconds.
Sorted in 5.8392250537872314 seconds.


"""



