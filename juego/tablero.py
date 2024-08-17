from juego.piezas import *
from juego.BD import *

class Tablero:
    def __init__(self):
        self.__tablero__, self.__BD_piezas__, self.__BD_espacios__ = self.crear_tablero_inicial()

    def crear_tablero_inicial(self):
        # Creo las piezas y los espacios:
        # Quite los atributos 'num' y 'color_casilla' de las piezas.

        #Piezas blancas.
        info_piezas = [
        ("P1" , "blanca", (1,7), u"\u2659", "Peon"), # ♙
        ("P2" , "blanca", (2,7), u"\u2659", "Peon"), # ♙
        ("P3" , "blanca", (3,7), u"\u2659", "Peon"), # ♙
        ("P4" , "blanca", (4,7), u"\u2659", "Peon"), # ♙
        ("P5" , "blanca", (5,7), u"\u2659", "Peon"), # ♙
        ("P6" , "blanca", (6,7), u"\u2659", "Peon"), # ♙
        ("P7" , "blanca", (7,7), u"\u2659", "Peon"), # ♙
        ("P8" , "blanca", (8,7), u"\u2659", "Peon"), # ♙
        ("C1" , "blanca", (2,8), u"\u2658", "Caballo"), # ♘
        ("C2" , "blanca", (7,8), u"\u2658", "Caballo"), # ♘
        ("A1" , "blanca", (3,8), u"\u2657", "Alfil"), # ♗
        ("A2" , "blanca", (6,8), u"\u2657", "Alfil"), # ♗
        ("T1" , "blanca", (1,8), u"\u2656", "Torre"), # ♖
        ("T2" , "blanca", (8,8), u"\u2656", "Torre"), # ♖
        ("D1" , "blanca", (4,8), u"\u2655", "Dama"), # ♕
        ("R1" , "blanca", (5,8), u"\u2654", "Rey"), # ♔
        
        # Piezas negras.
        ("p1" , "negra", (1,2), u"\u265F", "Peon"), # ♟
        ("p2" , "negra", (2,2), u"\u265F", "Peon"), # ♟
        ("p3" , "negra", (3,2), u"\u265F", "Peon"), # ♟                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        ("p4" , "negra", (4,2), u"\u265F", "Peon"), # ♟
        ("p5" , "negra", (5,2), u"\u265F", "Peon"), # ♟
        ("p6" , "negra", (6,2), u"\u265F", "Peon"), # ♟
        ("p7" , "negra", (7,2), u"\u265F", "Peon"), # ♟
        ("p8" , "negra", (8,2), u"\u265F", "Peon"), # ♟
        ("c1" , "negra", (2,1), u"\u265E", "Caballo"), # ♞
        ("c2" , "negra", (7,1), u"\u265E", "Caballo"), # ♞                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        ("a1" , "negra", (3,1), u"\u265D", "Alfil"), # ♝
        ("a2" , "negra", (6,1), u"\u265D", "Alfil"), # ♝                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        ("t1" , "negra", (1,1), u"\u265C", "Torre"), # ♜
        ("t2" , "negra", (8,1), u"\u265C", "Torre"), # ♜
        ("d1" , "negra", (4,1), u"\u265B", "Dama"), # ♛
        ("r1" , "negra", (5,1), u"\u265A", "Rey") # ♚
        ]
        
        # Espacios.
        info_espacios = [
        ("B" , "blanca", u"\u25A1"), # Espacio blanco □
        ("N" , "negra", u"\u25A0") # Espacio negro ■
        ]
        
        # Creo las BDs.
        BD_piezas = BD()
        BD_espacios = BD()
        
        # Añado las piezas a la BD.
        # Quite los atributos 'num' y 'color_casilla' de las piezas.
        for var, color, posicion, s, nom in info_piezas:
            
            # Uso globals() para obtener la clase a partir del nombre (string) de la pieza.
            clase_pieza = globals().get(nom)
            
            if clase_pieza:
                pieza = clase_pieza(var, color, posicion, s, nom)
                BD_piezas.add(pieza)

            # Para depurar:
            # else:
            #     print(f"No se encontró la clase: {nom}")
        
        # Añado los espacios a la BD.
        for var, color, s in info_espacios:
            espacio = Espacio(var, color, s)
            BD_espacios.add(espacio)
        
        # Creo el tablero vacío.
        tablero = [[" " for _ in range(10)] for _ in range(10)]
        
        # Coloco las coordenadas del tablero.
        letras = [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "]
        for i in range(10):
            # Las letras:
            tablero[0][i] = tablero[9][i] = letras[i]
            # Las números:
            tablero[i][0] = tablero[i][9] = str(9 - i) if i > 0 and i < 9 else " "
        
        # Coloco las piezas en el tablero según su posición.
        for pieza in BD_piezas.__base_datos__.values():
            x, y = pieza.__posicion__
            # Importante: x e y van invertidos porque el tablero es una lista de listas.
            tablero[y][x] = pieza
        
        # Coloco los espacios en las casillas vacías.
        for y in range(3, 7):
            for x in range(1, 9):
                # Acá lo mismo, ¡x e y invertidos!
                tablero[y][x] = BD_espacios.search('B' if (x + y) % 2 == 0 else 'N')
        
        # Devuelvo el tablero y las BDs para la interfaz.
        return tablero, BD_piezas, BD_espacios
    
    def __str__(self):
        string_tablero = "\n"
        for fila in self.__tablero__:
            for casilla in fila:
                # Si es una pieza o una casilla, muestro el símbolo.
                if isinstance(casilla, Pieza):
                    string_tablero += (str(casilla.__s__) + (" "))
                elif isinstance(casilla, Espacio):
                    string_tablero += (str(casilla.__s__) + (" "))
                else:
                    string_tablero += (str(casilla) + (" "))
            string_tablero += ("\n")
        return string_tablero

    def obtener_piezas_movibles(self, color):
        # Devuelvo una lista de nombres de piezas que pueden moverse para el color dado.
        # Luego una lista de las instancias de esas piezas.
        # Y después pido la posición a la que se quiere avanzar.

        
        lista_piezas = [] # Lista para los nombres las piezas que voy a mostrar.
        lista_instancias = [] # Lista para las instancias de las piezas que voy a mostrar.
        lista_posibilidades = [] # Lista para las posibilidades de cada una de las piezas.
        
        # Para depurar:
        # print(BD_piezas.__base_datos__)
        
        # Para las 16 piezas del jugador:
        for i in range(1, 17):
            
            if i <= 8:
            ## Para los peones.
                cant = i
                if color == "blanca":
                    letra = "P"
                else:
                    letra = "p"
            
            elif i <= 10:
            ## Para los caballos.
                cant = i - 8
                if color == "blanca":
                    letra = "C"
                else:
                    letra = "c"
            
            elif i <= 12:
            ## Para los alfiles.
                cant = i - 10
                if color == "blanca":
                    letra = "A"
                else:
                    letra = "a"

            elif i <= 14:
            ## Para las torres.
                cant = i - 12
                if color == "blanca":
                    letra = "T"
                else:
                    letra = "t"
            
            elif i == 15:
            ## Para la dama.
                cant = i - 14
                if color == "blanca":
                    letra = "D"
                else:
                    letra = "d"
            
            elif i == 16:
            ## Para el rey.
                cant = i - 15
                if color == "blanca":
                    letra = "R"
                else:
                    letra = "r"
            
            # Reviso que piezas puedo mostrar en base a cuales son movibles y sus posibilidades.
            resultado, movible, posibilidades = self.instancias_piezas(self.__BD_piezas__, letra, cant)
            
            # Para depurar:
            # print(resultado, " : ", movible)

            if movible == False:
                continue # Volver a preguntar por el resto de piezas.
            
            # Si se puede mover, añado a la lista de piezas, instancias y posibilidades.
            # Que solo se pueda añadir una vez en cada una.
            if resultado.__nom__ not in lista_piezas:
                lista_piezas.append(resultado.__nom__)

            if resultado not in lista_instancias:
                lista_instancias.append(resultado)
                lista_posibilidades.append(posibilidades)
            
        # Acá hice la división de la función de obtener_piezas_moviles. La otra parte la mando
        # a interfaz.py ya que tiene más sentido que el texto se ejecute en la parte de la
        # interfaz.

        return self, lista_piezas, lista_instancias, lista_posibilidades


    def instancias_piezas(self, BD_piezas, letra, i):
        
        # Uso el método 'search' para repasar la BD de piezas, donde están las instancias, 
        # entregando el valor var (usando la letra más el numero de pieza).
        pieza = BD_piezas.search(letra + str(i))
        # Reviso si se puede mover.
        movible, posibilidades = self.movible(pieza)  
        
        # Devuelvo la instancia de la pieza, si es movible (bool) y las posibilidades.
        return pieza, movible, posibilidades
        

    def movible(self, pieza):
        # Verifico si la pieza vive.
        if not pieza.__vive__:
            return False, []

        # Creo las listas de posibles movimientos, diferentes checkers para pasar cada requisito.
        posibilidades_checked = []
        posibilidades_double_checked = []

        # Obtengo la lista de posibles movimientos.
        posibilidades = pieza.movimientos_posibles()

        # Itero sobre todas las posiciones posibles.
        for posicion in posibilidades:
            x, y = posicion

            # Verifico si la posición está dentro del rango del tablero 
            # (sin contar las coordenadas).
            # No debería ser necesario, porque ya está comprobado en
            # movimientos_posibles(), pero por si acaso.
            if not (1 <= x <= 8 and 1 <= y <= 8):
                continue
            
            # Guardo la posición destino en casilla.
            casilla = self.__tablero__[y][x]
            
            # Para depurar:
            # print("casilla es : ", casilla)
            # print("pieza es : ", pieza)

            # Para todas las piezas que no sean peones:
            if not isinstance(pieza, Peon):
                
                # Verifico si es una instancia de Espacio o una pieza enemiga:
                if isinstance(casilla, Espacio):
                    posibilidades_checked.append(posicion)

                elif isinstance(casilla, Pieza):
                    if casilla.__color__ != pieza.__color__:
                        posibilidades_checked.append(posicion)
            else:
                # Para los peones:
                # Movimiento vertical:
                if pieza.__posicion__ == (x, y + 1) or pieza.__posicion__ == (x, y - 1) \
                    or pieza.__posicion__ == (x, y + 2) or pieza.__posicion__ == (x, y - 2):

                    if isinstance(casilla, Espacio):
                        posibilidades_checked.append(posicion)

                # Movimiento diagonal:
                elif pieza.__posicion__ == (x + 1, y + 1) or pieza.__posicion__ == (x - 1, y - 1) \
                    or pieza.__posicion__ == (x + 1, y - 1) or pieza.__posicion__ == (x - 1, y + 1):

                    if isinstance(casilla, Pieza):
                        if casilla.__color__ != pieza.__color__:
                            posibilidades_checked.append(posicion)

        # Si la pieza es un caballo, no necesito comprobar el camino
        # así que pasa directamente el checkeo.
        if isinstance(pieza, Caballo):
            posibilidades_double_checked = posibilidades_checked

        # Ahora, verifico si el camino entre el origen y el destino está libre.
        for posicion in posibilidades_checked:
            x, y = posicion
                
            # Si es caballo, lo salta al camino, así que no lo verifico.
            if not isinstance(pieza, Caballo):
                x_start, y_start = pieza.__posicion__
                x_end, y_end = posicion

                # Determino dx y dy, que es la dirección del camino.
                dx = 0 if x_end == x_start else (1 if x_end > x_start else -1)
                dy = 0 if y_end == y_start else (1 if y_end > y_start else -1)
                
                # Calculo la posición de avance de la pieza.
                x_avance, y_avance = x_start + dx, y_start + dy
                
                # Mientras no llegue al destino.
                while x_avance != x_end or y_avance != y_end:
                    # Mientras no encuentre ninguna pieza.
                    if isinstance(self.__tablero__[y_avance][x_avance], Pieza):
                        break # Salgo del bucle si encuentro una pieza.
                    # Si no, avanzo.
                    x_avance += dx
                    y_avance += dy
                else:
                    # Si el camino está libre, paso el checkeo.
                    posibilidades_double_checked.append(posicion)
                    continue
        
        # Para depurar:
        # print(pieza, " : ", posibilidades)
        # print(pieza, " : ", posibilidades_checked)
        # print(pieza, " : ", posibilidades_double_checked)
        # print(pieza, " : ", bool(posibilidades_double_checked))

        # Devuelvo el bool de si es un movimiento válido y las posibilidades.
        return bool(posibilidades_double_checked), posibilidades_double_checked                      


    def mover_pieza(self, pieza, nueva_posicion_str, \
                    nueva_posicion_int, vieja_posicion, posibilidades):
        # Acá está la logica para mover la pieza.
        
        # Convierto la nueva posición de notación de la tabla a coordenadas.
        # Esta no va a la función de conversión coordenadas, porque es la 
        # función inversa, así que lo reviso acá.
        # Try/Except por si envié un valor incorrecto.

        x, y = nueva_posicion_int

        # Obtengo la casilla destino.
        casilla_destino = self.__tablero__[y][x]

        x_vieja, y_vieja = vieja_posicion
        
        # Verifico si hay una pieza en la casilla destino.
        # Si casilla es una instancia pieza digo que la capturó.
        string_movimiento = ""
        if isinstance(casilla_destino, Pieza):
            string_movimiento += f"\nMovimiento realizado: {pieza.__nom__} {pieza.__color__} {x_vieja}{y_vieja}"
            string_movimiento += f" ha capturado {casilla_destino.__nom__} {casilla_destino.__color__} en {nueva_posicion_str}\n"
        
            # Actualizo el estado de la pieza capturada.
            casilla_destino.__vive__ = False

        else:
            string_movimiento += f"\nMovimiento realizado: {pieza.__nom__} {pieza.__color__} {x_vieja}{y_vieja}"
            string_movimiento += f" se ha movido a {nueva_posicion_str}\n"

        # Actualizo el tablero con la nueva posición de la pieza:
        # Saco las viejas coordenadas.
        x_actual, y_actual = pieza.__posicion__
        # Restauro la casilla original con el espacio correspondiente.
        self.__tablero__[y_actual][x_actual] = self.__BD_espacios__.search('B' if (x_actual + y_actual) \
                                                                            % 2 == 0 else 'N')
        # Coloco la pieza en la nueva posición.
        self.__tablero__[y][x] = pieza  

        # Actualizo los atributos de la pieza con la nueva posición de la pieza y 
        # ya no más su nuevo color de casilla. Ya que no estoy usando este atributo.
        # De todas formas, lo dejo por si acaso.
        ## nuevo_color_casilla = 'blanca' if casilla_destino.__color__ == 'blanca' else 'negra'
        pieza.mover((x, y)) # , nuevo_color_casilla)

        return True, string_movimiento # Devuelvo que se completó el movimiento 
                                       # y el string para printear.

    
    def verificar_victoria(self):
        # Verifico si el juego ha terminado.

        # Para una victoria por piezas:
        string_victoria, piezas_blancas_vivas, piezas_negras_vivas = self.victoria_por_piezas()

        # Para una victoria por movimientos:
        # Reviso si hay al menos un movimiento posible para cada jugador.
        movimientos_blancas = any(self.movible(pieza)[0] for pieza in piezas_blancas_vivas)
        movimientos_negras = any(self.movible(pieza)[0] for pieza in piezas_negras_vivas)

        if not movimientos_blancas and not movimientos_negras:
            string_victoria += "¡Empate por movimientos!"

        if not movimientos_blancas:
            string_victoria += "¡El jugador negro ha ganado por movimientos!"

        if not movimientos_negras:
            string_victoria += "¡El jugador blanco ha ganado por movimientos!"

        return string_victoria # Devuelvo el string de victoria, si está vacío no pasó nada.
    
    def victoria_por_piezas(self):

        # Reviso cada una de las piezas vivas de cada jugador.
        piezas_blancas_vivas = [pieza for pieza in self.__BD_piezas__.__base_datos__.values() if \
                                 pieza.__color__ == 'blanca' and pieza.__vive__]
        piezas_negras_vivas = [pieza for pieza in self.__BD_piezas__.__base_datos__.values() if \
                                pieza.__color__ == 'negra' and pieza.__vive__]

        string_victoria = ""

        if not piezas_blancas_vivas:
            string_victoria += "¡El jugador negro ha ganado por piezas!"

        if not piezas_negras_vivas:
            string_victoria += "¡El jugador blanco ha ganado por piezas!"
        
        # Devuelvo las piezas vivas de cada jugador.
        return string_victoria, piezas_blancas_vivas, piezas_negras_vivas 