from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI(title="API de Predicción de Gastos Operativos")

# Carga de modelos
modelo_rf = joblib.load("modelo_random_forest_pipeline.joblib")
modelo_xgb = joblib.load("modelo_xgboost_pipeline.joblib")

# Entrada de datos
class DatosEntrada(BaseModel):
    anio_id: int
    mes_id: int
    salario_basico: float
    canasta_basica_familiar: float
    iva: int
    valor_activos_fijos: float
    numero_activos_fijos: int
    empleados_menor_basico: int
    empleados_basico_mil: int
    empleados_mil_dos_mil: int
    empleados_dos_mil_cuatro_mil: int
    jubilados_menor_basico: int
    ingreso_operacional: float
    ingreso_no_operacional: float
    gasto_operativo: str

# Ruta de predicción
@app.post("/predecir/")
def predecir_gasto(data: DatosEntrada):
    entrada_df = pd.DataFrame([data.dict()])

    # Predicciones
    pred_rf = modelo_rf.predict(entrada_df)[0]
    pred_xgb = modelo_xgb.predict(entrada_df)[0]

    # Convertir a tipo float de Python
    pred_rf = float(pred_rf)
    pred_xgb = float(pred_xgb)
    promedio = (pred_rf + pred_xgb) / 2

    return {
        "prediccion_random_forest": round(pred_rf, 2),
        "prediccion_xgboost": round(pred_xgb, 2),
        "promedio_predicciones": round(promedio, 2)
    }
