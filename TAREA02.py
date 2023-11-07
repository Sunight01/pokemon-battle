class habilidad: # Esta clase hace que el ataque seleccionado tenga sus propios atributos y que serán utilizados en la siguiente clase.

    ataque = ""
    poder  = 0
    tipo_ataque = ""
    categoría = ""

    def __init__(self, ataque, poder, tipo_ataque, categoría):

        self.ataque = ataque
        self.poder = poder
        self.tipo_ataque = tipo_ataque
        self.categoría = categoría

    def imprimir(self):
        print("\n\t| Estadisticas de la habilidad |\n")
        print(f"Ataque: {self.ataque}")
        print(f"Poder: {self.poder}")
        print(f"Tipo: {self.tipo_ataque}")
        print(f"Categoría: {self.categoría}\n")

class lucha: # En esta clase se juntarán toda la información obtenida de cada pokemon elegido y el ataque seleccionado para terminar con el programa.

    rivales = list()
    ability = list()
    #En esta función se agregarán los stats a nivel 50 de los pokémon.
    def agregar_stats(self, nombre_pokemon, tipo, hp, atk_fisico_base, def_fisico_base, atk_esp_base, def_esp_base, vel, movimientos):

        stats_pokemon = [atk_fisico_base, def_fisico_base, atk_esp_base, def_esp_base, vel]
        statslvl50 = []

        a = (eval(hp) + 31) * 2
        ev = (250**0.5)
        b = (ev / 4)
        c = ((a + b) * 50)
        d = c / 100
        e = d + 50 + 10
        hp_lvl50 = round(e, 2)
        statslvl50.append(nombre_pokemon)
        statslvl50.append(hp_lvl50)

        for estadistica in stats_pokemon:
            a = (eval(estadistica) + 31) * 2
            ev = (250**0.5)
            b = (ev / 4)
            c = ((a + b) * 50)
            d = c / 100
            e = d + 5
            f = round(e, 2)
            statslvl50.append(f)
        
        nombre_pokemon = statslvl50[0]
        hp = statslvl50[1]
        atk_fisico_base = statslvl50[2]
        def_fisico_base = statslvl50[3]
        atk_esp_base = statslvl50[4]
        def_esp_base = statslvl50[5]
        vel = statslvl50[6]
        movimientos = movimientos

        pokemon_stats = pokemon(nombre_pokemon, tipo, hp, atk_fisico_base, def_fisico_base, atk_esp_base, def_esp_base, vel, movimientos)
        self.rivales.append(pokemon_stats)

    def stats_habilidad(self, ataque, poder, tipo_ataque, categoría): # En esta funcioón se guardan los stats de la habilidad seleccionada
        habilidad_stats = habilidad(ataque, poder, tipo_ataque, categoría)
        self.ability.append(habilidad_stats)

    def batalla_pokemon(self):

        nombres_pokemon = []
        hp_pokemon =[]
        tipo_pokemon = []
        atk_pokemon = []
        atk_esp_pokemon = []
        def_pokemon = []
        def_esp_pokemon = []

        tipo_habilidad = []
        ataque_habilidad = []
        categoria_habilidad = []
        
        for stat in self.rivales:
            estadistica = stat.nombre_pokemon
            nombres_pokemon.append(estadistica)

        for stat in self.rivales:
            estadistica = stat.hp
            hp_pokemon.append(estadistica)

        for stat in self.rivales:
            estadistica = stat.atk_fisico_base
            atk_pokemon.append(estadistica)

        for stat in self.rivales:
            estadistica = stat.atk_esp_base
            atk_esp_pokemon.append(estadistica)

        for stat in self.rivales:
            estadistica = stat.def_fisico_base
            def_pokemon.append(estadistica)

        for stat in self.rivales:
            estadistica = stat.def_esp_base
            def_esp_pokemon.append(estadistica)

        for stat in self.rivales:
            estadistica = stat.tipo
            tipo_pokemon.append(estadistica)

        for estad in self.ability:
            estadistica_habilidad_01 = estad.tipo_ataque
            tipo_habilidad.append(estadistica_habilidad_01)
        
        for estad in self.ability:
            estadistica_habilidad = estad.poder
            ataque_habilidad.append(estadistica_habilidad)
        
        for estad in self.ability:
            estadistica_habilidad = estad.categoría
            categoria_habilidad.append(estadistica_habilidad)

        print(f"\nNombre del segundo pokémon seleccionado: {nombres_pokemon[1].upper()}\n")

        if tipo_habilidad[0] == tipo_pokemon[0]:
            from csv import reader
            import random
            stab = 1.2

            with open('tabla_efectividad.csv', 'r') as csv_file:
                csv_reader = reader(csv_file)
                list_of_row= list(csv_reader)

            lista_de_tipos = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
            largo = len(lista_de_tipos)

            for i in range(0, largo):
                if tipo_pokemon[0] == lista_de_tipos[i]:
                    tipo_atacante = i + 1

            for x in range(0, largo):
                if tipo_pokemon[1] == lista_de_tipos[x]:
                    tipo_victima = x + 1          
                
            efectividad = list_of_row[tipo_atacante][tipo_victima]
            efectividad = eval(efectividad)

            print("\t| Simulación de batalla |\n")

            if categoria_habilidad[0] == "special":

                atk_esp_pokemon01 = atk_esp_pokemon[0]
                def_esp_pokemon02 = def_esp_pokemon[1]
                numero = random.uniform(0.85, 1)
                
                modifier = efectividad*stab*numero*1

                a = (2*50)
                b = (a / 5)
                c = (b + 2)
                d = (c * ataque_habilidad[0])
                e = (d * (atk_esp_pokemon01/def_esp_pokemon02))
                f = (e/50)
                g = (f+2)
                damage = (g * modifier)
                damage = round(damage, 2)

                print(f"- El HP de {nombres_pokemon[1].upper()} a nivel 50 es: {hp_pokemon[1]}")
                print(f"- El daño que realizó {nombres_pokemon[0].upper()} a {nombres_pokemon[1].upper()} es: {damage}")
                
                if efectividad == 2.0:
                    print("- ¡Es muy efectivo!")
                
                elif efectividad == 0.5:
                    print("- No es muy efectivo...")

                vida_restante = hp_pokemon[1] - damage
                vida_restante = round(vida_restante, 2)
            
                print(f"- {nombres_pokemon[1].upper()} quedó con un HP de: {vida_restante}\n")

                if vida_restante <= 0:
                    monedas = random.randint(1000,2500)
                    print(f"- ¡{nombres_pokemon[1].upper()} se ha debilitado!")
                    print("- ¡Has ganado la batalla!")
                    print(f"- Has ganado {monedas} PK\n")
                
                print("\t◖ Fin de la Simulación ◗\n")

            else:
                atk_pokemon01 = atk_pokemon[0]
                def_pokemon01 = def_pokemon[1]

                numero = random.uniform(0.85, 1)
                modifier = efectividad*stab*numero*1

                a = (2*50)
                b = (a / 5)
                c = (b + 2)
                d = (c * ataque_habilidad[0])
                e = (d * (atk_pokemon01/def_pokemon01))
                f = (e/50)
                g = (f+2)
                damage = (g * modifier)
                damage = round(damage, 2)

                print(f"- El HP de {nombres_pokemon[1].upper()} a nivel 50 es: {hp_pokemon[1]}")
                print(f"- El daño que realizó {nombres_pokemon[0].upper()} a {nombres_pokemon[1].upper()} es: {damage}")
                
                if efectividad == 2.0:
                    print("- ¡Es muy efectivo!")
                
                elif efectividad == 0.5:
                    print("- No es muy efectivo...")

                vida_restante = hp_pokemon[1] - damage
                vida_restante = round(vida_restante, 2)
            
                print(f"- {nombres_pokemon[1].upper()} quedó con un HP de: {vida_restante}\n")

                if vida_restante <= 0:
                    monedas = random.randint(1000,2500)
                    print(f"- ¡{nombres_pokemon[1].upper()} se ha debilitado!")
                    print("- ¡Has ganado la batalla!")
                    print(f"- Has ganado {monedas} PK\n")
                
                print("\t◖ Fin de la Simulación ◗\n")

        else:
            from csv import reader
            import random
            stab = 1

            with open('tabla_efectividad.csv', 'r') as csv_file:
                csv_reader = reader(csv_file)
                list_of_row= list(csv_reader)

            lista_tipos = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
            largo = len(lista_tipos)

            for o in range(0, largo):
                if tipo_pokemon[0] == lista_tipos[o]:
                    tipo_atacante = o + 1
            
            for y in range(0, largo):
                if tipo_pokemon[1] == lista_tipos[y]:
                    tipo_victima = y + 1                       
                
            efectividad = list_of_row[tipo_atacante][tipo_victima]
            efectividad = eval(efectividad)

            print("\t| Simulación de batalla |\n")

            if categoria_habilidad[0] == "special":

                atk_esp_pokemon01 = atk_esp_pokemon[0]
                def_esp_pokemon02 = def_esp_pokemon[1]
                numero = random.uniform(0.85, 1)
                
                modifier = efectividad*stab*numero*1

                a = (2*50)
                b = (a / 5)
                c = (b + 2)
                d = (c * ataque_habilidad[0])
                e = (d * (atk_esp_pokemon01/def_esp_pokemon02))
                f = (e/50)
                g = (f+2)
                damage = (g * modifier)
                damage = round(damage, 2)

                print(f"- El HP de {nombres_pokemon[1].upper()} a nivel 50 es: {hp_pokemon[1]}")
                print(f"- El daño que realizó {nombres_pokemon[0].upper()} a {nombres_pokemon[1].upper()} es: {damage}")
                
                if efectividad == 2.0:
                    print("- ¡Es muy efectivo!")
                
                elif efectividad == 0.5:
                    print("- No es muy efectivo...")

                vida_restante = hp_pokemon[1] - damage
                vida_restante = round(vida_restante, 2)
            
                print(f"- {nombres_pokemon[1].upper()} quedó con un HP de: {vida_restante}\n")

                if vida_restante <= 0:
                    monedas = random.randint(1000,2500)
                    print(f"- ¡{nombres_pokemon[1].upper()} se ha debilitado!")
                    print("- ¡Has ganado la batalla!")
                    print(f"- Has ganado {monedas} PK\n")
                
                print("\t◖ Fin de la Simulación ◗\n")

            else:
                atk_pokemon01 = atk_pokemon[0]
                def_pokemon01 = def_pokemon[1]

                numero = random.uniform(0.85, 1)
                modifier = efectividad*stab*numero*1

                a = (2*50)
                b = (a / 5)
                c = (b + 2)
                d = (c * ataque_habilidad[0])
                e = (d * (atk_pokemon01/def_pokemon01))
                f = (e/50)
                g = (f+2)
                damage = (g * modifier)
                damage = round(damage, 2)

                print(f"- El HP de {nombres_pokemon[1].upper()} a nivel 50 es: {hp_pokemon[1]}")
                print(f"- El daño que realizó {nombres_pokemon[0].upper()} a {nombres_pokemon[1].upper()} es: {damage}")
                
                if efectividad == 2.0:
                    print("- ¡Es muy efectivo!")
                
                elif efectividad == 0.5:
                    print("- No es muy efectivo...")

                vida_restante = hp_pokemon[1] - damage
                vida_restante = round(vida_restante, 2)
            
                print(f"- {nombres_pokemon[1].upper()} quedó con un HP de: {vida_restante}\n")

                if vida_restante <= 0:
                    monedas = random.randint(1000,2500)
                    print(f"- ¡{nombres_pokemon[1].upper()} se ha debilitado!")
                    print("- ¡Has ganado la batalla!")
                    print(f"- Has ganado {monedas} PK\n")
                
                print("\t◖ Fin de la Simulación ◗\n")

class pokemon: # En esta clase se guardarán los "atributos" de los dos objetos que se encuentran en el programa, es decir los stats de los pokémon.

    tipo = ""
    hp = ""
    atk_fisico_base = ""
    def_fisico_base = ""
    atk_esp_base = ""
    def_esp_base = ""
    vel = ""
    movimientos = []

    def __init__ (self, nombre_pokemon, tipo, hp, atk_fisico_base, def_fisico_base, atk_esp_base, def_esp_base, vel, movimientos):
        self.nombre_pokemon = nombre_pokemon
        self.tipo = tipo
        self.hp = hp
        self.atk_fisico_base = atk_fisico_base
        self.def_fisico_base = def_fisico_base
        self.atk_esp_base = atk_esp_base
        self.def_esp_base = def_esp_base
        self.vel = vel
        self.movimientos = movimientos

    def mostrar_stats(self):
        print(f"\nPokémon seleccionado: {self.nombre_pokemon.upper()}\n")
        print("\t| Estadisticas base del Pokémon |\n")
        print(f"Tipo: {self.tipo}")
        print(f"Vida: {self.hp}")
        print(f"Ataque: {self.atk_fisico_base}")
        print(f"Defensa: {self.def_fisico_base}")
        print(f"Ataque especial: {self.atk_esp_base}")
        print(f"Defensa especial: { self.def_esp_base}")
        print(f"Velocidad: {self.vel}\n")
        print("Movimientos que puede aprender el Pokémon: \n")
        largo = len(self.movimientos)
        for i in range(0, largo):
            print(f"{i} - {self.movimientos[i]}")
        
        return self.tipo
    
    def stats_lvl50(self): 
        stats_pokemon = [self.atk_fisico_base, self.def_fisico_base, self.atk_esp_base, self.def_esp_base, self.vel]
        statslvl50 = []

        print("\t| Estadisticas a nivel 50 |\n")
        a = (eval(self.hp) + 31) * 2
        ev = (250**0.5)
        b = (ev / 4)
        c = ((a + b) * 50)
        d = c / 100
        e = d + 50 + 10
        hp_lvl50 = round(e, 2)
        statslvl50.append(self.nombre_pokemon)
        statslvl50.append(hp_lvl50)
        print(f"Nombre: {self.nombre_pokemon}")
        print(f"Vida a nivel 50: {hp_lvl50}")

        for estadistica in stats_pokemon:
            a = (eval(estadistica) + 31) * 2
            ev = (250**0.5)
            b = (ev / 4)
            c = ((a + b) * 50)
            d = c / 100
            e = d + 5
            f = round(e, 2)
            statslvl50.append(f)
        
        print(f"Ataque a nivel 50: {statslvl50[2]}")
        print(f"Defensa a nivel 50: {statslvl50[3]}")
        print(f"Ataque especial a nivel 50: {statslvl50[4]}")
        print(f"Defensa especial a nivel 50: {statslvl50[5]}")
        print(f"Velocidad a nivel 50: {statslvl50[6]}")

def estadisticas_pokemon(nombre_usuario): # En esta función nos permite obtener las estadisticas de los pokémon.
    from csv import reader
    archivo = open('pokemon_data.csv', 'r')
    lector = reader(archivo)
    lista = list(lector)

    for i in range(0, len(lista)):
        nombre = lista[i][0]

        if nombre_usuario.lower() == nombre:
            nombre_pokemon = lista[i][0]
            tipo = lista[i][1]
            hp = lista[i][2]
            atk_fisico_base = lista[i][3]
            def_fisico_base = lista[i][4]
            atk_esp_base = lista[i][5]
            def_esp_base = lista[i][6]
            vel = lista[i][7]
            
            ataques = [lista[i][8]]
            a = len(ataques[0])
            lista_ataques = []
            nombre_atk = []
            nombre = ""

            for i in range(0, a):
                atk = ataques[0][i]
                if (atk != ";"):
                    nombre = nombre + atk
                    nombre_atk.append(nombre)
                else:
                    lista_ataques.append(nombre)
                    nombre = ""
                if a == (i+1):
                    lista_ataques.append(nombre)
                    nombre = ""
    archivo.close()
    return nombre_pokemon, tipo, hp, atk_fisico_base, def_fisico_base, atk_esp_base, def_esp_base, vel, lista_ataques

def stats_movimiento(seleccion_ataque): # Esta funcion guarda las estadisticas de la habilidad elegida por el usuario.
    from moves import get_move

    ataque_usuario = lista_ataques[seleccion_ataque]

    lista_ataque = get_move(ataque_usuario)

    ataque = lista_ataque[0]
    poder  =lista_ataque[1]
    tipo_ataque = lista_ataque[2]
    categoría = lista_ataque[3]

    return ataque, poder, tipo_ataque, categoría

#programa

print("Bienvenido a esta simulación. Este programa es un simulador del daño de un pokémon a otro previamente seleccionados ambos junto con un ataque que tú seleccionarás. ¡Comencemos!\n")

nombre_usuario = input("Ingrese nombre del primer Pokémon: ")

# En las siguientes lineas se realizará la tarea de encontrar, guardar y mostrar los stats del pokémon elegido.
nombre_pokemon, tipo, hp, atk_fisico_base, def_fisico_base, atk_esp_base, def_esp_base, vel, lista_ataques = estadisticas_pokemon(nombre_usuario)
pokemon01 = pokemon(nombre_pokemon, tipo, hp, atk_fisico_base, def_fisico_base, atk_esp_base, def_esp_base, vel, lista_ataques)
pokemon01.mostrar_stats()

seleccion_ataque = eval(input("\nSeleccione un ataque a ejecutar digitando el número: "))

# En las siguientes lineas se realizará la tarea de encontrar, guardar y mostrar los stats de la habilidad elegida.
ataque, poder, tipo_ataque, categoría = stats_movimiento(seleccion_ataque) # Encontrar
movimiento = habilidad(ataque, poder, tipo_ataque, categoría) # Guardado para que sea un objeto con atritos propios
movimiento.imprimir() # Mostrar
movimiento = lucha()
movimiento.stats_habilidad(ataque, poder, tipo_ataque, categoría) #Guardado para usar los atributos del objeto.

pokemon01.stats_lvl50() # Esta linea muestra los stats del Pokémon elegido a nivel 50, siguiendo las formulas entregadas.

# En las siguientes lineas se guardarán los stats del 1er pokemon en la clase donde "luchará" con el otro pokémon elegido posteriormente.
pokemon1 = lucha()
pokemon1.agregar_stats(nombre_pokemon, tipo, hp, atk_fisico_base, def_fisico_base, atk_esp_base, def_esp_base, vel, lista_ataques)

nombre_usuario = input("\nIngrese nombre del segundo Pokémon: ")

# En las siguientes lineas se realizará la tarea de encontrar, guardar y mostrar los stats del segundo pokémon elegido.
nombre_pokemon, tipo, hp, atk_fisico_base, def_fisico_base, atk_esp_base, def_esp_base, vel, lista_ataques = estadisticas_pokemon(nombre_usuario)
pokemon02 = pokemon(nombre_pokemon, tipo, hp, atk_fisico_base, def_fisico_base, atk_esp_base, def_esp_base, vel, lista_ataques)

# En las siguientes lineas se guardarán los stats del 1er pokemon en la clase donde "luchará" con el 1er pokémon
pokemon02 = lucha()
pokemon02.agregar_stats(nombre_pokemon, tipo, hp, atk_fisico_base, def_fisico_base, atk_esp_base, def_esp_base, vel, lista_ataques)

pokemon02.batalla_pokemon() # En esta linea se ejecuta la funcion establecida dentro de la clase "Lucha" mostrando el daño causado y la vida 
# restante del pokémon atacante al atacado y finaliza el programa.

input("Presione ENTER para finalizar programa...")