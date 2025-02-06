import os
import subprocess
import time

def scan_wifi():
    print("Сканирование Wi-Fi сетей...")
    result = subprocess.run(['termux-wifi-scaninfo'], stdout=subprocess.PIPE)
    networks = result.stdout.decode('utf-8').splitlines()
    for i, network in enumerate(networks):
        print(f"{i + 1}. {network}")
    return networks

def select_network(networks):
    choice = input("Выберите сеть (введите номер) или 'all' для выбора всех сетей: ")
    if choice.lower() == 'all':
        return networks
    else:
        return [networks[int(choice) - 1]]

def send_requests(network):
    count = int(input("Введите количество запросов: "))
    for i in range(count):
        print(f"Отправка запроса {i + 1} на {network}...")
        time.sleep(1)  # Имитация отправки запроса

def main():
    while True:
        print("1. Сканировать Wi-Fi сети")
        print("2. Выход")
        choice = input("Выберите опцию: ")
        if choice == '1':
            networks = scan_wifi()
            selected_networks = select_network(networks)
            for network in selected_networks:
                send_requests(network)
        elif choice == '2':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
