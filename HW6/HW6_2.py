import numpy as np
import matplotlib.pyplot as plt

# Devore Example 12.18
x = np.array([55.10, 44.83, 46.32, 51.10, 49.89, 45.20, 48.18, 46.70, 54.31, 41.50, 47.50, 52.00, 52.25, 50.86, 51.66, 54.77, 57.06, 57.84, 55.22])
y = np.array([49.10, 31.20, 32.80, 42.60, 42.50, 32.70, 36.21, 40.40, 37.42, 30.80, 35.34, 44.80, 41.75, 39.35, 44.07, 43.40, 45.30, 39.08, 41.89])

def get_sxx(x: np.array) -> float:
    return (x**2).sum() - (x.sum())**2 / x.shape[0]

def get_sxy(x: np.array, y: np.array) -> float:
    return (x*y).sum() - x.sum() * y.sum() / x.shape[0]

def get_syy(y: np.array) -> float:
    return (y**2).sum() - (y.sum())**2 / y.shape[0]

def get_r(sxy: float, sxx: float, syy: float) -> float:
    return sxy / np.sqrt(sxx * syy)

def get_cov(x: np.array, y: np.array) -> float:
    return ((x - x.mean()) * (y - y.mean())).sum() / (x.shape[0] - 1)

def get_rho(x: np.array, y: np.array) -> float:
    return get_cov(x, y) / (x.std(ddof=1) * y.std(ddof=1))

def get_v(r: float) -> float:
    # Fisher transformation of r
    return .5 * np.log((1 + r) / (1 - r))

def get_z(v: float, rho_0: float, n: int) -> float:
    return (v - .5 * np.log((1 + rho_0) / (1 - rho_0))) / (1 / np.sqrt(n - 3))

def get_P(z: float, tail: str = "upper", N: int = 10000) -> float:
    # simulate N standard normal Z values; P is the fraction at least as extreme as z
    Z = np.random.default_rng(0).standard_normal(N)
    if tail == "two":
        return np.where(np.abs(Z) >= np.abs(z), 1, 0).sum() / N  # Ha: rho != rho_0
    if tail == "upper":
        return np.where(Z >= z, 1, 0).sum() / N                  # Ha: rho > rho_0
    return np.where(Z <= z, 1, 0).sum() / N                      # Ha: rho < rho_0

def plot(x: np.array, y: np.array, r: float, P: float, fname: str) -> None:
    figure, axes = plt.subplots(figsize=(8, 6), layout='constrained')
    axes.scatter(x, y)
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_title('Devore Example 12.18: y vs. x')
    axes.annotate(f'r = {r:.4f}\nP = {P:.4f}', xy=(0.05, 0.95), xycoords='axes fraction',
                  va='top', bbox=dict(boxstyle='round', fc='white', ec='gray'))
    plt.savefig(fname, dpi=300)

def main() -> None:
    n   = x.shape[0]
    sxx = get_sxx(x)
    syy = get_syy(y)
    sxy = get_sxy(x, y)
    r   = get_r(sxy, sxx, syy)
    rho = get_rho(x, y)
    v   = get_v(r)
    z   = get_z(v, 0.5, n)  # H0: rho = 0.5, Ha: rho > 0.5
    P   = get_P(z, "upper")
    print(f'Sxx = {sxx:.4f}')
    print(f'Syy = {syy:.4f}')
    print(f'Sxy = {sxy:.4f}')
    print(f'r   = {r:.4f}')
    print(f'rho = {rho:.4f}')
    print(f'v   = {v:.4f}')
    print(f'z   = {z:.4f}')
    print(f'P   = {P:.4f}')
    plot(x, y, r, P, 'HW6_2.png')

main()
