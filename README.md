# ansible-kubernetes
Ansible Playbook for Deploying Base Kubernetes Cluster

# TODO
- [ ] Role for setting up OS
- [ ] Role for installing and configuring Container Runtime
- [ ] Role for installing kubernetes (k8s)
- [ ] Role for installing kubernetes (k3s)
- [ ] Role for deploying kubernetes cluster (controlplane)
- [ ] Role for installing CNI (Calico)
- [ ] Role for installing MetalLb
- [ ] Role for deploying kubernetes worker node

# Running Playbook
```
ansible-playbook all.yaml -i hosts.yaml
```

## Notes:
- Need to determine way to backup etcd