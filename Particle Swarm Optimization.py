# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:16:01 2022

@author: Soumyajit Sengupta
"""




import numpy as np

def func(x,y):
    "Objective function"
    return x**3 + (y-1)**2 + np.sin(3*y+1.41)

# a 2-variable objective function, for which the aim is to find out the minima



n_particles = 20

# total number of particles

np.random.seed(100)

# keeping random numbers same for every iteration


X = np.random.rand(2, n_particles)
V = np.random.randn(2, n_particles)

#print("", X)
# the location of the particles on x-y plane (random): an array of the given shape with random samples from a uniform distribution over [0, 1)
# the velocity : random floats sampled from a univariate “normal” (Gaussian) distribution of mean 0 and variance 1




a = X # X 
a_obj = func(X[0], X[1]) # the objective function value corresponding to each element of a

b = a[:, a_obj.argmin()] # that particular element of "a" (from among all the "a"s of all particles) which corresponds to the least value of objective function 
b_obj = a_obj.min() # the value of that objective function at that point

# Hyper-parameter of the algorithm
c1 = c2 = 0.1
w = 0.8


def pso():

    global V, X, a, a_obj, b, b_obj
    # Update params
    r1, r2 = np.random.rand(2)
    
    V = w * V + c1*r1*(a - X) + c2*r2*(b.reshape(-1,1)-X)  # this is how the algorithm updates X of each particle 
    X = X + V
    
    obj = func(X[0], X[1])
    print("", a)

    a[:, (a_obj >= obj)] = X[:, (a_obj >= obj)] # best of X found till now by a specific particle (and, the same is true for all the particles), so, for better points, a gets updated with that point (X), comparing earlier iteration's a_obj with current's obj
    a_obj = np.array([a_obj, obj]).min(axis=0) # the minimum of objectives for each particle

    b = a[:, a_obj.argmin()] # best of the points explored by any of the particles till now
    b_obj = a_obj.min()

# print values of a, a_obj, b, b_obj etc. in the for loops to track the progress


for i in range(0,50):
    pso()

# ideally there should be stopping criterion
# print values in the for loops to track the progress
# further post-processing like plots etc. can be included

print("", b)
print("",b_obj)