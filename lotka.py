import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import ipywidgets as ipw


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
x0 = 5
# predator
y0 = 2

""" Lotka-Volterra """


def lotka_volterra(animals, t, alpha, beta, delta, gamma):
    prey, predator = animals
    dxdt = prey * (alpha - (beta * predator))
    dydt = predator * (-gamma + (delta * prey))
    return np.array([dxdt, dydt])


def points():
    X0 = [x0, y0]
    res = integrate.odeint(lotka_volterra, X0, time, args=(alpha, beta, delta, gamma))
    x, y = res.T
    return [x, y]


x = points()[0]
y = points()[1]
plt.plot(time, x)
plt.plot(time, y)
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.legend(('Rabbits', 'Foxes'))
plt.title('Deterministic Lotka-Volterra')
plt.show()

plt.plot(x, y)
plt.xlabel('Fox Population')
plt.ylabel('Rabbit Population')
plt.title('Phase Portrait of Deterministic Lotka-Volterra')
plt.show()

plt.figure()
IC = np.linspace(1.0, 6.0, 21) # initial conditions for deer population (prey)
X0 = [x0, y0]
Xs = integrate.odeint(lotka_volterra, X0, time, args = (alpha, beta, delta, gamma))
plt.plot(Xs[:,0], Xs[:,1], "-", label = "$x_0 =$"+str(X0[0]))
plt.xlabel("Deer")
plt.ylabel("Wolves")
plt.legend()
plt.title("Deer vs Wolves");
plt.show()