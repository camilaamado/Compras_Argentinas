# ====================================================================================================================================
#                                          Arbol de decision (Decision Tree)
# ====================================================================================================================================

# Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_recall_curve

# Cargar datos
dataset = pd.read_csv("/home/mario/Documents/ComprasArg/Data/CleanData/Compras_Clean.csv")

# Selección de Variables Predictoras y Variable Objetivo
X = dataset.drop('Compras_ultimos_6_meses',  axis=1)  # Variables predictoras
y = dataset['Compras_ultimos_6_meses']  # Variable objetivo

# Dividir el dataset en Train y Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo de árbol de decisión
modelo = DecisionTreeClassifier(
    random_state=42, 
    max_depth=5,  
    min_samples_split=10, 
    min_samples_leaf=5, 
    class_weight={0: 1, 1: 2}  # Dar más importancia a la clase minoritaria
)

# Entrenar el modelo
modelo.fit(X_train, y_train)

# Predicciones en el conjunto de prueba
y_pred = modelo.predict(X_test)

# Evaluar el modelo
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Obtener probabilidades de predicción
y_probs = modelo.predict_proba(X_test)[:, 1]  # Probabilidad de clase "Compra"

# Ajuste del umbral de decisión
threshold = 0.4
y_pred_new = (y_probs > threshold).astype(int)

# Evaluación con umbral ajustado
print("Confusion Matrix (Threshold = 0.4):\n", confusion_matrix(y_test, y_pred_new))
print("Classification Report:\n", classification_report(y_test, y_pred_new))

# Visualizar el Árbol de Decisión
plt.figure(figsize=(20,10))
plot_tree(modelo, feature_names=X.columns, class_names=["No Compra", "Compra"], filled=True)
plt.show()

# Obtener importancia de variables
importances = modelo.feature_importances_
feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values(by="Importance", ascending=False)

# Mostrar las variables más importantes
print(feature_importance_df)

# Graficar importancia de variables
plt.figure(figsize=(10, 5))
plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'], color='royalblue')
plt.xlabel("Importancia")
plt.ylabel("Variables")
plt.title("Importancia de Variables en el Modelo")
plt.gca().invert_yaxis()
plt.show()
