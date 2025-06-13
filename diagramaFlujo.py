from graphviz import Digraph

# Crear un nuevo diagrama dirigido
uml_diagram = Digraph(comment='Plataforma de Telemedicina Simplificada')

# Definir los nodos principales del sistema
uml_diagram.node('Usuario', '''Usuario
+ username: String
+ email: String
+ registrar()
+ conectarDispositivo()''')

uml_diagram.node('DispositivoInteligente', '''Dispositivo Inteligente
+ tipo: String
+ signosVitales: JSON
+ enviarDatos()''')

uml_diagram.node('HistorialDeSalud', '''Historial de Salud
+ datos: JSON
+ almacenarDatos()
+ mostrarHistorial()''')

uml_diagram.node('InteligenciaArtificial', '''Inteligencia Artificial
+ algoritmo: String
+ analizarDatos()
+ predecirRiesgos()''')

uml_diagram.node('Medico', '''Médico
+ nombre: String
+ especialización: String
+ revisarHistorial()
+ darRetroalimentación()''')

uml_diagram.node('CitasMedicas', '''Citas Médicas
+ programarCita()
+ realizarConsulta()''')

uml_diagram.node('Notificaciones', '''Notificaciones
+ mensaje: String
+ enviarAlerta()''')

# Relacionar las clases en un flujo lógico
uml_diagram.edge('Usuario', 'DispositivoInteligente', label='Conectar Dispositivo')
uml_diagram.edge('DispositivoInteligente', 'HistorialDeSalud', label='Enviar Signos Vitales')
uml_diagram.edge('HistorialDeSalud', 'InteligenciaArtificial', label='Almacenar y Analizar Datos')
uml_diagram.edge('InteligenciaArtificial', 'Medico', label='Enviar Predicciones')
uml_diagram.edge('Medico', 'HistorialDeSalud', label='Revisar y Actualizar Historial')
uml_diagram.edge('Usuario', 'CitasMedicas', label='Programar Cita')
uml_diagram.edge('CitasMedicas', 'Medico', label='Realizar Consulta')
uml_diagram.edge('HistorialDeSalud', 'Notificaciones', label='Enviar Alertas')
uml_diagram.edge('Usuario', 'Notificaciones', label='Recibir Alertas')

# Mostrar el diagrama
uml_diagram.render('diagrama_telemedicina', format='png', view=True)


print("Diagrama UML generado exitosamente")
