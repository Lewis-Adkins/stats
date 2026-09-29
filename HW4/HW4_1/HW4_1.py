import numpy as np
from scipy import stats

confidence_level = .99

n_experiments = 1
sample_size = 20
sample_mean = 10
sample_var = 1.03

size_min = 5
size_max = 105
size_int = 5

def get_alpha(confidence_level:float)-> float:
    return 1 - confidence_level

def t_look_up(sample_size:int, alpha: float)-> float:
    return stats.t.ppf(confidence_level, df = (sample_size - 1))


def z_look_up(data:np.array, confidence_level:float)-> float:
    return stats.norm.ppf(confidence_level, loc = data.mean(), scale=data.var())

def create_confidence_interval(mean: float, score:float, var:float, size: int )-> tuple[float, float]:
    l_bound = mean - score * var / np.sqrt(size)
    u_bound = mean + score * var / np.sqrt(size)
    return (float(l_bound), float(u_bound))

def get_dataset(n_trials: int, n_experiments: int, mean: float, var: float)-> np.array:
    return np.random.normal(loc=mean, scale= var, size = (n_trials, n_experiments))


def part_1(sample_size: int)-> tuple[float, float]:
    alpha = get_alpha(confidence_level)
    t = t_look_up(sample_size, confidence_level)
    confidence_interval = create_confidence_interval(sample_mean, t, sample_var, sample_size)
    
    return confidence_interval

def part_2(sample_size:int)-> tuple[float, float]:
    data = get_dataset(sample_size, n_experiments, sample_mean, sample_var)
    alpha = get_alpha(confidence_level)
    z = z_look_up(data, alpha)
    confidence_interval = create_confidence_interval(data.mean(), z, data.var(), data.size)

    return confidence_interval

def part_3()->None:
    print("Answer 3:")
    print("\t size(n) \t ci1_length \t ci2_length")
    sample_sizes = np.arange(size_min, size_max, size_int)
    
    for ss in sample_sizes:
        ci1 = part_1(ss)
        ci1_diff = ci1[1] - ci1[0]
        ci2 = part_2(ss)
        ci2_diff = ci2[1] - ci2[0]
        print(f"\t n = {ss} \t {ci1_diff:.5f} \t {ci2_diff:.5f}")


def main():
    ci1 = part_1(sample_size)
    print(f"Answer 1: The {confidence_level*100}% CI interval is {ci1}")

    ci2 = part_2(sample_size)
    print(f"Answer 2: The {confidence_level*100}% CI interval is {ci2}")
    part_3()
if __name__ == "__main__":
    main()

# Answer 1: The 99.0% CI interval is (9.415118924678817, 10.584881075321183)
# Answer 2: The 99.0% CI interval is (4.3389441461200935, 15.765350924748772)
# Answer 3:
#          size(n)         ci1_length      ci2_length
#          n = 5   3.45191         21.14082
#          n = 10          1.83797         17.00533
#          n = 15          1.39594         7.94957
#          n = 20          1.16976         5.02799
#          n = 25          1.02677         2.04093
#          n = 30          0.92597         6.43247
#          n = 35          0.85002         5.10949
#          n = 40          0.79013         3.32269
#          n = 45          0.74135         4.25931
#          n = 50          0.70061         4.10005
#          n = 55          0.66593         2.91986
#          n = 60          0.63594         3.72418
#          n = 65          0.60966         4.29743
#          n = 70          0.58639         3.49176
#          n = 75          0.56560         2.50464
#          n = 80          0.54688         3.39865
#          n = 85          0.52990         2.98401
#          n = 90          0.51441         2.47802
#          n = 95          0.50020         2.87414
#          n = 100         0.48711         2.52836