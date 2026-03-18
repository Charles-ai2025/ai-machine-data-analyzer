from src.load_data import load_data
from src.analyze import plot_data
from src.anomaly import detect_anomaly

def main():
    df = load_data("data/sample_data.csv")
    
    print("=== Data Preview ===")
    print(df.head())

    plot_data(df)

    anomalies = detect_anomaly(df)
    print("\n=== Detected Anomalies ===")
    print(anomalies)

if __name__ == "__main__":
    main()