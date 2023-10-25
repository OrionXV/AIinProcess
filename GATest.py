import random
import string

# Parameters
target_string = "hello, world!"  # The string we want to evolve to
population_size = 10000  # Size of the population
mutation_rate = 0.05  # Probability of mutation for each character
num_generations = 10000  # Number of generations

# Generate a random initial population
def generate_random_string(length):
    return ''.join(random.choice(string.printable) for _ in range(length))

population = [generate_random_string(len(target_string)) for _ in range(population_size)]

# Fitness function
def calculate_fitness(individual):
    return sum(1 for a, b in zip(individual, target_string) if a == b)

# GA loop
for generation in range(num_generations):
    # Calculate fitness for each individual
    fitness_scores = [calculate_fitness(ind) for ind in population]
    
    # Select parents for the next generation based on fitness
    parents = random.choices(population, weights=fitness_scores, k=population_size)
    
    # Create the next generation using crossover and mutation
    new_population = []
    for _ in range(population_size):
        parent1, parent2 = random.choices(parents, k=2)
        crossover_point = random.randint(1, len(target_string) - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        for i in range(len(child)):
            if child[i] != target_string[i] and random.random() < mutation_rate:
                child = child[:i] + random.choice(string.printable) + child[i+1:]
        new_population.append(child)
    
    population = new_population

    # Check if we've found the target string
    best_individual = max(population, key=calculate_fitness)
    if calculate_fitness(best_individual) == len(target_string):
        print(f"Found the target string in generation {generation}: {best_individual}")
        break

print(f"Best match at gen {generation}: {best_individual}")