## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
mean_group_a = np.mean(weight_lost_a)

mean_group_b = np.mean(weight_lost_b)

plt.hist(weight_lost_a)

plt.show()

plt.hist(weight_lost_b)

plt.show()

## 4. Test statistic ##

mean_difference =  mean_group_b  - mean_group_a

print(mean_difference )

## 5. Permutation test ##

mean_difference = 2.52
print(all_values)
mean_differences = []

for i in range(1000):
    group_a =[]
    group_b =[]
    for n in all_values:
        k = np.random.rand()
        if k >= .5 :
            group_a.append(n)
        else :
            group_b.append(n)
            
    iteration_mean_difference = np.mean( group_b) - np.mean(group_a)  
    mean_differences .append(iteration_mean_difference)
    
plt.hist(iteration_mean_difference)
plt.show()

## 7. Dictionary representation of a distribution ##

sampling_distribution ={}

for i in mean_differences:
    if i in sampling_distribution:
        sampling_distribution[i]= sampling_distribution[i]+1
    else :
        sampling_distribution[i] = 1
        
    

## 8. P value ##

frequencies =[]

for i in sampling_distribution :
    if i > 2.5 :
        frequencies.append(i)
        
p_value=sum(frequencies)/1000
 