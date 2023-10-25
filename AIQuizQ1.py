'''
CHO404 Quiz 1
Question 1 
Syed Arsalaan Nadim 
20JE1008
'''
import random 
import math
# Initializing data
y = [5.054,9.794,14.341,18.68,22.53,26,29,32.7,25.4,38,]
t = [x for x in range(10)]

# Define Objective function, integrated it 
def obj_func(y, t, k1 = 0.01, k2 = 0.01):
    y = - k1 * t**2 + k2 * t + 5
    return y 

t0 = 0 
y0 = 5
cost = obj_func(y0, t0)


# Define the objective function to be minimized
def cost_function(k1, k2):
    # Initialize variables
    t = [x for x in range(10)]
    y_pred = [y0]
    
    for i in range(1, len(t)):
        dydt = obj_func(y_pred[-1], t[i - 1], k1, k2)
        y_pred.append(y_pred[-1] + dydt)
    
    mse = sum((y - y_pred[i])**2 for i, y in enumerate(y)) / len(y)
    # We use MSE as the cost, can use RMSE too
    return mse

# Simulated annealing function
def simulated_annealing(objective_function, initial_solution, temperature, cooling_rate, num_iterations):
    current_solution = initial_solution
    current_cost = objective_function(*current_solution)
    
    best_solution = current_solution
    best_cost = current_cost
    
    for i in range(num_iterations):
        # Random neighbors
        k1_neighbor = current_solution[0] + random.uniform(-0.01, 0.01)
        k2_neighbor = current_solution[1] + random.uniform(-0.01, 0.01)
        neighbor_solution = (k1_neighbor, k2_neighbor)
        
        neighbor_cost = objective_function(*neighbor_solution)
        
        # Accept the neighbor solution if it's better or with a certain probability or tolerence
        if neighbor_cost < current_cost or random.random() < math.exp((current_cost - neighbor_cost) / temperature):
            current_solution = neighbor_solution
            current_cost = neighbor_cost
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
        
        temperature *= cooling_rate
        if i%1000 == 0:
            print(f"Iteration number: {i}")
            print(f"Current best cost: {best_cost}" )
    
    return best_solution, best_cost

# Initial parameters 
initial_solution = (0.01, 0.01)
initial_temperature = 1.0
cooling_rate = 0.95
iterations = 10000

optimal_solution, optimal_cost = simulated_annealing(cost_function, initial_solution, initial_temperature, cooling_rate, iterations)

print("Optimal Solution (k1, k2):", optimal_solution)
print("Optimal Cost:", optimal_cost)
