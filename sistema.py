from datetime import datetime


class Produto:
def __init__(self, descricao: str, preco_unitario: float, estoque: int):
self.__descricao = descricao
self.__preco_unitario = preco_unitario
self.__estoque = estoque

@property
def descricao(self) -> str:
return self.__descricao

@property
def preco_unitario(self) -> float:
return self.__preco_unitario

@property
def estoque(self) -> int:
return self.__estoque

def decrementar_estoque(self, quant: int) -> bool:
"""Verifica se há quantidade suficiente e diminui o estoque."""
if quant <= self.__estoque:
self.__estoque -= quant
return True
return False

def incrementar_estoque(self, quant: int):
"""Devolve uma quantidade ao estoque."""
self.__estoque += quant


class ItemVenda:
def __init__(self, produto: Produto, quantidade: int):
self.__produto = produto
self.__quantidade = quantidade
self.__valor_item = produto.preco_unitario

@property
def produto(self) -> Produto:
return self.__produto

@property
def quantidade(self) -> int:
return self.__quantidade

def calcular_subtotal(self) -> float:
"""Multiplica a quantidade pelo preço unitário."""
return self.__quantidade * self.__valor_item


class Venda:
def __init__(self):
self.__data = datetime.now()
self.__valor_total = 0.0
self.__itens = []

@property
def data(self) -> datetime:
return self.__data

@property
def valor_total(self) -> float:
return self.__valor_total

def adicionar_item(self, produto: Produto, quant: int):
"""Verifica o estoque e adiciona o item à venda."""
if quant <= 0:
print("[ERRO] A quantidade deve ser maior que zero.")
return

if produto.decrementar_estoque(quant):
item = ItemVenda(produto, quant)
self.__itens.append(item)
self.calcular_total()

print(
f"[OK] {quant}x {produto.descricao} "
f"adicionado com sucesso!"
)
else:
print(
f"[ERRO] Estoque insuficiente para "
f"{produto.descricao} "
f"(disponível: {produto.estoque})."
)

def remover_item(self, produto: Produto):
"""Remove o item e devolve a quantidade ao estoque."""
for item in self.__itens:
if item.produto == produto:
self.__itens.remove(item)


produto.incrementar_estoque(item.quantidade)

self.calcular_total()

print(
f"[OK] {produto.descricao} "
f"removido da venda."
)
return

print(
f"[ERRO] {produto.descricao} "
f"não foi encontrado na venda."
)

def calcular_total(self) -> float:
"""Soma o subtotal de todos os itens da venda."""
self.__valor_total = sum(
item.calcular_subtotal()
for item in self.__itens
)

return self.__valor_total
