#Autor: Belyeud Prado

import pandas as pd
import numpy as np
import os

np.random.seed(42)

def generar_dataframe(n):
    return pd.DataFrame({
        'edad': np.random.randint(18, 80, size=n),
        'temperatura': np.round(np.random.normal(36.5, 0.5, size=n), 1),  # en °C
        'estatura': np.round(np.random.normal(1.7, 0.1, size=n), 2),      # en metros
        'peso': np.round(np.random.normal(70, 15, size=n), 1),            # en kg
        'presion_sistolica': np.random.randint(100, 150, size=n),
        'presion_diastolica': np.random.randint(60, 100, size=n),
        'glucosa': np.round(np.random.normal(90, 15, size=n), 1),         # mg/dL
        'frecuencia_cardiaca': np.random.randint(60, 100, size=n),
        'oxigeno_sangre': np.round(np.random.normal(98, 1, size=n), 1),   # en %
        'genero': np.random.choice(['M', 'F'], size=n)
    })

# DataFrame old y new
old_data = generar_dataframe(500)
new_data = generar_dataframe(500)

#Se agrega la desviación
new_data['glucosa'] += np.random.normal(10, 5, size=500)



#from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

output_dir = "/app/reporte" if os.environ.get("DOCKER_ENV") else "../reporte"
os.makedirs(output_dir, exist_ok=True)

# Generar y guardar el reporte
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=old_data, current_data=new_data)
report.save_html(os.path.join(output_dir, "data_drift_report.html"))
