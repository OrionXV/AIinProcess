'''
CHO404 Quiz 1
Question 2
Syed Arsalaan Nadim
20Je1008
'''
import random

def objective_function(x):
    return x**2

# Initialize four agents with random values between -10 and 10
agents = [{'value': random.uniform(-10, 10)} for _ in range(4)]
selected_agents = []

# Number of iterations or tournament rounds
num_tournaments = 4

for round in range(num_tournaments):
    tournament_subset = random.sample(agents, 3)
    
    for agent in tournament_subset:
        agent['fitness'] = objective_function(agent['value'])
    winner = max(tournament_subset, key=lambda x: x['fitness'])
    
    selected_agents.append(winner)
    print(f"Winners of the tournment round {round}")
    print(*selected_agents)

# Print the initial and selected agents
print("Initial Agents:")
for i, agent in enumerate(agents):
    print(f"Agent {i+1}: Value = {agent['value']}")

print("Selected Agents:")
for i, agent in enumerate(selected_agents):
    print(f"Agent {i+1}: Value = {agent['value']}")
