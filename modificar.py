def reordenar_bytes(data):
    # Creamos una lista para almacenar los datos reorganizados
    new_data = bytearray(len(data))
    
    # Iteramos de 4 en 4 bytes, ya que el patrón afecta a los 4 primeros bytes de cada grupo
    for i in range(0, len(data), 4):
        if i + 3 < len(data):
            # Cambiar el orden de los bytes según el patrón
            new_data[i] = data[i + 3]
            new_data[i + 1] = data[i + 2]
            new_data[i + 2] = data[i + 1]
            new_data[i + 3] = data[i]
        else:
            # Si no hay suficientes bytes (últimos bloques), copiamos tal cual
            new_data[i:i+len(data[i:])] = data[i:i+len(data[i:])]
    
    return new_data

def cambiar_orden_bytes(archivo_entrada, archivo_salida):
    # Abrir el archivo en modo binario para lectura
    with open(archivo_entrada, 'rb') as f_in:
        data = f_in.read()

    # Reordenar los bytes de acuerdo al patrón
    data_reordenada = reordenar_bytes(data)

    # Guardar los datos modificados en otro archivo
    with open(archivo_salida, 'wb') as f_out:
        f_out.write(data_reordenada)

# Llamamos a la función con el archivo de entrada y salida
archivo_entrada = 'archivo_original.bin'
archivo_salida = 'archivo_modificado.bin'
cambiar_orden_bytes(archivo_entrada, archivo_salida)
