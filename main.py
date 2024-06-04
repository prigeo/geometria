def exibir_menu():
    print('1 - Área do círculo.')
    print('2 - Área do triângulo.')
    print('3 - Área do trapézio.')
    print('4 - Sair do programa.')

def calcular_circulo(r):
    area_circulo = 3.14*r**2
    return area_circulo

def calcular_triangulo(base, altura):
    area_triangulo = (base*altura)/2
    return area_triangulo

def calcular_trapezio(base_menor, base_maior, altura_trapezio):
    area_trapezio = ((base_menor+base_maior)*altura_trapezio/2)
    return area_trapezio

while True:
    exibir_menu()
    opcao = input('Opção desejada: ')

    match opcao:
        case '1':
            print('Área do círculo é π*r²')
            r = int(input('Informe o valor do raio: '))
            print(f'Área do círculo: {calcular_circulo(r)}.\n')
        case '2':
            print('Área do trinângulo é a = (b*a)/2')
            base = int(input('Informe o valor da base do triângulo: '))
            altura = int(input('Informe o valor da altura do triângulo: '))
            print(f'Área do retângulo: {calcular_triangulo(base, altura)}.\n')
            continue
        case '3':
            print('Área do trapézio é a = ((base1+base2)*altura/2)')
            base_menor = int(input('Informe o valor da base menor: '))
            base_maior = int(input('Informe o valor da base maior: '))
            altura_trapezio = int(input('Informe a altura do trapézio: '))
            print(f'A área do trapézio: {calcular_trapezio(base_menor, base_maior, altura_trapezio)}.\n')
            continue
        case '4':
            break
        case _:
            print('Opção inválida.')
            continue