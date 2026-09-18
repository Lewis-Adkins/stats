import numpy as np
import matplotlib.pyplot as plt
import math

n_days = 1000
n_flares = 900
n_experiments = n_days
hours_in_day = 24 # 24 hrs/day

def calculate_prob_flare_per_hour(n_flares:int, n_days: int) -> float:
    '''
    Use a random number generator to create a dataset that simulates the following result.
    Every hour, the number of x-ray flares is tabulated.
    It is found that over 1,000 days,
    900 flares occurred so that the average probability of a flare in a given hour is 900/(1000⋅24).  

    arg1 n_flares: number of flares observed 
    arg2 n_days: number of days   
    '''
    p_h = n_flares / (n_days * hours_in_day)
    print(f"Probability of a flare happening within 24 hour window: {p_h *100}%")
    return p_h # Day times 24


def get_number_of_flares_per_day(n: int,  p: float, n_days: int) -> np.array:
    '''
    24 hourly trials in one day, with a probability of a flare occuring per hour, p
    arg1 n: number of trials, 24 hours
    arg2 p: probability of a flare occuring in an hour
    arg3 n_days: number of days
    '''
    
    return np.random.binomial(n, p, n_days)

def p_s(data: np.array)-> None:
    '''
    P_s(x) the probability of x flare events occurring per day for the Simulated dataset

    arg1 p = probability of a flare occuring in an hour
    '''

    counts = np.unique(data)

    results = {i: 0  for i in range(counts.size)}

    for c in counts:
        results[c] = np.count_nonzero(data == c)/ n_days

    return results


def p_p(x:int, n: int, p: float)-> None:
    '''
    P(x) = ((\\lambda * t)^x *e^(-\\lambda * t)) / x!

    t = n * dt
    \\lambda = p / dt

    dt = 1 hour, n = 24 trials

    t = 24
    \\lambda = p
    \\lambda * t =  p * t

    P(x) = ((p * t)^x * e^(p * t)) / x!

    arg3 p = probability of a flare occuring in an hour
    '''
    return (((p* n)**x) * math.exp(-p * n) )/ math.factorial(x)

def p_b(x:int , n: int, p: float)-> None:
    '''
    P_B(x) expected from the Binomial distribution, from which the Poisson distribution was derived.
    The Poisson distribution is discrete therefore we will use the discrete binomial distribution
    For n trials, the probability of successess is given bth the Binomial distribution:
    P(x) = (n x) p^x (1-p)^(n-x)
    
    arg1 x: number of flares a day
    arg2 n: number of trials, 24 hours
    arg3 p: probability of a flare occuring in an hour
    '''
    return math.factorial(n) / (math.factorial(x) * math.factorial(n-x)) * p**x * (1-p) ** (n-x)


def q1(data: np.array,n: int, p: float, ax: plt.axes.Axes)->None:
    '''
    Plot
    a. P_S(x), the probability of x flare events occurring per day for the Simulated dataset
    b. P_P(x) expected from the equation above using the value of λ computed based on the Poisson distribution equation above
    c. P_B(x) expected from the Binomial distribution, from which the Poisson distribution was derived.

    arg1 data: recorded number of flare per day, size of n_days
    arg2 n: number of trials, 24 hours
    arg3 p: probability of a flare occuring in an hour
    arg4 ax: ax to plot results
    '''
    
    Ps = p_s(data)
    xs = np.arange(np.unique(data).size + 1)

    Pb = [p_b(x, n, p)  for x in xs]
    Pp = [p_p(x, n, p)  for x in xs]
    

    ax.plot(list(Ps.keys()), list(Ps.values()), label = "simulation")
    ax.plot(xs,Pb, label = "binomial")
    ax.plot(xs, Pp, label = "poisson")
    
    ax.set_title("Distrbution of Flares in a Day")
    ax.set_ylabel(r"$P(x)$, Probability of obseving a flare in a day")
    ax.set_xlabel("Number of flares observed in a day")
    ax.legend()



def q2(data: np.array, n_days: int, ax: plt.axes.Axes)-> None:
    '''
    From your dataset, derive a new dataset, the time between flares, and plot a histogram of the time between flares

    arg1 data: recorded number of flare per day, size of n_days
    arg2 n_days: number of days
    arg3 ax: ax to plot results
    '''
    zero_counter = 0

    time_between_flares_in_days = np.array([], dtype=int)

    for day in range(n_days):
        if data[day] != 0:
            time_between_flares_in_days = np.append(time_between_flares_in_days, zero_counter )
            zero_counter  = 0
        else:
            zero_counter +=1

    ax.hist(time_between_flares_in_days, bins = np.unique(data), density = True, edgecolor='black',  align='left')

    ax.set_title("Time between flares in days")
    ax.set_xlabel("Days between flares")
    ax.set_ylabel("Count of days betwen flares")

def main():

    fig, (ax1, ax2) = plt.subplots(1,2, figsize = (10,4))

    p_h = calculate_prob_flare_per_hour(n_flares, n_days)
    data = get_number_of_flares_per_day(hours_in_day, p_h, n_days)

    q1(data, hours_in_day, p_h, ax1)
    q2(data, n_days, ax2)

    plt.savefig("HW3_1.png")
    plt.show()

if __name__ == "__main__":
    main()