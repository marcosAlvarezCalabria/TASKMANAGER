
# Task Manager

Gestor de tareas en Python para la gestión sencilla de tareas desde consola.

## Características
- Añadir, listar, completar y eliminar tareas
- Guardado y carga de tareas en archivo JSON
- Pruebas unitarias incluidas

## Requisitos
- Python 3.8 o superior
- (Opcional) pdoc o Sphinx para documentación automática

## Estructura del proyecto

```
python_project/
├── main.py                # Interfaz de consola para gestionar tareas
├── task_manager.py        # Lógica de las clases Task y TaskManager
├── test_task_manager.py   # Pruebas unitarias
├── README.md              # Este archivo
├── DOCUMENTACION.md       # Guía para generar documentación automática
└── ...
```

## Instalación
1. Clona el repositorio:
   ```bash
   git clone <URL-del-repo>
   cd taskmanager
   ```
2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Instala dependencias si las hubiera (por ejemplo, para documentación):
   ```bash
   pip install -r requirements.txt
   ```

## Uso
Ejecuta el gestor de tareas:
```bash
python main.py
```

### Ejemplo de uso

```
--- Gestor de Tareas ---
1. Agregar Tarea
2. Listar Tareas
3. Completar Tarea
4. Eliminar Tarea
5. Salir
Seleccione una opción: 1
Ingrese la descripción de la tarea: Hacer la compra
Tarea agregada.
```

## Ejecutar tests
```bash
python -m unittest test_task_manager.py
```

## Generar documentación automática
Puedes usar [pdoc](https://pdoc.dev/) para generar documentación HTML:
```bash
pip install pdoc
pdoc task_manager.py main.py
```

## Licencia
Este proyecto se distribuye bajo la licencia MIT.

## Autor
marcosAlvarezCalabria
