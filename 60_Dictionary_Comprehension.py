# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
# Format 1: dictionary = {key:(expression) for (key,value) in (iterable)}
# Format 2: dictionary = {key:(expression) for (key,value) in (iterable) if (conditional)}
# Format 3: dictionary = {key:(if/else) for (key,value) in (iterable)}
# Format 4: dictionary = {key: function(value) for (key,value) in (iterable)}


# Example 1: {key:(expression) for (key,value) in (iterable)}
cities_in_F = {'New York':32, 'Boston':75, 'Los Angles':100, 'Chicago':50}

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}   # dictionary = {key:expression for (key,value) in iterable}
print(cities_in_C)


# Example 2: {key:(expression) for (key,value) in (iterable) if (conditional)}
weathers = {'New York':"snowing", 'Boston':"sunny", 'Los Angles':"sunny", 'Chicago':"cloudy"} 
sunny_weather = {key: value for (key,value) in weathers.items() if value == "sunny"}  # dictionary = {key:(expression) for (key,value) in (iterable) if (conditional)}
print (sunny_weather)                                                                 # condition: value == "sunny"

# Example 3: {key:(if/else) for (key,value) in (iterable)}
cities= {'New York':32, 'Boston':75, 'Los Angles':100, 'Chicago':50}
desc_cities = {key:("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}      # dictionary = {key:(if/else) for (key,value) in (iterable)}
print(desc_cities)

# Example 4: {key: function(value) for (key,value) in (iterable)}

def check_temp(value):                                                              # Check Temperature Functions
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities= {'New York':32, 'Boston':75, 'Los Angles':100, 'Chicago':50}
desc_cities = {key:check_temp(value) for (key,value) in cities.items()}             # dictionary = {key: function(value) for (key,value) in (iterable)}
print(desc_cities)