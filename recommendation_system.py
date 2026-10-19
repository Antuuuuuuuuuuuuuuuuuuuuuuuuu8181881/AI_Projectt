# recommendation_system.py
# Sistema de recomendación de productos simple, generado con apoyo de GitHub Copilot.
# Recomienda productos parecidos a uno dado, usando el algoritmo K-Nearest Neighbors (KNN).

# Importar las librerías necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors
from sklearn.preprocessing import MinMaxScaler

# Cargar los datos (dataset de ejemplo de productos)
# Cada producto tiene: precio (miles de pesos), valoración (1 a 5),
# popularidad (ventas del mes) y su categoría (etiqueta).
data = pd.DataFrame({
    "producto": ["Notebook A", "Notebook B", "Tablet C", "Tablet D", "Audífonos E",
                 "Audífonos F", "Smartwatch G", "Smartwatch H", "Notebook I", "Tablet J",
                 "Audífonos K", "Smartwatch L", "Notebook M", "Tablet N", "Audífonos O",
                 "Smartwatch P"],
    "precio":      [650, 720, 280, 310, 45, 60, 150, 170, 590, 260, 35, 140, 800, 330, 75, 190],
    "valoracion":  [4.5, 4.7, 4.1, 4.3, 3.9, 4.4, 4.0, 4.6, 4.2, 3.8, 3.7, 4.1, 4.8, 4.4, 4.5, 4.3],
    "popularidad": [120, 95, 210, 180, 400, 350, 160, 140, 110, 230, 420, 150, 80, 170, 300, 130],
    "categoria":   ["notebook", "notebook", "tablet", "tablet", "audifonos", "audifonos",
                    "smartwatch", "smartwatch", "notebook", "tablet", "audifonos",
                    "smartwatch", "notebook", "tablet", "audifonos", "smartwatch"],
})

# Preprocesamiento de datos: seleccionar características y etiqueta, y escalarlas (0 a 1)
features = data[["precio", "valoracion", "popularidad"]]
labels = data["categoria"]
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    features_scaled, labels, test_size=0.25, random_state=42, stratify=labels)

# Crear y entrenar el modelo de clasificación
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Realizar predicciones y evaluar el modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

# Modelo de recomendación: busca los productos más parecidos
recommender = NearestNeighbors(n_neighbors=4)
recommender.fit(features_scaled)


def recommend(product_name, n=3):
    """Devuelve los n productos más parecidos al producto indicado."""
    index = data.index[data["producto"] == product_name][0]
    _, indices = recommender.kneighbors([features_scaled[index]], n_neighbors=n + 1)
    similares = [i for i in indices[0] if i != index][:n]
    return data.loc[similares, ["producto", "precio", "valoracion", "categoria"]]


def predict_category(precio, valoracion, popularidad):
    """Predice la categoría de un producto nuevo a partir de sus características."""
    nuevo = pd.DataFrame([[precio, valoracion, popularidad]], columns=features.columns)
    return model.predict(scaler.transform(nuevo))[0]


# Ejemplo de uso de las funciones
if __name__ == "__main__":
    print("\nProductos recomendados para quien vio 'Notebook A':")
    print(recommend("Notebook A").to_string(index=False))

    categoria = predict_category(precio=300, valoracion=4.2, popularidad=190)
    print(f"\nCategoría predicha para un producto nuevo: {categoria}")
