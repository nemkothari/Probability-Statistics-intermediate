## 2. Calculating differences ##

female_diff = (10771- 16280.5 )/16280.5

male_diff =  ( 21790 - 16280.5 ) / 16280.5

## 3. Updating the formula ##

female_diff = ( (10771- 16280.5 ) ** 2 ) /16280.5

male_diff =  ( ( 21790 - 16280.5 ) ** 2) / 16280.5

gender_chisq = female_diff  + male_diff

## 4. Generating a distribution ##

import numpy as np
chi_squared_values = []

for i in range(1000):
    m =0 
    f =0 
    k =  np.random.random((32561,))
    for j in  k :
        if j > 0.5 :
            m  = m + 1
        else :
            f = f + 1 
        
    male_diff= ( m -  16280.5 ) ** 2 / 16280.5
    
    female_diff = ( f -  16280.5 ) ** 2 / 16280.5
    
    chi_squared_values.append(male_diff + female_diff)
 

plt.hist(chi_squared_values)

plt.show()
    
    
        

## 6. Smaller samples ##

female_diff = (107.71 -  162.805 ) ** 2 / 162.805
male_diff = ( 217.90 -  162.805 ) ** 2 / 162.805

gender_chisq = female_diff + male_diff

## 7. Sampling distribution equality ##

import numpy as np 
chi_squared_values = []

for i in range(1000):
    m =0 
    f =0 
    k =  np.random.random((300,))
    for j in  k :
        if j > 0.5 :
            m  = m + 1
        else :
            f = f + 1 
        
    male_diff= ( m -  150 ) ** 2 / 150
    
    female_diff = ( f -  150 ) ** 2 / 150
    
    chi_squared_values.append(male_diff + female_diff)
 

plt.hist(chi_squared_values)

plt.show()
    
    
        
            

## 9. Increasing degrees of freedom ##

ob = [ 27816 ,3124, 1039, 311 , 271 ]
ex = [26146.5,3939.9,944.3,260.5,1269.8]
result =[]
for i, j in  zip(ob,ex) :
    dif = ((i - j ) ** 2 ) / j
    result.append(dif)
    
race_chisq = sum(result)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np
ob = np.array([ 27816 ,3124, 1039, 311 , 271 ])
ex = np.array([26146.5,3939.9,944.3,260.5,1269.8])

chisquare_value, race_pvalue = chisquare(ob, ex)