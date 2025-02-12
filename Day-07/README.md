### Installing Prometheus, Grafana and alert manager ###

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
kubectl create ns monitoring
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring -f ./custom_kube_prometheus_stack.yml
kubectl port-forward --address 0.0.0.0 service/prometheus-operated -n monitoring 9090:9090
kubectl port-forward --address 0.0.0.0 service/monitoring-grafana -n monitoring 8080:80
Grafana UI: password is prom-operator
kubectl port-forward--address 0.0.0.0  service/alertmanager-operated -n monitoring 9093:9093
