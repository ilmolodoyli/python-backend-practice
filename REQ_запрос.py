import requests
ip_list = ["8.8.8.8", "1.1.1.1"]
def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    print(data)
    return f"IP: {ip_address} Владелец {data['country']}, статус {data['status']}"
with open("ip_report.txt", "w", encoding="utf-8") as file:
    for ip in ip_list:
        result = get_ip_info(ip)
        print(result)
        file.write(result + "\n")