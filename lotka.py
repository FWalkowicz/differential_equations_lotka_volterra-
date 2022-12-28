import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import ipywidgets as ipw
from scipy.integrate import odeint

alpha = 2
beta = 1
delta = 1
gamma = 1

x0 = 4.0
y0 = 1.0


def derivative(X, t, alpha, beta, delta, gamma):
    x, y = X
    dxdt = alpha * x - beta * x * y
    dydt = -delta * y + gamma * x * y
    return [dxdt, dydt]


Nt = 1000
tmax = 30.0
t = np.linspace(0.0, tmax, Nt)
X0 = [x0, y0]
res = integrate.odeint(derivative, X0, t, args=(alpha, beta, delta, gamma))
x, y = res.T


def diagram():
    plt.figure()
    plt.grid()
    plt.title("odeint method")
    plt.plot(t, x, "xb", label="Deer")
    plt.plot(t, y, "+r", label="Wolves")
    plt.xlabel("Time t, [days]")
    plt.ylabel("Population")
    plt.legend()
    return plt.savefig('diagram.png')


def faze_diagram():
    plt.figure()
    IC = np.linspace(1.0, 6.0, 21)  # initial conditions for deer population (prey)
    for deer in IC:
        X0 = [deer, 1.0]
        Xs = integrate.odeint(derivative, X0, t, args=(alpha, beta, delta, gamma))
        plt.plot(Xs[:, 0], Xs[:, 1], "-", label="$x_0 =$" + str(X0[0]))
    plt.xlabel("Deer")
    plt.ylabel("Wolves")
    plt.legend()
    plt.title("Deer vs Wolves")
    plt.savefig('faze.png')
    return plt.show()


print(faze_diagram())
print(diagram())
