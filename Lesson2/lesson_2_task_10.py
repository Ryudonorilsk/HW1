def bank(X, Y):    
    balance = X      
    interest_rate = 0.10    
    
    for _ in range(Y):        
        balance += balance * interest_rate        
        interest_rate *= 1.10
    
    return balance

X = float(input("Введите сумму вклада: "))
Y = int(input("Введите срок вклада в годах: "))

total_balance = bank(X, Y)
print("Сумма на счету спустя", Y, "лет:", total_balance)