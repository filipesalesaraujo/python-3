lockdown = False

grana = 30

status = 'Em casa' if lockdown or grana <= 100 else 'Uhu'

print(f'O status é: {status}')