import pandas as pd
print('pregunta 1:')
df = pd.read_csv('tabla_posiciones_2024.csv', sep= ';')
print(df)



print('pregunta 2:')
#cambiar el nombre de las columnas
df2 = df.rename(columns={'equipos':'Equipos','pj':'Partidos jugados','g':'Goles','e':'Empates','p':'Perdidos','gf':'Goles a favor','gc':'Goles en contra','dg':'Diferencia de goles','p.1':'Puntos' })
print(df2)

 

print('pregunta 3: imprimir los 4 primeros clasificados')
print(df2.iloc[:4])



print('pregunta 4:Generar una tabla con Equipos, Puntos, Goles a favor y goles en contra con los 8 equipos en cuadrangulares')
print(df2.iloc[:8, [0,8,5,6]])



print('pregunta 5:Restarle 3 puntos a cada equipo de la tabla')
print(df2.loc[:20, ['Puntos']] -3)




print('pregunta 6: Sumarle 3 puntos a los primeros 8 equipos')
print(df2.loc[:8, ['Puntos']] +3)



print('pregunta 7:imprimir los primeros 8 equipos')
print(df2.iloc[:8])


print('pregunta 8: sumarle 10 goles a favor a los equipos')
print(df2.loc[:20, ['Goles a favor']]+10)