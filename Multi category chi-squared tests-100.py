## 2. Calculating expected values ##

males_over50k = .67 * .241 * 32561
males_under50k = .67 * .759 * 32561
females_over50k = .33 * .241 * 32561
females_under50k = .33 * .759 * 32561

## 3. Calculating chi-squared ##

observed = [6662, 1179, 15128, 9592]
expected = [5249.8, 2597.4, 16533.5, 8180.3]
values = []

for i, obs in enumerate(observed):
    exp = expected[i]
    value = (obs - exp) ** 2 / exp
    values.append(value)

chisq_gender_income = sum(values)

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare
m = [5249.8,2597.4,16533.5,8180.3]
f = [6662,1179,15128,9592]
k , pvalue_gender_income = chisquare(m, f)

## 5. Cross tables ##

import pandas as pd
income = pd.read_csv("income.csv")
table = pd.crosstab(income["sex"], [income["race"]])
print(table)

## 6. Finding expected values ##

import numpy as np
from scipy.stats import chi2_contingency
import pandas as pd
income = pd.read_csv("income.csv")
table = pd.crosstab(income["sex"], [income["race"]])

chisq_value, pvalue_gender_race, df, expected = chi2_contingency(table)