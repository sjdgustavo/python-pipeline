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
from transform.transform_dfs_auxiliares_rateio import (gerar_df_custo_rep_canal,
                                                      gerar_df_receita_canal,
                                                      gerar_df_custo_rep_fonte_base,
                                                      gerar_df_var_mapeada_canal_base)
from transform.transform_dfs_rateios import (gerar_rateio_abatimentos,
                                            gerar_rateio_provisao_obsoleto,
                                            gerar_rateio_incentivos_fiscais_custo,
                                            gerar_rateio_avp,
                                            gerar_rateio_custo_fixo,
                                            gerar_rateio_ganho_cpv)
from transform.transform_colunas_base_rateio import (coluna_abatimentos,
                                                     coluna_provisao_obsoleto,
                                                     coluna_incentivos_fiscais_custo,
                                                     coluna_avp_cpv,
                                                     coluna_custo_fixo,
                                                     coluna_dif,
                                                     coluna_part_lp,
                                                     coluna_alocacao_crossdocking,
                                                     coluna_part_ov,
                                                     coluna_alocacao_ov,
                                                     coluna_variacao_mapeada,
                                                     coluna_custo_base_rateio,
                                                     coluna_custo_base_rateio2,
                                                     coluna_part_cbr,
                                                     coluna_variacao_adicional,
                                                     coluna_variacao_cpv)

# %% --- Extrações dos dados em dataframes ---
df_base_fonte_1 = load_base_fonte_1()
df_base_fonte_2 = load_base_fonte_2()
df_base_fonte_3 = load_base_fonte_3()
df_base_ajuste_valor = load_base_ajuste_valor()

# %% --- Transformações ---
base_rateio = gerar_base_rateio(df_base_fonte_1)
base_check_valores = gerar_base_check_valores(df_base_fonte_2, df_base_fonte_3, df_base_ajuste_valor)

# Adicionando colunas com os rateios gerados pela base_rateio com base_check_valores
df_receita_canal = gerar_df_receita_canal(base_rateio)
rateio_abatimentos = gerar_rateio_abatimentos(df_receita_canal, base_check_valores)
base_rateio = coluna_abatimentos(base_rateio, rateio_abatimentos)

df_custo_rep_canal = gerar_df_custo_rep_canal(base_rateio)
rateio_provisao_obsoleto = gerar_rateio_provisao_obsoleto(df_custo_rep_canal, base_check_valores)
base_rateio = coluna_provisao_obsoleto(base_rateio, rateio_provisao_obsoleto)

df_custo_rep_fonte_base = gerar_df_custo_rep_fonte_base(base_rateio)
rateio_incentivos_fiscais_custo = gerar_rateio_incentivos_fiscais_custo(df_custo_rep_fonte_base, base_check_valores)
base_rateio = coluna_incentivos_fiscais_custo(base_rateio, rateio_incentivos_fiscais_custo)

rateio_avp = gerar_rateio_avp(base_rateio, base_check_valores)
base_rateio = coluna_avp_cpv(base_rateio, rateio_avp)

rateio_custo_fixo = gerar_rateio_custo_fixo(df_custo_rep_fonte_base, df_base_fonte_3, base_check_valores)
base_rateio = coluna_custo_fixo(base_rateio, rateio_custo_fixo)

base_rateio = coluna_dif(base_rateio)
base_rateio = coluna_part_lp(base_rateio)
base_rateio = coluna_alocacao_crossdocking(base_rateio, df_base_ajuste_valor)
base_rateio = coluna_part_ov(base_rateio)
base_rateio = coluna_alocacao_ov(base_rateio, df_base_ajuste_valor)
base_rateio = coluna_variacao_mapeada(base_rateio)
base_rateio = coluna_custo_base_rateio(base_rateio)
base_rateio = coluna_custo_base_rateio2(base_rateio)
base_rateio = coluna_part_cbr(base_rateio)

df_var_mapeada_canal_base = gerar_df_var_mapeada_canal_base(base_rateio)
rateio_ganho_cpv = gerar_rateio_ganho_cpv(base_check_valores, df_var_mapeada_canal_base)
base_rateio = coluna_variacao_adicional(base_rateio, rateio_ganho_cpv)

base_rateio = coluna_variacao_cpv(base_rateio)

# %% --- Exportação arquivos transformados --- 
base_rateio.to_excel(caminho_export/'base_rateio.xlsx', index=False)