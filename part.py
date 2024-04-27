import socket

def perform_transaction():
    # Simulated transaction: Printing numbers 1 to 100
    print("Performing transaction: Printing numbers from 1 to 100.")
    for i in range(1, 101):
        print(i, end=' ')
    print("\nTransaction performed successfully.")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 5000))
        print("Connected to coordinator.")

        while True:
            data = s.recv(1024).decode()
            if data.startswith('PREPARE'):
                print("Received PREPARE message from coordinator.")
                decision = input("ACK_Are you prepared to commit? (yes/no): ").strip().lower()
                if decision == 'yes':
                    perform_transaction()
                s.sendall(decision.encode())
            elif data.startswith('COMMIT'):
                print("Received COMMIT message from coordinator.")
                decision = input("ACK_Are you ready to commit? (yes/no): ").strip().lower()
                s.sendall(decision.encode())
            elif 'ABORT' in data or 'COMMIT SUCCESSFUL' in data or 'TRANSACTION aborted' in data:
                print(data)
                break

if __name__ == "__main__":
    main()
