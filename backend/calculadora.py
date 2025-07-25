# calculadora.py

def calcular_simples(receita_comercio, receita_servico, folha_pagamento):
    receita_total = receita_comercio + receita_servico

    # Cálculo simplificado da alíquota efetiva (apenas ilustrativo)
    if receita_total <= 180000:
        aliquota = 0.06
    elif receita_total <= 360000:
        aliquota = 0.112
    else:
        aliquota = 0.16

    total_impostos = receita_total * aliquota
    return round(total_impostos, 2)


def calcular_presumido(receita_comercio, receita_servico, folha_pagamento):
    base_irpj_comercio = receita_comercio * 0.08
    base_irpj_servico = receita_servico * 0.32

    irpj = (base_irpj_comercio + base_irpj_servico) * 0.15
    csll = (base_irpj_comercio + base_irpj_servico) * 0.09
    pis = (receita_comercio + receita_servico) * 0.0065
    cofins = (receita_comercio + receita_servico) * 0.03

    total_impostos = irpj + csll + pis + cofins
    return round(total_impostos, 2)


def calcular_real(receita_comercio, receita_servico, folha_pagamento, despesas):
    lucro_real = receita_comercio + receita_servico - despesas

    if lucro_real <= 0:
        return 0.0

    irpj = lucro_real * 0.15
    csll = lucro_real * 0.09
    pis = (receita_comercio + receita_servico) * 0.0165
    cofins = (receita_comercio + receita_servico) * 0.076

    total_impostos = irpj + csll + pis + cofins
    return round(total_impostos, 2)


def comparar_regimes(receita_comercio, receita_servico, folha_pagamento, despesas_anuais):
    simples = (receita_comercio + receita_servico) * 0.06
    presumido = (receita_comercio + receita_servico) * 0.11
    real = (receita_comercio + receita_servico - despesas_anuais) * 0.15

    melhor = min([('Simples Nacional', simples), ('Lucro Presumido', presumido), ('Lucro Real', real)], key=lambda x: x[1])

    return {
        "simples_nacional": round(simples, 2),
        "lucro_presumido": round(presumido, 2),
        "lucro_real": round(real, 2),
        "melhor_regime": melhor[0]
    }



