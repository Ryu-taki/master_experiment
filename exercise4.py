import os

import numpy as np
import pandas as pd

from common_func import (
    calc_utilitiy,
    load_values_from_pickle,
    save_values_as_pickle,
    simulation,
)

if __name__ == "__main__":
    # --- Define parameters ---
    R0: float = 2.9
    phi: float = 0.029
    i0: float = 1e-6

    # --- Simulation parameters for each weeks and b values
    os.makedirs("./output/exercise4/simulation_values", exist_ok=True)
    for weeks in [25, 50, 100]:
        for b in [10, 8, 6, 5]:
            # --- Run simulation ---
            s_values, i_values, r_values, d_values = simulation(
                R0=R0, b=b / 10, phi=phi, i0=i0, weeks=weeks
            )

            # --- Save simulation values as a pickle file ---
            save_values_as_pickle(
                s_values,
                i_values,
                r_values,
                d_values,
                f"./output/exercise4/simulation_values/simulation_values_b{b}_{weeks}weeks.pkl",
            )

    # Calculate utilities for each b value and weeks
    utility_values_dict: dict[str, list[float]] = {}
    cs: float = 1.0
    ci: float = 3.0
    cd: float = 1000.0

    for weeks in [25, 50, 100]:
        utility_values: list[float] = []
        for b in [10, 8, 6, 5]:
            # Load the simulation values for the current b and weeks
            value_dict = load_values_from_pickle(
                f"./output/exercise4/simulation_values/simulation_values_b{b}_{weeks}weeks.pkl"
            )
            s_values: np.ndarray = value_dict["s_values"]
            i_values: np.ndarray = value_dict["i_values"]

            # Calculate utilities
            utility_value: float = calc_utilitiy(
                b / 10, phi, s_values, i_values, cs, ci, cd
            )
            utility_values.append(utility_value)

        utility_values_dict[f"{weeks}weeks"] = utility_values

    # --- Save utility values as a pickle file ---
    df = pd.DataFrame(
        utility_values_dict, index=[b / 10 for b in [10, 8, 6, 5]]
    ).reset_index()
    df = df.rename(columns={"index": "b"})
    print(df)
    df.to_csv("./output/exercise4/utility_values.csv", index=False)
