# Projeto Simples: Conversor de Temperatura

def celsius_para_fahrenheit(celsius):
    """
    Converte uma temperatura de Celsius para Fahrenheit.
    Fórmula: (C * 9/5) + 32
    """
    # Note: Usamos 9.0/5 para garantir que a divisão retorne um número decimal (float).
    fahrenheit = (celsius * 9.0/5) + 32
    return fahrenheit

# --- Exemplos de Uso (Prática) ---

# 1. Temperatura ambiente: 25°C
temp_ambiente_celsius = 25
ambiente_fahrenheit = celsius_para_fahrenheit(temp_ambiente_celsius)
print(f"{temp_ambiente_celsius}°C é equivalente a {ambiente_fahrenheit}°F")

# 2. Temperatura de congelamento: 0°C
temp_congelamento_celsius = 0
congelamento_fahrenheit = celsius_para_fahrenheit(temp_congelamento_celsius)
print(f"{temp_congelamento_celsius}°C é equivalente a {congelamento_fahrenheit}°F")

# 3. Temperatura de ebulição da água: 100°C
temp_ebulicao_celsius = 100
ebulicao_fahrenheit = celsius_para_fahrenheit(temp_ebulicao_celsius)
print(f"{temp_ebulicao_celsius}°C é equivalente a {ebulicao_fahrenheit}°F")
