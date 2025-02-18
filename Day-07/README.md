helm repo add prometheus-community
https://prometheus-community.github.io/helm-charts

helm repo update

kubectl create ns monitoring

helm install monitoring prometheus-community/kube-prometheus-stack -n
monitoring -f ./custom\\\_kube\\\_prometheus\\\_stack.yml

kubectl port-forward \--address 0.0.0.0 service/prometheus-operated -n
monitoring 9090:9090

kubectl port-forward \--address 0.0.0.0 service/monitoring-grafana -n
monitoring 8080:80 (localhostport:serviceport)

Grafana UI: password is prom-operator

kubectl port-forward \--address 0.0.0.0 service/alertmanager-operated -n
monitoring 9093:9093

once we provision prometheus, grafana then automatically prometheus will
install kube-state-metrics and node-export as service in cluster\'s
monitor service. we can curl the service inside every node curl
:/metrics, also curl :/metrics

Service Discovery: basically define from where prometheus will scrape
the metrics (automatically detect the service/pod if any pod or service
gets added in the cluster)

Exporter: define what metrics prometheus will scrape

In production we create the servicemonitor or podmonitor

serviceMonitor: It is used to configure prometheus to scrape metrics at
service level

podMonitor: It is used to configure prometheus to scrape the metrics at
pod level
