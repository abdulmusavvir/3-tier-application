curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
helm create 3-tier-architecture-project // This will create the helm chart
# make the changes in values.yaml file and add our manifest files into template folder
# helm install <ReleaseName> <Chart that we created using helm create command i.e  3-tier-architecture-project  > This will install the helm chart
helm install applicationrelease3 DAY-6/3-tier-architecture-project --values DAY-6/3-tier-architecture-project/values
# During installation if we want to display some message to user then we have to create NOTES.txt inside the template folder

# Chart.yaml will have the basic information about the helm chart


# we can have helmfile sync command that will execute both helm install and helm uninstall command. 
helmfile is an utility that we need to install in our system. after that we have to create a helmfile.yaml

releases:
  - name: helloworld // release name 
    chart: ./helloworld // chart name (chart is in local)
    installed: true // to install and if we want to uninstall it the we heve to make the value to false

then execute helmfile sync command

if chart is git then we have to install the git utility 

repositories:
  - name: helloworld
    url: git+https://github.com/rahulwagh/helmchart@helloworld?ref=master&sparse=0
releases:
  - name: helloworld
    chart: helloworld/helloworld
    installed: false 



multiple charts

releases:
  - name: helloworld1
    chart: ./helloworld1
    installed: true
  - name: helloworld2
    chart: ./helloworld2
    installed: true

