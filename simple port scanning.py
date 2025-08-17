import socket
import sys

def scan_target(target):
    print(f"[+] Scanning target: {target}")
    for port in range(1, 1025):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open")
            sock.close()
        except KeyboardInterrupt:
            print("\n[!] Scan stopped.")
            sys.exit()
        except socket.error:
            print("[!] Host unreachable.")
            sys.exit()

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    scan_target(target_ip)