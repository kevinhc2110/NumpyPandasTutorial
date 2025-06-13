from graphviz import Digraph

# Crear un objeto Digraph
dot = Digraph()

# Agregar nodos al gráfico
dot.node('A', 'Registro de Usuario')
dot.node('B', 'Selección de Preferencias')
dot.node('C', 'Generación de Paquete')
dot.node('D', 'Entrega Semanal')
dot.node('E', 'Interacción en Discord')
dot.node('F', 'Feedback y Mejoras')

# Agregar aristas entre los nodos
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF'])

# Renderizar y mostrar el gráfico
dot.render('mapa_conceptual', format='png', view=True)
