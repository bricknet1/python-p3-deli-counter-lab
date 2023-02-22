katz_deli = []

def line(restaurant):
    if len(restaurant) > 0:
        output = "The line is currently:"
        for i in range(len(restaurant)):
            output += f" {i+1}. {restaurant[i]}"
        print(output)
    else:
        print("The line is currently empty.")

line(katz_deli)

def take_a_number(restaurant, name):
    restaurant.append(name)
    print(f"Welcome, {name}. You are number {len(restaurant)} in line.")

# take_a_number(katz_deli, "flanders")

def now_serving(restaurant):
    if len(restaurant) > 0:
        print(f"Currently serving {restaurant[0]}.")
        restaurant.pop(0)
    else:
        print("There is nobody waiting to be served!")

# now_serving(katz_deli)
# now_serving(katz_deli)
# now_serving(katz_deli)
# now_serving(katz_deli)
# now_serving(katz_deli)
# now_serving(katz_deli)