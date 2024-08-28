from prometheus_client import start_http_server, Gauge

metrics = {
    "anomalies": Gauge("spark_anomalies", "Detected anomalies"),
    "throughput": Gauge("spark_throughput", "Records processed/sec")
}

def export_metrics(anomaly_count, throughput):
    metrics["anomalies"].set(anomaly_count)
    metrics["throughput"].set(throughput)
