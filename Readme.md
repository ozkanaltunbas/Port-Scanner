Port Scanner
This is a simple port scanner written in Python. It uses threading to scan multiple ports concurrently, making it efficient for scanning a range of ports on a target IP address.

Features:

Scans a range of ports on a target IP address.
Uses threading to perform the scan concurrently, improving performance.
Handles common errors gracefully (e.g., invalid IP address, connection errors).
Requirements
Python 3.x

Usage:

Clone or download this repository.
git clone https://github.com/ozkanaltunbas/Port-Scanner.git
Navigate to the directory containing the script.
Run the script using Python.

Example Usage:

$ python port_scanner.py
Enter target IP: 192.168.1.1
Enter port range (exp. 1-1000): 1-100

Port 22 is open !
Port 80 is open !
