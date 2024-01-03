with open("familia.csv", 'r') as archivo:
    archivo_familia = [i.split(",") for i in archivo.read().split("\n")]

diccionario = {"nodos": [], "enlaces": []}


def encontrar_persona(lista_personas, id_persona):
    for p in lista_personas:
        if p.id == id_persona:
            return p
    return None


class Persona:
    def __init__(self, lista):
        print(lista)
        self.id = int(lista[0])
        self.id_padre = int(lista[1])
        self.id_madre = int(lista[2])
        self.padres = [self.id_padre, self.id_madre]
        self.nombre = lista[3]
        self.nacimiento = lista[4]
        self.defuncion = lista[5]
        self.genero = lista[6]
        self.conexiones = []
        self.nivel = int(lista[-1])


class Relacion:
    def __init__(self, personas, id, opacidad=1):
        self.id = id
        self.personas = personas
        self.ides = [self.personas[0].id, self.personas[1].id]
        self.nivel = self.personas[0].nivel
        self.opacidad = opacidad

    def nombre(self):
        return f"Relación entre {self.personas[0].nombre} y {self.personas[1].nombre}"


personas = []

for persona in archivo_familia[1:-1]:
    personas.append(Persona(persona))

# Solo casados o que tuvieron hijos entre ellos
relaciones = [[90, 91], [139, 140], [68, 69]]

# Agrego todas las relaciones que encuentre
for persona in personas:
    relacion = persona.padres
    relacion2 = [relacion[1], relacion[0]]
    if (relacion not in relaciones) and (relacion2 not in relaciones) and (relacion[0] != 0 and relacion[1] != 0):
        relaciones.append(relacion)

relaciones.sort()

nodos_relaciones = []

# Aquí van conectadas las personas a las relaciones
union_relaciones = []
# Aquí van conectadas las personas a las personas que están o estuvieron en una relación
union_personas = []

# Creo los nodos para las relaciones (id tipo "rx" donde x es un número)
i = 1
for r in relaciones:
    personas_relacion = [encontrar_persona(
        personas, r[0]), encontrar_persona(personas, r[1])]
    relacion = Relacion(personas_relacion, "r"+str(i))
    union_relaciones.append([personas_relacion[0].id, relacion.id])
    union_relaciones.append([personas_relacion[1].id, relacion.id])
    union_personas.append(
        [personas_relacion[0].id, personas_relacion[1].id, 0])
    nodos_relaciones.append(relacion)
    i += 1

# Hijo con dos padres
union_padres_hijos = []

for n in nodos_relaciones:
    for p in personas:
        if n.ides == p.padres:
            union_padres_hijos.append([p.id, n.id])

union_padre_hijo = []
# Hijos con un solo padre
for p in personas:
    if ((p.id_madre == 0) or (p.id_padre == 0)) and (p.padres != [0, 0]):
        id_padre = p.id_madre + p.id_padre
        if p.padres not in union_padre_hijo:
            union_padre_hijo.append([p.id, id_padre])


# Todos los enlaces = unidas las parejas + unidas los hijos a las relaciones parentales + union solo un padre/madre
uniones = union_relaciones + union_padres_hijos + \
    union_padre_hijo + union_personas


print(uniones)

for u in uniones:
    if len(u) == 3:
        opacidad = 0
    else:
        opacidad = 1
    diccionario["enlaces"].append(
        {"source": u[0], "target": u[1], "op": opacidad})

for p in personas:
    if p.genero == "M":
        color = "blue"
    else:
        color = "pink"
    diccionario["nodos"].append({"id": p.id,
                                 "name": p.nombre,
                                 "birth": p.nacimiento,
                                 "death": p.defuncion,
                                 "genre": p.genero,
                                 "color": color,
                                 "nivel": p.nivel
                                 })
for n in nodos_relaciones:
    diccionario["nodos"].append({"id": n.id,
                                 "name": n.nombre(),
                                 "birth": 0,
                                 "death": 0,
                                 "genre": 0,
                                 "color": "white",
                                 "nivel": n.nivel - 0.1,
                                "p1": n.ides[0],
                                 "p2": n.ides[1]
                                 })


with open("datos.json", "w") as a:
    a.write(str(diccionario))
