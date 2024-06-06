#In this project, we will be using a dataset containing census information from the 1994 Census database to 
#create a logistic regression model that predicts whether or not a person makes more than $50,000.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns



col_names = ['age', 'workclass', 'fnlwgt','education', 'education-num', 
'marital-status', 'occupation', 'relationship', 'race', 'sex',
'capital-gain','capital-loss', 'hours-per-week','native-country', 'income']

df = pd.read_csv('Data Science\Regular Projects\Supervised-Learning-RCT\Income Classification Lin Reg\dataset.data',header= None, names = col_names)


#Clean columns by stripping extra whitespace for columns of type "object"
for c in df.select_dtypes(include=['object']).columns:
    df[c] = df[c].str.strip()
#print(df.head())

#Our outcome variable here is the income, so it's a good idea to check if the dataset is balanced or not regarding the outcome variable

print(df['income'].value_counts())
#<=50K    24720
#>50K      7841

#Very very imbalanced, makes sense, median income is probably lower than 50.000 USD
feature_cols = ['age','capital-gain', 'capital-loss', 'hours-per-week', 'sex','race', 'hours-per-week', 'education']

#We transform the dataset to dummy vars 
X = pd.get_dummies(df[feature_cols],drop_first=True)

#sns.heatmap(X.corr())
#plt.show()
#plt.clf()

y = np.where(df.income=='<=50K', 0, 1)

X_train, X_test, y_train, y_test =train_test_split(X,y, random_state=1, test_size=.2)


model = LogisticRegression(C=0.05,penalty='l1',solver='liblinear')

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("--------------------------------------------------------")
print(model.coef_)
print("--------------------------------------------------------")
print(confusion_matrix(y_test,y_pred))
print("--------------------------------------------------------")
print(accuracy_score(y_test,y_pred))
print("--------------------------------------------------------")

coef_df = pd.DataFrame(zip(X_train.columns, model.coef_[0]), columns=['var', 'coef']).sort_values('coef')
coef_df = coef_df[coef_df.coef.abs()>0].sort_values('coef')
print(coef_df)


""" sns.barplot(data=coef_df, x='var', y='coef')
plt.xticks(rotation=90)
plt.show()

 """


y_pred_prob = model.predict_proba(X_test)
roc_auc = roc_auc_score(y_test, y_pred_prob[:,1])
fpr, tpr, thresholds = roc_curve(y_test,y_pred)
plt.figure()
plt.plot(fpr, tpr, color='darkorange',
         label='ROC curve (area = %0.2f)' % roc_auc)


plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.plot([0,1],[0,1], color='navy',linestyle='--')
plt.title('ROC Curve')
plt.grid()
plt.show()