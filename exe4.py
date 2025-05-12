def calculate_percentages(revenue_by_state):
    total = sum(revenue_by_state.values())
    print(f"Total monthly revenue: R$ {total / 100:.2f}\n")

    for state, value in revenue_by_state.items():
        percentage = (value / total) * 100
        print(f"{state}: R$ {value / 100:.2f} → {percentage:.2f}%")


##Usando dinheiro como inteiro por segurança contra arredondamento
if __name__ == "__main__":
    revenue_by_state = {
        "SP": 6783643,   # R$67,836.43
        "RJ": 3667866,   # R$36,678.66
        "MG": 2922988,   # R$29,229.88
        "ES": 2716548,   # R$27,165.48
        "Others": 1984953  # R$19,849.53
    }

    calculate_percentages(revenue_by_state)