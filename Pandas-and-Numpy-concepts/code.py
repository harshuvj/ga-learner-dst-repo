# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)

bank = pd.read_csv(path)
#Code starts here
categorical_var = bank.select_dtypes(include='object')
categorical_var

numerical_var = bank.select_dtypes(include='number')
numerical_var

banks = bank.drop('Loan_ID',axis=1)

banks.isnull().sum()

bank_mode = banks.mode().iloc[0]

banks = banks.fillna(bank_mode)

avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married','Self_Employed'],values='LoanAmount',aggfunc=np.mean)

loan_approved_se = banks.loc[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=="Y"),['Loan_Status']].count()

loan_approved_nse = banks.loc[(banks['Self_Employed']=='No') & (banks['Loan_Status']=="Y"),['Loan_Status']].count()

percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]

banks['loan_term'] = banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term = banks.loc[banks['loan_term']>=25,['loan_term']].count()

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

mean_values=loan_groupby.agg([np.mean])


