# %% 
import pandas as pd

# %% 
def coluna_abatimentos(base_rateio: pd.DataFrame, rateio_abatimentos: pd.DataFrame) -> pd.DataFrame: 

    fator_franquias = rateio_abatimentos.loc[rateio_abatimentos["Indicador"] == "Franquias (%)", "Valor"].iloc[0]

    base_rateio["Abatimentos"] = base_rateio.apply(
        lambda row: row["$ Receita"] * fator_franquias if row["Canal_Projeção"] == "Franquias" else 0,
        axis=1
    )

    return base_rateio

# %%
def coluna_provisao_obsoleto(base_rateio: pd.DataFrame, rateio_provisao_obsoleto: pd.DataFrame) -> pd.DataFrame:

    fator_outras_vendas = rateio_provisao_obsoleto.loc[rateio_provisao_obsoleto["Indicador"] == "Outras Vendas (%)", "Valor"].iloc[0]

    base_rateio["Provisão para Obsoleto"] = base_rateio.apply(
        lambda row: row["$ Custo Reposição"] * fator_outras_vendas if row["Canal_Projeção"] == "Outras Vendas" else 0,
        axis=1
    )
    
    return base_rateio

# %%
def coluna_incentivos_fiscais_custo(base_rateio: pd.DataFrame, rateio_incentivos_fiscais_custo: pd.DataFrame) -> pd.DataFrame:

    fator_eng = rateio_incentivos_fiscais_custo.loc[rateio_incentivos_fiscais_custo["Indicador"] == "ENG (%)", "Valor"].iloc[0]

    base_rateio["Incentivos Fiscais Custo"] = base_rateio.apply(
        lambda row: row["$ Custo Reposição"] * fator_eng if row["Fonte"] == "ENG" else 0,
        axis=1
    )

    return base_rateio

# %%
def coluna_avp_cpv(base_rateio: pd.DataFrame, rateio_avp: pd.DataFrame) -> pd.DataFrame:

    fator_avp = rateio_avp.loc[rateio_avp["Indicador"] == "AVP Rateio (%)", "Valor"].iloc[0]
    
    base_rateio["AVP CPV"] = base_rateio.apply(
        lambda row: row["$ Custo Reposição"] * fator_avp,
        axis=1
    )

    return base_rateio

# %%
def coluna_custo_fixo(base_rateio: pd.DataFrame, rateio_custo_fixo: pd.DataFrame) -> pd.DataFrame:

    base_rateio = base_rateio.merge(rateio_custo_fixo, on="Fonte", how="left")
    base_rateio["CPV Indireto (Custo Fixo)"] = base_rateio["$ Custo Reposição"] * base_rateio["(%) Custo Fixo"]
    base_rateio.drop(columns="(%) Custo Fixo", inplace=True)

    return base_rateio

# %%
def coluna_dif(base_rateio: pd.DataFrame) -> pd.DataFrame:

    base_rateio["Dif (Int - Rep)"] = base_rateio["$ CPV Preço Interno"] - base_rateio["$ Custo Reposição"]

    return base_rateio

# %%
def coluna_part_lp(base_rateio: pd.DataFrame) -> pd.DataFrame:

    soma_dif_lp = base_rateio.loc[(base_rateio["Dados"] == "Base") &
                                           (base_rateio["Canal_Projeção"] == "Lojas Próprias"),
                                           "Dif (Int - Rep)"].sum()
    
    base_rateio["% Part LP Mês"] = base_rateio.apply(
        lambda row: row["Dif (Int - Rep)"] / soma_dif_lp if (row["Canal_Projeção"] == "Lojas Próprias" or
                                                             row["Dados"] == "OMNI") else 0,
        axis=1                                                             
    )

    return base_rateio
# %%
def coluna_alocacao_crossdocking(base_rateio: pd.DataFrame, base_ajuste_valor: pd.DataFrame) -> pd.DataFrame:
    
    crossdocking = -base_ajuste_valor.loc[base_ajuste_valor["Indicador"] == "Crossdocking", "Valor"].sum() 

    base_rateio["Alocação Crossdocking"] = base_rateio["% Part LP Mês"] * crossdocking

    return base_rateio

# %% 
def coluna_part_ov(base_rateio: pd.DataFrame) -> pd.DataFrame:
    
    soma_dif_ov = base_rateio.loc[(base_rateio["Dados"] == "Base") &
                                           (base_rateio["Canal_Projeção"] == "Outras Vendas"),
                                           "Dif (Int - Rep)"].sum()
    
    base_rateio["% Part OV Mês"] = base_rateio.apply(
        lambda row: row["Dif (Int - Rep)"] / soma_dif_ov if row["Canal_Projeção"] == "Outras Vendas" else 0,
        axis=1                                                             
    )

    return base_rateio

# %%
def coluna_alocacao_ov(base_rateio: pd.DataFrame, base_ajuste_valor: pd.DataFrame) -> pd.DataFrame:
    
    dif_lnr = base_ajuste_valor.loc[base_ajuste_valor["Indicador"] == "Dif LNR / Ajuste estoque", "Valor"].sum()

    base_rateio["Alocação LNR OV"] = base_rateio["% Part OV Mês"] * dif_lnr

    return base_rateio
# %%
def coluna_variacao_mapeada(base_rateio: pd.DataFrame) -> pd.DataFrame:

    base_rateio["Variação Mapeada"] = (base_rateio["Dif (Int - Rep)"] + base_rateio["Alocação Crossdocking"] +
                                                base_rateio["Alocação LNR OV"]) 

    return base_rateio

# %% 
def coluna_custo_base_rateio(base_rateio: pd.DataFrame) -> pd.DataFrame:
     
    base_rateio["Custo Base Rateio"] = base_rateio.apply(
        lambda row: row["$ Custo Reposição"] if (row["Canal_Projeção"] == "Lojas Próprias" or
                                                 row["Dados"] == "OMNI") else row["$ Custo Reposição"] + row["Variação Mapeada"],
        axis=1                                                             
    )

    return base_rateio
# %%
def coluna_custo_base_rateio2(base_rateio: pd.DataFrame) -> pd.DataFrame:

    base_rateio["Custo Base Rateio 2"] = base_rateio.apply(
        lambda row: row["Custo Base Rateio"] if row["Fonte"] == "ENG" else 0,
        axis=1
    )

    return base_rateio

# %%
def coluna_part_cbr(base_rateio: pd.DataFrame) -> pd.DataFrame:

    total_cbr2 = base_rateio["Custo Base Rateio 2"].sum()    

    base_rateio["% Part CBR"] = base_rateio["Custo Base Rateio 2"] / total_cbr2

    return base_rateio


# %%
def coluna_variacao_adicional(base_rateio: pd.DataFrame, rateio_ganho_cpv: pd.DataFrame) -> pd.DataFrame:

    a_distribuir = rateio_ganho_cpv.loc[rateio_ganho_cpv["Indicador"] == "A distribuir", "Valor"].sum()

    base_rateio["Variação Adicional"] = base_rateio["% Part CBR"] * a_distribuir

    return base_rateio

# %%

def coluna_variacao_cpv(base_rateio: pd.DataFrame) -> pd.DataFrame:

    base_rateio["Variação de CPV"] = base_rateio["Variação Mapeada"] + base_rateio["Variação Adicional"]

    return base_rateio
# %%
