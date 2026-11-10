"""Regras de negócio do LocalEats."""

VALOR_MINIMO_PEDIDO = 30.00
QUANTIDADE_MINIMA_ITENS = 1
QUANTIDADE_MAXIMA_ITENS = 10


# Responsável: Éverton Lopes
def pedido_atingiu_valor_minimo(valor_pedido):
    """Indica se o pedido alcançou o valor mínimo de R$ 30,00."""
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    return valor_pedido >= VALOR_MINIMO_PEDIDO


# Responsável: Lorenzo Maciel
def quantidade_itens_valida(quantidade):
    """Indica se a quantidade de itens está entre 1 e 10."""
    if quantidade < 0:
        raise ValueError("A quantidade de itens não pode ser negativa.")
    return QUANTIDADE_MINIMA_ITENS <= quantidade <= QUANTIDADE_MAXIMA_ITENS
