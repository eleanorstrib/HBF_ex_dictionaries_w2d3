
scores_file = open("scores.txt")

restaurant_dictionary = {}

for line in scores_file: 
    stripped = line.rstrip()
    data = stripped.split(":")

    restaurant_name = data[0]
    restaurant_rating = data[1]
    restaurant_dictionary[restaurant_name] = restaurant_rating

sorted_restaurant_list = sorted(restaurant_dictionary)

for restaurant in sorted_restaurant_list:
    print "restaurant %r is rated at %r." % (restaurant, restaurant_dictionary[restaurant])
