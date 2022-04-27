# Desafio: colocar todos os carros do tipo sport na garagem de número 10
import json

f = open("carros.json", encoding="utf8")
data_carro = json.load(f)
cars = data_carro["data"]


def verify_sport(car):
    if car["type"] == "Sport":
        return True
    return False


sport_car = list(filter(verify_sport, cars))


def car_name(car):
    return car["name"]


sport_car_names = list(map(car_name, sport_car))



def assign_to_garage(cars, names_selected, new_garage_number):
    def change_garage_number(car):
        if car ["name"] in names_selected:
            car["garage number"] = new_garage_number
        return car
    return list(map(change_garage_number, cars))

new_garage = assign_to_garage(cars, sport_car_names,10)
print (new_garage)




