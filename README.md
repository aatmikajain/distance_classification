# Distance-Based Classification Algorithms

## 1. Common Distance Metrics Used in Distance-Based Classification Algorithms
Distance-based classification algorithms, such as **k-Nearest Neighbors (KNN)**, rely on measuring the distance between data points. Some common distance metrics include:

- **Euclidean Distance**: Measures the straight-line distance between two points in a multi-dimensional space.
- **Manhattan Distance**: Computes the sum of absolute differences between the coordinates of two points.
- **Minkowski Distance**: A generalization of both Euclidean and Manhattan distances, controlled by a parameter \( p \).
- **Cosine Similarity**: Measures the cosine of the angle between two vectors, useful in text analysis.
- **Hamming Distance**: Counts the number of positions at which corresponding symbols differ, commonly used in binary and categorical data.

## 2. Real-World Applications of Distance-Based Classification Algorithms
Distance-based classification algorithms have various real-world applications, including:

- **Medical Diagnosis**: KNN is used to classify diseases based on patient symptoms and medical history.
- **Recommender Systems**: Measures similarity between users or items for personalized recommendations.
- **Image Recognition**: Helps in classifying images by comparing features extracted from different images.
- **Fraud Detection**: Identifies fraudulent transactions by measuring similarity with past legitimate transactions.
- **Text Classification**: Used in spam filtering and document categorization.

## 3. Explanation of Various Distance Metrics

### **1. Euclidean Distance**

- Measures the direct line distance between two points.
- Best suited for continuous numerical data.

### **2. Manhattan Distance (Taxicab or L1 Distance)**

- Measures the distance along grid-like paths.
- Used in cases where movement is restricted to horizontal and vertical directions.

### **3. Minkowski Distance**

- When \( p = 1 \), it becomes Manhattan Distance.
- When \( p = 2 \), it becomes Euclidean Distance.

### **4. Cosine Similarity**

- Measures the cosine of the angle between two vectors.
- Commonly used in NLP and text processing.

### **5. Hamming Distance**

- Measures the number of positions with differing elements.
- Used for categorical and binary data.

## 4. Role of Cross Validation in Model Performance
Cross-validation is a technique used to assess the generalization ability of a machine learning model by splitting the dataset into training and testing sets multiple times. Its key roles include:

- **Prevents Overfitting**: Ensures that the model performs well on unseen data.
- **Provides a More Reliable Accuracy Score**: By averaging results across multiple folds.
- **Helps in Hyperparameter Tuning**: Useful for selecting the best \( k \) in KNN or other model parameters.
- **Reduces Model Variance**: Ensures results are consistent and robust.

### **Types of Cross-Validation**
- **k-Fold Cross-Validation**: The dataset is split into \( k \) subsets, and the model is trained \( k \) times, each time leaving out one subset for validation.
- **Leave-One-Out Cross-Validation (LOOCV)**: Each data point is used as a test set once, with the rest as training data.
- **Stratified k-Fold Cross-Validation**: Ensures class distribution is maintained across folds.

## 5. Variance and Bias in Terms of KNN

### **Bias**
Bias refers to the error introduced due to approximations in the model. A **high bias** model makes strong assumptions and underfits the data.

- In KNN, a **large value of \( k \)** leads to high bias because the model considers too many neighbors, resulting in oversimplified predictions.

### **Variance**
Variance refers to the sensitivity of the model to small fluctuations in the training set. A **high variance** model overfits the training data.

- In KNN, a **small value of \( k \)** leads to high variance because the model becomes too sensitive to noise and individual data points.

### **Bias-Variance Tradeoff in KNN**
- A **small \( k \) (e.g., 1-5)** leads to **high variance** and low bias.
- A **large \( k \) (e.g., 20-50)** leads to **high bias** and low variance.
- The optimal \( k \) balances both bias and variance.
### **WANDB DASHBOARD**
![image](https://github.com/user-attachments/assets/fee3185c-6dab-474f-af88-d44772ad4882)
![image](https://github.com/user-attachments/assets/1342d4dd-a198-4125-8b1e-82ca389825a7)
![image](https://github.com/user-attachments/assets/05432d46-3670-4abf-90be-702ceca5c046)



---

This README provides an in-depth understanding of distance-based classification algorithms, their applications, and essential concepts like distance metrics, cross-validation, and bias-variance tradeoff. 🚀
