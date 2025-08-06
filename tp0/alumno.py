# La Escuela Nacional 32 "Alan Turing" de Bragado tiene una forma particular de requerir que los alumnos formen fila. En vez del clásico "de menor a mayor altura", lo hacen primero con alumnos yendo con altura decreciente, hasta llegado un punto que empieza a ir de forma creciente, hasta terminar con todos los alumnos.

# Por ejemplo las alturas podrían ser 1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23.

# Implementar una función indice_mas_bajo que dado un arreglo/lista de alumnos(*) que represente dicha fila, devuelva el índice del alumno más bajo, en tiempo logarítmico. Se puede asumir que hay al menos 3 alumnos. En el ejemplo, el alumno más bajo es aquel con altura 0.98.

# Implementar una función validar_mas_bajo que dado un arreglo/lista de alumnos(*) y un índice, valide (devuelva True o False) si dicho índice corresponde al del alumno más bajo de la fila. (Aclaración: esto debería poder realizarse en tiempo constante)

# (*)
# Los alumnos son de la forma:

# alumno {
#     nombre (string)
#     altura (float)
# }
# Se puede acceder a la altura de un alumno haciendo variable_tipo_alumno.altura.

# Importante: considerar que si la prueba de volumen no pasa, es probable que sea porque no están cumpliendo con la complejidad requerida.

def indice_mas_bajo(alumnos):
    return encontrar_mas_bajo(alumnos, 0, len(alumnos) - 1)

def encontrar_mas_bajo(alumnos, inicio, fin):
    if inicio == fin:
        return inicio
    
    medio = (inicio + fin) // 2

    if alumnos[medio].altura < alumnos[medio + 1].altura:
        return encontrar_mas_bajo(alumnos, inicio, medio)
    
    return encontrar_mas_bajo(alumnos, medio + 1, fin)
    
def validar_mas_bajo(alumnos, indice):
    if indice == 0:
        return alumnos[indice].altura < alumnos[indice + 1].altura
    
    if indice == len(alumnos) - 1:
        return alumnos[indice].altura < alumnos[indice - 1].altura
    
    return alumnos[indice].altura < alumnos[indice + 1].altura and alumnos[indice].altura < alumnos[indice - 1].altura




class Alumno:
    def __init__(self, nombre, altura):
        self.nombre = nombre
        self.altura = altura
    



if __name__ == "__main__":
    alumni = [Alumno("Juan", 1.2), Alumno("Pedro", 1.15), Alumno("Pablo", 1.14), Alumno("Jose", 1.12),
              Alumno("Maria", 1.02), Alumno("Ana", 0.98), Alumno("Lucas", 1.0), Alumno("b", 1.01),
              Alumno("Lucia", 1.18), Alumno("Marta", 1.23)]

    print(alumni[indice_mas_bajo(alumni)].altura)
    print(validar_mas_bajo(alumni, indice_mas_bajo(alumni)))

    assert validar_mas_bajo(alumni, indice_mas_bajo(alumni)) == True
    assert validar_mas_bajo(alumni, 0) == False
    assert validar_mas_bajo(alumni, len(alumni) - 1) == False
    assert validar_mas_bajo(alumni, 5) == True
    assert validar_mas_bajo(alumni, 6) == False
    assert validar_mas_bajo(alumni, 7) == False
    assert validar_mas_bajo(alumni, 8) == False