class Biblioteca:

    def __init__(self):
        self.lista_filiais = []
        self.carregar_livros_do_arquivo('dados.txt')

    def menu(self):
        while True:
            print('---------------------------------')
            selection = input(
                f' 1 – Cadastrar novo livro \n 2 - Listagem estoque da filial \n 3 – Buscar livros por nome \n 4 – Buscar livros por categoria \n 5 – Buscar livros por preço \n 6 – Busca por quantidade em estoque \n 7 – Valor total no estoque \n 8 – Cadastrar Filial \n 9 - Buscar livro pelo codigo em filiais \n 10 – Informação filial \n 0 – Encerrar atividades \n ---------------------------------\n')

            if selection == '1':
                self.cadastrar_livro()

            elif selection == '2':
                filial = self.buscar_numero_filial()
                if filial:
                    filial.listar_estoque_filial()

            elif selection == '3':
                filial = self.buscar_numero_filial()
                if filial:
                    filial.buscar_nome()
    
            elif selection == '4':
                filial = self.buscar_numero_filial()
                if filial:
                    filial.buscar_categoria()

            elif selection == '5':
                filial = self.buscar_numero_filial()
                if filial:
                    filial.buscar_preco()

            elif selection == '6':
                filial = self.buscar_numero_filial()
                if filial:
                    filial.buscar_estoque()

            elif selection == '7':
                self.valortotal_estoque()

            elif selection == '8':
                self.cadastrar_filial()
    
            elif selection == '9':
                filial = self.buscar_codigo_filial()
                if filial:
                    filial.listar_estoque_filial()
            elif selection == '10':
                self.listar_filiais()
            else:
                print('Opção inválida. Tente novamente.')
            if not self.voltar_ou_encerrar():
                self.menu_salvar()
                break
        
    def carregar_livros_do_arquivo(self,caminho):
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivotxt:
                filial_linha = None
                for linha in arquivotxt:
                    linha = linha.strip()
                    if linha.startswith('#FL'):
                        dados = linha.split(',')[1:]
                        codigofilial = int(dados[0])
                        nome = dados[1]
                        endereco = dados[2]
                        contato = dados[3]
                        filial_linha = Filial(codigofilial, nome, endereco, contato)
                        self.lista_filiais.append(filial_linha)
                    else:
                        if filial_linha:
                            dadoslivro = linha.split(',')
                            titulo = dadoslivro[1].strip()
                            codigo = int(dadoslivro[0])
                            area = dadoslivro[3].strip()
                            editora = dadoslivro[4].strip() 
                            ano = int(dadoslivro[2])
                            valorCifrao = dadoslivro[5].replace('R$', '')
                            valor = float(valorCifrao)
                            estoque = int(dadoslivro[6])
                            livro = Livro(titulo,codigo,editora,area,ano,valor,estoque)
                            filial_linha.listalivros.append(livro)
        except FileNotFoundError:
            print(f'Arquivo {caminho} não encontrado.')


    def salvar_arquivo(self):

        try:
            with open('dados.txt', 'w', encoding='utf-8') as arquivotxt:
                for filial in self.lista_filiais:
                    arquivotxt.write(f'#FL,{filial.codigo},{filial.nome},{filial.endereco},{filial.contato}\n')
                    for livro in filial.listalivros:
                        valorCifrao = f'R${livro.valor:.2f}'
                        dados = f'{livro.codigo},{livro.titulo},{livro.ano},{livro.area},{livro.editora},{valorCifrao},{livro.estoque}\n'
                        arquivotxt.write(dados)
            print('Dados salvos com sucesso!')
        except Exception as e:
            print(f'Erro ao salvar os dados: {e}')


    def cadastrar_filial(self):
        codigo = input("Digite o codigo da filial: ")
        nome = input("Digite o nome da filial: ")
        for filial in self.lista_filiais:
            if filial.codigo == codigo or filial.nome == nome:
                print('Filial já cadastrada!')
        endereco = input("Digite o endereco da filial: ")
        contato = input("Digite o contato da filial: ")
        filianovo = Filial(codigo,nome,endereco,contato)
        self.lista_filiais.append(filianovo)
        print(f'Filial {filianovo.nome} cadastrada com sucesso!')

    def listar_filiais(self):
        codigofilial = int(input('Digite o código da filial: '))
        filialencontrada = False
        for filial in self.lista_filiais:
            if filial.codigo == codigofilial:
                filialencontrada = filial
        if filialencontrada:
            print(filialencontrada)
            print('---------------------------------')
        else:
            print(f'Filial com código {codigofilial} não encontrada.')
            print('---------------------------------')


    def menu_salvar(self):
        salvar = input('Deseja salvar as alterações?\n 1 - Sim \n 0 - Não')
        if salvar == '1':
            self.salvar_arquivo()
            print('')
        else:
            print('')
            print('Alterações não salvas, sistema encerrado!')


    def voltar_ou_encerrar(self):
        opcao = input(f' 1 - Voltar ao menu \n 0 - Encerrar atividades')
        return opcao == '1'
    
    def valortotal_estoque(self):
        soma = 0
        codigofilial = int(input('Digite o código da filial: '))
        filialencontrada = False
        for filial in self.lista_filiais:
            if filial.codigo == codigofilial:
                filialencontrada = filial
        if filialencontrada:
             for livro in filialencontrada.listalivros:
                soma += livro.valor * livro.estoque
        print('')
        print(f'Valor total no estoque: R$ {soma}')
        print('')

    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        codigo = int(input("Digite o código do livro: "))
        editora = input("Digite a editora do livro: ")
        area = input("Digite a categoria do livro: ")
        ano = int(input("Digite o ano do livro: "))
        valor = float(input("Digite o valor do livro: "))
        estoque = int(input("Digite o estoque do livro: "))
        filialcodigo = input("Digite o código da filial: ")
        filialencontrada = False
        livroexistente = False
        for filial in self.lista_filiais:
            if filial.codigo == filialcodigo:
                filialencontrada = filial
        if not filialencontrada:
            print(f'Filial não encontrada.')
        livronovo = Livro(titulo, codigo, editora, area, ano, valor, estoque) 

        for livro in filial.listalivros:
            if livro.codigo == codigo or livro.titulo.lower() == titulo.lower():
                livroexistente = livro
        if livroexistente:
            livroexistente.estoque += estoque
            print(f'Livro {livroexistente.titulo} atualizado na filial {filial.nome} agora com estoque total de {livroexistente.estoque}.')
                
        else:
            for filial in self.lista_filiais:
                for livro in filialencontrada.listalivros:
                    if livro.codigo == codigo or livro.titulo.lower() == titulo.lower():
                        livro.codigo = codigo
                        livro.titulo = titulo
            filial.listalivros.append(livronovo)
            filial.livrosalvar.append(livronovo)
            print(f'Livro {livronovo.titulo} cadastrado na filial {filial.nome}.')
    
    def buscar_codigo_filial(self):
        codigolivro = int(input('Digite o código do livro: '))
        print('---------------------------------')
        livroencontrado = None
        estoquelivro = 0
        somaestoque = 0
        for filial in self.lista_filiais:
            for livro in filial.listalivros:
                if livro.codigo == codigolivro:
                    livroencontrado = livro
                    estoquelivro = livro.estoque * livro.valor
            somaestoque += estoquelivro
        if livroencontrado:
            print(f'Cod#{livroencontrado.codigo}')
            print(f'Título/Editora: {livroencontrado.titulo}/{livroencontrado.editora}')
            print(f'Categoria: {livroencontrado.area}')
        else:
            print(f'Livro com código {codigolivro} não encontrado em nenhuma filial.')
        for filial in self.lista_filiais:
            for livro in filial.listalivros:
                if livro.codigo == codigolivro:
                    print(f'Valor: R$ {livro.valor} >>> {filial.nome}, estoque: {livro.estoque} unidades')
        if livroencontrado:
            print(f'Valor total em estoque: R$ {somaestoque}\n')

    def buscar_numero_filial(self):
        codigofilial = int(input('Digite o código da filial: '))
        filialencontrada = False
        for filial in self.lista_filiais:
            if filial.codigo == codigofilial:
                filialencontrada = filial
                return filialencontrada
        if not filialencontrada:
            return None

## ------------------------------------------------------------

class Filial:
    def __init__(self,codigo,nome, endereco,contato):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.listalivros = []
        self.livrosalvar = []

    def __str__(self):
        return (f' >>>>> Cod#: {self.codigo}\n Nome: {self.nome}\n Endereço: {self.endereco}\n Contato: {self.contato}\n')

    def buscar_estoque(self):
        numeroestoque = int(input(f'Digite o numero minimo de estoque que deseja buscar: '))
        print('')
        livroencontrado = False
        for livro in self.listalivros:
            if livro.estoque >= numeroestoque:
                print(livro)
                livroencontrado = True
        if not livroencontrado:
            print(f'Nenhum livro com estoque maior ou igual a {numeroestoque} encontrado.')

    def buscar_preco_livro(self):
        preco = float(input(f'Digite o preço limite que deseja buscar: '))
        livroencontrado = None
        for livro in self.listalivros:
            if livro.valor >= preco:
                livroencontrado = livro
                print('')
                print(livro)
                print('')
            if not livroencontrado:
                print(f'Livro com preço menor que {preco} não encontrado.')

    def buscar_nome(self):

        nome = input(f'Digite o nome do livro que deseja buscar: ')
        for livro in self.listalivros:
            if livro.titulo == nome:
                livroencontrado = livro
                print('')
                print(livro)
                print('')
            if not livroencontrado:
                print(f'Livro com nome {nome} não encontrado.')

    def buscar_categoria(self):
            categoria = input(f'Digite a categoria do livro que deseja buscar: ')
            livroencontrado = False
            for livro in self.listalivros:
                if livro.area.lower() == categoria.lower():
                     print('')
                     print(livro)
                     print('')
                     livroencontrado = True
            if not livroencontrado:
                print(f'Livro com categoria {categoria} não encontrado.')

    def listar_estoque_filial(self):
        print('')
        for livro in self.listalivros:
            print(livro)
    
    def mostrar_estoque_filial(self):
        codigofilial = int(input('Digite o código da filial: '))
        filialencontrada = False
        for filial in self.lista_filiais:
            if filial.codigo == codigofilial:
                filialencontrada = filial
        if filialencontrada:
            print(f'Filial: {filialencontrada.nome}')
            print('')
            filialencontrada.listar_estoque_filial()
        else:
            print(f'Filial com código {codigofilial} não encontrada.')

## ------------------------------------------------------------
class Livro:
    def __init__(self,titulo,codigo,editora,area,ano,valor,estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area    
        self.ano = ano
        self.valor = valor
        self.estoque = estoque

    def __str__(self):
        return  (f' >>>>> Cod#: {self.codigo}\n Título: {self.titulo}\n Ano: {self.ano}\n Editora: {self.editora}\n Área: {self.area}\n Valor: {self.valor}\n Estoque: {self.estoque} \n Total em Estoque: {self.estoque * self.valor}\n')
    
if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.menu()