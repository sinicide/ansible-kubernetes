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
- [ ] Add Upgrade playbook for k8s
- [x] Add role for deploying ArgoCD

## Wish list
- Deploy Kubernetes Dashboard
- Deploy External ETCD

## Running Playbook
The below runs everything, you can also specify specific tags
```
ansible-playbook -i hosts.yaml all.yaml
```