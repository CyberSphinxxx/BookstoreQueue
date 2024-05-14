class Queue:
    def __init__(self):
        self.items = []

    def add_to_queue(self, item):
        self.items.insert(0, item)

    def remove_from_queue(self):
        if not self.is_queue_empty():
            return self.items.pop()
        return None

    def is_queue_empty(self):
        return len(self.items) == 0

    def queue_size(self):
        return len(self.items)


class Bookstore:
    def __init__(self):
        self.queue = Queue()

    def come_inside(self, client_name):
        print(f"{client_name} comes into the bookstore.")
        self.queue.add_to_queue(client_name)

    def buy_a_book(self):
        if not self.queue.is_queue_empty():
            client_name = self.queue.remove_from_queue()
            print(f"{client_name} buys a book.")
        else:
            print("There's no one in the store to buy a book.")


def main():
    bookstore = Bookstore()

    while True:
        print("\nWhat would you like to do?")
        print("1. Enter the bookstore")
        print("2. Buy a book")
        print("3. Leave")

        choice = input("\nWhat would you like to do? Enter the number: ")

        if choice == "1":
            client_name = input("What's your name? ")
            bookstore.come_inside(client_name)

        elif choice == "2":
            bookstore.buy_a_book()

        elif choice == "3":
            print("You are now leaving. Goodbye!")
            break

        else:
            print("Oops! That's not a valid option. Please try again.")


if __name__ == "__main__":
    main()
