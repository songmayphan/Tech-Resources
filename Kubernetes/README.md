# Kubernetes 

- Kubernetes simplifies our docker containers. 

## Kubepod 

 - A grouping of 1 or n containers. The containers are inside the pod.
 - typically one container per pod

## Worker Nodes 
 - Virtual machines

## Get started with Kubernetes with Linode

1) Set up worker nodes on Linode

2) Download Kubernetes on your Kali machine 

`https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
`

3) Make it exceutable 

`chmod +x kubectl`

4) Move to our path

`sudo mv ./kubectl /usr/local/bin/kubectl`


5) Copied the YAML file from Linode console 

6) Make a new yaml file in our Kali machine 

`nano kubeconfig.yaml`

7) paste the content into the file, save and exit 

8) Export the yaml file

`export KUBECONFIG=kubeconfig.yaml`

## Check nodes

`kubectl get nodes`

more info about our cluster : `kubectl cluster-info`


## Pods
### Create a pod

`kubectl run <name> -- image<image link>`

### Check pods description

`kubectl describe pods`


## Deployment

`kubectl apply -f <yaml file>`

In this yaml file, we can specify the number of replica we want to deploy. The cmd is for the master to launch


To show our deployments `kubectl get deployments`

we can add or delete pods if we edit the deployment.
The master will always ensure that the load are balanced between the pods. Each pod has their own internal IP address; 

We can also add an Auto scaling policy to our workers (if utilization is >75%, add more servers)

## Expose our pods 

### Deploy a service

Edit our manifest file to add our load balancer 

We can specify the URL we want to redirect our users to in the load balancer

check our services: `kubectl get serivces`
