from graphviz import Digraph

# Crear el grafo
dot = Digraph(comment='Relative Clauses Mind Map', graph_attr={'size': '12,12', 'splines': 'ortho'})  # Tamaño y ortogonalidad

# Nodo central
dot.node('A', 'Relative Clauses')

# Ramas principales
dot.node('B', 'Definition')
dot.node('C', 'Relative Pronouns')
dot.node('D', 'Use in Speech')
dot.node('E', 'Examples')

# Conectar las ramas principales al nodo central de forma radial
dot.edge('A', 'B')
dot.edge('A', 'C')
dot.edge('A', 'D')
dot.edge('A', 'E')

# Definición
dot.node('B1', 'Connect ideas \nand add information \nabout a noun')
dot.edge('B', 'B1')

# Pronombres Relativos
dot.node('C1', 'Who: people')
dot.node('C2', 'Which: things/animals')
dot.node('C3', 'That: people/things')
dot.node('C4', 'Whose: possession')

# Conectar pronombres de manera más centrada y radial
dot.edge('C', 'C1')
dot.edge('C', 'C2')
dot.edge('C', 'C3')
dot.edge('C', 'C4')

# Uso en el Discurso
dot.node('D1', 'Defining Clauses: \nEssential information')
dot.node('D2', 'Non-Defining Clauses: \nAdditional information (commas)')
dot.edge('D', 'D1')
dot.edge('D', 'D2')

# Ejemplos
dot.node('E1', '"The man **who** is talking is my teacher."')
dot.node('E2', '"The book **that** I bought is interesting."')
dot.node('E3', '"The house, **which** is blue, is mine."')
dot.node('E4', '"I met the girl **whose** brother is a doctor."')
dot.edge('E', 'E1')
dot.edge('E', 'E2')
dot.edge('E', 'E3')
dot.edge('E', 'E4')

# Renderizar y mostrar con tamaño ajustado
dot.render('relative_clauses_symmetric_map', format='png', view=True)
