from random import randrange, choice 
print(' ')
print(' ')
print('                                                      BIENVENIDO                                                          ')
print('                                                                                                                          ')
print('                                                           A                                                              ')
print(' ')
print('                                        ||||||||||||||||||||||||||||||||||||||                                            ')
print('                                        ----------- ADIVINA PALABRA ----------                                            ')
print('                                        ||||||||||||||||||||||||||||||||||||||                                            ')
print('                                                                                                                          ') 
print('                                                                                                                          ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
input('                                             PRESIONE ENTER PARA CONTINUAR ')
print(' ')
print(' ')
print(' ')

print('CONFIGURACIÓN')
j1m = input('INGRESE EL NOMBRE DEL JUGADOR 1 = ')
j2m = input('INGRESE EL NOMBRE DEL JUGADOR 2 = ')
j1 = j1m.upper()
j2 = j2m.upper()
cp = int(input('INGRESE LA CANTIDAD DE PALABRAS QUE DEBE ADIVINAR CADA JUGADOR = '))
ci = int(input('INGRESE CANTIDAD MAXIMA DE INTENTOS PARA ADIVINAR = '))

def comprobacion(pa):
    ab = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    if len(pa) <= 20:
        pru = []
        for i in pa:   
            if i in ab:
                pru.append(i)
    
        if pru == pa:
            return True
        elif pru != pa:
            ic = print('INCORRECTO REINGRESE LA PALABRA SIN CARACTERES Y TODO EN MINUSCULAS')
            return ic 

    elif len(pa) > 20:
        ic = print('INCORRECTO REINGRESE UNA PALABRA QUE TENGA MENOS DE 20 LETRAS')    
        return ic


print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')

                


puntj1t = []
puntj2t = []
pl = 1
if pl == 1:
    pro = choice([j1,j2])
ro = 1
print('_____________________________________________________________________________________________________________________________________________________________')
print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print(' ')
print(' ')
while ro <= cp:
    puntj1 = []
    puntj2 = []
    print('                                                             |||||||||||||||                              ')
    print(f'                                                             ----RONDA {ro}----                              ')
    print('                                                             |||||||||||||||                              ')
    tur = 1
    while tur <= 2:
        if pro == j1:
            adi = j2
        elif pro == j2:
            adi = j1
        print(' ')
        print(f'AHORA JUEGA EL PROPONEDOR {pro}')
        print(' ')
        print(' ')
        print(' ')
        pala = str(input('PALABRA PARA ADIVINAR = '))
        pa = []
        for i in pala:
            pa.append(i)
        if comprobacion(pa) != True: # SI NO CONCUERDA LA LA PALABRA CON LOS PARAMETROS ESTE TIENE DOS OPORTUNIDADES MAS 
            o = 2
            if o == 3:
                print('ESTA ES LA ULTIMA OPORTUNIDAD PARA INGRESAR LA PALABRA CON LOS PARAMETROS CORRECTOS ')
            while o <= 3:
                pala = str(input('REINGRESE LA PALABRA = '))
                pa = []
                for i in pala:
                    pa.append(i)
                if comprobacion(pa) == True:
                    break
                else:
                    o = o + 1
               # SI SE SALIO DEL BUCLE Y SI TODAVIA NO CUMPLE LOS PARAMETROS TERMINA EL JUEGO AUTOMATICAMENTE EL JUGADOR CONTRARIO GANA
                
            if comprobacion(pa) != True:
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(f'                                                             EL JUGADOR {adi} GANA POR DEFAULT TODO EL JUEGO')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                exit()
        print(f'AHORA JUEGA EL ADIVINADOR {adi}')
        print(' ')
        print(' ')
        print(' ')

        
        bu = 0
        gui =['_']      
        print(f'LA PALABRA CONTIENE {len(pa)}')
        print(' ')
        guil = gui * len(pa)
        guild = ''.join(guil) 
        print(f'           {guild}')
        print(' ')
        while bu <= ci:
            if guil == pa:
                break
            c = input('INGRESE UNA LETRA DE LA PALABRA = ')
            print(' ')
            if c in pa:
                kj =[]
                for k,j in enumerate(pa):       # aca esta encontrando en todas las posiciones que se encuentra la letra
                    if j == c:
                        kj.append(k)
                        guil[k]= c
                print(f'LA LETRA SE ENCUNTRA EN LA POSICION {kj}')
                guild = ''.join(guil)
                print(' ')

                print(f'           {guild}')
                print(' ')
            elif c not in pa:
                print('INCORRECTO LA LETRA NO SE ENCUNTRA EN LA PALABRA ')
                print(' ')
                bu = bu + 1   
        pala1 = pala.upper()
        if guil == pa:
            print(f'FELICIDADES HAS ADIVINADO, LA PALABRA ERA = {pala1}')
            # se realiza el conteo de puntaje
            punt = (1-(bu/ci))* len(pa)
            if adi == j1:
                puntj1.append(punt)
                puntj1t.append(punt)
            elif adi == j2:
                puntj2.append(punt)
                puntj2t.append(punt)
        else:
            print(f'NÚMEROS DE INTENTOS SUPERADOS, LA PALABRA ERA = {pala1}')
            print(' ')
        tur = tur + 1
        if pro == j1:
            pro = j2
        elif pro == j2:
            pro = j1
        pl = pl + 1 
    
    print(' ')  
    print(f'                                                        PUNTAJE DE LA RONDA {ro} ')
    print(' ')
    print(f'                                                        PUNTAJE DE {j1} = {sum(puntj1)}')
    print(f'                                                        PUNTAJE DE {j2} = {sum(puntj2)}') 

    print(' ')
    print(f'                                                        PUNTAJE PARCIAL ')
    print(' ')
    print(f'                                                        PUNTAJE DE {j1} = {sum(puntj1t)}')
    print(f'                                                        PUNTAJE DE {j2} = {sum(puntj2t)}')
    print(' ')
    print(' ')
    ro = ro + 1
    
print(' ')
print(' ')
print(' ')
print('_____________________________________________________________________________________________________________________________________________________________')
print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print(' ')
print(f'                                                        PUNTAJE TOTAL ')

print(' ')
print(f'                                                        PUNTAJE DE {j1} = {sum(puntj1t)}')
print(f'                                                        PUNTAJE DE {j2} = {sum(puntj2t)}')         

if sum(puntj1t) > sum(puntj2t):
    print(' ')
    print(' ')
    print(f'                                                        ¡FELICIDADES {j1} HA GANADO LA PARTIDA!')      
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    exit()
elif sum(puntj2t) > sum(puntj1t):
    print(' ')
    print(' ')
    print(f'                                                        ¡FELICIDADES {j2} HA GANADO LA PARTIDA!')      
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    exit()
elif sum(puntj2t) == sum(puntj1t):
    print(' ')
    print(' ')
    print(f'                                                        SE A PRODUCIDO UN EMPATE ENTRE {j1} Y {j2}')      
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    exit()

        
    
    
    


