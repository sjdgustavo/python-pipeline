# %%
import pandas as pd

# %%
def gerar_rateio_abatimentos(df_receita_canal: pd.DataFrame, base_check_valores: pd.DataFrame) -> pd.DataFrame:
    
    franquias_receita = df_receita_canal.loc[df_receita_canal["Canal"] == "Franquias","Soma de Receita"].sum()
    abatimentos = base_check_valores.loc[base_check_valores["DRE Base"] == "Abatimentos e TMD", "Real"].sum()
    abatimentos_rateio = abatimentos / franquias_receita

    linhas = [
        "Receita de Franquias",
        "Abatimentos e TMD",
        "Franquias (%)"
    ]
    valores = [
        franquias_receita,
        abatimentos,
        abatimentos_rateio
    ]
    rateio_abatimentos = pd.DataFrame({
        "Indicador": linhas,
        "Valor": valores
    })

    return rateio_abatimentos

# %%
def gerar_rateio_provisao_obsoleto(df_custo_rep_canal: pd.DataFrame, base_check_valores: pd.DataFrame) -> pd.DataFrame:

    outras_custo_rep = df_custo_rep_canal.loc[df_custo_rep_canal["Canal"] == "Outras Vendas", "Soma de Custo Reposição"].sum()
    provisao_obsoleto = base_check_valores.loc[base_check_valores["DRE Base"] == "Provisão para Obsoleto", "Real"].sum()
    provisao_obsoleto_rateio = provisao_obsoleto / outras_custo_rep

    linhas =  [
        "Custo Reposição de Outras Vendas",
        "Provisão para Obsoleto",
        "Outras Vendas (%)"
    ]
    valores = [
        outras_custo_rep,
        provisao_obsoleto,
        provisao_obsoleto_rateio
    ]

    rateio_provisao_obsoleto = pd.DataFrame({
        "Indicador": linhas,
        "Valor": valores

    })

    return rateio_provisao_obsoleto

# %%
def gerar_rateio_incentivos_fiscais_custo(df_custo_rep_fonte_base: pd.DataFrame, base_check_valores: pd.DataFrame) -> pd.DataFrame:
    
    eng_custo_rep = df_custo_rep_fonte_base.loc[df_custo_rep_fonte_base["Fonte"] == "ENG", "Soma de Custo Reposição"].sum()
    incentivos_fiscais_custo = base_check_valores.loc[base_check_valores["DRE Base"] == "Incentivos Fiscais Custo", "Real"].sum()
    incentivos_fiscais_custo_rateio = incentivos_fiscais_custo / eng_custo_rep
    
    linhas = [
        "Custo Reposição de ENG",
        "Incentivos Fiscais Custo",
        "ENG (%)"
    ]
    valores = [
        eng_custo_rep,
        incentivos_fiscais_custo,
        incentivos_fiscais_custo_rateio
    ]

    rateio_incentivos_fiscais_custo =pd.DataFrame({
        "Indicador": linhas,
        "Valor": valores
    })
    
    return rateio_incentivos_fiscais_custo

# %% 
def gerar_rateio_avp(base_rateio: pd.DataFrame, base_check_valores: pd.DataFrame) -> pd.DataFrame:

    total_custo_rep = base_rateio.loc[base_rateio["Dados"] == "Base", "$ Custo Reposição"].sum()
    avp_cpv = base_check_valores.loc[base_check_valores["DRE Base"] == "AVP CPV", "Real"].sum()
    avp_rateio = avp_cpv / total_custo_rep

    linhas = [
        "Total de Custo Reposição",
        "AVP CPV",
        "AVP Rateio (%)"
    ]
    valores = [
        total_custo_rep,
        avp_cpv,
        avp_rateio
    ]

    rateio_avp = pd.DataFrame({
        "Indicador": linhas,
        "Valor": valores
    })

    return rateio_avp

# %% 
def gerar_rateio_custo_fixo(df_custo_rep_fonte_base: pd.DataFrame, base_fonte_3: pd.DataFrame,
                            base_check_valores: pd.DataFrame) -> pd.DataFrame:

    eng_custo_rep = df_custo_rep_fonte_base.loc[df_custo_rep_fonte_base["Fonte"] == "ENG", "Soma de Custo Reposição"].sum()
    total_custo_rep = df_custo_rep_fonte_base.loc[df_custo_rep_fonte_base["Fonte"] == "Total", "Soma de Custo Reposição"].sum()

    cpv_indireto_custo_fixo = base_check_valores.loc[base_check_valores["DRE Base"].str.contains("(Custo Fixo)", na=False),
                                                       "Real"].sum()
    custo_fixo_logistica = base_fonte_3.loc[base_fonte_3["Abertura_Lucro_Bruto"].str.contains("Logistica", na=False),
                                                 "Real"].sum()
    demais_custo_fixo = cpv_indireto_custo_fixo - custo_fixo_logistica

    si_custo_fixo = custo_fixo_logistica / total_custo_rep
    sn_custo_fixo = custo_fixo_logistica / total_custo_rep
    eng_custo_fixo = (demais_custo_fixo / eng_custo_rep) + (custo_fixo_logistica / total_custo_rep)

    linhas = [
        "ENG",
        "SI",
        "SN"
    ]

    valores = [
        eng_custo_fixo,
        si_custo_fixo,
        sn_custo_fixo
    ]

    rateio_custo_fixo = pd.DataFrame({
        "Fonte": linhas,
        "(%) Custo Fixo": valores
    })

    return rateio_custo_fixo

# %% 
def gerar_rateio_ganho_cpv(base_check_valores: pd.DataFrame, df_var_mapeada_canal_base: pd.DataFrame) -> pd.DataFrame:

    ganho_cpv = base_check_valores.loc[base_check_valores["DRE Base"] == "Ganho de CPV", "Real"].sum()
    total_variacao_mapeada = df_var_mapeada_canal_base.loc[df_var_mapeada_canal_base["Canal"] == "Real", "Soma de Variação Mapeada"].sum()

    a_distribuir = ganho_cpv - total_variacao_mapeada

    linhas = [
        "Ganho de CPV",
        "Total Variação Mapeada",
        "A distribuir"
    ]

    valores = [
        ganho_cpv,
        total_variacao_mapeada,
        a_distribuir
    ]

    rateio_ganho_cpv = pd.DataFrame({
        "Indicador": linhas,
        "Valor": valores
    })

    return rateio_ganho_cpv
# %%
