import numpy as np
from scipy import stats
mu = 0
confidence_level = .95
n_trials = 1000
n_experiments = 10000

def get_dataset(n_trials: int, n_experiments: int)-> np.array:
    return np.random.normal(size = (n_trials, n_experiments))

def get_alpha(confidence_level:float)-> float:
    return 1 - confidence_level

def z_look_up(alpha:float)-> float:
    return stats.norm.ppf(1 - alpha/2)

def create_confidence_interval(dataset: np.array, score:float)-> tuple[float, float]:
    means = dataset.mean(axis = 0)
    vars = dataset.var(axis = 0)
    size = dataset.shape[0]

    l_bound = means - score * vars / np.sqrt(size)
    u_bound = means + score * vars / np.sqrt(size)
    return np.vstack((l_bound, u_bound))

def main():
    dataset = get_dataset(n_trials, n_experiments)
    alpha = get_alpha(confidence_level)
    z = z_look_up(alpha)


    bounds = create_confidence_interval(dataset, z)
    check = (0 > bounds[0, :]) & (0 < bounds[1, :])
    traps = check.sum() / check.shape[0]
    print(fr"The condfidence interval 'traps' mu {traps * 100}% of the time")
main()

# The condfidence interval 'traps' mu 94.98% of the time

