
# Generador de Códigos QR

Este proyecto proporciona una API y una interfaz de usuario (UI) para generar códigos QR basados en texto proporcionado por el usuario. Soporta la generación de códigos QR en formatos PNG y SVG.

## Características

- API construida con FastAPI para generar códigos QR.
- Soporte para generar códigos QR en formatos PNG y SVG.
- Interfaz de usuario construida con HTML y TailwindCSS que interactúa con la API.
- Opciones de personalización para el color de relleno y el color de fondo del código QR.

## Tecnologías Utilizadas

- FastAPI
- Pydantic
- qrcode
- TailwindCSS
- JavaScript (Fetch API para solicitudes asíncronas)

## Requisitos

Para ejecutar este proyecto, necesitarás:

- Python 3.6+
- FastAPI
- Uvicorn (como servidor ASGI)
- La biblioteca `qrcode` con soporte para SVG

Puedes instalar las dependencias necesarias con el siguiente comando:

```bash
pip install fastapi uvicorn qrcode[pil]
```

## Configuración y Ejecución

### API

Para ejecutar la API, navega al directorio del proyecto y ejecuta:

```bash
uvicorn main:app --reload
```

Esto iniciará el servidor en `http://127.0.0.1:8000`. La documentación de la API estará disponible en `http://127.0.0.1:8000/docs`.

### Interfaz de Usuario

Abre el archivo `index.html` en tu navegador para acceder a la interfaz de usuario. Asegúrate de que la API esté ejecutándose, ya que la UI interactuará con ella para generar los códigos QR.

## Uso

Desde la interfaz de usuario:

1. Ingresa el texto que deseas codificar en el campo proporcionado.
2. Selecciona los colores de relleno y de fondo para el código QR.
3. Elige el formato de salida deseado (PNG o SVG).
4. Haz clic en "Generar QR" para ver el código QR generado.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, envía un pull request o abre un issue si tienes sugerencias de mejora o correcciones.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
