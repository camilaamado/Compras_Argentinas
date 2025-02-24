## Exploración de los Datos

### 1. Ver las Primeras Filas del Dataset
Para obtener una visión general de los datos, es recomendable visualizar las primeras filas del dataset.

Ejemplo de datos:

| Fecha      | Género   | Edad | Medio de Pago           | Tipo de Tarjeta  | Compras últimos 6 meses | Provincia       | Monto Compra | Categoría     | Web                  |
|------------|----------|------|-------------------------|------------------|-------------------------|----------------|--------------|--------------|----------------|
| 2024-04-04 | Femenino | 67   | Tarjeta de débito       | American Express | True                    | Tierra del Fuego | 880486        | Ropa         | mercadolibre.com.ar |
| 2023-06-25 | Masculino| 48   | Tarjeta de crédito      | Mastercard       | False                   | Córdoba        | 739447        | Electrónicos  | fravega.com       |
| 2024-01-28 | Masculino| 29   | Tarjeta de crédito      | Visa             | False                   | Misiones        | 183404        | Hogar         | tiendabna.com.ar   |
| 2023-10-30 | Otro     | 24   | Tarjeta de débito       | Visa             | True                    | Jujuy          | 860619        | Otros         | tiendabna.com.ar   |
| 2023-06-25 | Otro     | 32   | Transferencia bancaria  | Maestro          | False                   | Catamarca      | 702336        | Ropa         | mercadolibre.com.ar |

---

### 2. Información General del Dataset

Para conocer la estructura del dataset, se analiza el número de filas y columnas, los tipos de datos y si existen valores nulos.

**Columnas y tipos de datos:**

| Columna                  | Tipo de Dato |
|--------------------------|-------------|
| Fecha                    | object      |
| Género                   | object      |
| Edad                     | int64       |
| Medio de Pago            | object      |
| Tipo de Tarjeta          | object      |
| Compras últimos 6 meses  | bool        |
| Provincia                | object      |
| Monto Compra             | int64       |
| Categoría               | object      |
| Web                      | object      |

---

### 3. Análisis de Valores Nulos

No se encontraron valores nulos en el dataset:

| Columna                  | Valores Nulos | Porcentaje |
|--------------------------|--------------|------------|
| Fecha                    | 0            | 0.0%       |
| Género                   | 0            | 0.0%       |
| Edad                     | 0            | 0.0%       |
| Medio de Pago            | 0            | 0.0%       |
| Tipo de Tarjeta          | 0            | 0.0%       |
| Compras últimos 6 meses  | 0            | 0.0%       |
| Provincia                | 0            | 0.0%       |
| Monto Compra             | 0            | 0.0%       |
| Categoría               | 0            | 0.0%       |
| Web                      | 0            | 0.0%       |

---

### 4. Frecuencia de Categorías

#### **Frecuencia de Género**
| Género    | Frecuencia |
|-----------|-----------|
| Otro      | 36        |
| Femenino  | 33        |
| Masculino | 31        |

#### **Frecuencia de Medio de Pago**
| Medio de Pago            | Frecuencia |
|-------------------------|-----------|
| QR                      | 28        |
| Tarjeta de débito       | 27        |
| Transferencia bancaria  | 25        |
| Tarjeta de crédito      | 20        |

#### **Frecuencia de Tipo de Tarjeta**
| Tipo de Tarjeta  | Frecuencia |
|-----------------|-----------|
| Mastercard      | 25        |
| Visa           | 21        |
| American Express| 20        |
| Maestro        | 18        |
| Naranja        | 16        |

#### **Frecuencia de Provincia**
| Provincia              | Frecuencia |
|-----------------------|-----------|
| Córdoba               | 7         |
| Catamarca             | 7         |
| Chaco                 | 7         |
| Formosa               | 6         |
| Buenos Aires          | 6         |
| Misiones              | 6         |
| La Rioja              | 6         |
| Tierra del Fuego      | 5         |
| La Pampa             | 5         |
| San Luis              | 5         |
| ...                   | ...       |

#### **Frecuencia de Categoría**
| Categoría     | Frecuencia |
|--------------|-----------|
| Otros       | 18        |
| Deportes    | 16        |
| Electrónicos| 16        |
| Juguetes    | 14        |
| Ropa        | 13        |
| Hogar       | 13        |
| Belleza     | 10        |

#### **Frecuencia de Web**
| Web                  | Frecuencia |
|---------------------|-----------|
| musimundo.com      | 24        |
| mercadolibre.com.ar| 21        |
| fravega.com       | 21        |
| tiendabna.com.ar  | 20        |
| dafity.com        | 14        |

---

## Limpieza y Transformación de Datos

Se limpiaron los datos y se transformaron las variables categóricas asignando números a cada una:

- **Genero**:
  - Masculino: 0
  - Femenino: 1
  - Otro: 3

- **Medio_de_pago**:
  - QR: 0
  - Tarjeta de débito: 1
  - Transferencia bancaria: 2
  - Tarjeta de crédito: 3

- **Tipo_de_tarjeta**:
  - Mastercard: 0
  - Visa: 1
  - American Express: 2
  - Maestro: 3
  - Naranja: 4

- **Provincia**:
  - Córdoba: 0
  - Catamarca: 1
  - Chaco: 2
  - Formosa: 3
  - Buenos Aires: 4
  - Misiones: 5
  - La Rioja: 6
  - Tierra del Fuego: 7
  - La Pampa: 8
  - San Luis: 9
  - Chubut: 10
  - Entre Ríos: 11
  - Tucumán: 12
  - Santa Fe: 13
  - Neuquén: 14
  - Salta: 15
  - San Juan: 16
  - Santiago del Estero: 17
  - Río Negro: 18
  - Mendoza: 19
  - Corrientes: 20
  - Jujuy: 21

- **Categoria**:
  - Otros: 0
  - Deportes: 1
  - Electrónicos: 2
  - Juguetes: 3
  - Ropa: 4
  - Hogar: 5
  - Belleza: 6

- **Web**:
  - musimundo.com: 0
  - mercadolibre.com.ar: 1
  - fravega.com: 2
  - tiendabna.com.ar: 3
  - dafity.com: 4


Esto permite que las variables categóricas sean utilizadas en análisis y modelos de aprendizaje automático de manera eficiente.

