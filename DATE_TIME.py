from datetime import datetime
servers = [
    {"ip": "192.168.1.10", "cpu": 45, "ram": 60},
    {"ip": "192.168.1.11", "cpu": 95, "ram": 80},
    {"ip": "192.168.1.12", "cpu": 50, "ram": 96},
    {"ip": "192.168.1.13", "cpu": 30, "ram": 40}
]

def get_alerts(server_list):
    bad_aps = [] 
    for server in server_list:
        if server["cpu"] >90 or server["ram"] > 90:
            bad_aps.append(server["ip"])
    return bad_aps
print(get_alerts(servers))

bad_ips = get_alerts(servers)

with open ("alerts.txt", "a") as file:
    for ipp in bad_ips:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{now}] Cервер {ipp} перегружен!\n")
