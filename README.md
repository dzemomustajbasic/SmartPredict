# SmartPredict

SmartPredict is a Django web application that allows users to test and use the end-to-end machine learning models I have developed. The frontend is built with HTML, CSS, and JavaScript, while the backend is implemented using Django with a MySQL database and ORM.

## Features

### User Registration and Login
The user registration module allows users to sign up and log in to the application to access all features. User data is stored in the MySQL database through Django ORM.

### User Dashboard
The user dashboard provides users with an overview of their data and predictions for models such as Titanic Survival and Laptop Price Predictions. Users can view detailed prediction results, displayed in tables with relevant attributes, and can update or add new information required for re-executing predictions. They can also edit their profile information such as email address, first name, and last name.

### Admin Dashboard
Superusers have access to the admin dashboard where they can view all users and their predictions. This dashboard allows superusers to perform CRUD operations on users and their data, providing comprehensive management capabilities.

### Machine Learning Models
SmartPredict integrates two end-to-end machine learning models:

#### Titanic Survival Prediction
- **Dataset**: The dataset is sourced from Kaggle as part of their competition.
- **Preprocessing**: The dataset is thoroughly analyzed and preprocessed using a pipeline that includes:
  - Handling missing values with `SimpleImputer`
  - Encoding categorical columns with `OneHotEncoder`
  - Scaling data with `StandardScaler`
  - Creating Pipeline to automate preprocessing
- **Model**: A Random Forest Classifier is developed, optimized, and evaluated.
- **Feature Engineering**: Feature engineering is performed using a correlation matrix.

#### Laptop Price Prediction
- **Preprocessing**: Data preprocessing is done using pandas and numpy, including:
  - Handling missing values
  - Encoding categorical columns
  - Scaling data
- **Model**: A Random Forest Regressor (RFR) is developed, optimized, and evaluated.
