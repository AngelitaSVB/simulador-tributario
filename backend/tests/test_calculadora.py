import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from calculadora import comparar_regimes

def test_comparar_regimes_basico():
    resultado = comparar_regimes(100000, 50000, 30000, 20000)
    assert isinstance(resultado, dict)
    assert 'simples_nacional' in resultado
    assert 'lucro_presumido' in resultado
    assert 'lucro_real' in resultado
    assert 'melhor_regime' in resultado

def test_comparar_regimes_valores_zero():
    resultado = comparar_regimes(0, 0, 0, 0)
    assert resultado['simples_nacional'] >= 0
    assert resultado['lucro_presumido'] >= 0
    assert resultado['lucro_real'] >= 0
    assert resultado['melhor_regime'] in ['Simples Nacional', 'Lucro Presumido', 'Lucro Real']
    
    
def test_comparar_regimes_com_entrada_invalida():
    with pytest.raises(TypeError):
        comparar_regimes("cem mil", None, "trinta mil", {})
