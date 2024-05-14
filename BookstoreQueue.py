from collections import deque

def enter_bookstore(queue):
    num_clients = int(input("Enter number of persons to buy: "))
    i = 1
    while i <= num_clients:
        client_name = input(f"Enter the name of person {i}: ")
        queue.append(client_name)
        i += 1
    print("\nInitial queue:", queue)

def buy_book(queue):
    if not queue:
        print("No one is in the queue.")
        return False
    current_client = queue.popleft()
    print(f"{current_client} is buying books.")
    return True

def main():
    queue = deque()
    while True:
        print("\nWhat would you like to do?")
        print("1. Enter the bookstore")
        print("2. Buy a book")
        print("3. Leave")
        choice = input("Enter your choice: ")
        if choice == "1":
            enter_bookstore(queue)
        elif choice == "2":
            while buy_book(queue):
                pass
        elif choice == "3":
            print("\nExiting the bookstore.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
