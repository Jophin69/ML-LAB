#DATA PREPROCESSING

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import LabelEncoder

data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print("Dataset:")
print(df.head())

X = df.drop(columns=['target'])
y = df['target']

label_encoder = LabelEncoder()
y_label_encoded = label_encoder.fit_transform(y)
print("Target\n", y_label_encoded)
