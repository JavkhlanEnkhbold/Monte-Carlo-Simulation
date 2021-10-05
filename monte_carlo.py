import numpy as np
import random
import matplotlib.pyplot as plt

def flip_coin():
    return random.randint(0, 1)

def plot_simulation_result(result):
    plt.figure()
    plt.axhline(y =0.5, color="b", linestyle="-")
    plt.xlabel("number of iterations")
    plt.ylabel("probability")
    plt.grid(True)
    plt.plot(result)
        
def run_simulation(number_of_iteration):
    probability_of_values = []
    results = 0
    results = __iterate_simulation(number_of_iteration, results, probability_of_values)
    plot_simulation_result(probability_of_values)
    return results/number_of_iteration

def __iterate_simulation(number_of_iteration, results, probability_of_values):
    for iteration in range(number_of_iteration):
        coin_flipped = flip_coin()
        results = results + coin_flipped
        intermediate_probability = results / (iteration +1)
        probability_of_values.append(intermediate_probability)
    return results

probability_values = run_simulation(10000)

plt.show()

