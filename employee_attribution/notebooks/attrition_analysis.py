import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import shap


df = pd.read_csv("/Users/kadendavis/PycharmProjects/employee-attrition-ml/data/HR-Employee-Attrition.csv")

# Convert Attrition to binary
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# Feature engineering
df['TenureBucket'] = pd.cut(df['YearsAtCompany'], bins=[0,2,5,10,40],
                            labels=['0-2','3-5','6-10','10+']).astype('category')

df['IncomeBucket'] = pd.cut(df['MonthlyIncome'], bins=4,
                            labels=['Low','Mid','High','Very High']).astype('category')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier

X = df.drop(columns=['Attrition'])
y = df['Attrition']

categorical = X.select_dtypes(include=['object', 'category']).columns
numeric = X.select_dtypes(exclude=['object', 'category']).columns

preprocess = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical),
    ('num', 'passthrough', numeric)
])

model = Pipeline([
    ('prep', preprocess),
    ('clf', XGBClassifier(random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)
preds = model.predict_proba(X_test)[:,1]

print("ROC-AUC:", roc_auc_score(y_test, preds))

# Transform X_test into dense matrix
X_test_transformed = model.named_steps['prep'].transform(X_test)

explainer = shap.TreeExplainer(model.named_steps['clf'])
shap_values = explainer.shap_values(X_test_transformed)

# Create the plot
shap.summary_plot(
    shap_values,
    X_test_transformed,
    feature_names=model.named_steps['prep'].get_feature_names_out(),
    show=False  # prevents auto-display
)

plt.tight_layout()
plt.savefig("/Users/kadendavis/PycharmProjects/employee-attrition-ml/visuals/shap_summary.png", bbox_inches="tight")
plt.close()


plt.figure(figsize=(10,6))
sns.countplot(data=df, x='Department', hue='Attrition')
plt.title("Attrition by Department")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("/Users/kadendavis/PycharmProjects/employee-attrition-ml/visuals/attrition_by_department.png")

plt.figure(figsize=(10,6))
sns.countplot(data=df, x='TenureBucket', hue='Attrition')
plt.title("Attrition by Tenure")
plt.tight_layout()
plt.savefig("/Users/kadendavis/PycharmProjects/employee-attrition-ml/visuals/attrition_by_tenure.png")
