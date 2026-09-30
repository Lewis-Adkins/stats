from scipy import stats
import numpy as np


confidence_level = .95

data = np.array([1470, 1510, 1690, 1740, 1900, 2000, 2030, 2100, 2190, 2200, 2290, 2380, 2390, 2480, 2500, 2580, 2700])

def get_chi2_critical_values(alpha: float, data: np.array)-> tuple[float,float]:

    l_chi2_cv = stats.chi2.ppf(1 - alpha, df = data.size - 1)
    u_chi2_cv = stats.chi2.ppf(alpha, df = data.size - 1)
    return (l_chi2_cv, u_chi2_cv)

def get_alpha(confidence_level:float)-> float:
    return 1 - confidence_level

def get_chi2_confidence_interval(chi2_critcal_values: tuple[float,float], data: np.array)-> tuple[float,float]:
    l_bound = (data.size - 1) * data.var() / chi2_critcal_values[0]
    u_bound = (data.size - 1) * data.var() / chi2_critcal_values[1]
    return (l_bound, u_bound)

def main():
    alpha = get_alpha(confidence_level)
    crit_vals = get_chi2_critical_values(confidence_level, data)
    confidence_interval = get_chi2_confidence_interval(crit_vals,data)

    print(f"alpha/2:{alpha/2}, 1-alpha/2: {1-alpha/2}")
    print(f"var: {data.var()}")
    print(f"cv: {crit_vals}")
    print(f"formula: ({data.size-1} * {data.var()} / {crit_vals[0]}, {data.size-1} * {data.var()} / {crit_vals[1]})")
    print(f"ci: {np.sqrt(confidence_interval)}")


if __name__ == "__main__":
    main()