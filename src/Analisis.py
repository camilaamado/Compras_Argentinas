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

# Ver los valores nulos y el porcentaje de nulos por columna
missing_values = dataset.isnull().sum()
missing_percentage = (missing_values / len(dataset)) * 100
print(pd.DataFrame({'Missing Values': missing_values, 'Percentage': missing_percentage}))

# Verificar los tipos de datos
print(dataset.dtypes)

# Estadísticas descriptivas para datos numéricos
print(dataset.describe())

# Estadísticas para datos categóricos
print(dataset['Eğitim_Seviyesi'].value_counts())

