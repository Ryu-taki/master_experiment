
import numpy as np

from common_func import calc_utilitiy, load_values_from_pickle

if __name__ == "__main__":
    # --- Define parameters ---
    phi: float = 0.029
    cs: float = 1.0
    ci: float = 3.0
    cd: float = 1000.0

    # --- Calculate utilities for four scenarios ---
    utility_values: dict[str, float] = {}
    for b in [10, 8, 6, 5]:
        # Load the simulation values for the current b
        if b == 10:
            value_dict = load_values_from_pickle(
                "./output/exercise1/simulation_values/simulation_values.pkl"
            )
        else:
            value_dict = load_values_from_pickle(
                f"./output/exercise2/simulation_values/simulation_values_b{b}.pkl"
            )
        s_values: np.ndarray = value_dict["s_values"]
        i_values: np.ndarray = value_dict["i_values"]

        # Calculate utilities
        utility_value: float = calc_utilitiy(
            b / 10, phi, s_values, i_values, cs, ci, cd
        )
        utility_values[b] = utility_value
        print(f"Utility value (b={b / 10}): {utility_value}")
