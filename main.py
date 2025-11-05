# %% --- Importações caminhos --- 
import pandas as pd
from config import caminho_export

# %% --- Importações funções --- 
from load.load_base_fonte_1 import load_base_fonte_1
from load.load_base_fonte_2 import load_base_fonte_2
from load.load_base_fonte_3 import load_base_fonte_3
from load.load_base_ajuste_valor import load_base_ajuste_valor

# %% --- Extrações dos dados em dataframes ---
df_base_fonte_1 = load_base_fonte_1()
df_base_fonte_2 = load_base_fonte_2()
df_base_fonte_3 = load_base_fonte_3()
df_base_ajuste_valor = load_base_ajuste_valor()

# %% --- Transformações ---

# %% --- Exportação arquivos transformados --- 