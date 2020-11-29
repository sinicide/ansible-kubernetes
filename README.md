# ansible-kubernetes
Ansible Playbook for a Green Field Deployment Kubernetes Cluster (k3s or k8s)

# TODO
- [ ] Role for setting up OS
- [ ] Role for installing and configuring Container Runtime
- [ ] Role for installing kubernetes (k8s)
- [ ] Role for installing kubernetes (k3s)
- [ ] Role for deploying kubernetes cluster (controlplane)
- [ ] Role for installing CNI (Calico)
- [ ] Role for installing MetalLb
- [ ] Role for deploying kubernetes worker node
- [ ] Grab the kube config file and store locally?

# Running Playbook
```
ansible-playbook all.yaml -i hosts.yaml
```

## Notes:
- Need to determine way to backup etcd
- When deploying controlplanes and worker nodes, if I'm adding new worker nodes, I don't want to re-create the controlplane node, I don't want to re-generate the token. So I add logic for this or add a separate role/tasks for adding worker.
- What about replacing a server node?
- Need to think about default configs for k3s and k8s.