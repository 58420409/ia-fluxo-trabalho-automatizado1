# Crie testes unitários para a função calcular_total_com_desconto
# considerando diferentes percentuais de desconto
from app.pedidos import calcular_total_com_desconto

def test_calcular_total_com_desconto_10_porcento():
    total = calcular_total_com_desconto(100, 10)
    assert total == 90

def test_calcular_total_com_desconto_sem_desconto():
    total = calcular_total_com_desconto(200, 0)
    assert total == 200    
# Gerado com o prompt:
# "Crie testes unitários para a função calcular_total_com_desconto
# considerando diferentes percentuais de desconto"
