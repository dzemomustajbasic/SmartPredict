from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
import pandas as pd
import joblib

class AgeImputer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.imputer = SimpleImputer(strategy="mean")
        
    def fit(self, X, y=None):
        self.imputer.fit(X[['Age']])
        return self
    
    def transform(self, X):
        X = X.copy()
        X['Age'] = self.imputer.transform(X[['Age']])
        return X

from sklearn.preprocessing import OneHotEncoder

class FeatureEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.encoder_embarked = OneHotEncoder()
        self.encoder_sex = OneHotEncoder()
        print("TESTTT")
    
    def fit(self, X, y=None):
        self.encoder_embarked.fit(X[['Embarked']])
        self.encoder_sex.fit(X[['Sex']])
        return self
    
    def transform(self, X):
        X = X.copy()
        embarked_encoded = self.encoder_embarked.transform(X[['Embarked']]).toarray()
        sex_encoded = self.encoder_sex.transform(X[['Sex']]).toarray()
        
        embarked_df = pd.DataFrame(embarked_encoded, columns=self.encoder_embarked.get_feature_names_out(['Embarked']))
        sex_df = pd.DataFrame(sex_encoded, columns=['Female', 'Male'])
        
        X = pd.concat([X.reset_index(drop=True), embarked_df.reset_index(drop=True), sex_df.reset_index(drop=True)], axis=1)
        return X
    
class FeatureDropper(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X.drop(['Embarked', 'Name', 'Ticket', 'Cabin', 'Sex', 'Embarked_nan'], axis=1, inplace=True, errors='ignore')
        return X

def load_pipeline():
    path = 'C:/Users/Lenovo/Desktop/SmartPredict/smartpredict/app/pipeline.pkl'
    
    return joblib.load(path)
