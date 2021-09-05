import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

# data
data = np.random.random([100, 100]) * 50

# create colormaps
N = 256

dark_red = np.ones((N, 4))
dark_red[:, 0] = np.linspace(159 / 256, 1, N)
dark_red[:, 1] = np.linspace(3 / 256, 1, N)
dark_red[:, 2] = np.linspace(3 / 256, 1, N)
dark_red_cmp = ListedColormap(dark_red)

red = np.ones((N, 4))
red[:, 0] = np.linspace(245 / 256, 1, N)
red[:, 1] = np.linspace(3 / 256, 1, N)
red[:, 2] = np.linspace(3 / 256, 1, N)
red_cmp = ListedColormap(red)

d_orange = np.ones((N, 4))
d_orange[:, 0] = np.linspace(230 / 256, 1, N)
d_orange[:, 1] = np.linspace(104 / 256, 1, N)
d_orange[:, 2] = np.linspace(8 / 256, 1, N)
d_orange_cmp = ListedColormap(d_orange)

orange = np.ones((N, 4))
orange[:, 0] = np.linspace(230 / 256, 1, N)
orange[:, 1] = np.linspace(186 / 256, 1, N)
orange[:, 2] = np.linspace(8 / 256, 1, N)
orange_cmp = ListedColormap(orange)

yellow = np.ones((N, 4))
yellow[:, 0] = np.linspace(255 / 256, 1, N)
yellow[:, 1] = np.linspace(255 / 256, 1, N)
yellow[:, 2] = np.linspace(6 / 256, 1, N)
yellow_cmp = ListedColormap(yellow)

light_green = np.ones((N, 4))
light_green[:, 0] = np.linspace(106 / 256, 1, N)
light_green[:, 1] = np.linspace(255 / 256, 1, N)
light_green[:, 2] = np.linspace(6 / 256, 1, N)
light_green_cmp = ListedColormap(light_green)

green = np.ones((N, 4))
green[:, 0] = np.linspace(6 / 256, 1, N)
green[:, 1] = np.linspace(146 / 256, 1, N)
green[:, 2] = np.linspace(6 / 256, 1, N)
green_cmp = ListedColormap(green)

# define colormaps - Esempio 1
BLQcmap = np.vstack(
    (
        green_cmp(np.linspace(0.5, 0, 128)),
        light_green_cmp(np.linspace(0.5, 0, 128)),
        yellow_cmp(np.linspace(0.5, 0, 128)),
        orange_cmp(np.linspace(0.5, 0, 128)),
        d_orange_cmp(np.linspace(0.5, 0, 128)),
        red_cmp(np.linspace(0.5, 0, 128)),
        dark_red_cmp(np.linspace(0.5, 0, 128)),
    )
)

double = ListedColormap(BLQcmap, name="double")


plt.figure(figsize=(7, 6))


def normalize(d):
    value = 0
    thresholds = [0, 0.5, 2, 5, 9, 30, 50]
    for i, t in enumerate(thresholds):
        if d > t:
            value = i
        else:
            break
    return value


normalized = [[normalize(d) for d in r] for r in data]

print(data, normalized)

plt.pcolormesh(normalized, cmap=double)

plt.colorbar(label="BLQ-Air Index", extend="both", pad=0.1)

plt.show()
