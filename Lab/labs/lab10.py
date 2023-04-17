def knapsack(values, weights, capacity, n):
    grid = [[0 for x in range(capacity + 1)] for x in range(n+1)]
    items_used = []

    for item in range(n+1):
        for capacity in range(capacity+1):
            if item == 0 or capacity == 0:
                grid[item][capacity] = 0
            elif weights[item-1] <= capacity:
                grid[item][capacity] = max(values[item-1] + grid[item -1][capacity-weights[item-1]], grid[item - 1][capacity])
                
            else:
                grid[item][capacity] = grid[item - 1][capacity]
    return grid#f'Max profit: {grid[n][capacity]}\nItems used: {set(items_used)}'


values = [120, 200, 150, 350, 100, 90]
weights = [15, 20, 40, 50, 20, 10]
capacity = 100

#print(knapsack(values, weights, capacity, len(weights)))

class Flight:
    def __init__(self, origin, destination, airline, number) -> None:
        self.origin = origin
        self.destination = destination
        self.airline = airline
        self.number = number

    def set_origin(self, new_origin):
        self.origin = new_origin

    def get_origin(self):
        return self.origin
    
    def set_airline(self, new_airline):
        self.airline = new_airline
    
    def get_airline(self):
        return self.airline

flight_reacs = Flight('USA', 'UK', 'American_flight', 1586)
print(flight_reacs.get_airline())
print(flight_reacs.get_origin())
flight_reacs.set_airline('No plane :(')
print(flight_reacs.get_airline())

class RocketParts():
    def __init__(self) -> None:
        self.engine = Engine()

class Engine():
    def __init__(self) -> None:
        pass

class ComsTools():
    def __init__(self) -> None:
        self.transmitter = 'beepboop'

class Rocket:
    def __init__(self) -> None:
        self.parts = RocketParts()
        self.communicationTools = ComsTools()

    def launch():
        pass

    def land():
        pass

    def cruise():
        pass

rocket1 = Rocket()
print(rocket1.communicationTools.transmitter)