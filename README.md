# Aplicación de Recetas con Redis

## Descripción del Proyecto
Este proyecto consiste en una aplicación de línea de comandos para la gestión de recetas de cocina, que ha sido migrada a usar Redis, una base de datos en memoria, en lugar de sistemas de gestión de bases de datos tradicionales. Esta transición a Redis permite operaciones de almacenamiento y recuperación de datos altamente eficientes, optimizando la respuesta y escalabilidad de la aplicación.

## Funcionalidades
- **Agregar recetas**: Permite a los usuarios introducir nuevas recetas, almacenando detalles como nombre, descripción, ingredientes y pasos.
- **Actualizar recetas**: Los usuarios pueden modificar recetas existentes.
- **Eliminar recetas**: Permite la eliminación de recetas de la base de datos.
- **Listar recetas**: Muestra todas las recetas almacenadas.
- **Buscar recetas**: Permite a los usuarios buscar recetas específicas basadas en varios criterios.
- **Salir de la aplicación**: Cierra la aplicación de forma segura.

## Tecnologías Utilizadas
- Python 3.8+
- Redis
- Flask (para crear una pequeña API REST opcional)

## Configuración del Proyecto

### Prerrequisitos
- Python 3.8 o superior.
- Redis server instalado y en ejecución en tu máquina local o en un servidor remoto.

### Instalación
1. Clona el repositorio a tu máquina local:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
