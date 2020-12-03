# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts

loan_status = data['Loan_Status'].value_counts()
#Plotting bar plot
loan_status.plot(kind='bar')
plt.title('Loan Staus count')
plt.xlabel('Loan Status')
plt.ylabel('Count')
plt.show()


# Step 2
#Plotting an unstacked bar plot

property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()

property_and_loan.plot(kind='bar',stacked=False,rot=45)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.show()
#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot

education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True,rot=45)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.show()

#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education']=='Graduate']
not_graduate = data[data['Education']=='Not Graduate']

#Subsetting the dataframe based on 'Education' column


#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density',label='Graduate')
plt.show()

#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')
plt.show()

#For automatic legend display


# Step 5
#Setting up the subplots

fig, (ax_1, ax_2,ax_3) = plt.subplots(3,1, figsize=(14,10))
ax_1 = data.plot(kind='scatter',x='ApplicantIncome',y='LoanAmount',ax=ax_1)
ax_1.set_title('Applicant Income')
ax_2 = data.plot(kind='scatter',x='CoapplicantIncome',y='LoanAmount',ax=ax_2)
ax_2.set_title('Co Applicant Income')
data['TotalIncome']  = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3 = data.plot(kind='scatter',x='TotalIncome',y='LoanAmount',ax=ax_3)
ax_3.set_title('Total Income')
#Plotting scatter plot


#Setting the subplot axis title


#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



