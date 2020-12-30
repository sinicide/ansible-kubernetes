# ansible-kubernetes
Ansible Playbook for a Green Field Deployment Kubernetes Cluster (k3s or k8s)

# TODO
- [x] Role for setting up OS
- [x] Role for installing and configuring Container Runtime
- [x] Role for installing kubernetes (k8s)
- [x] Role for installing kubernetes (k3s)
- [x] Role for deploying kubernetes cluster (controlplane)
- [x] Role for installing CNI (Calico)
- [ ] Role for installing MetalLb
- [x] Role for deploying kubernetes worker node
- [ ] Grab the kube config file and store locally?
- [x] Role for Creating External ETCD datastore
- [ ] Add containerd as alternate container runtime
- [ ] Add Upgrade playbook for k8s

# Prerequisite
Please note, you'll need to supply your own SSL Certificates

# Running Playbook
```
ansible-playbook all.yaml -i hosts.yaml
```

## Notes:
- Create solution for backing up/restoring etcd?
- When deploying controlplanes and worker nodes, if I'm adding new worker nodes, I don't want to re-create the controlplane node, I don't want to re-generate the token. So I add logic for this or add a separate role/tasks for adding worker.
- What about replacing a server node?
- Ensure that I can create HA for kubernetes control plane nodes.