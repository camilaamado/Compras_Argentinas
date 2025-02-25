# Importar librerías
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Cargar datos (puedes reemplazar con tu propio dataset)
dataset = pd.read_csv("/home/mario/Documents/ComprasArg/Data/CleanData/Compras_Clean.csv")

# Selección de Variables Predictoras y Variable Objetivo
X = dataset.drop(['Compras_ultimos_6_meses'], axis=1)  # Variables predictoras
y = dataset['Compras_ultimos_6_meses']  # Variable objetivo

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el rango de valores para n_estimators
# Definir el rango de valores para los parámetros
param_grid = {
    'n_estimators': [400],
    'max_depth': [5],
    'min_samples_split': [2],  # Ajustar este parámetro
    'min_samples_leaf': [1],  # Ajustar este parámetro
    'class_weight': ['balanced']  # Mantener el balanceo de clases
}

# Crear el clasificador
rf = RandomForestClassifier(random_state=42)

# Crear GridSearchCV con validación cruzada de 5 pliegues
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)

# Ajustar el modelo con los datos de entrenamiento
grid_search.fit(X_train, y_train)

# Mostrar los mejores parámetros encontrados
print(f"Mejores parámetros encontrados: {grid_search.best_params_}")
print(f"Mejor precisión: {grid_search.best_score_}")

# Evaluar el modelo ajustado
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# Evaluar precisión y otras métricas
print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))

print("Reporte de clasificación:")
print(classification_report(y_test, y_pred))
