class Biblioteca:

    def __init__(self):
        self.listaLivro = []
        self.livrosalvar = []

        arquivotxt = open('../biblioteca/dados.txt', 'r', encoding='utf-8')

        dados = arquivotxt.readlines()
        arquivotxt.close()

        for linha in dados:
            linha = linha.strip()
            dadoslivro = linha.split(',')
            codigo = int(dadoslivro[1])
            ano = int(dadoslivro[4])
            valor = float(dadoslivro[5])
            estoque = int(dadoslivro[6])
            livro = Livro(dadoslivro[0].strip(), codigo, dadoslivro[2].strip(),dadoslivro[3].strip(),ano,valor,estoque)
            self.listaLivro.append(livro)


    def listar_livro(self):
        for livro in self.listaLivro:
            print(f'>>>>> Cod#{livro.codigo} \n Titulo/Editora: {livro.titulo}/{livro.editora} \n Categoria: {livro.area} \n Valor: R$ {livro.valor} \n Estoque: {livro.estoque} unidades  \n Valor total em estoque: R$ {livro.estoque * livro.valor}')
            print('')

    def buscar_estoque(self):
        numeroestoque = int(input(f'Digite o numero minimo de estoque que deseja buscar: '))
        for livro in self.listaLivro:
            if livro.estoque >= numeroestoque:
                 print(f'>>>>> Cod#{livro.codigo} \n Titulo/Editora: {livro.titulo}/{livro.editora} \n Categoria: {livro.area} \n Valor: R$ {livro.valor} \n Estoque: {livro.estoque} unidades  \n Valor total em estoque: R$ {livro.estoque * livro.valor}')
    def buscar_preco(self):
        preco = float(input(f'Digite o preço limite que deseja buscar: '))
        for livro in self.listaLivro:
            if livro.valor <= preco:
                 print(f'>>>>> Cod#{livro.codigo} \n Titulo/Editora: {livro.titulo}/{livro.editora} \n Categoria: {livro.area} \n Valor: R$ {livro.valor} \n Estoque: {livro.estoque} unidades  \n Valor total em estoque: R$ {livro.estoque * livro.valor}')
    def buscar_nome(self):
        nome = (input(f'Digite o nome do livro que deseja buscar: '))
        for livro in self.listaLivro:
            if livro.titulo == nome:
                 print(f'>>>>> Cod#{livro.codigo} \n Titulo/Editora: {livro.titulo}/{livro.editora} \n Categoria: {livro.area} \n Valor: R$ {livro.valor} \n Estoque: {livro.estoque} unidades  \n Valor total em estoque: R$ {livro.estoque * livro.valor}')
    def buscar_categoria(self):
        categoria = input(f'Digite a categoria do livro que deseja buscar: ')
        for livro in self.listaLivro:
            if livro.area == categoria:
                 print(f'>>>>> Cod#{livro.codigo} \n Titulo/Editora: {livro.titulo}/{livro.editora} \n Categoria: {livro.area} \n Valor: R$ {livro.valor} \n Estoque: {livro.estoque} unidades  \n Valor total em estoque: R$ {livro.estoque * livro.valor}')


    def valortotal_estoque(self):
        soma = 0
        for livro in self.listaLivro:
            soma += livro.valor * livro.estoque
        print(f'Valor total no estoque: R$ {soma}')

    def cadastrar_livro(self):
        titulo = (input("Digite o titulo do livro: "))
        codigo = (input("Digite o codigo do livro: "))
        editora = input("Digite o editora do livro: ")
        area = input("Digite a categoria do livro: ")
        ano = (input("Digite o ano do livro: "))
        valor = float(input("Digite o valor do livro: "))
        estoque = int(input("Digite o estoque do livro: "))
        livronovo = Livro(titulo,codigo,editora,area,ano,valor,estoque)
        self.listaLivro.append(livronovo)
        self.livrosalvar.append(livronovo)


    def menu_salvar(self):
        salvar = int(input('Deseja salvar as alterações?\n 1 - Sim \n 0 - Não'))
        if salvar == 1:
            self.salvar_arquivo()
            print('')
            print('Salvado com sucesso!')
        else:
            print('')
            print('Alterações não salvas, sistema encerrado!')

    def salvar_arquivo(self):

        arquivotxt = open('dados.txt', 'a', encoding='utf-8')
        for livro in self.livrosalvar:
            dados = f'{livro.titulo},{livro.codigo},{livro.editora},{livro.area},{livro.ano},{livro.valor},{livro.estoque}\n'
            arquivotxt.writelines(dados)
        arquivotxt.close()

    def menu(self):
        while True:
            print('---------------------------------')
            selection = int(input(
                f' 1 – Cadastrar novo livro \n 2 – Listar livros \n 3 – Buscar livros por nome \n 4 – Buscar livros por categoria \n 5 – Buscar livros por preço \n 6 – Busca por quantidade em estoque \n 7 – Valor total no estoque \n 0 – Encerrar atividades \n ---------------------------------\n'))

            if selection == 1:
                biblioteca.cadastrar_livro()
                print()
                print('Livro cadastrado com sucesso!')
                print('---------------------------------')
                opcao = int(input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades'))
                
                if opcao == 0:
                    biblioteca.menu_salvar()
                    break
            
            elif selection == 2:
                biblioteca.listar_livro()
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
                break

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
    biblioteca.menu()
