# AI_Project – Sistema de recomendación con GitHub Copilot

**Estudiante:** Romina Antonia Tapia Tapia
**Asignatura:** ETDI02 – Unidad 3: Tendencias emergentes en inteligencia artificial
**Actividad:** Actividad formativa – GitHub Copilot

## Descripción del proyecto

Este repositorio contiene un sistema de recomendación de productos simple, escrito en Python con apoyo de **GitHub Copilot**, un asistente de programación basado en inteligencia artificial generativa.

El programa `recommendation_system.py`:

1. Crea un conjunto de datos de ejemplo con 16 productos (precio, valoración, popularidad y categoría).
2. Entrena un modelo de **K-Nearest Neighbors (KNN)** para predecir la categoría de un producto.
3. Mide la precisión del modelo con datos de prueba.
4. Recomienda los productos más parecidos a uno elegido por el usuario.

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
python recommendation_system.py
```

Resultado esperado:

```
Precisión del modelo: 75.00%

Productos recomendados para quien vio 'Notebook A':
  producto  precio  valoracion categoria
Notebook B     720         4.7  notebook
Notebook I     590         4.2  notebook
Notebook M     800         4.8  notebook

Categoría predicha para un producto nuevo: tablet
```

## Proceso seguido

### Paso 1: Creación de la cuenta en GitHub
Ingresé a https://github.com, creé una cuenta con mi correo electrónico y la validé. Luego, en la sección de precios de GitHub Copilot, seleccioné el plan gratuito.

*(Captura de pantalla de la cuenta creada)*

### Paso 2: Creación del repositorio
Hice clic en **New**, asigné el nombre `AI_Project`, lo dejé como **público** y agregué un archivo README, un archivo `.gitignore` (plantilla Python) y una licencia MIT. Finalmente, hice clic en **Create repository**.

*(Captura de pantalla del repositorio creado)*

### Paso 3: Creación del archivo de código con GitHub Copilot
Creé el archivo `recommendation_system.py`. Escribí comentarios en español que describían lo que necesitaba (por ejemplo, `# Importar las librerías necesarias` o `# Crear y entrenar el modelo`), y GitHub Copilot sugirió el código correspondiente, que revisé y ajusté.

*(Captura de pantalla del código y de las sugerencias de Copilot)*

### Paso 4: Prueba del programa
Ejecuté el programa y verifiqué que entregara la precisión del modelo y las recomendaciones.

*(Captura de pantalla del resultado)*

### Paso 5: Subida de los cambios a GitHub
Agregué los archivos al repositorio y guardé los cambios con el mensaje `Add recommendation system example`, usando estos comandos:

```bash
git add .
git commit -m "Add recommendation system example"
git push -u origin main
```

*(Captura de pantalla del repositorio con los archivos subidos)*

## Reflexión

GitHub Copilot es un ejemplo de una tendencia emergente de la IA: los **asistentes de programación basados en IA generativa**. Permite escribir código más rápido a partir de instrucciones en lenguaje natural, lo que facilita el aprendizaje y aumenta la productividad. Sin embargo, sus sugerencias pueden contener errores, por lo que siempre es necesario revisar, probar y comprender el código antes de usarlo.

## Referencias

- GitHub. (s. f.). *GitHub Copilot documentation*. https://docs.github.com/en/copilot
- GitHub. (s. f.). *Getting started with GitHub Copilot*. https://docs.github.com/en/copilot/getting-started-with-github-copilot
