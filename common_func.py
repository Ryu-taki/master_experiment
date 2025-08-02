import pickle

import numpy as np

dt: float = 0.01


def s_dot(R0: float, b: float, s: float, i: float) -> float:
    return -R0 * b**2 * s * i


def i_dot(R0: float, b: float, s: float, i: float) -> float:
    return R0 * b**2 * s * i - i


def r_dot(phi: float, i: float) -> float:
    return (1 - phi) * i


def d_dot(phi: float, i: float) -> float:
    return phi * i


def generate_t_values(weeks: int) -> np.ndarray:
    return np.arange(0, weeks + dt, dt)


def simulation(
    R0: float, b: float, phi: float, i0: float, weeks: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    s_values: list[float] = [1 - i0]
    i_values: list[float] = [i0]
    r_values: list[float] = [0]
    d_values: list[float] = [0]

    for t in range(1, int(weeks / dt) + 1):
        s_values.append(
            s_values[t - 1] + s_dot(R0, b, s_values[t - 1], i_values[t - 1]) * dt,
        )
        i_values.append(
            i_values[t - 1] + i_dot(R0, b, s_values[t - 1], i_values[t - 1]) * dt,
        )
        r_values.append(r_values[t - 1] + r_dot(phi, i_values[t - 1]) * dt)
        d_values.append(d_values[t - 1] + d_dot(phi, i_values[t - 1]) * dt)

    return (
        np.array(s_values),
        np.array(i_values),
        np.array(r_values),
        np.array(d_values),
    )


def calc_utilitiy(
    b: float,
    phi: float,
    s_values: np.ndarray,
    i_values: np.ndarray,
    cs: float,
    ci: float,
    cd: float,
) -> float:
    uv: float = -(ci + phi * cd) * float(i_values[-1])
    integral_term: float = -cs * (b - 1.0) ** 2 * s_values - (ci + phi * cd) * i_values
    ub: float = np.sum(integral_term * dt) * uv

    return ub


def save_values_as_pickle(
    s_values: np.ndarray,
    i_values: np.ndarray,
    r_values: np.ndarray,
    d_values: np.ndarray,
    filepath: str,
) -> None:
    with open(filepath, "wb") as f:
        pickle.dump(
            {
                "s_values": s_values,
                "i_values": i_values,
                "r_values": r_values,
                "d_values": d_values,
            },
            f,
        )


def load_values_from_pickle(filepath: str) -> dict[str, np.ndarray]:
    with open(filepath, "rb") as f:
        value_dict = pickle.load(f)
    return value_dict
