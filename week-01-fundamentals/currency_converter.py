print("EUR to BRL Converter")

euro_amount = float(input("Enter the amount in euros: "))
exchange_rate = float(input("Enter the exchange rate EUR to BRL: "))

brl_amount = euro_amount * exchange_rate

print(f"{euro_amount:.2f} EUR = {brl_amount:.2f} BRL")