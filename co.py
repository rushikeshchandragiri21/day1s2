import socket
import threading

class Coordinator:
    def __init__(self):
        self.num_participants = 0
        self.participants = []
        self.responses = {}

    def start_server(self):
        self.num_participants = int(input("Enter the number of participants: "))

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind(('localhost', 5000))
            server_socket.listen()
            print("Coordinator running and waiting for participants to join...")

            while len(self.participants) < self.num_participants:
                client_socket, addr = server_socket.accept()
                print(f"Participant connected from {addr}")
                self.participants.append(client_socket)

            print("All participants have joined.")
            self.send_prepare_message()

    def send_prepare_message(self):
        print("Sending PREPARE message to all participants...")
        for participant in self.participants:
            participant.sendall(b'PREPARE')
        self.wait_for_prepare_responses()

    def wait_for_prepare_responses(self):
        all_prepared = True
        for participant in self.participants:
            response = participant.recv(1024).decode()
            if response != 'yes':
                all_prepared = False

        if all_prepared:
            print("All participants are prepared. Sending COMMIT message...")
            self.send_commit_message()
        else:
            print("At least one participant is not prepared. Sending ABORT message...")
            self.send_abort_message()

    def send_commit_message(self):
        for participant in self.participants:
            participant.sendall(b'COMMIT')
        self.wait_for_commit_responses()

    def send_abort_message(self):
        for participant in self.participants:
            participant.sendall(b'ABORT')
        self.end_transaction(False)

    def wait_for_commit_responses(self):
        all_committed = True
        for participant in self.participants:
            response = participant.recv(1024).decode()
            if response != 'yes':
                all_committed = False

        if all_committed:
            self.end_transaction(True)
        else:
            self.end_transaction(False)

    def end_transaction(self, commit_success):
        decision = "COMMIT SUCCESSFUL" if commit_success else "TRANSACTION ABORTED"
        final_message = f"Transaction committed successfully.\nEnd of transaction. {decision}. Logs are recorded."
        for participant in self.participants:
            participant.sendall(final_message.encode())
        print(final_message)

if __name__ == "__main__":
    coordinator = Coordinator()
    coordinator.start_server()
