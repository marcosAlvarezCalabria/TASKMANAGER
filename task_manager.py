class Task:
    """
    Clase que representa una tarea individual.
    Contiene información sobre el ID, nombre, descripción y estado de la tarea.
    """
    
    def __init__(self, id, name, description, status=False):
        """
        Constructor de la clase Task.
        Args:
            id: Identificador único de la tarea
            name: Nombre de la tarea
            description: Descripción detallada de la tarea
            status: Estado de la tarea (False=pendiente, True=completada)
        """
        self.id = id
        self.name = name
        self.description = description
        self.status = status

    def __str__(self):
        """
        Método que devuelve una representación en texto de la tarea.
        Returns:
            String con la información formateada de la tarea
        """
        status = "Completed" if self.status else "Pending"
        return f"Task ID: {self.id}, Description: {self.description}, Status: {status}"
    
class TaskManager:
    """
    Clase que gestiona una colección de tareas.
    Proporciona métodos para agregar, eliminar y buscar tareas.
    """

    def __init__(self):
        """
        Constructor de la clase TaskManager.
        Inicializa una lista vacía de tareas y un contador para IDs.
        """
        self.tasks = []
        self.next_id = 1

    def add_task(self, task):
        """
        Agrega una nueva tarea a la lista de tareas.
        Args:
            task: Objeto Task que se agregará a la lista
        """
        task = Task(self.next_id, task.description, task.status)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Tarea agregada: {task}")

    

    def list_tasks(self):
        """
        Obtiene todas las tareas almacenadas.
        Returns:
            Lista con todas las tareas
        """
        return self.tasks
    
    def complete_task(self, task_id):
        """
        Marca una tarea como completada según su ID.
        Args:
            task_id: ID de la tarea que se marcará como completada
        """
        for task in self.tasks:
            if task.id == task_id:
                task.status = True
                print(f"Tarea completada: {task}")
                return
        print(f"Tarea con ID {task_id} no encontrada.")

    
    def delete_task(self, task):
        """
        Elimina una tarea específica de la lista.
        Args:
            task: Objeto Task que se eliminará de la lista
        """
        self.tasks.remove(task)