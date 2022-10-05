def pizza(food_list):  # Function to guess pizza toppings
    for top in food_list:  # for loop to loop though array 'food_list'
        if top not in ['pineapple', 'bacon', 'hot peppers']:  # if the toppings are not in this list they are liked.
            print('I like ' + top + ' on my pizza')  # output of toppings that are liked.
        else:
            print('I hate ' + top + ' on my pizza')  # output toppings that are disliked.

pizza(['pepperoni', 'cheese', 'pineapple', 'bacon'])  # array of pizza top,can be any size. For the problem its only 4.
