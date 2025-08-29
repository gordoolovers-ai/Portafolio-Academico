#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Clases del empleado 
struct Empleado {
    //Atributos
    int id;
    string nombre;
    string contrasena;
    string correo;
    string telefono;
    string puesto;
};

//Agregar un empleado
void agregarEmpleado(vector<Empleado>& empleados) {
    Empleado nuevoEmpleado;
    
    cout << "Ingrese el ID del empleado: ";
    cin >> nuevoEmpleado.id;
    cin.ignore(); // Para limpiar el buffer de entrada
    cout << "Ingrese el nombre del empleado: ";
    getline(cin, nuevoEmpleado.nombre);// Nos permite poner un nombre completo
    //lee la cadena completa de texto que el usuario ingresa y la almacena en el atributo
    cout << "Ingrese la contraseña del empleado: ";
    getline(cin, nuevoEmpleado.contrasena);
    cout << "Ingrese el correo del empleado: ";
    getline(cin, nuevoEmpleado.correo);
    cout << "Ingrese el correo del telefono: ";
    getline(cin, nuevoEmpleado.telefono);
    cout << "Ingrese el nombre del puesto: ";
    getline(cin, nuevoEmpleado.puesto);
    
    //Agrega el objeto nuevoEmpleado al final del vector empleados. 
    //Esta es la manera de insertar un nuevo empleado en la lista de empleados.
    empleados.push_back(nuevoEmpleado);
    cout << "Empleado agregado exitosamente.\n";
}

//Eliminar un empleado 
void eliminarEmpleado(vector<Empleado>& empleados) {
    int id;
    cout << "Ingrese el ID del empleado a eliminar: ";
    cin >> id;
    
    bool encontrado = false;
    for (auto it = empleados.begin(); it != empleados.end(); ++it) {
        if (it->id == id) {
            empleados.erase(it);
            cout << "Empleado eliminado exitosamente.\n";
            encontrado = true;
            break;
        }
    }
    // Cuando no esta registrado agregamos una cadena 
    if (!encontrado) {
        cout << "Empleado no encontrado.\n";
    }
}

//Cambia la contraseña de un empleado
void cambiarContrasena(vector<Empleado>& empleados) {
    int id;//Ayuda para localizar el id a cambiar 
    cout << "Ingrese el ID del empleado para cambiar la contraseña: ";
    cin >> id;
    
    bool encontrado = false;
    for (auto& emp : empleados) {
        if (emp.id == id) {
            cout << "Ingrese la nueva contraseña: ";
            cin.ignore(); // Limpiar el buffer de entrada
            getline(cin, emp.contrasena);
            cout << "Contraseña cambiada exitosamente.\n";
            encontrado = true;
            break;
        }
    }
    
    if (!encontrado) {
        cout << "Empleado no encontrado.\n";
    }
}

//Actualizar los datos del empleado
void actualizarDatos(vector<Empleado>& empleados) {
    int id;
    cout << "Ingrese el ID del empleado para actualizar sus datos: ";
    cin >> id;
    
    bool encontrado = false;
    for (auto& emp : empleados) {
        if (emp.id == id) {
            cin.ignore(); // Limpiar el buffer de entrada
            cout << "Ingrese el nuevo nombre: ";
            getline(cin, emp.nombre);
            cout << "Ingrese el nuevo correo: ";
            getline(cin, emp.correo);
            cout << "Ingrese el nuevo telefono: ";
            getline(cin, emp.telefono);
            cout << "Ingrese el nuevo puesto: ";
            getline(cin, emp.puesto);
            cout << "Datos actualizados exitosamente.\n";
            encontrado = true;
            break;
        }
    }
    
    if (!encontrado) {
        cout << "Empleado no encontrado.\n";
    }
}

// Menú principal
int main() {
    vector<Empleado> empleados;
    int opcion;
    
    do {
        cout << "\nMenu de Recursos Humanos:\n";
        cout << "1. Alta de empleado\n";
        cout << "2. Baja de empleado\n";
        cout << "3. Cambio de contraseña\n";
        cout << "4. Actualización de datos\n";
        cout << "5. Salir\n";
        cout << "Seleccione una opción: ";
        cin >> opcion;
        
        switch(opcion) {
            case 1:
                agregarEmpleado(empleados);
                break;
            case 2:
                eliminarEmpleado(empleados);
                break;
            case 3:
                cambiarContrasena(empleados);
                break;
            case 4:
                actualizarDatos(empleados);
                break;
            case 5:
                cout << "Saliendo del sistema.\n";
                break;
            default:
                cout << "Opción no válida, intente nuevamente.\n";
        }
    } while(opcion != 5);
    
    return 0;
}