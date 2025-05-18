import os
from time import sleep

def limpar_tela():
    os.system(
        "Cls"
        )

def pausa():
    print(
        "Calculando..."
        )
    sleep(1.5)

def voltar_ao_menu():
    opcao = input("" \
    "\nDeseja voltar ao menu principal? (S/N): "
    ).strip().lower()
    return opcao == 's'

def soma():
    print(
        "\n-=-=-=- CALCULADORA DE SOMA -=-=-=-\n"
        )
    total = 0
    while True:
        total += float(input(
            "Digite um número para somar: "
            ))
        if input(
            "Deseja adicionar mais um número? (S/N): "
            ).strip().lower() == 'n':
            break
    pausa()
    print(
        f"\nO resultado da soma é: {total}\n"
        )

def subtracao():
    print(
        "\n-=-=- CALCULADORA DE SUBTRAÇÃO -=-=-\n"
        )
    resultado = float(input(
        "Digite o primeiro número: "
        ))
    while input(
        "Deseja subtrair outro número? (S/N): "
        ).strip().lower() == "s":
        resultado -= float(input(
            "Digite o número que será subtraído: "
            ))
    pausa()
    print(
        f"\nO resultado da subtração é: {resultado}\n"
        )

def multiplicacao():
    print(
        "\n-=-=- CALCULADORA DE MULTIPLICAÇÃO -=-=-\n"
        )
    resultado = float(input(
        "Digite o primeiro número: "
        ))
    while input(
        "Deseja multiplicar outro número? (S/N): "
        ).strip().lower() == 's':
        resultado *= float(input("Digite o próximo número: "))
    pausa()
    print(
        f"\nO resultado da multiplicação é: {resultado}\n"
        )

def divisao():
    print(
        "\n-=-=- CALCULADORA DE DIVISÃO -=-=-\n"
        )
    resultado = float(input(
        "Digite o primeiro número: "
        ))
    while input(
        "Deseja dividir por outro número? (S/N): "
        ).strip().lower() == 's':
        divisor = float(input(
            "Digite o divisor: "
            ))
        if divisor != 0:
            resultado /= divisor
        else:
            print(
                "Erro: divisão por zero!"
                )
    pausa()
    print(
        f"\nO resultado da divisão é: {resultado}\n"
        )

def exponenciacao():
    print(
        "\n-=-=- CALCULADORA DE EXPONENCIAÇÃO -=-=-\n"
        )
    base = float(input(
        "Digite a base: "
        ))
    expoente = float(input(
        "Digite o expoente: "
        ))
    resultado = base ** expoente
    pausa()
    print(
        f"O resultado da exponenciação é: {resultado}"
        )

def tabuada():
    print(
        "\n-=-=- TABUADA -=-=-\n"
        )
    numero = int(input(
        "Digite um número: "
        ))
    for i in range(1, 11):
        print(
            f"{numero} x {i} = {numero * i}"
            )

def calcular_porcentagem():
    print(
        "\n-=-=- CALCULADORA DE PORCENTAGEM -=-=-\n"
        )
    print(
        "[1] - Apenas porcentagem\n[2] - Desconto\n[3] - Juros"
        )
    tipo = int(input(
        "Escolha: "
        ))

    if tipo == 1:
        valor = float(input(
            "Digite o valor: "
            ))
        percentual = float(input(
            "Digite a porcentagem: "
            ))
        resultado = (percentual / 100) * valor
        pausa()
        print(
            f"{percentual}% de {valor} é {resultado}"
            )

    elif tipo == 2:
        valor = float(input(
            "Digite o valor do produto: "
            ))
        taxa = float(input(
            "Digite a taxa (%): "
            )) / 100
        tempo = int(input(
            "Digite o tempo (meses): "
            ))
        juros = valor * taxa * tempo
        total = valor + juros
        pausa()
        print(
            f"Juros: R${juros:.2f}, Total: R${total:.2f}"
            )

    elif tipo == 3:
        valor = float(input(
            "Digite o valor original: "
            ))
        taxa = float(input(
            "Digite a taxa de desconto (%): "
            )) / 100
        tempo = int(input(
            "Digite o tempo (meses): "
            ))
        desconto = valor * taxa * tempo
        final = valor - desconto
        pausa()
        print(
            f"Desconto: R${desconto:.2f}, Valor com desconto: R${final:.2f}"
            )

def potencia():
    print(
        "\n-=-=- POTENCIAÇÃO -=-=-\n"
        )
    base = float(input(
        "Digite a base: "
        ))
    expoente = float(input(
        "Digite o expoente: "
        ))
    resultado = base ** expoente
    pausa()
    print(
        f"Resultado: {resultado}"
        )

def area():
    print(
        "\n-=-=- CÁLCULO DE ÁREA -=-=-\n"
        )
    print(
        "[1] Triângulo\n[2] Quadrado\n[3] Trapézio\n[4] Círculo\n[5] Losango"
        )
    opcao = int(input(
        "Escolha: "
        ))

    if opcao == 1:
        base = float(input(
            "Base: "
            ))
        altura = float(input(
            "Altura: "
            ))
        print(
            f"Área do triângulo: {(base * altura) / 2}"
            )

    elif opcao == 2:
        lado = float(input(
            "Lado do quadrado: "
            ))
        print(
            f"Área do quadrado: {lado ** 2}"
            )

    elif opcao == 3:
        b_menor = float(input(
            "Base menor: "
            ))
        b_maior = float(input(
            "Base maior: "
            ))
        altura = float(input(
            "Altura: "
            ))
        print(
            f"Área do trapézio: {((b_maior + b_menor) * altura) / 2}"
            )

    elif opcao == 4:
        raio = float(input(
            "Raio: "
            ))
        print(
            f"Área do círculo: {3.14 * (raio ** 2):.2f}"
            )

    elif opcao == 5:
        d_menor = float(input(
            "Diagonal menor: "
            ))
        d_maior = float(input(
            "Diagonal maior: "
            ))
        print(
            f"Área do losango: {(d_maior * d_menor) / 2}"
            )

def radiciacao():
    print(
        "\n-=-=- RADICIAÇÃO -=-=-\n"
        )
    numero = float(input(
        "Digite o número: "
        ))
    indice = float(input(
        "Digite o índice (ex: 2 para raiz quadrada): "
        ))
    raiz = numero ** (1 / indice)
    pausa()
    print(
        f"A raiz {indice} de {numero} é: {raiz}"
        )

while True:
    limpar_tela()
    print(
        "\n===== CALCULADORA CIENTÍFICA ====="
        )
    print(
        "[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Exponenciação\n[6] Tabuada\n[7] Porcentagem\n[8] Potenciação\n[9] Área\n[10] Radiciação\n[0] Sair"
        )

    try:
        escolha = int(input(
            "Escolha uma opção: "
            ))
        limpar_tela()

        if escolha == 0:
            break
        elif escolha == 1:
            soma()
        elif escolha == 2:
            subtracao()
        elif escolha == 3:
            multiplicacao()
        elif escolha == 4:
            divisao()
        elif escolha == 5:
            exponenciacao()
        elif escolha == 6:
            tabuada()
        elif escolha == 7:
            calcular_porcentagem()
        elif escolha == 8:
            potencia()
        elif escolha == 9:
            area()
        elif escolha == 10:
            radiciacao()
        else:
            print(
                "Opção inválida!"
                )

        if not voltar_ao_menu():
            break

    except ValueError:
        print(
            "Por favor, digite uma opção válida."
            )