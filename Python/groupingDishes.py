# You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish, followed by all the ingredients used in preparing it. You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it(if there are at least 2 such dishes).

# Return an array where each element is a list beginning with the ingredient name, followed by the names of all the dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically, and the result array should be sorted lexicographically by the names of the ingredients.


def groupingDishes(dishes):
    dishesDict = {}
    gDishDict = []

    for i in range(0, len(dishes)):
        subArray = dishes[i]
        for j in range(1, len(subArray)):
            if subArray[j] in dishesDict.keys():
                toInsert = subArray[0]
                existingKey = subArray[j]
                dishesDict[existingKey].append(toInsert)
                valueArray = sorted(dishesDict[existingKey])
                dishesDict[existingKey] = valueArray
            else:
                # create new key and insert value in new array
                newKey = subArray[j]
                dishesDict[newKey] = [subArray[0]]

    for existingKey in dishesDict:
        variable = existingKey
        if len(dishesDict[existingKey]) > 1:
            dishesDict[existingKey].insert(0, variable)
            gDishDict.append(dishesDict[existingKey])

    print(sorted(gDishDict))


food = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
        ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
        ["Quesadilla", "Chicken", "Cheese", "Sauce"],
        ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
groupingDishes(food)
