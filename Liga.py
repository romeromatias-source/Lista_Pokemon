from pokemon import lista_pokemon

def separador():
    print("-" * 50)

# Datos de cada pokémon
def mostrar_pokemon(p):
    print(f"""    Nombre        : {p[0]}
    Tipo          : {p[1]}
    Altura        : {p[2]} m
    Peso          : {p[3]} kg
    Nivel         : {p[4]}
    Fuerza Ataque : {p[5]}
    Región        : {p[6]}
    """)

#  OPCIÓN 1 – Listar todos los pokémon
def listar_pokemon(lista):
    if len(lista) == 0:
        print("  La Pokédex está vacía.")
        return

    print(f"\n   Pokédex  —  {len(lista)} Pokémon registrados \n")
    for i in range(len(lista)):
        print(f"  ── #{i + 1} ──────────────────────────────")
        mostrar_pokemon(lista[i])
    separador()

#  OPCIÓN 2 – Agregar pokémon
def pedir_nombre(lista):
    while True:
        nombre = input("  Nombre: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue
        encontrado = False
        for p in lista:
            if p[0].lower() == nombre.lower():
                encontrado = True
                break
        if encontrado:
            print(f"Ya existe un Pokémon llamado '{nombre}'.")
        else:
            return nombre


def pedir_tipo():
    while True:
        tipo = input("  Tipo: ").strip()
        if tipo == "":
            print("El tipo no puede estar vacío.")
        else:
            return tipo


def pedir_decimal(mensaje):
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = float(entrada)
            if valor <= 0:
                print("Debe ser mayor a 0.")
            else:
                return valor
        except ValueError:
            print("Ingresá un número válido.")


def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor <= 0:
                print("Debe ser mayor a 0.")
            else:
                return valor
        except ValueError:
            print("Ingresá un número entero válido.")


def pedir_region():
    regiones_validas = ["Kanto", "Johto", "Hoenn", "Sinnoh"]
    print("  Regiones disponibles: Kanto, Johto, Hoenn, Sinnoh") 
    while True:
        region = input("  Región: ").strip().capitalize()
        match region:
            case "Kanto" | "Johto" | "Hoenn" | "Sinnoh":
                return region
            case _:
                print(f"  Región inválida. Elegí entre: {', '.join(regiones_validas)}")


def agregar_pokemon(lista):
    print("\n  ── Nuevo Pokémon ──────────────────────────────")
    nombre        = pedir_nombre(lista)
    tipo          = pedir_tipo()
    altura        = pedir_decimal("  Altura (m): ")
    peso          = pedir_decimal("  Peso (kg): ")
    nivel         = pedir_entero("  Nivel: ")
    fuerza_ataque = pedir_entero("  Fuerza ataque: ")
    region        = pedir_region()

    nuevo = [nombre, tipo, altura, peso, nivel, fuerza_ataque, region]
    lista.append(nuevo)
    print(f"\n{nombre} fue añadido a la Pokédex")
    separador()

#  OPCIÓN 3 – Eliminar pokémon por nombre
def eliminar_pokemon(lista):
    if len(lista) == 0:
        print("La Pokédex está vacía.")
        return

    nombre = input("\nNombre del Pokémon a eliminar: ").strip()
    if nombre == "":
        print("No ingresaste ningún nombre.")
        return

    a_eliminar = None
    for p in lista:
        if p[0].lower() == nombre.lower():
            a_eliminar = p
            break

    if a_eliminar is None:
        print(f"No se encontró '{nombre}' en la Pokédex.")
    else:
        lista.remove(a_eliminar)
        print(f"{a_eliminar[0]} fue eliminado de la Pokédex.")
    separador()

#  OPCIÓN 4 – Ordenar por nombre Z > A 
def ordenar_z_a(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if lista[j][0].lower() < lista[j + 1][0].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print("\nLista ordenada de Z a A por nombre.")
    listar_pokemon(lista)

#  OPCIÓN 5 – Pokémon más pesado de tipo Agua
def pokemon_mas_pesado_agua(lista):
    mas_pesado = None
    for p in lista:
        if p[1].lower() == "agua":
            if mas_pesado is None or p[3] > mas_pesado[3]:
                mas_pesado = p

    print()
    if mas_pesado is None:
        print("No hay pokémon de tipo Agua en la Pokédex.")
    else:
        print("Pokémon más pesado de tipo Agua\n")
        mostrar_pokemon(mas_pesado)
    separador()

#  OPCIÓN 6 – Pokémon con mayor fuerza de ataque
def pokemon_mayor_ataque(lista):
    if len(lista) == 0:
        print("La Pokédex está vacía.")
        return

    mas_fuerte = lista[0]
    for i in range(1, len(lista)):
        if lista[i][5] > mas_fuerte[5]:
            mas_fuerte = lista[i]

    print("\nPokémon con mayor fuerza de ataque\n")
    mostrar_pokemon(mas_fuerte)
    separador()

#  OPCIÓN 7 – Listar pokémon de una región
def listar_por_region(lista):
    region = input("\nIngresá la región (Kanto / Johto / Hoenn / Sinnoh): ").strip()
    if region == "":
        print("No ingresaste ninguna región.")
        return

    encontrados = []
    for p in lista:
        if p[6].lower() == region.lower():
            encontrados.append(p)

    print()
    if len(encontrados) == 0:
        print(f"No se encontraron Pokémon de la región '{region}'.")
    else:
        print(f"Pokémon de la región {region.capitalize()} "
              f"({len(encontrados)} encontrados)\n")
        for i in range(len(encontrados)):
            print(f"  ── #{i + 1} ──────────────────────────────")
            mostrar_pokemon(encontrados[i])
    separador()

#  MENÚ PRINCIPAL
def mostrar_menu():
    print("\n" + "=" * 50)
    print("""  "LABORATORIO POKÉMON DEL PROFESOR SAMUEL OAK"
           Sistema Pokédex v1.0
    
    1. Listar todos los Pokémon
    2. Agregar un Pokémon
    3. Eliminar un Pokémon por nombre
    4. Ordenar lista de Z a A por nombre
    5. Ver el Pokémon de tipo Agua más pesado
    6. Ver el Pokémon con mayor fuerza de ataque
    7. Listar Pokémon por región
    8. Salir
    """)
    print("=" * 50)


def main():
    print("""\n    Bienvenido al Laboratorio del Profesor Oak.
    Los datos de la Pokédex fueron importados correctamente.
    """)

    opcion = ""
    while opcion != "8":
        mostrar_menu()
        opcion = input("  Seleccioná una opción (1-8): ").strip()

        match opcion:
            case "1":
                listar_pokemon(lista_pokemon)
            case "2":
                agregar_pokemon(lista_pokemon)
            case "3":
                eliminar_pokemon(lista_pokemon)
            case "4":
                ordenar_z_a(lista_pokemon)
            case "5":
                pokemon_mas_pesado_agua(lista_pokemon)
            case "6":
                pokemon_mayor_ataque(lista_pokemon)
            case "7":
                listar_por_region(lista_pokemon)
            case "8":
                print("\nHasta la próxima, Entrenador")
            case _:
                print("Opción inválida. Ingresá un número del 1 al 8.")
main()