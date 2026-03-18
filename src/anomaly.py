from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomaly(df):
    # 使用 cycle_time, temperature, pressure 做異常偵測
    features = df[['cycle_time', 'temperature', 'pressure']]
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(features)
    df['anomaly'] = model.predict(features)
    
    # IsolationForest 輸出 1 = 正常, -1 = 異常
    anomalies = df[df['anomaly'] == -1]
    return anomalies