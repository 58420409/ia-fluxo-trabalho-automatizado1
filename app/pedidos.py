def calcular_total_com_desconto(valor_total, percentual_desconto):
    """
    Calcula o valor final de um pedido aplicando um desconto percentual.
    """
    desconto = valor_total * (percentual_desconto / 100)
    return valor_total - desconto
