# 절차지향 프로그래밍(Procedural Programming)

# 데이터 초기화
balance = 0

# 입금 함수
def deposit(amount):
    global balance
    balance += amount

# 출금 함수
def withdraw(amount):
    global balance
    balance -= amount

# 잔액 조회 함수
def check_balance():
    global balance
    return balance

# 테스트
deposit(50000)
withdraw(20000)
print("잔액: ", check_balance())

# 객체 지향 프로그래맹(Object-Oriented Programming)

class BankUtil:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def check_balance(self):
        return self.balance

# 계좌 객체 생성
my_account = BankUtil(5000000000)
my_account.withdraw(1000000000)
my_account.deposit(2000000000)
print("잔액: ", my_account.check_balance())


