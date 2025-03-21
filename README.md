# CI/CD Web App

Este es un proyecto de ejemplo para implementar un pipeline CI/CD utilizando GitHub Actions. El proyecto es una aplicación web sencilla utilizando Node.js y Express.

## Instrucciones

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu_usuario/ci-cd-web-app.git
    cd ci-cd-web-app
    ```

2. Instala las dependencias:

    ```bash
    npm install
    ```

3. Ejecuta las pruebas:

    ```bash
    npm test
    ```

4. Para iniciar la aplicación en desarrollo:

    ```bash
    npm start
    ```

## Pipeline de CI/CD

El pipeline de CI/CD está configurado con GitHub Actions. Cada vez que se realiza un *push* o *pull request* en la rama `main`, se ejecutan los siguientes pasos:

- Instalación de dependencias
- Ejecución de pruebas unitarias
- Despliegue automático a GitHub Pages

## Contribuciones

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature-nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agregando nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature-nueva-funcionalidad`).
5. Crea un Pull Request.
