Nunca se deben crear migraciones en el entorno de produccion, solo en el de desarrollo, 

Flujo general de migraciones con Alembic en desarrollo y producción:

La idea principal es que las migraciones se generan en desarrollo, se versionan (generalmente con Git) y luego se aplican en producción. No se generan migraciones directamente en producción.

    Desarrollo:
        Realizas cambios en tus modelos de base de datos (e.g., agregas una nueva tabla, modificas una columna).
        Ejecutas alembic revision --autogenerate -m "Descripción del cambio" para generar un nuevo script de migración dentro de alembic/versions/. Este script contiene las instrucciones para aplicar (upgrade) y revertir (downgrade) los cambios.
        Pruebas localmente la migración con alembic upgrade head y, si es necesario, alembic downgrade <revisión> para asegurarte de que funciona correctamente.
        Commiteas los cambios, incluyendo el nuevo script de migración, a tu sistema de control de versiones (Git).

    Producción:
        Despliegas tu aplicación a producción (e.g., con Docker).
        Aquí está el punto clave: No necesitas generar la carpeta alembic/ desde cero en producción. Debes copiar la carpeta alembic/ (completa, con los scripts de migración dentro de versions/) dentro de tu imagen de Docker. Esto asegura que tienes el historial de migraciones disponible.
        Una vez desplegada la aplicación, ejecutas alembic upgrade head en el entorno de producción. Esto aplicará todas las migraciones pendientes a la base de datos de producción.
