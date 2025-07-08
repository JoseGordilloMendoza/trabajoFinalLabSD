import time
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Simulación del reloj del servidor (UTC simulado)
def servidor_tiempo():
    return time.time()

# Simulación del algoritmo de Cristian
def algoritmo_cristian():
    print("\n==> Iniciando sincronización con el servidor de tiempo...")

    # Cliente toma el tiempo antes de enviar solicitud
    t0 = time.time()
    print(f"Cliente envía solicitud en t0 = {t0:.3f}")

    # Simula latencia de red (ida)
    latencia_ida = random.uniform(0.05, 0.1)
    time.sleep(latencia_ida)

    # Servidor recibe la solicitud y responde con su tiempo actual
    tiempo_servidor = servidor_tiempo()
    print(f"Servidor responde con su hora t = {tiempo_servidor:.3f}")

    # Simula latencia de red (vuelta)
    latencia_vuelta = random.uniform(0.05, 0.1)
    time.sleep(latencia_vuelta)

    # Cliente recibe respuesta y toma tiempo actual
    t1 = time.time()
    print(f"Cliente recibe respuesta en t1 = {t1:.3f}")

    # Tiempo de ida y vuelta
    rtt = t1 - t0
    print(f"Tiempo ida y vuelta (RTT) = {rtt:.3f}")

    # Estimación de reloj del servidor
    tiempo_estimado = tiempo_servidor + (rtt / 2)
    print(f"Cliente ajusta su reloj a ≈ {tiempo_estimado:.3f}")

    return t0, tiempo_servidor, t1, tiempo_estimado

# Graficar la sincronización
def graficar_sincronizacion(t0, ts, t1, tc):
    fig, ax = plt.subplots()
    ax.set_title("Algoritmo de Cristian - Sincronización de Reloj")
    ax.set_xlim(t0 - 0.1, t1 + 0.1)
    ax.set_ylim(0, 3)
    ax.set_yticks([1, 2])
    ax.set_yticklabels(["Cliente", "Servidor"])

    # Líneas de tiempo
    ax.hlines(1, t0 - 0.1, t1 + 0.1, colors='gray', linestyles='dotted')
    ax.hlines(2, t0 - 0.1, t1 + 0.1, colors='gray', linestyles='dotted')

    # Mensaje enviado
    ax.plot([t0, ts], [1, 2], color='blue', marker='o', label='Solicitud')

    # Mensaje recibido
    ax.plot([ts, t1], [2, 1], color='green', marker='o', label='Respuesta')

    # Tiempo ajustado
    ax.vlines(tc, 0.8, 1.2, color='red', linestyles='--', label='Reloj Ajustado')

    ax.legend()
    plt.xlabel("Tiempo (segundos)")
    plt.tight_layout()
    plt.show()

# Ejecutar
t0, ts, t1, tc = algoritmo_cristian()
graficar_sincronizacion(t0, ts, t1, tc)
