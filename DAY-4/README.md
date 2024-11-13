### Setting up Ingress Controller ###

curl -O https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
or else take the Custom Resource file from this repository
kubectl apply -f deploy.yaml




## After that execute kubectl apply -f deploy.yaml, This will create the necessary ingress controller inside ingress-nginx namespaces ##

## Check ingress-nginx-controller deployment and ingress-nginx-controller  in ingress-nginx namespace. the If ingress-nginx-controller is throwing FailedScheduling then execute kubectl get deployment ingress-nginx-controller -n ingress-nginx -o yaml and remove the nodeSelector from spec.template.spec ##



## Once your ingress-nginx-controller in ingress-nginx namespace is ready then deploy the ingress Resource file ##
# Here I am using path based routing and domain is localhost #

### In WSL make sure that backend service and frontend service is using running on localhost using port-forward ###

## kubectl port-forward --address 0.0.0.0 svc/frontend-service 30080:80 ##
## kubectl port-forward --address 0.0.0.0 svc/backend-service 30070:7000 ##
## sudo ufw allow 8081 ##
## kubectl port-forward --address 0.0.0.0  -n ingress-nginx svc/ingress-nginx-controller 8081:80 --> for http ##
## kubectl port-forward --address 0.0.0.0  -n ingress-nginx svc/ingress-nginx-controller 8081:443 --> for https ##


### Imp Note ###
The nginx.ingress.kubernetes.io/rewrite-target annotation is used to modify the URL path when it is forwarded from the Ingress controller to the backend service. This annotation helps manage situations where the path in the incoming request (e.g., /api/users) doesn't match the path expected by the backend service (e.g., /users).

How the nginx.ingress.kubernetes.io/rewrite-target Works:
When you use this annotation, it rewrites the URL path before forwarding the request to the backend. This can be useful if the Ingress routes traffic with a certain path, but your backend expects a different path format.

Example:
If you have a service configured to handle /api/users, but the path from the incoming request is /api/*, the rewrite rule can strip or modify the /api part of the URL.

Example Ingress configuration:
yaml
Copy code
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: api-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: "localhost"
      http:
        paths:
        - path: /api
          pathType: Prefix
          backend:
            service:
              name: backend-service
              port:
                number: 7000
In this example:

If the request is http://localhost/api/users, the nginx.ingress.kubernetes.io/rewrite-target: / will strip the /api part and forward the request to http://backend-service:7000/users.
If your backend service doesn't expect /api in the URL, you can strip that prefix using the rewrite-target. If you want to retain it, don't apply the rewrite rule.

Common Use Cases:
Stripping a Prefix: If the incoming request has a path like /api/users, but your backend expects /users, you would use:

yaml
Copy code
nginx.ingress.kubernetes.io/rewrite-target: /
Replacing or Modifying Paths: If you need to add or replace a part of the path (e.g., replace /api with /v1), you can use:

yaml
Copy code
nginx.ingress.kubernetes.io/rewrite-target: /v1
No Rewrite: If you want the path to remain as is, simply omit the rewrite rule or use an empty target:

yaml
Copy code
nginx.ingress.kubernetes.io/rewrite-target: ""
Troubleshooting:
If you're still getting 404 errors, double-check both your backend path definitions and Ingress annotations to ensure consistency in the path structure.
Also, ensure that the NGINX Ingress controller is configured and functioning correctly.
For more information on the nginx.ingress.kubernetes.io/rewrite-target and other related Ingress annotations, you can refer to the official NGINX Ingress Controller documentation: NGINX Ingress Annotations.






