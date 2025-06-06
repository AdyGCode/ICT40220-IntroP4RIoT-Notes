from number_plates import number_plates as NumberPlates


if __name__ == "__main__":
    # Number plates will have 5 letters, ":" and 3 numbers.
    number_plate = NumberPlates(5,3,":")
    plate = number_plate.create()
    print(plate)
    print()

    # create number plate instance (with default LLL-NNN)
    number_plate = NumberPlates()
    # set up empty list of number plates
    plates = []
    # generate random starter number plate
    new_plate = number_plate.create()

    # generate a list of 30 random number plates
    for count in range(30):
        while new_plate in plates:
            new_plate = number_plate.create()
        plates.append(new_plate)

    # Show the number plates
    for counter in range(len(plates)):
        print(f"{plates[counter]:10s}", end="")

        # start new line every 10 number plates
        if ((counter + 1) % 10) == 0:
            print()
