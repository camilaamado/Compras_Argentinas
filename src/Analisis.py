# ====================================================================================================================================0
#                                           Transformación y Limpieza de Datos (ETL - Transform)
# ====================================================================================================================================0


# importar librerías
import pandas as pd

# cargar datos
dataset = pd.read_csv("/home/mario/Documents/ComprasArg/Data/Raw/churn_dataset4.csv")


#============================================
# 1. Exploración de los Datos
#============================================

# Ver las primeras filas del dataset para obtener una visión general
print(dataset.head())

# Obtener información general del dataset (tipos de datos, valores nulos, etc.)
print(dataset.info())

# Verificar los tipos de datos
print(dataset.dtypes)


# Ver los valores nulos y el porcentaje de nulos por columna
missing_values = dataset.isnull().sum()
missing_percentage = (missing_values / len(dataset)) * 100
print(pd.DataFrame({'Missing Values': missing_values, 'Percentage': missing_percentage}))

# Asegurarte de que no hay valores nulos
print(dataset.isnull().sum())
if dataset.isnull().sum().sum() == 0:
    print("No hay valores nulos en el dataset.")
else:
    print("Hay valores nulos en el dataset.")   

# categorías presentes en cada variable categórica y su frecuencia
for col in dataset.select_dtypes(include=['object', 'category']).columns:
    print(f"Frecuencia de categorías en {col}:")
    print(dataset[col].value_counts())
    print("-" * 50)


