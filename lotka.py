import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from scipy import integrate
import pandas as pd
import pylab as p

"""" definition of lotka-volterra parameters """
# birth rate of prey
alpha = 0.08
# death rate of prey due to predators
beta = 0.001
# natural death rate of predators
delta = 0.02
# factor that describes how many eaten preys give birth to a new predator
gamma = 0.00002

# simulation time
end_time = 100
samples = 1000
time = np.linspace(0, end_time, samples)

# initial population
# prey
x0 = 10
# predator
y0 = 2

""" Lotka-Volterra """


def lotka_volterra(animals, t, alpha, beta, delta, gamma):
    prey, predator = animals
    dxdt = prey * (alpha - (beta * predator))
    dydt = predator * (-gamma + (delta * prey))
    return np.array([dxdt, dydt])


def wykres(alpha, beta, delta, gamma):
    X0 = [x0, y0]
    res = integrate.odeint(lotka_volterra, X0, time, args=(alpha, beta, delta, gamma))
    x, y = res.T
    data = pd.DataFrame({
        "prey": x,
        "predator": y
    })
    return data

def lotka_volterra2(animals):
    prey, predator = animals
    dxdt = prey * (alpha - (beta * predator))
    dydt = predator * (-gamma + (delta * prey))
    return np.array([dxdt, dydt])


vector_origin_x, vector_origin_y = np.meshgrid(np.linspace(1, 5000, 25), np.linspace(1, 5000, 25))
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)
ax.scatter(vector_origin_x, vector_origin_y, s=1, c='red')
fig.show()

dprey = lotka_volterra2([vector_origin_x, vector_origin_y])[0]
dpredator = lotka_volterra2([vector_origin_x, vector_origin_y])[1]
normalisation = np.sqrt(dprey**2 + dpredator**2)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.quiver(vector_origin_x, vector_origin_y, dprey/normalisation, dpredator/normalisation, angles='xy')

ax.axis('equal')
ax.set_title("Lotka Volterra predator prey vector field")
ax.set_xlabel("Prey Population")
ax.set_ylabel("Predator Population")
plt.show()


