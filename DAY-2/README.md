# lab setup needs a 3 node cluster setup, I'm using Kind cluster.
https://kind.sigs.k8s.io/docs/user/quick-start/#installation

kind create cluster --name three-tier-application --config three-node-cluster-setup.yaml
kubectl create secret generic backend-secret --from-literal=DB_USER='root' --from-literal=DB_PASSWORD='root' --from-literal=DB_HOST='172.21.147.236' --from-literal=DB_NAME='simple_app'
kubectl port-forward --address 0.0.0.0 svc/backend-service 30070:7000
this is for backend
kubectl port-forward --address 0.0.0.0 svc/backend-service 30080:80
this is for frontend
