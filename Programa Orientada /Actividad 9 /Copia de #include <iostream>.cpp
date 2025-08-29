#include <iostream>
#include <list>
#include <string>

using namespace std;

// Clase Persona 
class Persona {
public:
    string nombre;
    string apellido;
    char sexo;
    int edad;
    string ID;  

    // Constructor
    Persona(string nombre, string apellido, char sexo, int edad, string ID)
        : nombre(nombre), apellido(apellido), sexo(sexo), edad(edad), ID(ID) {}

    // Método para mostrar información
    virtual void mostrarInformacion() const {
        cout << "Nombre: " << nombre << " " << apellido << ", Edad: " << edad << ", Sexo: " << sexo << endl;
    }
};

// Clase Profesor
class Profesor : public Persona {
public:
    string titulo;
    string cedula;

    // Constructor
    Profesor(string nombre, string apellido, char sexo, int edad, string titulo, string cedula, string ID)
        : Persona(nombre, apellido, sexo, edad, ID), titulo(titulo), cedula(cedula) {}

    void mostrarInformacion() const override {
        Persona::mostrarInformacion();
        cout << "Título: " << titulo << ", Cédula: " << cedula << endl;
    }
};

// Clase Alumno
class Alumno : public Persona {
public:
    string noControl;
    int semestre;

    // Constructor
    Alumno(string nombre, string apellido, string noControl, int edad, char sexo, int semestre, string ID)
        : Persona(nombre, apellido, sexo, edad, ID), noControl(noControl), semestre(semestre) {}

    void mostrarInformacion() const override {
        Persona::mostrarInformacion();
        cout << "No. de Control: " << noControl << ", Semestre: " << semestre << endl;
    }
};

// Clase Materia
class Materia {
public:
    string nombre;
    int creditos;
    Profesor profesor;
    string ID;

    // Constructor
    Materia(string nombre, int creditos, Profesor profesor, string ID)
        : nombre(nombre), creditos(creditos), profesor(profesor), ID(ID) {}
};

// Clase Sistema Control Escolar
class SistemaControlEscolar {
private:
    list<Alumno> alumnos;
    list<Profesor> profesores;
    list<Materia> materias;

public:
    // Método para agregar
    void agregarAlumno(const Alumno& alumno) {
        alumnos.push_back(alumno);
    }

    void agregarProfesor(const Profesor& profesor) {
        profesores.push_back(profesor);
    }

    void agregarMateria(const Materia& materia) {
        materias.push_back(materia);
    }

    // Método para mostrar 
    void mostrarAlumnoPorID(const string& ID) const {
        for (const auto& alumno : alumnos) {
            if (alumno.ID == ID) {
                alumno.mostrarInformacion();
                return;
            }
        }
        cout << "Alumno con ID " << ID << " no encontrado." << endl;
    }

    void mostrarProfesorPorID(const string& ID) const {
        for (const auto& profesor : profesores) {
            if (profesor.ID == ID) {
                profesor.mostrarInformacion();
                return;
            }
        }
        cout << "Profesor con ID " << ID << " no encontrado." << endl;
    }

    void mostrarMateriaPorID(const string& ID) const {
        for (const auto& materia : materias) {
            if (materia.ID == ID) {
                cout << "Materia: " << materia.nombre << ", ID: " << materia.ID << ", Créditos: " << materia.creditos << ", Profesor: "
                     << materia.profesor.nombre << " " << materia.profesor.apellido << endl;
                return;
            }
        }
        cout << "Materia con ID " << ID << " no encontrada." << endl;
    }

    // Método para eliminar 
    void eliminarAlumno(const string& ID) {
        for (auto it = alumnos.begin(); it != alumnos.end(); ++it) {
            if (it->ID == ID) {
                alumnos.erase(it);
                cout << "Alumno con ID " << ID << " eliminado." << endl;
                return;
            }
        }
        cout << "Alumno no encontrado." << endl;
    }

    void eliminarProfesor(const string& ID) {
        for (auto it = profesores.begin(); it != profesores.end(); ++it) {
            if (it->ID == ID) {
                profesores.erase(it);
                cout << "Profesor con ID " << ID << " eliminado." << endl;
                return;
            }
        }
        cout << "Profesor no encontrado." << endl;
    }

    void eliminarMateria(const string& ID) {
        for (auto it = materias.begin(); it != materias.end(); ++it) {
            if (it->ID == ID) {
                materias.erase(it);
                cout << "Materia con ID " << ID << " eliminada." << endl;
                return;
            }
        }
        cout << "Materia no encontrada." << endl;
    }

    list<Profesor>& getProfesores() {
        return profesores;
    }
};

// Función para mostrar el menú
void mostrarMenu() {
    cout << "\nSistema de Control Escolar" << endl;
    cout << "1. Registrar Alumno" << endl;
    cout << "2. Eliminar Alumno" << endl;
    cout << "3. Registrar Profesor" << endl;
    cout << "4. Eliminar Profesor" << endl;
    cout << "5. Registrar Materia" << endl;
    cout << "6. Eliminar Materia" << endl;
    cout << "7. Alumno" << endl;
    cout << "8. Profesor" << endl;
    cout << "9. Materia" << endl;
    cout << "10. Salir" << endl;
    cout << "Seleccione una opción (1..10): ";
}

// Función principal (main)
int main() {
    SistemaControlEscolar sistema;
    int opcion;

    do {
        mostrarMenu();
        cin >> opcion;
        cin.ignore(); // Limpiar el buffer de entrada

        switch (opcion) {
            case 1: {  // Registrar Alumno
                string nombre, apellido, noControl, ID;
                int edad, semestre; 
                char sexo;
                cout << "\nIngrese el nombre del alumno: ";
                getline(cin, nombre);
                cout << "Ingrese el apellido del alumno: ";
                getline(cin, apellido);
                cout << "Ingrese el No. de Control: ";
                getline(cin, noControl);
                cout << "Ingrese la edad del alumno: ";
                cin >> edad;
                cout << "Ingrese el semestre: ";
                cin >> semestre;
                cout << "Ingrese el sexo (M/F): ";
                cin >> sexo;
                cin.ignore();
                cout << "Ingrese el ID del alumno: ";
                getline(cin, ID);

                Alumno nuevoAlumno(nombre, apellido, noControl, edad, sexo, semestre, ID);
                sistema.agregarAlumno(nuevoAlumno);
                break;
            }

            case 2: {  // Eliminar Alumno
                string ID;
                cout << "\nIngrese el ID del alumno a eliminar: ";
                getline(cin, ID);
                sistema.eliminarAlumno(ID);
                break;
            }

            case 3: {  // Registrar Profesor
                string nombre, apellido, titulo, cedula, ID;
                int edad;
                char sexo;
                cout << "\nIngrese el nombre del profesor: ";
                getline(cin, nombre);
                cout << "Ingrese el apellido del profesor: ";
                getline(cin, apellido);
                cout << "Ingrese la edad del profesor: ";
                cin >> edad;
                cout << "Ingrese el título del profesor: ";
                cin.ignore();
                getline(cin, titulo);
                cout << "Ingrese la cédula profesional del profesor: ";
                getline(cin, cedula);
                cout << "Ingrese el sexo (M/F): ";
                cin >> sexo;
                cin.ignore();
                cout << "Ingrese el ID del profesor: ";
                getline(cin, ID);

                Profesor nuevoProfesor(nombre, apellido, sexo, edad, titulo, cedula, ID);
                sistema.agregarProfesor(nuevoProfesor);
                break;
            }

            case 4: {  // Eliminar Profesor
                string ID;
                cout << "\nIngrese el ID del profesor a eliminar: ";
                getline(cin, ID);
                sistema.eliminarProfesor(ID);
                break;
            }

            case 5: {  // Registrar Materia
                string nombre, IDMateria, idProfesor;
                int creditos;
                cout << "\nIngrese el nombre de la materia: ";
                getline(cin, nombre);
                cout << "Ingrese los créditos de la materia: ";
                cin >> creditos;
                cin.ignore();
                cout << "Ingrese el ID del profesor: ";
                getline(cin, idProfesor);

                // Buscar al profesor por ID
                Profesor* profesor = nullptr;
                for (auto& prof : sistema.getProfesores()) {
                    if (prof.ID == idProfesor) {
                        profesor = &prof;
                        break;
                    }
                }

                if (profesor) {
                    cout << "\nIngrese el ID de la materia: ";
                    getline(cin, IDMateria);
                    Materia nuevaMateria(nombre, creditos, *profesor, IDMateria);
                    sistema.agregarMateria(nuevaMateria);
                } else {
                    cout << "Profesor no encontrado." << endl;
                }
                break;
            }

            case 6: {  // Eliminar Materia
                string ID;
                cout << "\nIngrese el ID de la materia a eliminar: ";
                getline(cin, ID);
                sistema.eliminarMateria(ID);
                break;
            }

            case 7: {  // Mostrar Alumno por ID
                string ID;
                cout << "\nIngrese el ID del alumno a mostrar: ";
                getline(cin, ID);
                sistema.mostrarAlumnoPorID(ID);
                break;
            }

            case 8: {  // Mostrar Profesor por ID
                string ID;
                cout << "\nIngrese el ID del profesor a mostrar: ";
                getline(cin, ID);
                sistema.mostrarProfesorPorID(ID);
                break;
            }

            case 9: {  // Mostrar Materia por ID
                string ID;
                cout << "\nIngrese el ID de la materia a mostrar: ";
                getline(cin, ID);
                sistema.mostrarMateriaPorID(ID);
                break;
            }

            case 10: {  // Salir
                cout << "Saliendo del sistema..." << endl;
                break;
            }

            default:
                cout << "Opción no válida. Intente nuevamente." << endl;
        }

    } while (opcion != 10);

    return 0;
}