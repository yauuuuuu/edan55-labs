import numpy as np
from sklearn.linear_model import LinearRegression

# Data points
x = np.array([30, 40, 50, 60])
y = np.array([4.284,5.199,6.024,6.944])
# Perform linear regression
X = x[:, np.newaxis]
model = LinearRegression().fit(X, y)

# Slope of the fitted line
c = model.coef_[0]

print(c)
