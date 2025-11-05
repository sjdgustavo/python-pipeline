# %%
from pathlib import Path

# %% Caminho absoluto para a raiz
root_dir = Path(__file__).resolve().parent

# %% É necessário alterar para o mês a obter o relatório
mes = "042025"

# %% 
caminho_extract = root_dir / "data" / mes
caminho_export = root_dir / "export" / mes

# %%
print(caminho_extract)
# %%
