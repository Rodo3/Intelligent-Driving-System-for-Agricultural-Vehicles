import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Leer los datos desde el archivo CSV
df = pd.read_csv("datos.csv")

# Convertir la columna de tiempo a segundos transcurridos
df['tiempo'] = df['tiempo'] - df['tiempo'].iloc[0]

# Crear la ventana principal de tkinter
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# Variables para el control de la animación
start_index = 0
end_index = 10

# Función de actualización para la animación
def update(frame):
    global start_index, end_index

    # Limpiar gráficos existentes
    for ax in axes.flatten():
        ax.clear()

    # Crear subgráficos actualizados para cada variable
    for i, col in enumerate(df.columns[1:]):  # Excluir la primera columna de tiempo
        axes[i // 3, i % 3].plot(df['tiempo'].iloc[start_index:end_index], df[col].iloc[start_index:end_index])
        axes[i // 3, i % 3].set(xlabel="Tiempo (segundos)")

        # Añadir labels personalizados para los ejes y
        if col == 'Vehicle Speed':
            axes[i // 3, i % 3].set(ylabel="Vehicle Speed (km/h)")
        elif col == 'Engine Speed':
            axes[i // 3, i % 3].set(ylabel="Engine Speed (rpm)")
        elif col == 'Throttle':
            axes[i // 3, i % 3].set(ylabel="Throttle (%)")

    # Actualizar índices para la próxima animación
    start_index += 1
    end_index += 1

    # Detener la animación cuando se alcance el final de los datos
    if end_index >= len(df):
        ani.event_source.stop()

# Crear la animación con intervalo de 1 segundo
ani = FuncAnimation(fig, update, frames=(len(df) - 10), interval=1000)

# Mostrar la ventana de matplotlib
plt.show()
