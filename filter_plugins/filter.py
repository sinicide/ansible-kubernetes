class FilterModule(object):
    def filters(self):
        return {
            'k3s_exec_arg_builder': self.k3s_exec_arg_builder,
            'etcd_bootstrap_builder': self.etcd_bootstrap_builder,
            'etcd_k3s_endpoint_builder': self.etcd_k3s_endpoint_builder
        }

# self can be passed in here to reference other modules?
    def k3s_exec_arg_builder(self, k3s_exec_type, k3s_cri_arg, apiserver_address, apiserver_port, advertise_address, advertise_port, tls_san, cluster_cidr, service_cidr, cluster_core_dns, cluster_domain, k3s_server_coredns_enabled, k3s_server_servicelb_enabled, k3s_server_traefik_enabled, k3s_server_local_storage_enabled, k3s_server_metrics_server_enabled):
        # initial empty list
        k3s_exec_arg = [ ]
        k3s_components = [ ]

        k3s_exec_arg.append( str(k3s_exec_type) + str(k3s_cri_arg) )

        if apiserver_address:
            k3s_exec_arg.append( "--bind-address " + str(apiserver_address) )

        if apiserver_port:
            k3s_exec_arg.append( "--https-listen-port " + str(apiserver_port) )
        
        if advertise_address:
            k3s_exec_arg.append( "--advertise-address " + str(advertise_address) )

        if advertise_port:
            k3s_exec_arg.append( "--advertise-port " + str(advertise_port) )

        if tls_san:
            k3s_exec_arg.append( "--tls-san " + str(tls_san) )

        if cluster_cidr:
            k3s_exec_arg.append( "--cluster-cidr " + str(cluster_cidr) )

        if service_cidr:
            k3s_exec_arg.append( "--service-cidr " + str(service_cidr) )

        if cluster_core_dns:
            k3s_exec_arg.append( "--cluster-dns " + str(cluster_core_dns) )

        if cluster_domain:
            k3s_exec_arg.append( "--cluster-domain " + str(cluster_domain) )

        # forming the disabled parameter
        if not k3s_server_coredns_enabled:
            k3s_components.append( "coredns" )
        
        if not k3s_server_servicelb_enabled:
            k3s_components.append( "servicelb" )
        
        if not k3s_server_traefik_enabled:
            k3s_components.append( "traefik" )
        
        if not k3s_server_local_storage_enabled:
            k3s_components.append( "local-storage" )
        
        if not k3s_server_metrics_server_enabled:
            k3s_components.append( "metrics-server" )

        if len(k3s_components) > 0:
            k3s_exec_arg.append( "--disable " + ','.join(k3s_components) )

        # return joined string
        return ' '.join(k3s_exec_arg)
    
# string builder for bootstrap etcd nodes
    def etcd_bootstrap_builder(self, blankignore, controlplane_hostnames, controlplane_ips, worker_hostnames, worker_ips, peer_port, ssl_enabled):
        
        ch = controlplane_hostnames.split(',')
        cpi = controlplane_ips.split(',')
        wh = worker_hostnames.split(',')
        whi = worker_ips.split(',')
        etcd_bootstrap_list = [ ]

        if ssl_enabled:
            protocol = "https://"
        else:
            protocol = "http://"

        # control plane nodes
        for index in range(len(ch)):
            etcd_bootstrap_list.append( ch[index] + "=" + protocol + cpi[index] + ":" + str(peer_port) )

        # worker nodes
        for index in range(len(wh)):
            etcd_bootstrap_list.append( wh[index] + "=" + protocol + whi[index] + ":" + str(peer_port) )

        return ','.join(etcd_bootstrap_list)

# etcd endpoint builder to supply to k3s instance for datastore reference
    def etcd_k3s_endpoint_builder(self, blankignore, cp_fqdn, worker_fqdn, client_port, ssl_enabled):
        
        ch = cp_fqdn.split(',')
        wh = worker_fqdn.split(',')
        etcd_k3s_endpoints = [ ]

        if ssl_enabled:
            protocol = "https://"
        else:
            protocol = "http://"

        # control plane nodes
        for index in range(len(ch)):
            etcd_k3s_endpoints.append( protocol + ch[index] + ":" + str(client_port) )

        # worker nodes
        for index in range(len(wh)):
            etcd_k3s_endpoints.append( protocol + wh[index] + ":" + str(client_port) )

        return ','.join(etcd_k3s_endpoints)