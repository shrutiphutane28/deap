"""Importing Libraries"""

import numpy as np

"""Objective function: minimize x^2"""

def objective(x):
    return x ** 2

"""Clonal Selection Algorithm"""

def clonal_selection():
    # Step 1: Initialize a population of 10 random solutions (antibodies) between -10 and 10
    population = np.random.uniform(-10, 10, 10)

    # Step 2: Run the optimization process for 20 generations
    for gen in range(20):
        # Step 3: Evaluate the fitness of each solution in the population
        fitness = np.array([objective(x) for x in population])

        # Step 4: Select the best 5 solutions (lowest fitness)
        best_half = population[np.argsort(fitness)[:5]]

        # Step 5: Clone each of the 5 best solutions 5 times (total 25 clones)
        clones = np.repeat(best_half, 5)

        # Step 6: Apply small random mutations to the clones (Gaussian noise)
        clones += np.random.normal(0, 0.1, clones.shape)

        # Step 7: Evaluate the fitness of the mutated clones
        fitness = np.array([objective(x) for x in clones])

        # Step 8: Select the 10 best clones to become the new population
        population = clones[np.argsort(fitness)[:10]]

        # Step 9: Identify and print the best solution of the generation
        best = population[0]
        print(f"Generation {gen+1}: Best = {best:.5f}, Fitness = {objective(best):.5f}")

    # Step 10: Return the best solution found after all generations
    return best

"""Run the algorithm and print the final best solution"""

result = clonal_selection()
print("\nFinal Best Solution:", result)

