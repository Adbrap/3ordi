import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import json
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import math
import os
import time

def get_angle(point1, point2):
    x_diff = point2[0] - point1[0]
    y_diff = point2[1] - point1[1]

    # Pour une ligne verticale, on retourne 90 directement
    if x_diff == 0:
        return 90

    angle = math.atan2(y_diff, x_diff)
    angle = math.degrees(angle)
    return angle


def plot_points(point1, point2):
    angle = get_angle(point1, point2)

    # Si l'angle est 90 (ligne verticale), la pente est "infinie"
    if angle == 90:
        slope_percent = "90"
        return slope_percent
    else:
        slope_percent = math.tan(math.radians(angle)) * 100
        return slope_percent
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('les courbes ne se coupent pas')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

final_final2 = 0

nombre_fini1 = 0
gain_moyenn1 = 0
temp_moyenn1 = 0
pourc_gagn_gagn1 = 0

nombre_fini2 = 0
gain_moyenn2 = 0
temp_moyenn2 = 0
pourc_gagn_gagn2 = 0

def prout2anto(chaineA,chaineB,nomfichier,clo11,pourc,clo22,pourc2,nombre):

    global nombre_fini1
    global gain_moyenn1
    global temp_moyenn1
    global gain_cumulé1
    global pourc_gagn_gagn1

    global nombre_fini2
    global gain_moyenn2
    global temp_moyenn2
    global gain_cumulé2
    global pourc_gagn_gagn2

    global final_final2


    nombre_point = 0
    nombre_magique = 0
    mise = 10000
    minargent = 5
    laquelle = []
    plusbas = []
    plusbas1 = 0
    changement = []
    pourcent_gain = 0
    nombre_regarder = 0
    nombre_gagnant = 0
    nombre_perdant = 0
    debug = []
    condition = 0
    placebas = 0
    pourcentbastete = []
    toutemoyennetete = []
    chemin_fichier = f"out/1{nomfichier}.txt"
    pourc = int(pourc)
    pourc2 = int(pourc2)
    nombre_vuvu = 0
    minimum_alex = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15]
    stratstrat = 1.5







    with open(chemin_fichier, 'w') as fichier:
        pass

    for t in range(chaineA,chaineB):
        try:

            nombre_regarder = nombre_regarder +1
            Write.Print(f'Figure Numero {t}', Colors.pink, interval=0.000)
            print('')
            dossier = "/home/mat/Bureau/mass/"
            nom_fichier = f"{t}.json"
            chemin_fichier = dossier + nom_fichier
            with open(chemin_fichier, 'r') as fichiers:
                data = json.load(fichiers)

            df = pd.DataFrame(data)
            df = df.reset_index(drop=True)
            #df = pd.DataFrame(data['results'])

            #with open(chemin_fichier, 'w') as fichier:
            #json.dump(data, fichier)
            local_max = argrelextrema(df['c'].values, np.greater, order=1, mode='clip')[0]
            local_min = argrelextrema(df['c'].values, np.less, order=1, mode='clip')[0]
            highs = df.iloc[local_max, :]
            lows = df.iloc[local_min, :]

            A = float(highs['c'].iloc[0])
            B = float(lows['c'].iloc[0])
            C = float(highs['c'].iloc[1])
            D = float(lows['c'].iloc[1])
            E = float(highs['c'].iloc[2])
            F = float(lows['c'].iloc[2])
            G = float(highs['c'].iloc[3])


            vert = []
            rouge = []
            bleu = []

            vert.append(local_max[0]) #A
            vert.append(local_max[1]) #C
            vert.append(local_max[2]) #E
            vert.append(local_max[3]) #G

            rouge.append(local_max[0])
            rouge.append(local_min[0])
            rouge.append(local_max[1])
            rouge.append(local_min[1])
            rouge.append(local_max[2])
            rouge.append(local_min[2])
            rouge.append(local_max[3])

            i = 0
            for i in range(local_min[2], len(df)):
                bleu.append(i)

            mirande2 = df.iloc[vert, :]
            mirande = df.iloc[rouge, :]
            mirande3 = df.iloc[bleu, :]

            if C > E:
                differ = (C - E)
                pas = (local_max[2] - local_max[1])
                suite = differ / pas
            if C < E:
                differ = (E - C)
                pas = (local_max[2] - local_max[1])
                suite = differ / pas

            if E > C:
                mirande2['c'].values[0] = mirande2['c'].values[1] - ((suite * (local_max[1] - local_max[0])))
                mirande2['c'].values[3] = mirande2['c'].values[2] + ((suite * (local_max[3] - local_max[2])))
            if E < C:
                mirande2['c'].values[0] = mirande2['c'].values[1] + ((suite * (local_max[1] - local_max[0])))
                mirande2['c'].values[3] = mirande2['c'].values[2] - ((suite * (local_max[3] - local_max[2])))
            if E == C:
                mirande2['c'].values[0] = df['c'].values[local_max[1]]
                mirande2['c'].values[3] = df['c'].values[local_max[1]]

            vert1 = {'c': vert}
            vert2 = pd.DataFrame(data=vert1)
            rouge1 = {'c': rouge}
            rouge2 = pd.DataFrame(data=rouge1)

            AI = [local_max[0], mirande2['c'].iloc[0]]
            BI = [local_max[1], mirande2['c'].iloc[1]]

            CI = [local_max[0], A]
            DI = [local_min[0], B]

            AJ = [local_max[2], mirande2['c'].iloc[2]]
            BJ = [local_max[3], mirande2['c'].iloc[3]]

            CJ = [local_max[3], G]
            DJ = [local_min[2], F]

            J = line_intersection((AJ, BJ), (CJ, DJ))
            I = line_intersection((AI, BI), (CI, DI))
            point_I = (I[0],I[1])
            point_J = (J[0],J[1])
            slope_percent = plot_points(point_I, point_J)
            moyenne_tete = ((C - D) + (E - D)) / 2
            pourcent_tete = ((((C - D) + (E - D)) / 2) * 100)/ D
            toutemoyennetete.append(pourcent_tete)

            #ticker = data['ticker']
            trouver = False
            try:
                for i in range(local_min[2], local_max[3] + 5):
                    if df['c'].iloc[i] >= J[1] and df['c'].iloc[i] <= J[1] + (moyenne_tete) / 4 and trouver == False:
                        # if df['c'].iloc[i] > df['c'].iloc[local_min[ff]] and df['c'].iloc[i] <= J[1] + (moyenne_tete) / 4 and trouver == False:
                        placejaune = i
                        trouver = True
                        plusbas1 = df['h'].iloc[placejaune]
                condition = J[1] - ((moyenne_tete)*pourc2 / 100)
                trouver2 = False
                trouver3 = False
                trouver4 = False
                changement1 = False

                #for lala in minimum_alex:
                if (((((J[1] + ((moyenne_tete) * pourc / 100)) - df['c'].iloc[placejaune])) * 100) / df['c'].iloc[placejaune]) > stratstrat:

                    if (((((( df['c'].iloc[placejaune] + ((moyenne_tete)*pourc / 100)) - df['c'].iloc[placejaune])) * 100) / df['c'].iloc[placejaune]) * mise )/100 >= minargent:
                        for i in range(placejaune, len(df)):
                            if df[f'{clo22}'].iloc[i] < condition and trouver3 == False and trouver2 == False:
                                placerouge = i
                                pourcent_gain = pourcent_gain + ((((df[f'{clo22}'].iloc[i] - df['c'].iloc[placejaune]))*100) /df['c'].iloc[placejaune])
                                #print(((((df['c'].iloc[i] - df['c'].iloc[placejaune]))*100) /df['c'].iloc[placejaune]))
                                prix = ((((df[f'{clo22}'].iloc[i] - df['c'].iloc[placejaune]))*100) /df['c'].iloc[placejaune])
                                debug.append(round(prix,2))
                                nombre_perdant = nombre_perdant +1
                                nombre_point = nombre_point + (placerouge - placejaune)


                                trouver3 = True
                            if df[f'{clo11}'].iloc[i] >= J[1] + ((moyenne_tete)*pourc / 100) and trouver2 == False and trouver3 == False:
                                placevert = i
                                #pourcent_gain = pourcent_gain + ((((df[f'{clo11}'].iloc[i] - df['c'].iloc[placejaune] ))*100) /df['c'].iloc[placejaune])
                                pourcent_gain = pourcent_gain + ((((( J[1]+ ((moyenne_tete)*pourc / 100)) - df['c'].iloc[placejaune])) * 100) / df['c'].iloc[placejaune])
                                #print(((((df['c'].iloc[i] - df['c'].iloc[placejaune] ))*100) /df['c'].iloc[placejaune]))
                                #prix = ((((df[f'{clo11}'].iloc[i] - df['c'].iloc[placejaune] ))*100) /df['c'].iloc[placejaune])
                                prix = ((((( J[1] + ((moyenne_tete)*pourc / 100)) - df['c'].iloc[placejaune])) * 100) / df['c'].iloc[placejaune])
                                print()
                                debug.append(round(prix, 2))
                                nombre_gagnant = nombre_gagnant +1
                                nombre_point = nombre_point + (placevert - placejaune)
                                trouver2 = True
                        if (A-B) >= (C-D) and  slope_percent <= 5:
                            nombre_magique = nombre_magique + 1
                            laquelle.append(len(debug))
                        if (((((( df['c'].iloc[placejaune] + ((moyenne_tete)*pourc / 100)) - df['c'].iloc[placejaune])) * 100) / df['c'].iloc[placejaune]) * mise )/100 >= minargent:
                            if trouver2 == True:
                                for m in range(placejaune, placevert+1) :
                                    if df['h'].iloc[m] < plusbas1:
                                        plusbas1 = df['h'].iloc[m]
                                        placebas = m
                                        changement1 = True
                                if changement1 == True:
                                    changement.append(t)
                                if changement1 == False:
                                    placebas = placejaune
                                plusbas.append(plusbas1)
                                trouver4 = True
                                pourcentbastete.append(round(((df['h'].iloc[placebas] - df['c'].iloc[placejaune])*100)/moyenne_tete,2))
                    # ----- creation des locals(min/max) -----#
                    fig1 = plt.figure(figsize=(10, 7))
                    plt.plot([], [], " ")
                    fig1.patch.set_facecolor('#17DE17')
                    fig1.patch.set_alpha(0.3)
                    plt.title(f'IETE : {t} {slope_percent}', fontweight="bold", color='black')
                    df['c'].plot(color=['blue'], label='Clotures')
                    mirande2['c'].plot(color=['green'], linestyle='--', label='Ligne de coup')
                    mirande['c'].plot(color=['red'], alpha = 0.3, linestyle='-', label='Forme IETE')
                    mirande3['h'].plot(color=['green'], alpha = 0.3, linestyle='-', label='Plus Haut')
                    mirande3['l'].plot(color=['red'], alpha = 0.3, linestyle='-', label='Plus Bas')
                    plt.axhline(y=J[1] + moyenne_tete, linestyle='--', alpha=0.3, color='red', label='100% objectif')
                    plt.axhline(y=J[1] + (((moyenne_tete) / 2) + ((moyenne_tete) / 4)), linestyle='--', alpha=0.3, color='black', label='75% objectif')
                    plt.axhline(y=J[1] + ((moyenne_tete)*50) / 100, linestyle='--', alpha=0.3, color='orange', label='50% objectif')
                    plt.axhline(y=J[1] + (moyenne_tete) / 4, linestyle='--', alpha=0.3, color='black', label='25% objectif')
                    plt.axhline(y=df['c'].iloc[placejaune] + ((moyenne_tete)*pourc) / 100, linestyle=':', color='pink', label=f'{pourc}% objectif')
                    plt.axhline(y=df['c'].iloc[placejaune] - ((moyenne_tete) * pourc2 / 100), linestyle='--', color='red', alpha=0.3, label=f'-{pourc2}% objectif')
                    #plt.scatter(x=highs.index, y=highs['c'], alpha=0.5)
                    #plt.scatter(x=lows.index, y=lows['c'], alpha=0.5
                    plt.scatter(local_max[0], A, color='blue')
                    plt.scatter(local_min[0], B, color='blue')
                    plt.scatter(local_max[1], C, color='blue')
                    plt.scatter(local_min[1], D, color='blue')
                    plt.scatter(local_max[2], E, color='blue')
                    plt.scatter(local_min[2], F, color='blue')
                    plt.scatter(local_max[3], G, color='blue')
                    plt.scatter(I[0], I[1], color='green')
                    plt.scatter(J[0], J[1], color='green')
                    plt.scatter(placejaune, df['c'].values[placejaune], color='orange', label='BUY')
                    if trouver2 == True:
                        plt.scatter(placevert, df['c'].iloc[placejaune] + ((moyenne_tete)*pourc / 100), color='green', label='SELL')
                    if trouver3 == True:
                        plt.scatter(placerouge, df['c'].values[placerouge], color='red', label='SELL')
                    if trouver4 == True:
                        plt.scatter(placebas, plusbas1, color='purple', label='PLUS BAS')

                    plt.text(local_max[0], A, "A", ha='left', style='normal', size=10.5, color='red', wrap=True)
                    plt.text(local_min[0], B, "B", ha='left', style='normal', size=10.5, color='red', wrap=True)
                    plt.text(local_max[1], C, "C", ha='left', style='normal', size=10.5, color='red', wrap=True)
                    plt.text(local_min[1], D, f"D {round(D, 5)}  +{round(pourcent_tete, 3)}%", ha='left', style='normal', size=10.5, color='red', wrap=True)
                    plt.text(local_max[2], E, "E", ha='left', style='normal', size=10.5, color='red', wrap=True)
                    plt.text(local_min[2], F, f"F  {round(F, 5)}", ha='left', style='normal', size=10.5, color='red', wrap=True)
                    plt.text(local_max[3], G, f"G  {round(G, 5)}", ha='left', style='normal', size=10.5, color='red', wrap=True)
                    plt.text(I[0], I[1], "I", ha='left', style='normal', size=10.5, color='#00FF36', wrap=True)
                    plt.text(J[0], J[1], "J", ha='left', style='normal', size=10.5, color='#00FF36', wrap=True)
                    # plt.scatter(x=local_max.values, y=df['c'].iloc[local_max], color=['red'], label='haut')
                    # plt.scatter(x=highs.index, y=highs["c"])
                    # plt.scatter(x=low.index, y=low["c"])
                    plt.legend()


        #exc    t        ept:
        #       t        print('')
        #       t        Write.Print(f'Probleme Titre', Colors.red, interval=0.000)
        #       t        print('')

                else:
                    print(f'en dessous de {stratstrat}' )

            except:
                print('probleme ticker')
        except:
            print('probleme ticker2')



    chemin_fichier = f"out/1{nomfichier}.txt"
    with open(chemin_fichier, 'w') as fichier:
        fichier.write(f'{round(pourcent_gain, 2)}' + "\n")
        fichier.write(f'{round(nombre_regarder, 2)}' + "\n")
        fichier.write(f'{round(nombre_gagnant, 2)}'+ "\n")
        fichier.write(f'{round(nombre_perdant, 2)}' + "\n")

        pourc_gagn = (nombre_gagnant * 100) / len(debug)
        pourc_gagn = round(pourc_gagn, 2)

        fichier.write(f'{pourc_gagn}' + "\n")

        pg_gain = max(debug)
        print(debug)
        pg_perte = min(debug)
        if pg_gain <= 0:
            pg_gain = 'NULL'
        if pg_perte >= 0:
            pg_perte = 'NULL'

        fichier.write(f'{pg_gain}' + "\n")
        fichier.write(f'{pg_perte}' + "\n")
        fichier.write(f'{round(nombre_point / len(debug), 2)}' + "\n")

        somme = sum(debug)
        moyenne = somme / len(debug)

        fichier.write(f'{round(moyenne, 3)}')



        print('=====================================================================')

        print(f'strategie au dessus de {stratstrat}')
        print(f'Gain cumulé (%) : ', round(pourcent_gain, 2),'%')
        print(f'Nombre testé : ', round(nombre_regarder, 2))
        print(f'Nombre Figure Fini : ', round(nombre_gagnant+nombre_perdant, 2))
        print(f'Nombre gagnants : ', round(nombre_gagnant, 2))
        print(f'Nombre Perdants : ', round(nombre_perdant, 2))
        print(f'Pourcentage gain : ', round(pourc_gagn, 2),'%')
        print(f'Plus gros Gain : ', pg_gain,'%')
        print(f'Plus Grosse perte : ', pg_perte,'%')
        print(f'Nombre points moyen : ', round(nombre_point / len(debug), 2))
        print(f'Gain moyen (%) : ', round(moyenne, 3),'%')
        denomdnom = 'minute'
        tempstemps = (round(nombre_point / len(debug), 2) * 256.24)
        if tempstemps >= 60 and tempstemps < 1440:
            denomdenom = 'heure'
            tempstemps = tempstemps / 60
        if tempstemps >= 1440:
            denomdenom = 'jour'
            tempstemps = (tempstemps / 60) / 7

        print(f'Temps moyen : {round(tempstemps, 3)} {denomdenom}')
        print('')

        if nombre == 2:
            nombre_fini2 = (round(nombre_gagnant, 2)+round(nombre_perdant, 2))
            gain_moyenn2 = (round(moyenne, 3))
            temp_moyenn2 = (round(nombre_point / len(debug), 2))
            pourc_gagn_gagn2 = pourc_gagn

        if nombre == 1:
            nombre_fini1 = (round(nombre_gagnant, 2)+round(nombre_perdant, 2))
            gain_moyenn1 = (round(moyenne, 3))
            temp_moyenn1 = (round(nombre_point / len(debug), 2))
            pourc_gagn_gagn1 = pourc_gagn

        if denomdenom == 'heure':
            final_final2 = 7 / tempstemps
        if denomdenom == 'jour':
            final_final2 = 7 / (tempstemps*24)








prout2anto(1,5000,'A','h',40,'c',85,1)
#prout2anto(5000,10000,'B','h',40,'c',85,2)
#prout2anto(10000,15000,'C','h',30,'c',10)
#prout2anto(15000,18388,'D','h',35,'c',17)


#nombre_fini2 = nombre_fini2 + nombre_fini1
#gain_moyenn2 = gain_moyenn2 + gain_moyenn1
#temp_moyenn2 = temp_moyenn2 +temp_moyenn1
#pourc_gagn_gagn2 = pourc_gagn_gagn2 + pourc_gagn_gagn1
#
#print(nombre_fini2)
#print(gain_moyenn2)
#print(temp_moyenn2)
#print(pourc_gagn_gagn2)
#
#final_final = gain_moyenn2 *100
#final_final = final_final * final_final2
#print('=====')
#print(final_final)
#
Write.Print('A fini ! :-)', Colors.green, interval=0.000)
#
#print('-------')
#print(f'nombre fini = {nombre_fini}')
#print(f'gain moyen = {gain_moyenn/4}')
#
#temp_moyenn = temp_moyenn /4
#
#
#
#denomdnom = 'minute'
#tempstemps = (temp_moyenn * 256.24)
#if tempstemps >= 60 and tempstemps < 1440:
#    denomdenom = 'heure'
#    tempstemps = tempstemps / 60
#if tempstemps >= 1440:
#    denomdenom = 'jour'
#    tempstemps = (tempstemps / 60) / 7
#print(f'Temps moyen : {round(tempstemps, 3)} {denomdenom}')