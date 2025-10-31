from ip_utils import ip_to_binary, get_network_prefix

class Router:
    def __init__(self, routes):
        self.forwarding_table = self.build_forwarding_table(routes)

    def build_forwarding_table(self, routes):
        table = []
        for cidr, link in routes:
            binary_prefix = get_network_prefix(cidr)
            table.append((binary_prefix, link))
        table.sort(key=lambda x: len(x[0]), reverse=True)
        return table

    def route_packet(self, dest_ip: str) -> str:
        binary_ip = ip_to_binary(dest_ip)
        for prefix, link in self.forwarding_table:
            if binary_ip.startswith(prefix):
                return link
        return "Default Gateway"
