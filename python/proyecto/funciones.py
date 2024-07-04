def find_dict(diccionario,parametro):
    for i in diccionario:
        if type(diccionario[i])!=str and type(diccionario[i])!=(int or float):
            if parametro in diccionario[i]:
                resultado=(i,diccionario[i].index(parametro))
                return resultado
        elif parametro==diccionario[i]:
            resultado=i
            return resultado


def registro_jugadores():
    import os
    jugador_1=input("Bienvenido al juego, ingrese aqui su nombre:   ")
    os.system("clear")
    jugador_2=input("Bienvenido al juego, ingrese aqui su nombre:   ")
    
    return jugador_1,jugador_2 

def repartir_cartas(jugador_1,jugador_2):
    from random import randint as random
    palos_cartas=["b","e","c","o"]
    maso={
        jugador_1:[],
        jugador_2:[]
    }
    c=0
    while True:
        indice_palos=random(0,3)
        numero_carta=random(1,12)
        carta= str(numero_carta) + palos_cartas[indice_palos]
        c+=1
        if carta not in maso[jugador_1] and carta not in maso[jugador_2]:
            if numero_carta!=9 and numero_carta!=8:
                if c%2==0:
                    maso[jugador_1].append(carta)
                else:
                    maso[jugador_2].append(carta)

        else:
            c-=1
        
        if c==6:
            break
        
    return maso


def filtro_jerarquia(maso):
    if "1e" in maso or "1b" in maso or "7e" in maso or "7o"in maso :
        top_cards=["1E","1B","7E","7O"]
        for index in top_cards:
            clave,pos_lista=find_dict(maso,index.lower())
            if (clave,pos_lista)!=None:
                