class FilterModule(object):
    def filters(self):
        return {
            'k3s_exec_arg_builder': self.k3s_exec_arg_builder
        }

# self can be passed in here to reference other modules?
    def k3s_exec_arg_builder(self, k3s_exec_type, k3s_cri_arg, apiserver_address, apiserver_port, advertise_address, advertise_port, tls_san, cluster_cidr, service_cidr, cluster_core_dns, cluster_domain):
        # initial empty list
        k3s_exec_arg = [ ]

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

        # return joined string
        return ' '.join(k3s_exec_arg)