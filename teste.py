from sistema import Produto, Venda


print(" INICIANDO TESTES DO SISTEMA DE VENDAS \n")


p1 = Produto("Notebook Gamer", 4500.00, 5)
p2 = Produto("Mouse Vertical", 180.00, 3)


print(
f"Estoque inicial -> "
f"{p1.descricao}: {p1.estoque} un | "
f"{p2.descricao}: {p2.estoque} un\n"
)


venda1 = Venda()


print(" TESTE DE ADIÇÃO ")

venda1.adicionar_item(p1, 2)


venda1.adicionar_item(p2, 5)


venda1.adicionar_item(p2, 2)


print("\n RESUMO DA VENDA ")

print(
f"Data da operação: "
f"{venda1.data.strftime('%d/%m/%Y %H:%M:%S')}"
)

print(
f"Valor total atual: "
f"R$ {venda1.valor_total:.2f}"
)


print("\n TESTE DE REMOÇÃO ")

venda1.remover_item(p1)

print(
f"Valor total após remoção: "
f"R$ {venda1.valor_total:.2f}"
)


print("\n ESTOQUE FINAL ")

print(
f"{p1.descricao}: "
f"{p1.estoque} restante(s)"
)

print(
f"{p2.descricao}: "
f"{p2.estoque} restante(s)"
)
