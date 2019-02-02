# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
total = len(df)

p_a = len(df[(df['fico'] > 700)]) / total
p_b = len(df[(df['purpose'] == 'debt_consolidation')]) / total

df1 = df[(df['purpose'] == 'debt_consolidation')]

p_a_b = len(df[((df['purpose'] == 'debt_consolidation') & (df['fico'] > 700))]) / total

result = (p_a_b == p_a)

print(result)
# code ends here


# --------------
# code starts here
prob_lp = len(df[(df['paid.back.loan'] == 'Yes')]) / total
prob_cs = len(df[(df['credit.policy'] == 'Yes')]) / total

new_df = df[(df['paid.back.loan'] == 'Yes')]

prob_pd_cs = len(df[((df['paid.back.loan'] == 'Yes') & (df['credit.policy'] == 'Yes'))]) / len(new_df)

bayes = (prob_pd_cs * prob_lp) / prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
grouped = df.groupby(['purpose'])
grouped.sum().plot(kind = 'bar')

df1 = df[(df['paid.back.loan'] == 'No')]

grouped1 = df1.groupby(['purpose'])
grouped1.sum().plot(kind = 'bar')
# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

plt.hist(x = df['installment'], bins = 10)
plt.hist(x = df['log.annual.inc'], bins = 10)
# code ends here


