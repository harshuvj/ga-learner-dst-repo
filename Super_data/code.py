# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here
data['Gender'].replace('-','Agender',inplace=True)

data['Gender'].value_counts().plot(kind='bar')
plt.show()

alignment = pd.Series(data['Alignment'].value_counts())

plt.pie(alignment.values,explode = (0,0,0.5,),labels=alignment.index,autopct = '%1.1f%%')
plt.show()


new = data[['Intelligence','Strength','Combat']].copy()

corr = new.corr()
print(corr)
corr_IC = corr.iloc[0,2]
print('corr_IC:' , corr_IC)

corr_SC = corr.iloc[1,2]
print('corr_SC:',corr_SC)

if corr_IC > corr_SC:
    print("Person's intelegence has more impact on his combat skills")
else:
    print("Person's strength has more impact on his combat skills")

super_best_names = [i for i in data[data['Total']> data['Total'].quantile(0.99)]['Name']]
super_best_names


