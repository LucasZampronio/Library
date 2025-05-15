class Biblioteca:

    def __init__(self):
        self.lista_filiais = []
        self.carregar_livros_do_arquivo('dados.txt')

## Definindo Abertura arquivo e leitura------------------------------------------------------------
        
    def carregar_livros_do_arquivo(self,caminho):
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivotxt:
                for linha in arquivotxt:
                    linha = linha.strip()
                    dadoslivro = linha.split(',')
                    codigo = int(dadoslivro[1])
                    ano = int(dadoslivro[4])
                    valor = float(dadoslivro[5])
                    estoque = int(dadoslivro[6])
                    livro = Livro(dadoslivro[0].strip(), codigo, dadoslivro[2].strip(),dadoslivro[3].strip(),ano,valor,estoque)
                    self.listaLivro.append(livro)
        except FileNotFoundError:
            print(f'Arquivo {caminho} não encontrado.')
        except Exception as e:
            print(f'Erro ao carregar o arquivo: {e}')

    def salvar_arquivo(self):

        arquivotxt = open('dados.txt', 'a', encoding='utf-8')
        for livro in self.livrosalvar:
            dados = f'{livro.titulo},{livro.codigo},{livro.editora},{livro.area},{livro.ano},{livro.valor},{livro.estoque}\n'
            arquivotxt.writelines(dados)
        arquivotxt.close()

## Definindo Funções filiais------------------------------------------------------------
    def cadastrar_filial(self):
        codigo = (input("Digite o codigo da filial: "))
        nome = (input("Digite o nome da filial: "))
        endereco = input("Digite o endereco da filial: ")
        contato = input("Digite o contato da filial: ")
        filianovo = Filial(codigo,nome,endereco,contato)
        self.lista_filiais.append(filianovo)
        print(f'Filial {filianovo.nome} cadastrada com sucesso!')

    def listar_filiais(self):
        codigofilial = input('Digite o código da filial: ')
        filial = next((f for f in self.lista_filiais if f.codigo == codigofilial), None)
        if filial:
            print(f'>>>>> Cod#{filial.codigo} \n Nome: {filial.nome} \n Endereço: {filial.endereco} \n Contato: {filial.contato}')
            print('---------------------------------')
        else:
            print(f'Filial com código {codigofilial} não encontrada.')
            print('---------------------------------')

## Definindo A Interface ------------------------------------------------------------
    def menu_salvar(self):
        salvar = int(input('Deseja salvar as alterações?\n 1 - Sim \n 0 - Não'))
        if salvar == 1:
            self.salvar_arquivo()
            print('')
            print('Salvado com sucesso!')
        else:
            print('')
            print('Alterações não salvas, sistema encerrado!')

    def menu(self):
        while True:
            print('---------------------------------')
            selection = int(input(
                f' 1 – Cadastrar novo livro \n 2 – Listar livros \n 3 – Buscar livros por nome \n 4 – Buscar livros por categoria \n 5 – Buscar livros por preço \n 6 – Busca por quantidade em estoque \n 7 – Valor total no estoque \n 8 – Cadastrar Filial \n 9 - Listagem estoque da filial \n 10 – Buscar filial \n 11 - Buscar livro pelo codigo em filiais \n 0 – Encerrar atividades \n ---------------------------------\n'))

            if selection == 1:
                #biblioteca.cadastrar_livro()
                biblioteca.cadastrar_livro()
                print()
                print('---------------------------------')
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                
                if opcao == 0:
                    biblioteca.menu_salvar()
                    break
            
            elif selection == 2:
                biblioteca.listar_estoque_filial()
                #biblioteca.listar_livro()
                print(f'\n')
                print('Esses são nossos livros!')
                print('---------------------------------')
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                if opcao == 0:
                    biblioteca.menu_salvar()
                    break
            elif selection == 3:
                biblioteca.buscar_nome()
                print('---------------------------------')
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                if opcao == 0:
                    biblioteca.menu_salvar()
                    break
            elif selection == 4:
                biblioteca.buscar_categoria()
                print('---------------------------------')
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                if opcao == 0:
                    biblioteca.menu_salvar()
                    break
            elif selection == 5:
                biblioteca.buscar_preco()
                print('---------------------------------')
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                if opcao == 0:
                    biblioteca.menu_salvar()
                    break
            elif selection == 6:
                biblioteca.buscar_estoque()
                print('---------------------------------')
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                if opcao == 0:
                    biblioteca.menu_salvar()
                    break
            elif selection == 7:
                biblioteca.valortotal_estoque()
                print('---------------------------------')
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                if opcao == 0:
                    biblioteca.menu_salvar()
                    break
            elif selection == 0:
                print('---------------------------------')
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                if opcao == 0:
                    biblioteca.menu_salvar()
                    break
            elif selection == 8:
                biblioteca.cadastrar_filial()
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                if opcao == 0:
                    biblioteca.menu_salvar()
                    break

            elif selection == 9:
                biblioteca.listar_estoque_filial()
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                if opcao == 0:
                    biblioteca.menu_salvar()
                    break

            elif selection == 10:
                biblioteca.listar_filiais()
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                if opcao == 0:
                    biblioteca.menu_salvar()
                    break
            elif selection == 11:
                biblioteca.buscar_codigo_filial()
                print('---------------------------------')
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                if opcao == 0:
                    biblioteca.menu
                    break



    def buscar_estoque(self):
        numeroestoque = int(input(f'Digite o numero minimo de estoque que deseja buscar: '))
        codigofilial = int(input('Digite o código da filial que deseja buscar: '))
        filial = next((f for f in self.lista_filiais if f.codigo == codigofilial), None)
        if filial:
            for livro in filial.listalivros:
                if livro.estoque >= numeroestoque:
                    print(f'>>>>> Cod#{livro.codigo} \n Titulo/Editora: {livro.titulo}/{livro.editora} \n Categoria: {livro.area} \n Valor: R$ {livro.valor} \n Estoque: {livro.estoque} unidades  \n Valor total em estoque: R$ {livro.estoque * livro.valor}')
        else:
            print(f'Filial com código {codigofilial} não encontrada.')
            print('---------------------------------')

    def buscar_preco(self):
        codigofilial = input('Digite o código da filial: ')
        filial = next((f for f in self.lista_filiais if f.codigo == codigofilial), None)
        if filial:
            preco = float(input(f'Digite o preço limite que deseja buscar: '))
            for livro in filial.listalivros:
                if livro.valor <= preco:
                     print(f'>>>>> Cod#{livro.codigo} \n Titulo/Editora: {livro.titulo}/{livro.editora} \n Categoria: {livro.area} \n Valor: R$ {livro.valor} \n Estoque: {livro.estoque} unidades  \n Valor total em estoque: R$ {livro.estoque * livro.valor}')
        else:
            print(f'Filial com código {codigofilial} não encontrada.')
            print('---------------------------------')

    def buscar_nome(self):
        codigofilial = input('Digite o código da filial: ')
        filial = next((f for f in self.lista_filiais if f.codigo == codigofilial), None)
        if filial:
            nome = (input(f'Digite o nome do livro que deseja buscar: '))
            for livro in filial.listalivros:
                if livro.titulo == nome:
                     print(f'>>>>> Cod#{livro.codigo} \n Titulo/Editora: {livro.titulo}/{livro.editora} \n Categoria: {livro.area} \n Valor: R$ {livro.valor} \n Estoque: {livro.estoque} unidades  \n Valor total em estoque: R$ {livro.estoque * livro.valor}')
        else:
            print(f'Filial com código {codigofilial} não encontrada.')
            print('---------------------------------')

    def buscar_categoria(self):
        codigofilial = input('Digite o código da filial: ')
        filial = next((f for f in self.lista_filiais if f.codigo == codigofilial), None)
        if filial:
            categoria = input(f'Digite a categoria do livro que deseja buscar: ')
            for livro in self.listaLivro:
                if livro.area == categoria:
                     print(f'>>>>> Cod#{livro.codigo} \n Titulo/Editora: {livro.titulo}/{livro.editora} \n Categoria: {livro.area} \n Valor: R$ {livro.valor} \n Estoque: {livro.estoque} unidades  \n Valor total em estoque: R$ {livro.estoque * livro.valor}')
        else:
            print(f'Filial com código {codigofilial} não encontrada.')
            print('---------------------------------')

    def valortotal_estoque(self):
        soma = 0
        codigofilial = input('Digite o código da filial: ')
        filial = next((f for f in self.lista_filiais if f.codigo == codigofilial), None)
        if filial:
             for livro in filial.listalivros:
                soma += livro.valor * livro.estoque
                print(f'Valor total no estoque: R$ {soma}')
        else:
            print(f'Filial com código {codigofilial} não encontrada.')
            print('---------------------------------')



    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        codigo = input("Digite o código do livro: ")
        editora = input("Digite a editora do livro: ")
        area = input("Digite a categoria do livro: ")
        ano = int(input("Digite o ano do livro: "))
        valor = float(input("Digite o valor do livro: "))
        estoque = int(input("Digite o estoque do livro: "))
        filialcodigo = input("Digite o código da filial: ")

        livronovo = Livro(titulo, codigo, editora, area, ano, valor, estoque)

        filial = next((f for f in self.lista_filiais if f.codigo == filialcodigo), None)
        if filial:
            filial.listalivros.append(livronovo)
            filial.livrosalvar.append(livronovo)
            print(f'Livro {livronovo.titulo} cadastrado na filial {filial.nome}.')
        else:
            print(f'Filial com código {filialcodigo} não encontrada.')

        
    def listar_estoque_filial(self):
        codigofilial = input('Digite o código da filial: ')
        filial = next((f for f in self.lista_filiais if f.codigo == codigofilial), None)
        if filial:
            for livro in filial.listalivros:
                print(f'>>>>> Cod#{livro.codigo} \n Título/Editora: {livro.titulo}/{livro.editora} \n Categoria: {livro.area} \n Valor: R$ {livro.valor} \n Estoque: {livro.estoque} unidades  \n Valor total em estoque: R$ {livro.estoque * livro.valor}')
        else:
            print(f'Filial com código {codigofilial} não encontrada.')

    def buscar_codigo_filial(self):
        codigolivro = int(input('Digite o código do livro: '))
        print('---------------------------------')
        somaestoque = 0
        for filial in self.lista_filiais:
            for livro in filial.listalivros:
                if livro.codigo == codigolivro:
                    livroencontrado = livro
                    filialencontrada = filial
                    estoquelivro = livro.estoque * livro.valor
            somaestoque += estoquelivro
        if livroencontrado:
            print(f'Cod#{livro.codigo}')
            print(f'Título/Editora: {livro.titulo}/{livro.editora}')
            print(f'Categoria: {livro.area}')
        else:
            print(f'Livro com código {codigolivro} não encontrado em nenhuma filial.')
        for filial in self.lista_filiais:
            for livro in filial.listalivros:
                if livro.codigo == codigolivro:
                    print(f'Valor: R$ {livro.valor} >>> {filial.nome}, estoque: {livro.estoque} unidades')
        if livroencontrado:
            print(f'Valor total em estoque: R$ {somaestoque}\n')       
        


## Definindo a classe Filial ------------------------------------------------------------

class Filial:
    def __init__(self,codigo,nome, endereco,contato):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.listalivros = []
        self.livrosalvar = []

## Definindo a classe Livro ------------------------------------------------------------
class Livro:
    def __init__(self,titulo,codigo,editora,area,ano,valor,estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area    
        self.ano = ano
        self.valor = valor
        self.estoque = estoque

if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.lista_filiais.append(Filial('1', 'Filial Centro', 'Rua A, 123', '1234-5678'))
    biblioteca.lista_filiais.append(Filial('2', 'Filial Sul', 'Rua B, 456', '9876-5432'))
    biblioteca.lista_filiais[0].listalivros.append(Livro('Livro A', 321, 'Editora A', 'Ficção', 2020, 29.90, 10))
    biblioteca.lista_filiais[0].listalivros.append(Livro('Livro B', 123, 'Editora B', 'Não-ficção', 2021, 39.90, 5))
    biblioteca.lista_filiais[1].listalivros.append(Livro('Livro B', 321, 'Editora B', 'Não-ficção', 2021, 39.90, 5))
    biblioteca.menu()
