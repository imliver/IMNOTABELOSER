import os
import subprocess
import time
import platform

def scan_wifi():
    print("Сканирование Wi-Fi сетей...")

    system_name = platform.system()

    if system_name == "Windows":
        # Используем команду Windows для отображения доступных сетей
        result = subprocess.run(['netsh', 'wlan', 'show', 'networks'], stdout=subprocess.PIPE, encoding='utf-8')
    elif system_name == "Linux":
        # Для Android через Termux используем стандартную команду
        result = subprocess.run(['iwlist', 'wlan0', 'scan'], stdout=subprocess.PIPE, encoding='utf-8')
    else:
        print("Эта ОС не поддерживается.")
        return []

    networks = result.stdout.splitlines()
    for i, network in enumerate(networks[:10]):  # Ограничиваем до 10 строк, чтобы не перегружать вывод
        print(f"{i + 1}. {network}")

    return networks

def select_network(networks):
    choice = input("Выберите сеть (введите номер) или 'all' для выбора всех сетей: ")
    if choice.lower() == 'all':
        return networks
    elif choice.isdigit() and 1 <= int(choice) <= len(networks):
        return [networks[int(choice) - 1]]
    else:
        print("Неверный ввод, попробуйте снова.")
        return select_network(networks)

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
            if networks:
                selected_networks = select_network(networks)
                for network in selected_networks:
                    send_requests(network)
        elif choice == '2':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
