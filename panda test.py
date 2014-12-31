# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys

#%matplotlib inline

# set seed
np.seed(1)

# Function to generate test data
def CreateDataSet(Number=1):

    Output = []

    for i in range(Number):

        # Create a weekly (mondays) date range
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')

        # Create random data
        data = np.randint(low=25,high=1000,size=len(rng))

        # Status pool
        status = [1,2,3]

        # Make a random list of statuses
        random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]

        # State pool
        states = ['GA','FL','fl','NY','NJ','TX']

        # Make a random list of states
        random_states = [states[np.randint(low=0,high=len(states))] for i in range(len(rng))]

        Output.extend(zip(random_states, random_status, data, rng))

    return Output

#dataset = CreateDataSet(4)

dataset = []
print (dataset)
df = pd.DataFrame(data=dataset, columns=['欄位一','狀態','自訂欄位','StatusDate'])
#df.info()

# Save results to excel
df.to_excel('Lesson3.xlsx', index=False)
print ('Done')