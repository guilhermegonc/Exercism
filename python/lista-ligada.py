class Celula:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None


class ListaLigada:
    def __init__(self):
        self._inicio = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def quantidade(self):
        return self._quantidade

    def inserir_no_inicio(self, conteudo):
        celula = Celula(conteudo)
        celula.proximo = self._inicio
        self._inicio = celula
        self._quantidade += 1

    def imprimir(self):
        atual = self.inicio
        for i in range(self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo

    def inserir(self, posicao, conteudo):
        if posicao == 0:
            self.inserir_no_inicio(conteudo)
            return
        celula = Celula(conteudo)
        esq = self._celula(posicao - 1)
        celula.proximo = esq.proximo
        esq.proximo = celula
        self._quantidade += 1

    def _celula(self, posicao):
        self._validar_posicao(posicao)
        atual = self.inicio
        for i in range(posicao):
            atual = atual.proximo
        return atual

    def _validar_posicao(self, posicao):
        if 0 <= posicao <= self.quantidade:
            return True
        raise IndexError(f'Posição inválida: {posicao}')


class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return f'{self.nome}\n  {self.endereco}'


loja1 = Loja('Mercadinho', 'Rua das Laranjeiras, 12')
loja2 = Loja('Hortifruti', 'Rua do Pomar, 300')
loja3 = Loja('Confeitaria', 'Rua das Flores, 600')
loja4 = Loja('Supermercado', 'Alameda S, 400')
loja5 = Loja('Minimercado', 'Rua da Fazenda, 100')
loja6 = Loja('Quitanda', 'Avenida do Governador, 1200')

lista = ListaLigada()
lista.inserir_no_inicio(loja1)
lista.inserir_no_inicio(loja2)
lista.inserir_no_inicio(loja3)
lista.inserir(1, loja4)
lista.inserir(3, loja5)
print(lista.quantidade)
lista.imprimir()
