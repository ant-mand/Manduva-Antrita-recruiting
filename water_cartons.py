import math

def water_cartons(people, thirst, volume, count):
    """Calculates the number of water bottles for a given 
    number of people at the party, their individual thirst in
    ounzes, volume of a water in a bottle in ounzes, and the
    count of water bottles in a carton.
    """
    water_needed = people * thirst
    num_bottles = math.ceil(water_needed / volume)
    num_cartons = math.ceil(num_bottles / count)
    answer = num_cartons * count
    return answer