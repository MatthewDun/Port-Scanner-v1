import socket

def scan_ports(target, start_port=1, end_port=1024):
    open_ports = []

    for port in range(start_port, end_port + 1):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()


    return open_ports

# Example usage:
if __name__ == "__main__":
    target_ip = input("Enter target IP: ").strip()
    scan_ports(target_ip, 1, 100)