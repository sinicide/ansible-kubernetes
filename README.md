# ansible-kubernetes
Ansible Playbook for a Green Field Deployment Kubernetes Cluster

## ToDo List
- [x] Role for setting up OS
- [x] Role for installing and configuring Container Runtime (containerd)
- [x] Role for installing kubernetes
- [x] Role for deploying kubernetes cluster (controlplanes)
- [x] Role for deploying kubernetes worker node
- [x] Role for deploying CNI (Calico)
- [x] Role for deploying MetalLb
- [x] Role for deploying Longhorn Storage
- [x] Fetch kube config from control plane
- [x] Add Upgrade playbook for k8s
- [x] Add role for deploying ArgoCD
- [ ] Create ArgoCD Notifications Task
- [X] Create Kubernetes Metrics Role

## Wish list
- Deploy Kubernetes Dashboard
- Deploy External ETCD
- Add TLS configuration for argocd
- Properly configure kubelet for TLS

## Running Initial Install
The below runs everything, you can also specify specific tags
```
ansible-playbook -i hosts.yaml all.yaml
```

## Running Cluster Info Checker
This will check current kubelet version as well as current CNI (Calico), MetalLB and Longhorn
```
ansible-playbook -i hosts.yaml check_info.yaml
```

## Running Upgrade
The below will upgrade kubernetes.
```
ansible-playbook -i hosts.yaml upgrade_k8s.yaml
```