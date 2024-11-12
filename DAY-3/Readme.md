### Here I have added HPA, PV, PVC ###

## To use HPA we need to install metrics server ##

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# After that we will be creating HPA #

HPA won't work on Deamonset
If ResourceLimit is not define then pod will get terminate frequently

# Command #
kubectl autoscale deployment backend-deployment --min=1 --max=6 --cpu-percent=80

## Create PV, PVC and then add PV name in deployment (containerpath->volume->pvc->pv) ##

