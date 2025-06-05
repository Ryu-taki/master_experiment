import os

import matplotlib.pyplot as plt
import numpy as np

weeks = 50
dt = 0.01


def s_dot(R0: float, b: float, s: float, i: float) -> float:
    return -R0 * b**2 * s * i


def i_dot(R0: float, b: float, s: float, i: float) -> float:
    return R0 * b**2 * s * i - i


def r_dot(phi: float, i: float) -> float:
    return (1 - phi) * i


def d_dot(phi: float, i: float) -> float:
    return phi * i


def simulation(
    R0: float, b: float, phi: float, i0: float
) -> tuple[list[float], list[float], list[float], list[float]]:
    s_values: list[float] = [1 - i0]
    i_values: list[float] = [i0]
    r_values: list[float] = [0]
    d_values: list[float] = [0]

    for t in range(1, int(weeks / dt) + 1):
        s_values.append(
            s_values[t - 1] + s_dot(R0, b, s_values[t - 1], i_values[t - 1]) * dt
        )
        i_values.append(
            i_values[t - 1] + i_dot(R0, b, s_values[t - 1], i_values[t - 1]) * dt
        )
        r_values.append(r_values[t - 1] + r_dot(phi, i_values[t - 1]) * dt)
        d_values.append(d_values[t - 1] + d_dot(phi, i_values[t - 1]) * dt)

    return s_values, i_values, r_values, d_values


def plot_four_compartments(
    s_values: list[float],
    i_values: list[float],
    r_values: list[float],
    d_values: list[float],
) -> None:
    t_values = np.arange(0, weeks + dt, dt)

    plt.plot(t_values, s_values, color="tab:blue", label="s")
    plt.plot(t_values, i_values, color="tab:red", label="i")
    plt.plot(t_values, r_values, color="tab:olive", label="r")
    plt.plot(t_values, d_values, color="black", label="d")

    plt.title(f"Baseline: R0={R0}, b={b}, φ={phi}")
    plt.xlabel("time t")
    plt.ylabel("compartment size")
    plt.legend()
    plt.savefig("./output/exercise1/four_compartments.png")


if __name__ == "__main__":
    os.makedirs("./output/exercise1", exist_ok=True)

    R0 = 2.9
    i0 = 1e-6
    phi = 0.029
    b = 1.0

    s_values, i_values, r_values, d_values = simulation(R0, b, phi, i0)
    total_infected = 1 - s_values[-1]
    total_dead = d_values[-1]
    print(f"Total infected: {total_infected}")
    print(f"Total dead: {total_dead}")

    plot_four_compartments(s_values, i_values, r_values, d_values)
