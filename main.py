# %% --- Importações caminhos --- 
import pandas as pd
from config import caminho_export

# %% --- Importações funções --- 
from load.load_base_fonte_1 import load_base_fonte_1
from load.load_base_fonte_2 import load_base_fonte_2
from load.load_base_fonte_3 import load_base_fonte_3
from load.load_base_ajuste_valor import load_base_ajuste_valor
from transform.transform_base_fonte_1 import gerar_base_rateio
from transform.transform_base_check_valores import gerar_base_check_valores

# %% --- Extrações dos dados em dataframes ---
df_base_fonte_1 = load_base_fonte_1()
df_base_fonte_2 = load_base_fonte_2()
df_base_fonte_3 = load_base_fonte_3()
df_base_ajuste_valor = load_base_ajuste_valor()

# %% --- Transformações ---
base_rateio = gerar_base_rateio(df_base_fonte_1)
base_check_valores = gerar_base_check_valores(df_base_fonte_2, df_base_fonte_3, df_base_ajuste_valor)

# Adicionando colunas com os rateios gerados pela base_rateio com base_check_valores



# %% --- Exportação arquivos transformados --- 