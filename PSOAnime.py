import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the PSO parameters
num_particles = 30
num_dimensions = 2
num_iterations = 100

# Define the objective function (you can change this)
def objective_function(x):
    return x[0]**3 - (x[1] -1)**2 # x**3 + (y-1)**2 + np.sin(3*y+1.41)

# Define the search space
x_min, x_max = -5, 5
y_min, y_max = -5, 5

# Initialize particles' positions and velocities randomly
particles = np.random.uniform(low=[x_min, y_min], high=[x_max, y_max], size=(num_particles, num_dimensions))
velocities = np.random.rand(num_particles, num_dimensions)

# Initialize personal best positions and global best position
personal_best_positions = particles.copy()
global_best_position = particles[np.argmin([objective_function(p) for p in particles])].copy()

# Initialize personal best values and global best value
personal_best_values = [objective_function(p) for p in particles]
global_best_value = min(personal_best_values)

# Create a figure and axis for plotting
fig, ax = plt.subplots()

# Create a scatter plot for particles
sc = ax.scatter(particles[:, 0], particles[:, 1])

# Function to update the animation
def update(frame):
    global particles, velocities, personal_best_positions, personal_best_values, global_best_position, global_best_value

    # PSO update equations (you can customize this part)
    inertia_weight = 0.9
    cognitive_weight = 0.5
    social_weight = 0.5

    r1, r2 = np.random.rand(num_particles, num_dimensions), np.random.rand(num_particles, num_dimensions)

    velocities = (inertia_weight * velocities +
                 cognitive_weight * r1 * (personal_best_positions - particles) +
                 social_weight * r2 * (global_best_position - particles))

    particles += velocities

    # Update personal bests and global best
    for i in range(num_particles):
        value = objective_function(particles[i])
        if value < personal_best_values[i]:
            personal_best_positions[i] = particles[i].copy()
            personal_best_values[i] = value
        if value < global_best_value:
            global_best_position = particles[i].copy()
            global_best_value = value

    # Update the scatter plot
    sc.set_offsets(particles)
    ax.set_title(f'Iteration {frame+1}, Best Value: {global_best_value:.2f}')
    
    return sc,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_iterations, interval=200, blit=True)

# Display the animation (note: this will not work in all environments)
plt.show()
