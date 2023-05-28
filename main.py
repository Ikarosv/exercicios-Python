menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

class Account:
  WITHDRAW_LIMIT = 500.0
  WITHDRAW_LIMIT_DAY = 3

  def __init__(self, balance=0.0):
    self.balance = balance # Saldo
    self.statement = [] # Histórico de transações

  def deposit(self, value: float):
    if value > 0:
      self.balance += value
      self.statement.append(f'Depositado: R$ {value}')
    else:
      print('Operação falhou! O valor informado é inválido.')

  def withdraw(self, value: float):
    if self.WITHDRAW_LIMIT_DAY <= 0:
      print('Operação falhou! Número de saques diários excedido.')
      return

    if value > self.WITHDRAW_LIMIT:
      print('Operação falhou! O valor de saque excede o limite.')
      return

    if value <= self.balance:
      self.balance -= value
      self.statement.append(f'Sacado: R$ {value}')
      self.WITHDRAW_LIMIT_DAY -= 1
    else:
      print('Operação falhou! Você não tem saldo suficiente.')
      return

  def extract(self):
    # print(f'Extrato da conta {self.statement}')
    for item in self.statement:
      print(item)
    print(f'Saldo atual: R$ {self.balance:.2f}')

  def __str__(self):
    return f'Saldo: R$ {self.balance}'

account = Account()

while True:
  option = input(menu)
  if option not in ['d','s','e','q']:
    print('Opção inválida! Tente novamente.')
    continue

  if option == 'q':
    break

  if option == 'd':
    value = float(input('Informe o valor do depósito: R$ '))
    account.deposit(value)

  elif option == 's':
    if account.WITHDRAW_LIMIT_DAY <= 0:
      print('Operação falhou! Número de saques diários excedido.')
      continue
    value = float(input('Informe o valor do saque: R$ '))
    account.withdraw(value)

  elif option == 'e':
    account.extract()
