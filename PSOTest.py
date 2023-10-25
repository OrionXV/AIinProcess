import random

# Parameters
num_particles = 100
num_dimensions = 3
num_iterations = 1000
c1 = 1.5  # Cognitive coefficient
c2 = 1.5  # Social coefficient

# Define the fitness (objective) function to minimize (e.g., a quadratic function)
def fitness_function(x):
    return sum(xi ** 2 for xi in x)

# Initialize particles
particles = []
for _ in range(num_particles):
    position = [random.uniform(-5, 5) for _ in range(num_dimensions)]
    velocity = [random.uniform(-1, 1) for _ in range(num_dimensions)]
    personal_best_position = position
    personal_best_fitness = fitness_function(position)
    particles.append({
        "position": position,
        "velocity": velocity,
        "personal_best_position": personal_best_position,
        "personal_best_fitness": personal_best_fitness,
    })

# Initialize global best
global_best_position = particles[0]["personal_best_position"]
global_best_fitness = particles[0]["personal_best_fitness"]

# PSO loop
for iteration in range(num_iterations):
    for particle in particles:
        # Update velocity
        for i in range(num_dimensions):
            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)
            cognitive_velocity = c1 * r1 * (particle["personal_best_position"][i] - particle["position"][i])
            social_velocity = c2 * r2 * (global_best_position[i] - particle["position"][i])
            particle["velocity"][i] += cognitive_velocity + social_velocity
        
        # Update position
        for i in range(num_dimensions):
            particle["position"][i] += particle["velocity"][i]
        
        # Update personal best
        current_fitness = fitness_function(particle["position"])
        if current_fitness < particle["personal_best_fitness"]:
            particle["personal_best_position"] = particle["position"]
            particle["personal_best_fitness"] = current_fitness
        
        # Update global best
        if current_fitness < global_best_fitness:
            global_best_position = particle["position"]
            global_best_fitness = current_fitness

# Print the global best solution
print(f"Global best position: {global_best_position}")
print(f"Global best fitness: {global_best_fitness}")
