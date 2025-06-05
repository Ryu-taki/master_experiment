import os

import matplotlib.pyplot as plt
import numpy as np

from common_func import generate_t_values, simulation


def plot_four_infection_curves(
    i_baseline_values: np.ndarray,
    i_b8_values: np.ndarray,
    i_b6_values: np.ndarray,
    i_b5_values: np.ndarray,
):
    t_values: np.ndarray = generate_t_values()

    plt.plot(t_values, i_baseline_values, color="tab:blue", label="b=1.0")
    plt.plot(t_values, i_b8_values, color="tab:red", label="b=0.8")
    plt.plot(t_values, i_b6_values, color="tab:olive", label="b=0.6")
    plt.plot(t_values, i_b5_values, color="black", label="b=0.5")

    plt.title(f"R0={R0}, φ={phi}")
    plt.xlabel("time t")
    plt.ylabel("compartment size (log-scale)")
    plt.legend()
    plt.yscale("log")
    plt.savefig("./output/exercise2/four_infection_curves.png")
    plt.close()


def plot_total_number_of_cases(
    what_to_plot: str,
    baseline_values: np.ndarray,
    b8_values: np.ndarray,
    b6_values: np.ndarray,
    b5_values: np.ndarray,
):
    t_values: np.ndarray = generate_t_values()

    plt.plot(t_values, baseline_values, color="tab:blue", label="b=1.0")
    plt.plot(t_values, b8_values, color="tab:red", label="b=0.8")
    plt.plot(t_values, b6_values, color="tab:olive", label="b=0.6")
    plt.plot(t_values, b5_values, color="black", label="b=0.5")

    plt.title(f"The total number of {what_to_plot}.")
    plt.xlabel("time t")
    plt.ylabel("compartment size")
    plt.legend()
    plt.savefig(f"./output/exercise2/total_number_of_{what_to_plot}.png")
    plt.close()

    plt.plot(t_values, baseline_values, color="tab:blue", label="b=1.0")
    plt.plot(t_values, b8_values, color="tab:red", label="b=0.8")
    plt.plot(t_values, b6_values, color="tab:olive", label="b=0.6")
    plt.plot(t_values, b5_values, color="black", label="b=0.5")

    plt.title(f"The total number of {what_to_plot}.")
    plt.xlabel("time t")
    plt.ylabel("compartment size (log-scale)")
    plt.legend()
    plt.yscale("log")
    plt.savefig(f"./output/exercise2/total_number_of_{what_to_plot}_log.png")
    plt.close()


if __name__ == "__main__":
    os.makedirs("./output/exercise2", exist_ok=True)

    R0 = 2.9
    i0 = 1e-6
    phi = 0.029

    # load baseline values from exeicise1
    s_baseline_values: np.ndarray = np.load(
        "./output/exercise1/simulation_values/s_values_baseline.npy"
    )
    i_baseline_values: np.ndarray = np.load(
        "./output/exercise1/simulation_values/i_values_baseline.npy"
    )
    d_baseline_values: np.ndarray = np.load(
        "./output/exercise1/simulation_values/d_values_baseline.npy"
    )

    s_b8_values, i_b8_values, r_b8_values, d_b8_values = simulation(R0, 0.8, phi, i0)
    s_b6_values, i_b6_values, r_b6_values, d_b6_values = simulation(R0, 0.6, phi, i0)
    s_b5_values, i_b5_values, r_b5_values, d_b5_values = simulation(R0, 0.5, phi, i0)

    plot_four_infection_curves(i_baseline_values, i_b8_values, i_b6_values, i_b5_values)
    plot_total_number_of_cases(
        "cases",
        1 - s_baseline_values,
        1 - s_b8_values,
        1 - s_b6_values,
        1 - s_b5_values,
    )
    plot_total_number_of_cases(
        "dead", d_baseline_values, d_b8_values, d_b6_values, d_b5_values
    )
