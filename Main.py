import socket
import threading

def open_sip_connection(ip_address, port=5060):
    try:
        # Create a socket object
        sip_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the IP address and port
        sip_socket.connect((ip_address, port))

        print(f"Successfully connected to {ip_address}:{port}")

        # Close the connection
        sip_socket.close()

    except Exception as e:
        print(f"Failed to connect: {e}")

def open_multiple_connections(ip_address, port, num_connections):
    threads = []
    for _ in range(num_connections):
        thread = threading.Thread(target=open_sip_connection, args=(ip_address, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Replace with the target IP address
target_ip = "192.168.1.1"
target_port = 5060
number_of_connections = 5

open_multiple_connections(target_ip, target_port, number_of_connections)
