from random import randint

### Gerador de CPF Válidos ###
numero = str(randint(100000000, 999999999))

new_cpf = numero
reverse = 10
total = 0

for index in range(19):
    if index > 8:               # Primeiro indice que vai de 0 a 9
        index -= 9              # 9 primeiros digitos do CPF

    total += int(new_cpf[index]) * reverse  # Valor total da multiplicação do algoritmo, contador reverso e cpf

    reverse -= 1                    # Diminui em 1 o contador reverso
    if reverse < 2:
        reverse = 11
        digit = 11 - (total % 11)
        
        if digit > 9:
            digit = 0
        total = 0               # Zera o total
        new_cpf += str(digit)   # Une/Liga o digito gerado com o novo CPF

print(f'Geramos um CPF válido para você: {new_cpf}')