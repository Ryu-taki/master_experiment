import os

import matplotlib.pyplot as plt
import numpy as np

from common_func import generate_t_values, simulation


def plot_four_compartments(
    s_values: np.ndarray,
    i_values: np.ndarray,
    r_values: np.ndarray,
    d_values: np.ndarray,
) -> None:
    t_values: np.ndarray = generate_t_values()

    plt.plot(t_values, s_values, color="tab:blue", label="s")
    plt.plot(t_values, i_values, color="tab:red", label="i")
    plt.plot(t_values, r_values, color="tab:olive", label="r")
    plt.plot(t_values, d_values, color="black", label="d")

    plt.title(f"Baseline: R0={R0}, b={b}, φ={phi}")
    plt.xlabel("time t")
    plt.ylabel("compartment size")
    plt.legend()
    plt.savefig("./output/exercise1/four_compartments.png")
    plt.close()


if __name__ == "__main__":
    os.makedirs("./output/exercise1", exist_ok=True)

    R0: float = 2.9
    i0: float = 1e-6
    phi: float = 0.029
    b: float = 1.0

    s_values, i_values, r_values, d_values = simulation(R0, b, phi, i0)
    total_infected: float = 1 - s_values[-1]
    total_dead: float = d_values[-1]
    print(f"Total infected: {total_infected}")
    print(f"Total dead: {total_dead}")

    plot_four_compartments(s_values, i_values, r_values, d_values)

    os.makedirs("./output/exercise1/simulation_values", exist_ok=True)
    np.save("./output/exercise1/simulation_values/s_values_baseline.npy", s_values)
    np.save("./output/exercise1/simulation_values/i_values_baseline.npy", i_values)
    np.save("./output/exercise1/simulation_values/r_values_baseline.npy", r_values)
    np.save("./output/exercise1/simulation_values/d_values_baseline.npy", d_values)
