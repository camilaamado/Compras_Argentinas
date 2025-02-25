# ====================================================================================================================================
#                                           Transformación y Limpieza de Datos (ETL - Transform)
# ====================================================================================================================================


import pandas as pd
from sklearn.preprocessing import LabelEncoder

# cargar datos
dataset = pd.read_csv("/home/mario/Documents/ComprasArg/Data/Raw/churn_dataset4.csv")

#============================================
# 2. Limpieza y transformación de Datos
#============================================

# 1° convertir fecha de string a datetime
dataset['Fecha'] = pd.to_datetime(dataset['Fecha'])
dataset['year'] = dataset['Fecha'].dt.year
dataset['month'] = dataset['Fecha'].dt.month
dataset['day'] = dataset['Fecha'].dt.day

# Eliminar la columna original de fecha 
dataset = dataset.drop(columns=['Fecha'])

# 2° Convertir de variables categóricas a numéricas
dataset['Genero'] = dataset['Genero'].map({'Masculino': 0, 'Femenino': 1, 'Otro': 3})
dataset['Medio_de_pago'] = dataset['Medio_de_pago'].map({'QR': 0, 'Tarjeta de débito': 1, 'Transferencia bancaria': 2, 'Tarjeta de crédito': 3})
dataset['Tipo_de_tarjeta'] = dataset['Tipo_de_tarjeta'].map({'Mastercard': 0, 'Visa': 1, 'American Express': 2, 'Maestro': 3, 'Naranja': 4})
dataset['Categoria'] = dataset['Categoria'].map({'Otros': 0, 'Deportes': 1, 'Electrónicos': 2, 'Juguetes': 3, 'Ropa': 4, 'Hogar': 5, 'Belleza': 6})
dataset['Web'] = dataset['Web'].map({'musimundo.com': 0, 'mercadolibre.com.ar': 1, 'fravega.com': 2, 'tiendabna.com.ar': 3, 'dafity.com': 4})

# Label Encoding (Codificación Ordinal) para la variable "Provincia"
encoder = LabelEncoder()
dataset['Provincia'] = encoder.fit_transform(dataset['Provincia'])


# Verificacion
print(dataset.head())

# Guardar el dataset limpio en un nuevo archivo CSV
dataset.to_csv('/home/mario/Documents/ComprasArg/Data/CleanData/Compras_Clean.csv', index=False)
print("Nuevo dataset limpio guardado: Compras_Clean.csv")

