import unittest
from unittest.mock import patch, mock_open, MagicMock
import json

from task_manager import Task, TaskManager

class TestTask(unittest.TestCase):
    # Verifica que el constructor de Task asigna correctamente los atributos
    def test_init_sets_attributes(self):
        t = Task(1, "Test task", True)
        self.assertEqual(t.id, 1)
        self.assertEqual(t.description, "Test task")
        self.assertTrue(t.status)

    # Comprueba que __str__ muestra correctamente una tarea pendiente
    def test_str_pending(self):
        t = Task(2, "Do homework", False)
        self.assertEqual(str(t), "Task ID: 2, Description: Do homework, Status: Pending")

    # Comprueba que __str__ muestra correctamente una tarea completada
    def test_str_completed(self):
        t = Task(3, "Read book", True)
        self.assertEqual(str(t), "Task ID: 3, Description: Read book, Status: Completed")

class TestTaskManager(unittest.TestCase):
    # Se ejecuta antes de cada test, inicializa TaskManager y simula save_tasks
    def setUp(self):
        self.tm = TaskManager()
        self.tm.save_tasks = MagicMock()  # Prevent file I/O

    # Verifica que al agregar una tarea, se incrementa el ID y se llama a save_tasks
    def test_add_task_increments_id_and_saves(self):
        t = Task(0, "Task 1")
        self.tm.add_task(t)
        self.assertEqual(len(self.tm.tasks), 1)
        self.assertEqual(self.tm.tasks[0].id, 1)
        self.assertEqual(self.tm.tasks[0].description, "Task 1")
        self.tm.save_tasks.assert_called()

    # Comprueba que list_tasks devuelve todas las tareas agregadas
    def test_list_tasks_returns_all(self):
        t1 = Task(0, "Task 1")
        t2 = Task(0, "Task 2")
        self.tm.add_task(t1)
        self.tm.add_task(t2)
        tasks = self.tm.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].description, "Task 1")
        self.assertEqual(tasks[1].description, "Task 2")

    # Verifica que una tarea se marca como completada y se guarda
    def test_complete_task_marks_completed_and_saves(self):
        t = Task(0, "Task to complete")
        self.tm.add_task(t)
        self.tm.tasks[0].status = False
        with patch("builtins.print"):
            self.tm.complete_task(1)
        self.assertTrue(self.tm.tasks[0].status)
        self.tm.save_tasks.assert_called()

    # Comprueba que si intentas completar una tarea inexistente, muestra el mensaje correcto
    def test_complete_task_not_found(self):
        with patch("builtins.print") as mock_print:
            self.tm.complete_task(99)
            mock_print.assert_called_with("Tarea con ID 99 no encontrada.")

    # Verifica que una tarea se elimina correctamente y se guarda
    def test_delete_task_removes_and_saves(self):
        t = Task(0, "Task to delete")
        self.tm.add_task(t)
        self.assertEqual(len(self.tm.tasks), 1)
        self.tm.delete_task(self.tm.tasks[0])
        self.assertEqual(len(self.tm.tasks), 0)
        self.tm.save_tasks.assert_called()

    # Simula la carga de tareas desde un archivo y verifica que se cargan correctamente
    @patch("builtins.open", new_callable=mock_open, read_data='[{"id":1,"description":"A","status":false}]')
    def test_load_tasks_loads_from_file(self, mock_file):
        tm = TaskManager()
        tm.FILENAME = "mock.json"
        tm.load_tasks()
        self.assertEqual(len(tm.tasks), 1)
        self.assertEqual(tm.tasks[0].id, 1)
        self.assertEqual(tm.tasks[0].description, "A")
        self.assertFalse(tm.tasks[0].status)
        self.assertEqual(tm.next_id, 2)

    # Simula guardar tareas en un archivo y verifica que se escribe el JSON correcto
    @patch("builtins.open", new_callable=mock_open)
    def test_save_tasks_writes_to_file(self, mock_file):
        t = Task(1, "Save me", False)
        self.tm.tasks = [t]
        self.tm.FILENAME = "mock.json"
        self.tm.save_tasks = TaskManager.save_tasks.__get__(self.tm)
        self.tm.save_tasks()
        mock_file.assert_called_with("mock.json", "w")
        handle = mock_file()
        # Concatenar todas las llamadas a write para comparar el contenido completo
        written = "".join(call.args[0] for call in handle.write.call_args_list)
        expected = json.dumps([t.__dict__], indent=4)
        self.assertEqual(written, expected)

if __name__ == "__main__":
    unittest.main()
