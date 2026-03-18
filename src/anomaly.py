from sklearn.ensemble import IsolationForest

def detect_anomaly(df):
    features = df[['cycle_time', 'temperature', 'pressure']]
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(features)
    df['anomaly'] = model.predict(features)
    anomalies = df[df['anomaly'] == -1]
    return anomalies