import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
n_trials = 1000
n_experiments = 10000
index = 5
chi2_df = 2
significance_level = .05

incoming_signal = np.array( [0.9286277042696437, 1.7045034622025108, 1.2050233168496631, 1.3845192085275169, 0.7431622214379727, -0.5679286290463883, -0.48302490734666614, -1.5114589444139053, -1.764577341185066, -1.418292052669948, 0.5691222893590951, 1.5289585406721782, -0.460701510623547, 1.2776882948506474, -2.6770015657394532, -0.08993270340891461, -1.3686260170604216, 0.41212214197362895, -1.8219485330400222, -0.9514020560144467, -0.2935061113992405, -1.248384532410733, 0.3339742830685172, 0.39336906362403434, -0.025834598877514714, -0.811666785526905, 0.6705521440034906, 0.2112093102712752, 0.6226097153544842, 0.1183604974191117, -0.05356324386643412, -0.6882896771055533, -0.48979126500005604, -0.09310013954981483, 0.28948660168776613, 2.162314587980623, 1.9419564408387695, 1.046727620184002, -1.03476056281878, -0.12472014892027071])

def get_y_t(n_trials:int, n_experiments: int)-> np.array:
    return np.random.normal(loc = 0, scale = 1, size = (n_trials, n_experiments))

def get_coeff(y_t: np.array, index: int)->np.array:
    N = y_t.shape[0]
    t = np.arange(N).reshape(-1, *([1] * (y_t.ndim - 1)))


    freq = 2 * np.pi * index / N * t
    return 2 / N * (y_t * np.cos(freq)).sum(axis = 0), 2 / N * (y_t * np.sin(freq)).sum(axis = 0) 

def get_periodogram_amplitude(a_5: np.array, b_5:np.array, signal: np.array)-> np.array:
    N = signal.shape[0]
    return N / 2 * (a_5**2 + b_5**2)

def get_chi2_curve(x: np.array)->np.array:
    return stats.chi2.pdf(x,chi2_df)


def get_confidence_interval(signal: np.array, significance_level: float)-> tuple[float]:
    N = signal.shape[0]
    signal_var = signal.var(ddof = 1)
    l_chi2 = stats.chi2.ppf(significance_level / 2, chi2_df)
    u_chi2 = stats.chi2.ppf(1 - significance_level / 2, chi2_df)

    l_bound = signal_var * l_chi2
    u_bound = signal_var* u_chi2
    print(l_bound, u_bound, signal_var)
    return l_bound, u_bound

def part_1(n_trials :int, n_experiments:int, index: int)->tuple[int]:
    y_t = get_y_t(n_trials, n_experiments)
    a_5, b_5 = get_coeff(y_t, index)
    periodogram_amplitudes = get_periodogram_amplitude(a_5, b_5, y_t) 
    counts, bins, _ = plt.hist(periodogram_amplitudes, density = True, bins = 100, edgecolor = "black", label = fr'$I(f_5)$')
    return counts, bins

def part_2()-> None:
    chi2_x = np.arange(20)

    plt.plot(chi2_x, get_chi2_curve(chi2_x), label = fr'$\chi^2$')

def part_3(incoming_signal: np.array)-> None:
    a_5, b_5 = get_coeff(incoming_signal, 5)
    print(a_5, b_5)
    periodogram_amplitudes = get_periodogram_amplitude(a_5, b_5, incoming_signal) 
    print(periodogram_amplitudes)
    plt.vlines(periodogram_amplitudes,0,.6, label = 'Incoming Signal', color = 'r')

def part_4(incoming_signal: np.array, significance_level:float)->None:
    for ci in get_confidence_interval(incoming_signal, significance_level):
        plt.vlines(ci, 0, .6, linestyles='dashed')


def main():
    counts, bins = part_1(n_trials, n_experiments, index)
    part_2()
    part_3(incoming_signal)
    part_4(incoming_signal, significance_level)
    plt.legend()

    plt.show()



if __name__ == "__main__":
    main()