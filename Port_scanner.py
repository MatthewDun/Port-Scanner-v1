import socket

def scan_ports(target, start_port=50, end_port=90):
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            print(f"Scanning port {port}")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error as err:
            print(f"Socket error on port {port}: {err}")
            break

    return open_ports
