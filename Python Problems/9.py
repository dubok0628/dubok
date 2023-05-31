import math

def usr_input(prompt_1: str, prompt_2: str):
    input_1 = input(prompt_1)
    input_2 = input(prompt_2)
    if input_1.isnumeric() & input_2.isnumeric():
        return int(input_1), int(input_2)
    else:
        if input_1 == "":
            return None
        print("Not a valid input number, please try again: ")
        return usr_input(prompt_1, prompt_2)

def euclidean_distance(coordinate_1: tuple[int, ...], coordinate_2: tuple[int, ...]):
    return math.sqrt((coordinate_2[0] - coordinate_1[0])**2 + (coordinate_2[1] - coordinate_1[1])**2)

my_inputs = usr_input("Please enter the x_coordinate: ", "Please input the y_coordinate: ")
polygon_coordinates = []
total_distance = 0
counter = 0
while my_inputs is not None:
    polygon_coordinates.append(my_inputs)
    if len(polygon_coordinates) >= 2:
        total_distance += euclidean_distance(polygon_coordinates[counter], polygon_coordinates[counter + 1])
        my_inputs = usr_input("Please enter the x_coordinate: ", "Please input the y_coordinate: ")
        counter += 1
    else:
        my_inputs = usr_input("Please enter the x_coordinate: ", "Please input the y_coordinate: ")
else:
    print("The total perimeter of the polygon is ", total_distance)