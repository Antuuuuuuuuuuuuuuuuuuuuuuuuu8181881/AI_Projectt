# AI_Projectt – Sistema de recomendación con IA generativa

**Estudiante:** Romina Antonia Tapia Tapia

**Asignatura:** ETDI02 – Unidad 3: Tendencias emergentes en inteligencia artificial

**Profesora:** Jacqueline Lisette San Martín Grandón

**Actividad:** Actividad formativa – GitHub Copilot

## Descripción del proyecto

Este repositorio contiene un sistema de recomendación de productos simple, escrito en Python con apoyo de herramientas de **inteligencia artificial generativa**, como GitHub Copilot.

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
## Proceso seguido

### Paso 1: Creación de la cuenta en GitHub

Ingresé a https://github.com, creé una cuenta con mi correo electrónico y la validé. Luego, en la sección de planes de GitHub Copilot, seleccioné el plan gratuito (Free).

### Paso 2: Creación del repositorio

Hice clic en **New**, asigné el nombre `AI_Projectt`, agregué una descripción y lo dejé como **público**. Además, agregué un archivo README, un archivo `.gitignore` con la plantilla de Python y la licencia MIT. Finalmente, hice clic en **Crear repositorio**.

CAPTURA1

### Paso 3: Creación del código con IA generativa

El archivo `recommendation_system.py` se desarrolló con apoyo de inteligencia artificial generativa. Se escribieron comentarios que describen cada parte del programa (por ejemplo, `# Cargar los datos` o `# Crear y entrenar el modelo`) y, a partir de ellos, la IA sugirió el código, que luego se revisó y se probó para comprobar que funcionara correctamente.

### Paso 4: Subida de los archivos a GitHub

Subí los archivos desde la página web de GitHub con la opción **Add file → Upload files** y guardé los cambios con el mensaje `Add files via upload`. Este paso equivale a los siguientes comandos de Git en la terminal:

```bash
git add .
git commit -m "Add recommendation system example"
git push -u origin main
```

CAPTURA2

## Reflexión

GitHub Copilot es un ejemplo de una tendencia emergente de la IA: los **asistentes de programación basados en IA generativa**. Estas herramientas permiten escribir código más rápido a partir de instrucciones en lenguaje natural, lo que facilita el aprendizaje y aumenta la productividad, incluso para personas que recién comienzan a programar. Sin embargo, sus sugerencias pueden contener errores, por lo que siempre es necesario revisar, probar y comprender el código antes de usarlo.

## Referencias

- GitHub. (s. f.). *GitHub Copilot documentation*. https://docs.github.com/en/copilot
- GitHub. (s. f.). *Getting started with GitHub Copilot*. https://docs.github.com/en/copilot/getting-started-with-github-copilot
