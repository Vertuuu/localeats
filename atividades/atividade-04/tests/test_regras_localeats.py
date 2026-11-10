import pytest

from src.regras_localeats import pedido_atingiu_valor_minimo, quantidade_itens_valida


# ---------------------------------------------------------------------------
# Regra 1: valor mínimo do pedido
# ---------------------------------------------------------------------------

# Responsável: Éverton Lopes
def test_pedido_acima_do_minimo_e_aceito():
    assert pedido_atingiu_valor_minimo(50) is True


# Responsável: Éverton Lopes
@pytest.mark.parametrize(
    ("valor_pedido", "esperado"),
    [(29.99, False), (30, True), (30.01, True)],
    ids=["um-centavo-abaixo", "exatamente-o-minimo", "um-centavo-acima"],
)
def test_pedido_no_limite_do_valor_minimo(valor_pedido, esperado):
    assert pedido_atingiu_valor_minimo(valor_pedido) is esperado


# Responsável: Éverton Lopes
def test_pedido_com_valor_negativo_gera_erro():
    with pytest.raises(ValueError, match="negativo"):
        pedido_atingiu_valor_minimo(-1)


# ---------------------------------------------------------------------------
# Regra 3: quantidade de itens
# ---------------------------------------------------------------------------

# Responsável: Lorenzo Maciel
def test_quantidade_dentro_do_intervalo_e_valida():
    assert quantidade_itens_valida(3) is True


# Responsável: Lorenzo Maciel
@pytest.mark.parametrize(
    ("quantidade", "esperado"),
    [(0, False), (1, True), (10, True), (11, False)],
    ids=["zero", "limite-inferior", "limite-superior", "acima-do-limite"],
)
def test_quantidade_nos_limites_do_intervalo(quantidade, esperado):
    assert quantidade_itens_valida(quantidade) is esperado


# Responsável: Lorenzo Maciel
def test_quantidade_negativa_gera_erro():
    with pytest.raises(ValueError, match="negativa"):
        quantidade_itens_valida(-1)
