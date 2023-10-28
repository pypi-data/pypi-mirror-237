#EXP1 -PREPROCESSING
import pandas as pd
import random
import numpy as np

# Generate sample data
random.seed(42)  # For reproducibility
data = []
for _ in range(1000):
    age = random.randint(18, 70)
    rooms = random.randint(1, 6)
    area = random.randint(100, 300)
    
    # Introduce missing values in 'price' and 'location'
    if random.random() < 0.3:  # 30% chance of missing value
        price = np.nan
    else:
        price = random.randint(100000, 500000)
        
    if random.random() < 0.2:  # 20% chance of missing value
        location = ''
    else:
        location = random.choice(['Suburb_A', 'Suburb_B', 'Suburb_C'])
        
    data.append([age, rooms, area, price, location])

# Create a DataFrame
columns = ['age', 'rooms', 'area', 'price', 'location']
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('housing_dataset.csv', index=False)
import pandas as pd


# Load the dataset
data = pd.read_csv('housing_dataset.csv')
from sklearn.impute import SimpleImputer


imputer = SimpleImputer(strategy='mean')  # You can choose strategy='median' or 'most_frequent' as well
data['price'] = imputer.fit_transform(data[['price']])

print(data)
from sklearn.ensemble import IsolationForest

outlier_detector = IsolationForest(contamination=0.05)  # Adjust the contamination parameter
data['is_outlier'] = outlier_detector.fit_predict(data[['age', 'rooms', 'area']])
data = data[data['is_outlier'] == 1] 
data.drop(columns=['is_outlier'], inplace=True)


print(data)
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.ensemble import IsolationForest

scaler = StandardScaler()
data[['age', 'rooms', 'area', 'price']] = scaler.fit_transform(data[['age', 'rooms', 'area', 'price']])


normalizer = MinMaxScaler()
data[['age', 'rooms', 'area', 'price']] = normalizer.fit_transform(data[['age', 'rooms', 'area', 'price']])


print(data)
encoder = OneHotEncoder()
encoded_features = pd.DataFrame(encoder.fit_transform(data[['rooms']]).toarray(),
                                columns=encoder.get_feature_names(['rooms']))
data = pd.concat([data, encoded_features], axis=1)
print(data)



#EXP2-GRADIENT DESCENT
import numpy as np

# Generate sample data
np.random.seed(42)
X = np.random.rand(100, 1)
y = 3 * X + 2 + 0.1 * np.random.randn(100, 1)  # y = 3X + 2 + noise

# Initialize parameters
learning_rate = 0.01
epochs = 1000
weights = np.random.rand(2, 1)  # Slope and intercept

# Print initial weights
print("Initial weights:", weights)

# Gradient Descent
for epoch in range(epochs):
    X_b = np.c_[np.ones((len(X), 1)), X]  # Add bias term to X
    y_pred = X_b.dot(weights)
    error = y_pred - y
    gradient = 2 * X_b.T.dot(error) / len(X_b)
    weights -= learning_rate * gradient
    
    mse = np.mean(error ** 2)
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, MSE: {mse:.4f}")

print("Final weights:", weights)

#EXP3-SIMPLE LINEAR REGRESSION

import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)
X = np.random.rand(100, 1)
y = 3 * X + 2 + 0.1 * np.random.randn(100, 1)  # y = 3X + 2 + noise

# Calculate mean of X and y
x_mean = np.mean(X)
y_mean = np.mean(y)

# Calculate slope (m) and intercept (b) using closed-form formulas
numerator = np.sum((X - x_mean) * (y - y_mean))
denominator = np.sum((X - x_mean) ** 2)
slope = numerator / denominator
intercept = y_mean - slope * x_mean

print("The slope and Intercept are:-")
print("Slope:", slope)
print("Intercept:", intercept)

plt.scatter(X, y, label='Data Points')
plt.plot(X, slope * X + intercept, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()




# EXP4- LOGISTIC REGRESSION
import numpy as np
import matplotlib.pyplot as plt

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None
        
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def initialize_params(self, num_features):
        self.weights = np.zeros(num_features)
        self.bias = 0
        
    def fit(self, X, y):
        num_samples, num_features = X.shape
        self.initialize_params(num_features)
        
        # Gradient descent
        for _ in range(self.num_iterations):
            linear_model = np.dot(X, self.weights) + self.bias
            predictions = self.sigmoid(linear_model)
            
            # Calculate gradients
            dw = (1/num_samples) * np.dot(X.T, (predictions - y))
            db = (1/num_samples) * np.sum(predictions - y)
            
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            
    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        predictions = self.sigmoid(linear_model)
        y_predicted = [1 if p > 0.5 else 0 for p in predictions]
        return y_predicted

# Example usage
if __name__ == "__main__":
    # Sample data
    X = np.array([[2.5, 3.0], [1.5, 2.2], [3.5, 2.5], [3.0, 3.5],
                  [1.0, 1.0], [3.5, 4.0], [4.0, 2.0], [2.7, 2.7]])
    y = np.array([0, 0, 1, 1, 0, 1, 1, 0])
    
    model = LogisticRegression(learning_rate=0.01, num_iterations=1000)
    model.fit(X, y)
    
    # Predictions
    new_samples = np.array([[2.0, 2.5], [3.5, 4.0]])
    predictions = model.predict(new_samples)
    print(predictions)
    
    # Visualize decision boundary
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
    
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    
    Z = np.array(model.predict(np.c_[xx.ravel(), yy.ravel()]))
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Logistic Regression Decision Boundary')
    plt.show()


# EXP5-DECISION TREE
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the Breast Cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target
print(X)
print(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree classifier
clf = DecisionTreeClassifier(random_state=42)

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
accuracy=accuracy*100
print(f"Accuracy: {accuracy:.2f}%")

# EXP6-SVM
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# Breast Cancer dataset ko load karein
cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target
print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Ek SVM classifier banayein
svm_classifier = SVC(kernel='linear', C=1.0)

# Model ko training data par train karein
svm_classifier.fit(X_train, y_train)

# Testing data par predictions banayein
y_pred = svm_classifier.predict(X_test)

# Accuracy calculate karein
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Classification report aur confusion matrix print karein
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))


# EXP7-ENSEMBLE

from sklearn.ensemble import StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Breast Cancer Wisconsin dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define base estimators
base_estimators = [
    ('decision_tree', DecisionTreeClassifier()),
    ('random_forest', RandomForestClassifier()),
    ('svm', SVC())
]

# Create a StackingClassifier with a meta-learner (e.g., Decision Tree Classifier)
stacking_classifier = StackingClassifier(estimators=base_estimators, final_estimator=DecisionTreeClassifier(), cv=5)

# Fit the ensemble model on the training data
stacking_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = stacking_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
accuracy = accuracy*100
print(f"Accuracy: {accuracy:}")


# EXP8-PCA
import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
# Load the Breast Cancer dataset
data = load_breast_cancer().data

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
print(scaled_data)
# Create a PCA instance with 2 components
n_components = 2
pca = PCA(n_components=n_components)
# Fit PCA to the scaled data
pca.fit(scaled_data)
# Transform the data to its principal components
transformed_data = pca.transform(scaled_data)
# Explained variance ratio
explained_variance_ratio = pca.explained_variance_ratio_
print("Explained Variance Ratio:", explained_variance_ratio)

# Principal components
principal_components = pca.components_
print("Principal Components:", principal_components)





# linear reg

import numpy as np

# Sample data
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Calculate the means of X and y
mean_X = np.mean(X)
mean_y = np.mean(y)

# Calculate the slope (m) and intercept (b) of the regression line
numerator = np.sum((X - mean_X) * (y - mean_y))
denominator = np.sum((X - mean_X) ** 2)
m = numerator / denominator
b = mean_y - m * mean_X

# Predict using the regression line
X_new = np.array([6, 7, 8])
y_pred = m * X_new + b

# Print the slope and intercept
print(f"Slope (m): {m:.2f}")
print(f"Intercept (b): {b:.2f}")

# Print the predicted values
print("Predicted values:")
for i, x in enumerate(X_new):
    print(f"X = {x}, Predicted y = {y_pred[i]:.2f}")




# grad descent
def gradient_descent(learning_rate, num_iterations):
    # Initialize the starting point
    x = 5.0
    
    # Define the target function to minimize (a quadratic function)
    def target_function(x):
        return x**2

    # Perform gradient descent
    for iteration in range(num_iterations):
        # Calculate the gradient of the target function at the current point
        gradient = 2 * x
        
        # Update the point in the direction of the negative gradient
        x = x - learning_rate * gradient
        
        # Calculate the value of the target function at the updated point
        cost = target_function(x)
        
        # Print the current iteration, point, gradient, and cost
        print(f"Iteration {iteration + 1}: x = {x:.4f}, Gradient = {gradient:.4f}, Cost = {cost:.4f}")

    return x

# Set hyperparameters
learning_rate = 0.1
num_iterations = 10

# Perform gradient descent and get the result
minimum = gradient_descent(learning_rate, num_iterations)

print(f"Minimum found at x = {minimum:.4f}")
