import serial
import csv
import time

# Configuración del puerto serie
ser = serial.Serial('/dev/ttyS0', 115200)

# Archivo CSV para almacenar datos
csv_filename = "datos.csv"

try:
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['tiempo', 'Vehicle Speed', 'Engine Speed', 'Gear', 'Throt>
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            tiempo_actual = time.time()  # Timestamp actual
            linea = ser.readline().decode('utf-8').strip()
            
            # Simplemente como ejemplo, asumiendo que los datos en la línea est>
            datos = dict(part.split(':') for part in linea.split(','))

            # Ajusta la estructura de datos según tus necesidades
            data_dict = {'tiempo': tiempo_actual}
            data_dict.update(datos)

            # Elimina espacios en los nombres de las claves
            data_dict = {key.strip(): value for key, value in data_dict.items()}

            # Almacena los datos en el archivo CSV
            writer.writerow(data_dict)
            print(f"Datos almacenados: {data_dict}")

except KeyboardInterrupt:
    print("Lectura del puerto serial detenida")