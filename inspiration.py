
import random
from time import time

alphabet = ("A", "B", "C", "D", "E", "F",
            "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X", 
            "Y", "Z")

class Car:
    """
    This class represents a vehicle with a license plate.
    """
    def __init__(self, license_plate: str = None):
        if license_plate is None:
            self.assign_random_license_plate()
        else:
            self.license_plate = license_plate

    def __repr__(self) -> str:
        return f"Car({self.license_plate})"

    def assign_random_license_plate(self):
        license_numbers = random.randint(111, 999)
        license_chars = ""
        for i in range(3):
            character = random.choice(alphabet)
            license_chars += character
        self.license_plate = f"{license_chars}{license_numbers}"
        
def find_car_by_license_plate(cars: list[Car], 
                              license_plate: str) -> Car or None:
    search_area = get_sublist_for_license_plate(cars, license_plate)
    for car in search_area: 
        if car.license_plate == license_plate:
            return car
    return None

def get_sublist_for_license_plate(cars: list[list[Car]], 
                                  license_plate: str) -> list[Car]:
    return cars[alphabet.index(license_plate[0])]

if __name__ == "__main__":
    cars = []

    for letter in alphabet:
        cars.append([])

    for i in range(10 ** 6):
        car = Car()
        
        # Spara bilen i rätt lista baserat på vad reg numret börjar på..
        car_sublist = get_sublist_for_license_plate(cars, car.license_plate)
        car_sublist.append(car)
    
    bmw = Car(license_plate="BBB123")
    car_sublist = get_sublist_for_license_plate(cars, bmw.license_plate)
    car_sublist.append(bmw)

    bmw2 = Car(license_plate="ZBB123")
    car_sublist = get_sublist_for_license_plate(cars, bmw2.license_plate)
    car_sublist.append(bmw2)


    # Just nu: Hur kan vi söka snabbare utan att använda dict? 
    # Flera listor, med indexering på första bokstaven i regnret? 
    # mindre sökyta...
    # ex: for car in cars: if car.license_plate.startwith("A"): ...
    
    start = time()
    result_car = find_car_by_license_plate(cars, "BBB123")
    end = time()
    print(result_car, f"took {end - start} seconds to find")

    start = time()
    result_car = find_car_by_license_plate(cars, "ZBB123")
    end = time()
    print(result_car, f"took {end - start} seconds to find")


    
    