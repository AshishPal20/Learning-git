#   BANK MANAGEMENT SYSTEM — Full OOP Project in Python

from abc import ABC, abstractmethod    # for Abstraction
from datetime import datetime          # for timestamps
import uuid                            # for unique account IDs


class BankAccount(ABC):
    """
    Abstract base class for all account types.
    Enforces that every account MUST implement deposit(),
    withdraw(), and get_account_type().
    """

    # Class variable shared by ALL instances — tracks total accounts opened
    total_accounts = 0

    def __init__(self, owner_name: str, initial_deposit: float):
        # Encapsulation: private attributes (__ prefix) are hidden from outside
        self.__account_id = str(uuid.uuid4())[:8].upper()  # e.g. "A3F9B12C"
        self.__owner_name = owner_name
        self.__balance = 0.0
        self.__transactions = []   # list of transaction history
        self.__created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__is_active = True

        BankAccount.total_accounts += 1  # increment class-level counter

        # Make the first deposit via the public method (not directly)
        if initial_deposit > 0:
            self.deposit(initial_deposit, note="Initial deposit")

    # Abstract Methods (must be overridden by child classes)

    @abstractmethod
    def deposit(self, amount: float, note: str = "") -> None:
        pass          # MUST be implemented by child

    @abstractmethod
    def withdraw(self, amount: float, note: str = "") -> None:
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        pass

    # Protected helper (single underscore = internal use, not private)

    def _add_transaction(self, txn_type: str, amount: float, note: str):
        """Logs a transaction into the history list."""
        record = {
            "id": f"TXN{len(self.__transactions)+1:04d}",
            "type": txn_type,
            "amount": amount,
            "balance_after": self.__balance,
            "note": note,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.__transactions.append(record)

    def _set_balance(self, new_balance: float):
        """Protected setter — child classes can update balance through this."""
        self.__balance = round(new_balance, 2)

    def _get_balance(self) -> float:
        """Protected getter — child classes read balance through this."""
        return self.__balance

    # Public Getters (Encapsulation: controlled access to private data)

    @property
    def account_id(self) -> str:
        return self.__account_id

    @property
    def owner_name(self) -> str:
        return self.__owner_name

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def is_active(self) -> bool:
        return self.__is_active

    @property
    def created_at(self) -> str:
        return self.__created_at

    def deactivate(self):
        """Close the account."""
        self.__is_active = False
        print(f"Account {self.__account_id} has been deactivated.")

    def get_transaction_history(self):
        """Returns a copy of transaction history (not the original list)."""
        return list(self.__transactions)

    def get_statement(self):
        """Prints a formatted account statement."""
        print("\n" + "=" * 55)
        print(f"  ACCOUNT STATEMENT — {self.get_account_type()}")
        print("=" * 55)
        print(f"  Account ID   : {self.__account_id}")
        print(f"  Owner        : {self.__owner_name}")
        print(f"  Opened On    : {self.__created_at}")
        print(f"  Status       : {'Active ✓' if self.__is_active else 'Inactive ✗'}")
        print(f"  Balance      : ₹{self.__balance:,.2f}")
        print("-" * 55)
        print(f"  {'TXN ID':<10} {'Type':<10} {'Amount':>12} {'Balance':>12}  Note")
        print("-" * 55)
        for txn in self.__transactions:
            sign = "+" if txn["type"] == "CREDIT" else "-"
            print(
                f"  {txn['id']:<10} {txn['type']:<10} "
                f"{sign}₹{txn['amount']:>9,.2f}  "
                f"₹{txn['balance_after']:>9,.2f}  {txn['note']}"
            )
        print("=" * 55 + "\n")

    def __str__(self):
        """String representation of the object (used when you print it)."""
        return (
            f"[{self.get_account_type()}] ID: {self.__account_id} | "
            f"Owner: {self.__owner_name} | Balance: ₹{self.__balance:,.2f}"
        )

    def __repr__(self):
        return f"BankAccount(id={self.__account_id}, owner={self.__owner_name})"


# 2. SAVINGS ACCOUNT  →  Inheritance + Polymorphism
#    Inherits from BankAccount and provides its OWN version
#    of deposit() and withdraw() (method overriding).

class SavingsAccount(BankAccount):
    """
    A savings account with a minimum balance rule
    and monthly interest calculation.
    """

    INTEREST_RATE = 0.04          # 4% annual interest
    MINIMUM_BALANCE = 1000.0      # can't go below ₹1,000

    def __init__(self, owner_name: str, initial_deposit: float):
        print(f"\n✅ Opening Savings Account for {owner_name}...")
        super().__init__(owner_name, initial_deposit)  # calls BankAccount.__init__

    def get_account_type(self) -> str:
        return "SAVINGS ACCOUNT"

    def deposit(self, amount: float, note: str = "Deposit") -> None:
        """Overrides abstract deposit() — credits money into the account."""
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return
        self._set_balance(self._get_balance() + amount)
        self._add_transaction("CREDIT", amount, note)
        print(f"  ✅ ₹{amount:,.2f} deposited. New balance: ₹{self.balance:,.2f}")

    def withdraw(self, amount: float, note: str = "Withdrawal") -> None:
        """Overrides abstract withdraw() — debits money, checks minimum balance."""
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return
        if self._get_balance() - amount < SavingsAccount.MINIMUM_BALANCE:
            print(
                f"❌ Cannot withdraw ₹{amount:,.2f}. "
                f"Minimum balance of ₹{SavingsAccount.MINIMUM_BALANCE:,.2f} must be maintained."
            )
            return
        self._set_balance(self._get_balance() - amount)
        self._add_transaction("DEBIT", amount, note)
        print(f" 💸 ₹{amount:,.2f} withdrawn. New balance: ₹{self.balance:,.2f}")

    def apply_interest(self) -> None:
        """
        Applies monthly interest (annual rate / 12).
        This method is specific to SavingsAccount — not in the base class.
        """
        monthly_interest = round(self._get_balance() * (self.INTEREST_RATE / 12), 2)
        self._set_balance(self._get_balance() + monthly_interest)
        self._add_transaction("CREDIT", monthly_interest, "Monthly Interest")
        print(f" 💵 Interest of ₹{monthly_interest:,.2f} applied. Balance: ₹{self.balance:,.2f}")


# 3. CURRENT ACCOUNT  →  Inheritance + Polymorphism
#    Different rules: overdraft allowed up to a limit,
#    no minimum balance, no interest.


class CurrentAccount(BankAccount):
    """
    A current account for businesses.
    Supports overdraft — you can withdraw more than your balance
    up to a defined overdraft limit.
    """

    def __init__(self, owner_name: str, initial_deposit: float, overdraft_limit: float = 10000.0):
        self.__overdraft_limit = overdraft_limit   # private to CurrentAccount
        print(f"\n✅ Opening Current Account for {owner_name}...")
        super().__init__(owner_name, initial_deposit)

    def get_account_type(self) -> str:
        return "CURRENT ACCOUNT"

    def deposit(self, amount: float, note: str = "Deposit") -> None:
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return
        self._set_balance(self._get_balance() + amount)
        self._add_transaction("CREDIT", amount, note)
        print(f"  ✅ ₹{amount:,.2f} deposited. New balance: ₹{self.balance:,.2f}")

    def withdraw(self, amount: float, note: str = "Withdrawal") -> None:
        """
        Allows overdraft — balance can go negative up to the overdraft limit.
        Polymorphism in action: same method name, DIFFERENT behaviour.
        """
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return
        if self._get_balance() - amount < -self.__overdraft_limit:
            print(
                f"❌ Exceeds overdraft limit of ₹{self.__overdraft_limit:,.2f}. "
                f"Maximum you can withdraw: ₹{self._get_balance() + self.__overdraft_limit:,.2f}"
            )
            return
        self._set_balance(self._get_balance() - amount)
        self._add_transaction("DEBIT", amount, note)
        print(f" 💸 ₹{amount:,.2f} withdrawn. New balance: ₹{self.balance:,.2f}")

    @property
    def overdraft_limit(self) -> float:
        return self.__overdraft_limit


# 4. FIXED DEPOSIT ACCOUNT  →  Inheritance + Extra Features
#    Locked for a term. Cannot withdraw until maturity.

class FixedDepositAccount(BankAccount):
    """
    A fixed deposit account where money is locked for a term.
    Withdrawal before maturity is not allowed.
    Demonstrates adding domain-specific logic in a child class.
    """

    INTEREST_RATE = 0.07   # 7% annual

    def __init__(self, owner_name: str, principal: float, term_months: int):
        self.__term_months = term_months
        self.__is_matured = False
        self.__maturity_amount = round(
            principal * (1 + self.INTEREST_RATE * term_months / 12), 2
        )
        print(f"\n✅ Opening Fixed Deposit for {owner_name} ({term_months} months)...")
        print(f"   Maturity amount: ₹{self.__maturity_amount:,.2f}")
        super().__init__(owner_name, principal)

    def get_account_type(self) -> str:
        return "FIXED DEPOSIT"

    def deposit(self, amount: float, note: str = "FD Principal") -> None:
        """FD only accepts one deposit at creation."""
        if self._get_balance() > 0 and "Initial" not in note:
            print("❌ Fixed Deposit cannot accept additional deposits.")
            return
        self._set_balance(self._get_balance() + amount)
        self._add_transaction("CREDIT", amount, note)
        print(f"  ✅ FD principal of ₹{amount:,.2f} locked in.")

    def withdraw(self, amount: float, note: str = "FD Withdrawal") -> None:
        """Cannot withdraw unless matured."""
        if not self.__is_matured:
            print("❌ FD has not matured yet. Cannot withdraw.")
            return
        if amount > self.balance:
            print(f"❌ Amount exceeds balance of ₹{self.balance:,.2f}.")
            return
        self._set_balance(self._get_balance() - amount)
        self._add_transaction("DEBIT", amount, note)
        print(f"  ✅ ₹{amount:,.2f} withdrawn from matured FD.")

    def mature(self):
        """
        Simulates the FD reaching maturity.
        In a real system, this would be triggered by a scheduler.
        """
        interest_earned = self.__maturity_amount - self._get_balance()
        self._set_balance(self.__maturity_amount)
        self._add_transaction("CREDIT", interest_earned, f"FD Maturity Interest ({self.__term_months}M)")
        self.__is_matured = True
        print(f"\n  🎉 FD matured! ₹{interest_earned:,.2f} interest credited. "
              f"Total: ₹{self.balance:,.2f}")

    @property
    def maturity_amount(self) -> float:
        return self.__maturity_amount

    @property
    def is_matured(self) -> bool:
        return self.__is_matured


# 5. BANK CLASS  →  Composition (Bank HAS accounts)
#    This is a manager/controller class. It holds a collection
#    of accounts and provides operations like transfer,
#    search, and summary.

class Bank:
    """
    Represents the bank itself.
    Uses Composition: Bank contains a list of BankAccount objects.
    Demonstrates: working with polymorphic objects in a collection.
    """

    def __init__(self, bank_name: str):
        self.__bank_name = bank_name
        self.__accounts: dict[str, BankAccount] = {}   # account_id → account object

    @property
    def bank_name(self) -> str:
        return self.__bank_name

    def add_account(self, account: BankAccount) -> None:
        """Register an account with the bank."""
        self.__accounts[account.account_id] = account
        print(f"  🏦 Account {account.account_id} registered with {self.__bank_name}.")

    def get_account(self, account_id: str) -> BankAccount | None:
        """Fetch an account by ID."""
        account = self.__accounts.get(account_id.upper())
        if not account:
            print(f"❌ No account found with ID: {account_id}")
        return account

    def transfer(self, from_id: str, to_id: str, amount: float) -> None:
        """
        Transfer money between two accounts.
        This works for ANY account type because deposit/withdraw
        are defined on the base class — Polymorphism at work.
        """
        sender = self.get_account(from_id)
        receiver = self.get_account(to_id)

        if not sender or not receiver:
            return
        if not sender.is_active or not receiver.is_active:
            print("❌ One or both accounts are inactive.")
            return

        print(f"\n  💸 Transferring ₹{amount:,.2f} from {from_id} → {to_id}...")
        sender.withdraw(amount, note=f"Transfer to {to_id}")
        receiver.deposit(amount, note=f"Transfer from {from_id}")
        print("  ✅ Transfer complete.")

    def search_by_owner(self, name: str) -> list[BankAccount]:
        """Find all accounts belonging to a name (case-insensitive)."""
        results = [
            acc for acc in self.__accounts.values()
            if name.lower() in acc.owner_name.lower()
        ]
        if not results:
            print(f"❌ No accounts found for '{name}'.")
        return results

    def bank_summary(self) -> None:
        """Print an overview of all accounts in the bank."""
        print("\n" + "=" * 60)
        print(f"  {self.__bank_name.upper()} — SUMMARY")
        print("=" * 60)
        print(f"  Total Accounts Opened (ever): {BankAccount.total_accounts}")
        print(f"  Currently Registered        : {len(self.__accounts)}")

        total_deposits = sum(
            acc.balance for acc in self.__accounts.values() if acc.is_active
        )
        print(f"  Total Funds Held            : ₹{total_deposits:,.2f}")
        print("-" * 60)
        for acc in self.__accounts.values():
            status = "Active" if acc.is_active else "Inactive"
            print(f"  {acc.account_id}  {acc.get_account_type():<22} "
                  f"₹{acc.balance:>12,.2f}  [{status}]")
        print("=" * 60 + "\n")


# 6. MAIN — putting it all together

if __name__ == "__main__":

    print("\n" )
    print("  BANK MANAGEMENT SYSTEM — Python OOP Demo")

    # Create the bank
    my_bank = Bank("Bank Of Maharashtra")

    # Create accounts (Inheritance: different classes, same interface)
    aman_savings = SavingsAccount("Aman Pal", 5000)
    avantika_current = CurrentAccount("Avantika", 15000, overdraft_limit=20000)
    anay_fd      = FixedDepositAccount("Anay Kumar", 50000, term_months=6)

    # Register accounts with the bank
    my_bank.add_account(aman_savings)
    my_bank.add_account(avantika_current)
    my_bank.add_account(anay_fd)

    # Savings Account operations
    print("\n Aman's Savings Account")
    aman_savings.deposit(3000, note="Salary")
    aman_savings.withdraw(1500, note="Rent")
    aman_savings.withdraw(6600, note="Should fail — below min balance")
    aman_savings.apply_interest()

    # Current Account operations (overdraft)
    print("\n Avantika's Current Account ")
    avantika_current.deposit(5000, note="Client payment")
    avantika_current.withdraw(18000, note="Bulk purchase")    # goes into overdraft
    avantika_current.withdraw(15000, note="Should fail — exceeds overdraft limit")

    # Fixed Deposit 
    print("\n Anay's Fixed Deposit")
    anay_fd.withdraw(1000)      # Should fail — not matured
    anay_fd.mature()            # Simulate maturity
    anay_fd.withdraw(10000)     # Now allowed

    #  Transfer between accounts 
    my_bank.transfer(aman_savings.account_id, avantika_current.account_id, 2000)

    # ── Polymorphism demo: iterate over different account types ──
    print("\n Polymorphism: Calling get_account_type() on each account ──")
    all_accounts = [aman_savings, avantika_current, anay_fd]
    for account in all_accounts:
        # Same method call, different output depending on which class it is
        print(f"  {account}")   # calls __str__ on each

    #  Print statements 
    aman_savings.get_statement()
    avantika_current.get_statement()
    anay_fd.get_statement()

    #  Bank-wide summary 
    my_bank.bank_summary()

    #  Search 
    print(" Search by owner name ")
    results = my_bank.search_by_owner("anay")
    for r in results:
        print(f"  Found: {r}")