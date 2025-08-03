import os
import pickle

import matplotlib.pyplot as plt
import numpy as np

from common_func import (
    calc_utilitiy,
    simulation,
)

if __name__ == "__main__":
    os.makedirs("./output/exercise5/plot_utility/", exist_ok=True)
    os.makedirs("./output/exercise5/utility_values/", exist_ok=True)

    # --- Define parameters ---
    # for simulation
    R0: float = 2.9
    i0: float = 1e-6
    weeks: int = 50

    # for calc utility
    cs = 1.0
    ci = 3.0
    cd = 1000.0

    # for loop
    phi_dict: dict[str, float] = {
        "Population average": 0.029,
        "Population consists only of young people": 0.002,
        "Population consists only of old people": 0.094,
    }
    b_list: list[float] = list(np.arange(0.5, 1.001, 0.001))
    utility_dict: dict[str, list[float]] = {}

    for situation, phi in phi_dict.items():
        utility_values: list[float] = []
        for b in b_list:
            # --- Run simulation ---
            s_values, i_values, r_values, d_values = simulation(
                R0=R0, b=b, phi=phi, i0=i0, weeks=weeks
            )

            # --- Calculation Utility ---
            utility: float = calc_utilitiy(b, phi, s_values, i_values, cs, ci, cd)
            utility_values.append(utility)

        utility_dict[situation] = utility_values

        # --- Show the result ---
        optimal_b_index: int = utility_values.index(max(utility_values))
        optimal_b: float = b_list[optimal_b_index]

        print(f"--- {situation} (phi={phi}) ---")
        print(f"Optimal b value: {round(optimal_b, 3)}")
        print(f"Optimal utility value: {round(max(utility_values), 3)}")

        # --- Save results as a pickle file ---
        with open(f"./output/exercise5/utility_values/phi={phi}.pkl", "wb") as f:
            pickle.dump(
                {
                    "optimal_b": optimal_b,
                    "optimal_utility": max(utility_values),
                    "utility_values": utility_values,
                },
                f,
            )

    # --- Plot Utility values ---
    plt.plot(b_list, utility_dict["Population average"], label="average")
    plt.plot(
        b_list,
        utility_dict["Population consists only of young people"],
        label="consists only of young people",
    )
    plt.plot(
        b_list,
        utility_dict["Population consists only of old people"],
        label="consists only of old people",
    )

    plt.xlabel("b")
    plt.ylabel("Utility")
    plt.title("Utility value change by b value")
    plt.legend()

    plt.savefig("./output/exercise5/plot_utility/all.png")
    plt.show()
    plt.close()
