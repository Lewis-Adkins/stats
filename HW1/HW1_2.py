
# 1. 

import random
possible_steps = [-1,1]


n_steps = 3
n_trials = int(10e4)
all_overall_steps = []
for nt in range(n_trials):
    steps = []
    for ns in range(n_steps):
        steps.append(random.choice(possible_steps))
    net_steps = sum(steps)
    all_overall_steps.append(net_steps)
print(all_overall_steps)
rf1 = all_overall_steps.count(1) / n_trials
print(f' There is a {rf1 * 100:.2f}% chance the cylinder will net 1 step to the right, given that you can only take {n_steps} steps')