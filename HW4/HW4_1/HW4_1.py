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
    return stats.t.ppf(0.995, df = (sample_size - 1))


def z_look_up(data:np.array, alpha:float)-> float:
    # data is not being used
    return stats.norm.ppf(0.995)

def create_confidence_interval(mean: float, score:float, var:float, size: int )-> tuple[float, float]:
    # Equation has "std" not "var". But you are passing std, so just poor
    # naming.
    l_bound = mean - score * np.sqrt(var) / np.sqrt(size)
    u_bound = mean + score * np.sqrt(var) / np.sqrt(size)
    return (float(l_bound), float(u_bound))

def get_dataset(n_trials: int, n_experiments: int, mean: float, var: float)-> np.array:
    # You don't need to generate data.
    # This is computing a normal with mean of 1.0
    return np.random.normal(size = (n_trials, n_experiments))


def part_1(sample_size: int)-> tuple[float, float]:
    alpha = get_alpha(confidence_level)
    t = t_look_up(sample_size, confidence_level)
    print(t)
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
        ci1_diff = abs(ci1[1] - ci1[0])
        ci2 = part_2(ss)
        ci2_diff = abs(ci2[1] - ci2[0])
        print(f"\t n = {ss} \t {ci1_diff:.5f} \t {ci2_diff:.5f}")


def main():
    ci1 = part_1(sample_size)
    print(f"Answer 1: The {confidence_level*100}% CI interval is {ci1}")

    ci2 = part_2(sample_size)
    print(f"Answer 2: The {confidence_level*100}% CI interval is {ci2}")
    part_3()
if __name__ == "__main__":
    main()

# Answer 1: The 99.0% CI interval is (9.997075132312402, 10.002924867687598)
# Answer 2: The 99.0% CI interval is (9.23297328436835, 10.278736751263407)
# Answer 3:
#          size(n)         ci1_length      ci2_length
#          n = 5           0.01228         1.02798
#          n = 10          0.00839         1.43500
#          n = 15          0.00679         1.46435
#          n = 20          0.00585         1.17110
#          n = 25          0.00522         0.90395
#          n = 30          0.00475         0.66180
#          n = 35          0.00440         1.00893
#          n = 40          0.00411         0.61500
#          n = 45          0.00387         0.54436
#          n = 50          0.00367         0.79538
#          n = 55          0.00350         0.56458
#          n = 60          0.00335         0.68521
#          n = 65          0.00321         0.59800
#          n = 70          0.00310         0.53263
#          n = 75          0.00299         0.71879
#          n = 80          0.00290         0.58002
#          n = 85          0.00281         0.67357
#          n = 90          0.00273         0.50827
#          n = 95          0.00266         0.53151
#          n = 100         0.00259         0.75243