# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data = pd.read_csv(path)
data['Gender'].replace('-', 'Agender', inplace = True)

gender_count = data['Gender'].value_counts()

plt.bar(np.arange(len(gender_count)),gender_count)
plt.show()


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()

plt.pie(alignment)
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here
sc_df = data[['Strength','Combat']].copy()

sc_covariance = data['Strength'].cov(data['Combat'])
sc_strength = data['Strength'].std()
sc_combat = data['Combat'].std()

sc_pearson = sc_covariance / (sc_strength * sc_combat)

ic_df = data[['Intelligence','Combat']].copy()

ic_covariance = data['Intelligence'].cov(data['Combat'])
ic_intelligence = data['Intelligence'].std()
ic_combat = data['Combat'].std()

ic_pearson = ic_covariance / (ic_intelligence * ic_combat)


# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)

super_best = data.loc[data['Total'] > total_high]

super_best_names = list(super_best['Name'])

print(super_best_names)


# --------------
#Code starts here
ax_1 = plt.subplots()
ax_1 = data.boxplot(column = 'Intelligence')
ax_1.set_title('Intelligence')

ax_2 = plt.subplots()
ax_2 = data.boxplot(column = 'Speed')
ax_2.set_title('Speed')

ax_3 = plt.subplots()
ax_3 = data.boxplot(column = 'Power')
ax_3.set_title('Power')


