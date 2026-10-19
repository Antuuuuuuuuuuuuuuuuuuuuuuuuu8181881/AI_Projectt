
## Proceso seguido

### Paso 1: Creación de la cuenta en GitHub

Ingresé a https://github.com, creé una cuenta con mi correo electrónico y la validé. Luego, en la sección de planes de GitHub Copilot, seleccioné el plan gratuito (Free).

### Paso 2: Creación del repositorio

Hice clic en **New**, asigné el nombre `AI_Projectt`, agregué una descripción y lo dejé como **público**. Además, agregué un archivo README, un archivo `.gitignore` con la plantilla de Python y la licencia MIT. Finalmente, hice clic en **Crear repositorio**.

(ARRASTRA AQUÍ LA CAPTURA DE LA PÁGINA DE CREAR REPOSITORIO)

### Paso 3: Creación del código con IA generativa

El archivo `recommendation_system.py` se desarrolló con apoyo de inteligencia artificial generativa. Se escribieron comentarios que describen cada parte del programa (por ejemplo, `# Cargar los datos` o `# Crear y entrenar el modelo`) y, a partir de ellos, la IA sugirió el código, que luego se revisó y se probó para comprobar que funcionara correctamente.

### Paso 4: Subida de los archivos a GitHub

Subí los archivos desde la página web de GitHub con la opción **Add file → Upload files** y guardé los cambios con el mensaje `Add files via upload`. Este paso equivale a los siguientes comandos de Git en la terminal:

```bash
git add .
git commit -m "Add recommendation system example"
git push -u origin main
```

(ARRASTRA AQUÍ LA CAPTURA DEL REPOSITORIO CON LOS ARCHIVOS SUBIDOS)

## Reflexión

GitHub Copilot es un ejemplo de una tendencia emergente de la IA: los **asistentes de programación basados en IA generativa**. Estas herramientas permiten escribir código más rápido a partir de instrucciones en lenguaje natural, lo que facilita el aprendizaje y aumenta la productividad, incluso para personas que recién comienzan a programar. Sin embargo, sus sugerencias pueden contener errores, por lo que siempre es necesario revisar, probar y comprender el código antes de usarlo.

## Referencias

- GitHub. (s. f.). *GitHub Copilot documentation*. https://docs.github.com/en/copilot
- GitHub. (s. f.). *Getting started with GitHub Copilot*. https://docs.github.com/en/copilot/getting-started-with-github-copilot
