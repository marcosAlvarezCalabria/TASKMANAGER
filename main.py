def print_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar Tarea")
    print("2. Listar Tareas")
    print("3. Completar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")





def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Seleccione una opción: ")
    
        match choice:
            case '1':
                task = input("Ingrese la descripción de la tarea: ")
                tasks.append({'desc': task, 'done': False})
                print("Tarea agregada.")
            case '2':
                if not tasks:
                    print("No hay tasks.")
                else:
                    for i, t in enumerate(tasks, 1):
                        status = "✔" if t['done'] else " "
                        print(f"{i}. [{status}] {t['desc']}")
            case '3':
                id = input("Número de tarea a completar: ")
                if id.isdigit() and 1 <= int(id) <= len(tasks):
                    tasks[int(id)-1]['done'] = True
                    print("Tarea marcada como completada.")
                else:
                    print("Índice inválido.")
            case '4':
                id = input("Número de tarea a eliminar: ")
                if id.isdigit() and 1 <= int(id) <= len(tasks):
                    removed = tasks.pop(int(id)-1)
                    print(f"Tarea '{removed['desc']}' eliminada.")
                else:
                    print("Índice inválido.")
            case '5':
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()