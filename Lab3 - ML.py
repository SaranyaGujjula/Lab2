import numpy as np
import pandas as pd

# Load the data from the customer_data excel
data = pd.read_excel(r"C:\Users\Lenovo\Downloads\Lab Session1 Data.xlsx")

# Segregate the data into matrices A & C (AX = C)
A = data.loc[:, ['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].values
C = data[['Payment (Rs)']].values

# Calculate the dimensionality of the vector space for this data
dimensionality = A.shape[1]

# Calculate the number of vectors in this vector space
num_vectors = A.shape[0]

# Calculate the rank of Matrix A
rank_A = np.linalg.matrix_rank(A)

# Using Pseudo-Inverse find the cost of each product available for sale
X = np.linalg.pinv(A).dot(C.reshape(-1, 1))

# Print the results
print('Dimensionality of the vector space:', dimensionality)
print('Number of vectors in this vector space:', num_vectors)
print('Rank of Matrix A:', rank_A)
print('Cost of each product available for sale:', X.flatten())

# A2. Use the Pseudo-inverse to calculate the model vector X for predicting the cost of the products
# available with the vendor.

# A3. Mark all customers (in “Purchase Data” table) with payments above Rs. 200 as RICH and others
# as POOR. Develop a classifier model to categorize customers into RICH or POOR class based on
# purchase behavior.

# Create a new column in the data to mark customers as RICH or POOR based on their payments
data['Payment Category'] = ['POOR' if payment <= 200 else 'RICH' for payment in data['Payment (Rs)']]

# Split the data into training and testing sets
train_data = data.iloc[:-1]
test_data = data.iloc[-1]

# Train the classifier model using the training data
classifier = np.zeros(train_data.shape[0])
for i, row in enumerate(train_data.values):
    classifier[i] = 1 if row[-1] == 'RICH' else -1

# Test the classifier model using the testing data
prediction = np.sign(np.dot(X.flatten(), test_data[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].values))

# Print the prediction
print('Prediction for the testing data:', 'RICH' if prediction == 1 else 'POOR')
