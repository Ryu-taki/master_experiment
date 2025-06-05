import numpy as np

weeks: int = 50
dt: float = 0.01


def s_dot(R0: float, b: float, s: float, i: float) -> float:
    return -R0 * b**2 * s * i


def i_dot(R0: float, b: float, s: float, i: float) -> float:
    return R0 * b**2 * s * i - i


def r_dot(phi: float, i: float) -> float:
    return (1 - phi) * i


def d_dot(phi: float, i: float) -> float:
    return phi * i


def generate_t_values() -> np.ndarray:
    return np.arange(0, weeks + dt, dt)


def simulation(
    R0: float, b: float, phi: float, i0: float
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
