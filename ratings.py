import random
"""Restaurant rating lister."""


# put your code here
scores = open('scores.txt')
restaurant_scores = {}
choices = ''

def add_rating():

    key = input(str('Enter store name(capitalize the first letter): '))
    value = input('Enter rating 1-5:')
    if int(value) > 5 or int(value) < 1:
        print("Needs to be between 1-5")
        add_rating()
    else:
        restaurant_scores[key] = value

def sort_print():
    for line in scores:
        key, value = line.rstrip().split(":")
        restaurant_scores[key] = value

    for line in sorted(restaurant_scores.items()):
        print(line[0], 'is rated at', line[1])

def to_do():
    select = input(str("What would you like to do?\n------\nadd: Add rating.\nupdate: Update a rating.\nupdate-rand: Update a random rating.\nratings: See all ratings\nexit: To quit\n------\nSelect: "))
    return select

def update():
    for line in scores:
        key, value = line.rstrip().split(":")
        restaurant_scores[key] = value


    random_key = random.choice(list(restaurant_scores.items()))
    print(random_key[0], "is rated at", random_key[1])
    new_rate = int(input("What is the new rating: "))
    if new_rate > 5 or new_rate < 1:
         print("Need to be between 1-5.")
         update()
    else:
        restaurant_scores[random_key[0]] = new_rate

def spec_update():
    for line in scores:
        key, value = line.rstrip().split(":")
        restaurant_scores[key] = value

    for line in sorted(restaurant_scores.items()):
        print(line[0], 'is rated at', line[1])
    
    print('')
    store = str(input('What store(need to cap first letter): '))
    print('')
    new_rate = int(input('Enter new rating: '))
    if new_rate > 5 or new_rate < 1:
        print('Needs to be between 1-5')
        spec_update()
    else:
        restaurant_scores[store] = new_rate
    


def main():
    choices = to_do()
    while choices != "exit":
        if choices == "add":
            add_rating()
            choices = to_do()
            print('')
        elif choices == "update-rand":
            update()
            choices = to_do()
            print('')
        elif choices == "update":
            spec_update()
            choices = to_do()
            print('')
        elif choices == "ratings":
            sort_print()
            choices = to_do()
            print('')
        else:
            choices = to_do()
            print('')
main()