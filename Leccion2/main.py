import pandas as pd
import matplotlib.pyplot as plt


# Mes mayor gasto (min)
def MayorGasto(self):
    return int(self.min())

# Mes mayor ahorro(max)
def MayorAhorro(self):
   return int(self.max())

    # Media de gasto del año (avg)
def MediaAnno(self):    
    return float(self.mean())
    
# Ingresos totales del año 
def IngresosTotales(self):
    df_total = self.sum(axis=0)
    return int(df_total)


# define Python user-defined exceptions
class Error(Exception):
    """Base class exceptions"""
    pass
class DatoError(Error):
    "Los datos tienen formato erroneo"
    pass
class ColumnasMesError(Error):
    "Las columnas no son correctas"
    pass
class NumColumnasMesError(Error):
    "El numero de columnas es erroneo"
    pass
class ColumnasVaciasError(Error):
    "Las columnas estan vacías"
    pass

try:
    df = pd.read_csv('finanzas2020.csv', sep = '\t')

    if(len(df.columns) != 12):
        raise NumColumnasMesError
    
    if(list(df.columns) !=    ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio',
                        'Agosto','Septiembre','Octubre','Noviembre','Diciembre']):
        raise ColumnasMesError

    for columna in df.columns:
            if(df[columna].empty):
                raise ColumnasVaciasError(columna)
            else:
                df[columna] = df[columna].astype(str)
                for i in df[columna].index:
                    if(type(df[columna][i]) is int):
                        break
                    else:
                        df[columna][i] = df[columna][i].replace("\'",'')
                        try:
                            a = int(df[columna][i])
                            #print("tipo de en dato:",type(df[columna][i]),"columna: ", columna, " indice:",i, " dato: ",df[columna][i])
                        except ValueError as de:
                            df[columna][i] = 0     
                            # si el dato es erroneo lo ponemos a 0 ni suma ni resta
                            # print("Error en dato:",df[columna][i],"columna: ", columna, "indice:",i, "convirtiendo a 0")
                            continue
                df[columna].astype(int)
except IOError as e:
    print("Error - archivo no encontrado",e)
except ColumnasMesError as cme:
    print("Headers incorrectos")
except NumColumnasMesError as ncme:
    print("Numero Columnas incorrectos")
except ColumnasVaciasError as cve:
    print("Hay una o mas Vacías ")
else:
    #cambiamos valores a int
    df = pd.DataFrame(df).astype(int)
    df_sum_column = df.sum(axis=0)
    
    # Mes mayor gasto (min)
    print("# Mes mayor gasto (min) ",df_sum_column.idxmin() ,MayorGasto(df_sum_column))

    # Mes mayor ahorro(max)
    print("# Mes mayor ahorro(max) ",df_sum_column.idxmax(),MayorAhorro(df_sum_column))

    # Media de gasto del año (avg)
    print("# Media de gasto del año (avg)",MediaAnno(df_sum_column))

    # ingresos totales (Mes a mes y total)
    print("# ingresos totales (Mes a mes)")
    print (df_sum_column)
    print("# ingresos totales(Total)")
    
    print(IngresosTotales(df_sum_column))

    # Opcional: Realice una gráfica de la evolución de ingresos a lo largo del año
    df2 = pd.DataFrame({"Mes":list(df.columns),
                         "Ahorro":[
                         df['Enero'].sum(axis=0),
                         df['Febrero'].sum(axis=0),
                         df['Marzo'].sum(axis=0),
                         df['Abril'].sum(axis=0),
                         df['Mayo'].sum(axis=0),
                         df['Junio'].sum(axis=0),
                         df['Julio'].sum(axis=0),
                         df['Agosto'].sum(axis=0),
                         df['Septiembre'].sum(axis=0),
                         df['Octubre'].sum(axis=0),
                         df['Noviembre'].sum(axis=0),
                         df['Diciembre'].sum(axis=0)]})
    
    df2.plot.bar(x='Mes', y='Ahorro', rot=0)
    plt.show()
    
