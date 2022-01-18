def crear_archivo_final(m_e,t_v,m_s,m_d,t_n,t_b,d_m_d,lista_candidatos_fin):
    archivo = open("LO PRADO.txt", "w+")

    archivo.write("####################\n")
    archivo.write("GENERAL\n")
    archivo.write("####################\n")
    archivo.write("MESAS ESCRUTADAS: "+str(m_e)+"\n")
    archivo.write("CORRECTAS: "+str(m_s)+"\n")
    archivo.write("DESCUADRADAS: "+str(m_d)+"\n")
    archivo.write("\n")
    archivo.write("####################\n")
    archivo.write("RESULTADOS PARCIALES\n")
    archivo.write("####################\n")
    archivo.write("\n")
    for detalle in lista_candidatos_fin:
        archivo.write(detalle+"\n")
    archivo.write("NULOS,"+str(t_n)+","+str(format((t_n*100)/t_v,'.2f'))+"%\n")
    archivo.write("BLANCOS,"+str(t_b)+","+str(format((t_b*100)/t_v,'.2f'))+"%\n")
    archivo.write("\n")
    archivo.write("####################\n")
    archivo.write("MESAS DESCUADRADAS\n")
    archivo.write("####################\n")
    for detalle2 in d_m_d:
        archivo.write(detalle2+"\n")
        
    archivo.close()

def colsum(arr, n, m):
    list_suma = []
    for i in range(n):
        su = 0;
        for j in range(m):
            su += arr[j][i]
        list_suma.append(int(su))
    return list_suma

def leer_archivos(num):
    i = 1
    t_n = 0 # TOTAL NULOS
    t_b = 0 # TOTAL BLANCOS
    t_v_c = 0 # TOTAL VOTOS CANDIDATOS
    m_s = 0 # MESAS CORRECTAS
    m_d = 0 # MESAS DESCUADRADAS
    d_m_d = [] # DETALLE MESAS DESCUADRADAS
    list_s_v = [] # LISTA SUMA VOTOS POR CANDIDATO
    list_suma = [] # SUMA DE VOTOS CANDIDATOS
    lista_candidatos_fin = [] # LISTA CANDIDATOS FINAL
    while i <= int(num):
        with open('mesa-'+str(i)+'.txt', encoding="utf8") as archivo:
            lineas = archivo.read().splitlines()
            n = 0 # NULOS
            b = 0 # BLANCOS
            v_c = 0 # VOTOS CANDIDATOS
            list_o_n = [] # ORDENAR NUMEROS
            list_n_c = [] # LISTA NOMBRE CANDIDATOS
            #print(lineas[1:-2])
            n = n + int(lineas[-2].split(',')[1]) # TOTAL NULOS
            b = b + int(lineas[-1].split(',')[1]) # TOTAL BLANCOS
            for candidato in lineas[1:-2]:
                v_c = v_c + int(candidato.split(",")[1]) # TOTAL VOTOS CANDIDATOS
            if v_c+n+b is int(lineas[0].split(",")[2]):
                m_s = m_s + 1 # SUMAR MESAS ESCRUTADAS
            else:
                m_d = m_d + 1 # SUMAR MESAS DESCUADRADAS
                d_m_d.append(lineas[0].split(",")[1]) # AGREGAR MESA DESCUADRADA
            #print(lineas[1:-2])
            for j in lineas[1:-2]:
                list_o_n.append(int(j.split(",")[1]))
                list_n_c.append(str(j.split(",")[0]))
            list_s_v.append(list_o_n)
        t_n = t_n + n
        t_b = t_b + b
        t_v_c = t_v_c + v_c
        i = i + 1
    list_suma = colsum(list_s_v,len(list_s_v[0]),len(list_s_v))
    for idx,ele in enumerate(list_n_c):
        lista_candidatos_fin.append(ele+","+str(list_suma[idx])+","+str(format((list_suma[idx]*100)/(t_v_c+t_n+t_b),'.2f'))+"%")
    crear_archivo_final(num,t_v_c+t_n+t_b,m_s,m_d,t_n,t_b,d_m_d,lista_candidatos_fin)

num = input("Favor ingrese un valor numérico: ")
leer_archivos(num)
