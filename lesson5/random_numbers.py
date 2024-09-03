from random_number_generator import uniform, initSeed


def list_random_numbers():
    initSeed(31416)
    max_number = 10

    for index in range(0, max_number):
        random_number = uniform()
        print(random_number)


list_random_numbers()
