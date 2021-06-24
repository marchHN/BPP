import pytest
import main as m
import pandas as pd

# Mes mayor Gasto(min)
def test_MayorGasto():
    d = {'col1': [1,2,3,4,5,6,7]}
    df = pd.DataFrame(data=d)
    resultado = 1
    assert resultado == m.MayorGasto(df)
    
# Mes mayor ahorro(max)
def test_MayorAhorro():
    d = {'col1': [1,2,3,4,5,6,7]}
    df = pd.DataFrame(data=d) 
    resultado = 7
    assert resultado == m.MayorAhorro(df)

# Media de gasto del año (avg)
def test_MediaAnno():    
    d = {'col1': [1,2,3,4,5,6,7]}
    df = pd.DataFrame(data=d) 
    resultado = 4
    assert resultado == m.MediaAnno(df)
    
# Ingresos totales del año 
def test_IngresosTotales():
    d = {'col1': [1,2,3,4,5,6,7]}
    df = pd.DataFrame(data=d) 
    resultado = 28
    assert resultado == m.IngresosTotales(df)