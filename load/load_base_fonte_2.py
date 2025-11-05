# %% 
import pandas as pd

# %% Adicionando a pasta raiz para poder acessar o módulo config
import sys  
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# %%
from config import caminho_extract

# %% 
def load_base_fonte_2() -> pd.DataFrame:
    caminho = caminho_extract / "base_fonte_2.xlsx" 
    df = pd.read_excel(caminho)
    df.columns = df.columns.str.strip()
    return df

# %%
