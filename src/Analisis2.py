# ====================================================================================================================================0
#                                           Transformación y Limpieza de Datos (ETL - Transform)
# ====================================================================================================================================0


# importar librerías
import pandas as pd

# cargar datos
dataset = pd.read_csv("/home/mario/Documents/ComprasArg/Data/Raw/churn_dataset4.csv")

#============================================
# 2. Limpieza y transformación de Datos
#============================================

# 1° convertir fecha de string a datetime
dataset['Fecha'] = pd.to_datetime(dataset['Fecha'])

# 2° Convertir de variables categóricas a numéricas
dataset['Genero'] = dataset['Genero'].map({'Masculino': 0, 'Femenino': 1, 'Otro': 3})
dataset['Medio_de_pago'] = dataset['Medio_de_pago'].map({'QR': 0, 'Tarjeta de débito': 1, 'Transferencia bancaria': 2, 'Tarjeta de crédito': 3})
dataset['Tipo_de_tarjeta'] = dataset['Tipo_de_tarjeta'].map({'Mastercard': 0, 'Visa': 1, 'American Express': 2, 'Maestro': 3, 'Naranja': 4})
dataset['Provincia'] = dataset['Provincia'].map({'Córdoba': 0, 'Catamarca': 1, 'Chaco': 2, 'Formosa': 3, 'Buenos Aires': 4, 'Misiones': 5, 
                                       'La Rioja': 6, 'Tierra del Fuego': 7, 'La Pampa': 8, 'San Luis': 9, 'Chubut': 10, 
                                       'Entre Ríos': 11, 'Tucumán': 12, 'Santa Fe': 13, 'Neuquén': 14, 'Salta': 15, 
                                       'San Juan': 16, 'Santiago del Estero': 17, 'Río Negro': 18, 'Mendoza': 19, 
                                       'Corrientes': 20, 'Jujuy': 21})
dataset['Categoria'] = dataset['Categoria'].map({'Otros': 0, 'Deportes': 1, 'Electrónicos': 2, 'Juguetes': 3, 'Ropa': 4, 'Hogar': 5, 'Belleza': 6})
dataset['Web'] = dataset['Web'].map({'musimundo.com': 0, 'mercadolibre.com.ar': 1, 'fravega.com': 2, 'tiendabna.com.ar': 3, 'dafity.com': 4})

# Verificacion
print("Tipos de datos")
print(dataset.dtypes)
print("forma dataset")
print(dataset.head())
print("Info de las variables")
print(dataset.info())


# Guardar el dataset limpio en un nuevo archivo CSV
dataset.to_csv('/home/mario/Documents/ComprasArg/Data/CleanData/Compras_Clean.csv', index=False)

