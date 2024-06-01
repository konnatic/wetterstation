import time
import RPi.GPIO as GPIO

# GPIO initialisieren
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Messparameter
measure_duration = 10  # Messdauer in Sekunden
num_measurements = 20  # Anzahl der Messungen

# 20 Messungen durchfuehren
for i in range(num_measurements):
    # Variablen initialisieren
    last_state = GPIO.LOW
    impulses = 0
    measure_time = time.time()

    # Zaehlvorgang starten
    while time.time() - measure_time < measure_duration:
        state = GPIO.input(8)
        if state != last_state:
            last_state = state
            if state == GPIO.HIGH:
                impulses += 1

    # Ergebnis der aktuellen Messung ausgeben
    print(f"Messung {i+1}: In 10 Sekunden wurden {impulses} Impulse gelesen")

# GPIO aufraeumen
GPIO.cleanup()



