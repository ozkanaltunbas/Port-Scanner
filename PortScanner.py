import socket
import threading

def port_scan(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open !")
            sock.close()
    except KeyboardInterrupt:
        print("The scan has been stopped by user")
        exit()
    except socket.gaierror:
        print("Hostname doesn't resolve")
    except socket.error:
        print("Connection failed")
    exit()


def main():
    try:
        target_ip = input(" Enter target IP: ")
        port_range = input("Enter port range (exp. 1-1000): ")


        start_port, end_port = map(int, port_range.split('-'))

        print(f"Tarama başliyor: {target_ip}")

        for port in range(start_port, end_port + 1):
            threading.Thread(target=port_scan, args=(target_ip, port)).start()
    except ValueError:
        print("Invalid Input")
        main()

if __name__ == "__main__":
    main()