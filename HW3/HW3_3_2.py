import numpy as np
import matplotlib.pyplot as plt

n_trials = 10
n_experiments = 10000

def get_dataset(n_trials: int, n_experiments: int)-> np.array:
    return np.random.standard_normal(size = (n_experiments, n_trials))

def generate_sample_means(datasets: np.array)-> np.array:

    X_bars = np.mean(datasets, axis = 0)

    return X_bars



def part_1():
    datasets = get_dataset(n_experiments, n_trials)
    X_bars = generate_sample_means(datasets)

    Sbs = np.array([])

    for n_ex in range(n_experiments):
        sum = 0
        for n_t in range(n_trials):
            sum +=(datasets[n_t, n_ex] - X_bars[n_ex])**2/n_trials
        Sbs = np.append(Sbs, sum)

    plt.title(fr"$S_b^2$ for std normal, $\langle S_b^2 \rangle$ = {Sbs.mean():.2f}, $var S_b^2 $ = {Sbs.var():.2f}")
    plt.ylabel(fr"Count")   
    plt.xlabel("$S_b^2$s")
    plt.hist(Sbs, bins = 50, edgecolor = "black")
    plt.savefig("HW3_3_2.png")
    plt.show()


def main():
    part_1()
    
if __name__ == "__main__":
    main()