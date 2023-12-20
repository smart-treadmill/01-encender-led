# Proyecto React con FastAPI

## Descripción
Este es un proyecto pequeño que combina una aplicación React en el frontend con un backend en Python usando FastAPI.

## Requisitos Previos
Asegúrate de tener instalado lo siguiente:
- Python 3.8 o superior
- Node.js y npm

## Instalación y Ejecución

### Backend: FastAPI
1. Instala FastAPI y Uvicorn:
   ```bash
   pip install fastapi uvicorn
   ```
2. Navega a la carpeta del servidor y ejecuta el servidor con Uvicorn:
   ```bash
   cd server
   uvicorn app:app --reload
   ```
   Esto iniciará el servidor en modo de desarrollo, recargando automáticamente ante cualquier cambio.

### Frontend: React
1. Navega a la carpeta del cliente:
   ```bash
   cd client
   ```
2. Instala las dependencias con npm:
   ```bash
   npm install
   ```
3. Inicia la aplicación React en modo de desarrollo:
   ```bash
   npm run dev
   ```

## Uso
Después de iniciar el servidor backend y el cliente frontend, la aplicación estará lista para ser utilizada en el navegador.

## Contribuir
Las contribuciones al proyecto son bienvenidas. Por favor, haz un fork del repositorio y crea un pull request con tus cambios.

## Licencia
Este proyecto está licenciado bajo [Nombre de la Licencia]. Consulta el archivo LICENSE para más detalles.
