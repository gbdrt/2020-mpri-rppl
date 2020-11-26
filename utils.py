import numpy as np
import matplotlib.pyplot as plt
import torch
from IPython.display import display, clear_output


def plot_posterior(results):
    theta = results[:, 0]
    score = results[:, 1]
    display(plt.vlines(theta, 0, score))


def plot_pdf(d):
    x = torch.linspace(0, 1, 1000)
    y = np.exp(d.log_prob(x))
    display(plt.plot(x, y))


def animate_model(m, r):
    m.reset()
    n = len(r)
    t = np.arange(n)

    s_min = []
    s_mean = []
    s_max = []

    for i in range(n):
        clear_output(wait=True)
        plt.plot(t[:i], s_mean)
        plt.plot(t[:i], r[:i], "xr")
        plt.fill_between(t[:i], s_min, s_max, alpha=0.2)
        plt.axis((0, n, -13, 13))
        plt.show()
        d = m.step(r[i])
        s_min.append(np.min(d[:,0]))
        s_mean.append(np.average(d[:,0], weights=d[:,1]))
        s_max.append(np.max(d[:,0]))
