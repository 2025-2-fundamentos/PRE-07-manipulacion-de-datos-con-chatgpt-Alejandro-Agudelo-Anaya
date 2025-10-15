import pandas as pd
import matplotlib.pyplot as plt
import os

# === 1. Cargar los datos ===
drivers = pd.read_csv("files/input/drivers.csv")
timesheet = pd.read_csv("files/input/timesheet.csv")

# === 2. Calcular el promedio de horas y millas por conductor ===
avg_timesheet = (
    timesheet.groupby("driverId")[["hours-logged", "miles-logged"]]
    .mean()
    .reset_index()
)

# === 3. Unir datos de conductores con los promedios ===
summary = pd.merge(drivers, avg_timesheet, on="driverId", how="inner")

# === 4. Crear carpeta de salida si no existe ===
os.makedirs("files/output", exist_ok=True)
os.makedirs("files/plots", exist_ok=True)

# === 5. Guardar resumen como CSV ===
summary.to_csv("files/output/summary.csv", index=False)

# === 6. Crear gráfico de los 10 conductores con más millas promedio ===
top10 = summary.nlargest(10, "miles-logged")

plt.figure(figsize=(10, 6))
plt.bar(top10["name"], top10["miles-logged"], color="steelblue")
plt.xticks(rotation=45, ha="right")
plt.xlabel("Conductor")
plt.ylabel("Millas promedio")
plt.title("Top 10 conductores por millas promedio")
plt.tight_layout()

# === 7. Guardar el gráfico ===
plt.savefig("files/plots/top10_drivers.png")
plt.close()
import pandas as pd
import matplotlib.pyplot as plt
import os

# === 1. Cargar los datos ===
drivers = pd.read_csv("files/input/drivers.csv")
timesheet = pd.read_csv("files/input/timesheet.csv")

# === 2. Calcular el promedio de horas y millas por conductor ===
avg_timesheet = (
    timesheet.groupby("driverId")[["hours-logged", "miles-logged"]]
    .mean()
    .reset_index()
)

# === 3. Unir datos de conductores con los promedios ===
summary = pd.merge(drivers, avg_timesheet, on="driverId", how="inner")

# === 4. Crear carpeta de salida si no existe ===
os.makedirs("files/output", exist_ok=True)
os.makedirs("files/plots", exist_ok=True)

# === 5. Guardar resumen como CSV ===
summary.to_csv("files/output/summary.csv", index=False)

# === 6. Crear gráfico de los 10 conductores con más millas promedio ===
top10 = summary.nlargest(10, "miles-logged")

plt.figure(figsize=(10, 6))
plt.bar(top10["name"], top10["miles-logged"], color="steelblue")
plt.xticks(rotation=45, ha="right")
plt.xlabel("Conductor")
plt.ylabel("Millas promedio")
plt.title("Top 10 conductores por millas promedio")
plt.tight_layout()

# === 7. Guardar el gráfico ===
plt.savefig("files/plots/top10_drivers.png")
plt.close()
