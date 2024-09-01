# Auto-Scaling Data Pipeline
Dynamically scales Spark on Kubernetes based on Prometheus metrics.

## Monitoring
Metrics exposed via Prometheus:
- `spark_anomalies`: Number of anomalous transactions
- `spark_throughput`: Processing rate (records/sec)
