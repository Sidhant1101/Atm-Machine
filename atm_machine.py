class AtmMachine:
    """Simple command-line ATM implementation."""

    # instance variable is a variable in which there are different values for different objects
    def __init__(self):
        self.__pin = ""
        self.__amount = 0.0
        self.manu()

    def menu(self):
        while True:
            user_input = input(
                "\n1. Create PIN\n2. Deposit\n3. Withdraw\n"
                "4. Check balance\n5. Exit\nChoose an option: "
            )
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Goodbye.")
                break
            else:
                print("Invalid option.")

    # Preserve the original misspelled method name for callers using it.
    def manu(self):
        self.menu()

    def create_pin(self):
        pin = input("Enter a 4-digit PIN: ")
        if pin.isdigit() and len(pin) == 4:
            self.__pin = pin
            print("PIN created successfully.")
        else:
            print("PIN must contain exactly 4 digits.")

    def deposit(self):
        if not self.__pin:
            print("Create a PIN first.")
            return

        temp = input("Enter your PIN: ")
        if temp != self.__pin:
            print("Invalid PIN.")
            return

        try:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                self.__amount += amount
                print(f"Deposited {amount:.2f}.")
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Enter a valid amount.")

    def withdraw(self):
        if not self.__pin:
            print("Create a PIN first.")
            return

        temp = input("Enter your PIN: ")
        if temp != self.__pin:
            print("Invalid PIN.")
            return

        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Amount must be positive.")
            elif amount > self.__amount:
                print("Insufficient balance.")
            else:
                self.__amount -= amount
                print(f"Withdrew {amount:.2f}.")
        except ValueError:
            print("Enter a valid amount.")

    def check_balance(self):
        print(f"Current balance: {self.__amount:.2f}")


sbi = AtmMachine()

