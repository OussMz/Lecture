devices = [ ("192.168.1.10", [22, 80, 443]),
("192.168.1.11", [21, 22, 80]), ("192.168.1.12", [23,
80, 3389]) ]

risky_ports = [21, 23, 3389]
risks_num = 0
print("Scanning network devices...")

for ip, ports in devices:
    for port in ports:
        if port in risky_ports:
            risks_num += 1
            print(f"{ip} has risky port {port} open!")
        
print(f"Complte: {risks_num} security risks found.")