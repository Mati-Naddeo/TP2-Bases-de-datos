import sqlite3
import datetime
"""
datetime.datetime.now().replace(microsecond=0).isoformat()

devuelve fecha hora actual en formato ISO8601 simple

yyyymmddThh:mm:ss

"""
class Persona:
    def __init__(self, dni, apellido, nombre='', movil=''):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.movil= movil

def ingresa_visita(persona, destino):
    """Guarda los datos de una persona al ingresar"""
    conn = sqlite3.connect('recepcion.db')

    q = f"""SELECT dni FROM personas WHERE dni = '{persona.dni}'"""

    resu = conn.execute(q)
    if resu.fetchone():
        print("ya existe")
    else:
        q = f"""INSERT INTO personas (dni, nombre, apellido, movil)
                VALUES ('{persona.dni}',
                        '{persona.nombre}',
                        '{persona.apellido}',
                        '{persona.movil}');"""
        
        r = f"""INSERT INTO ingresos_egresos (id, dni, fechahora_in, fechahora_out, destino)
                VALUES ('{0}',
                        '{persona.dni}',
                        '{datetime.datetime.now().replace(microsecond=0).isoformat()}',
                        '{"undefined"}',
                        '{destino}');"""
        
        print(q)
        print(r)
        conn.execute(q)
        conn.execute(r)
        conn.commit()
    conn.close()

# from visitas import * 
# carlos = Persona(222, "Gonzales", "Carlos", 341342)
# ingresa_visita(carlos, "nueva delhi") 
# egresa_visita(222)


def egresa_visita (dni):
    """Coloca fecha y hora de egreso al visitante con dni dado"""
    conn = sqlite3.connect('recepcion.db')
    q = f"""SELECT dni FROM ingresos_egresos WHERE dni = '{dni}'"""
    resu = conn.execute(q)
    if resu.fetchone():
        q = f"""INSERT INTO ingresos_egresos (fechahora_out) WHERE dni = '{dni}'
                VALUES ('{datetime.datetime.now().replace(microsecond=0).isoformat()}');"""
        print(q)
        conn.execute(q)
        conn.commit()
        conn.close()
    else:
        print("No existe")


def lista_visitantes_en_institucion ():
    """Devuelve una lista de objetos Persona presentes en la institución"""
    
    conn = sqlite3.connect('recepcion.db')
    q = f"""SELECT * FROM personas;"""

    resu = conn.execute(q)
    
    for fila in resu:
        print(fila)
    conn.close()


def busca_vistantes(fecha_desde, fecha_hasta, destino, dni):
    """ busca visitantes segun criterios """
    pass


def iniciar():
    conn = sqlite3.connect('recepcion.db')

    qry = '''CREATE TABLE IF NOT EXISTS
                            personas
                    (dni TEXT NOT NULL PRIMARY KEY,
                     nombre   TEXT,
                     apellido TEXT  NOT NULL,
                     movil    TEXT  NOT NULL

           );'''

    conn.execute(qry)

    qry = '''CREATE TABLE IF NOT EXISTS
                            ingresos_egresos
                    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     dni TEXT NOT NULL,
                     fechahora_in TEXT  NOT NULL,
                     fechahora_out TEXT,
                     destino TEXT

           );'''

    conn.execute(qry)


if __name__ == '__main__':
    iniciar()

    """
    p = Persona('28123456', 'Álavarez', 'Ana', '02352-456789')

    ingresa_visita(p)
    """
    
    """
    doc = input("Igrese dni> ")
    apellido = input("Igrese apellido> ")
    nombre = input("nombre> ")
    movil = input("móvil > ")

    p = Persona(doc, apellido, nombre, movil)
    
    ingresa_visita(p)
    """
    
    # lista_visitantes_en_institucion()

