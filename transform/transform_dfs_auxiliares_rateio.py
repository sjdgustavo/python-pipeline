# %%
import pandas as pd
# %%
def gerar_df_custo_rep_canal(base_rateio: pd.DataFrame) -> pd.DataFrame:
    
    digital_custo_rep = base_rateio.loc[base_rateio["Canal_Projeção"] == "Digital", "$ Custo Reposição"].sum()
    franquias_custo_rep = base_rateio.loc[base_rateio["Canal_Projeção"] == "Franquias", "$ Custo Reposição"].sum()
    lp_custo_rep = base_rateio.loc[base_rateio["Canal_Projeção"] == "Lojas Próprias", "$ Custo Reposição"].sum()
    mi_custo_rep = base_rateio.loc[base_rateio["Canal_Projeção"] == "Mercado Internacional", "$ Custo Reposição"].sum()
    multimarcas_custo_rep = base_rateio.loc[base_rateio["Canal_Projeção"] == "Multimarcas", "$ Custo Reposição"].sum()
    outras_custo_rep = base_rateio.loc[base_rateio["Canal_Projeção"] == "Outras Vendas", "$ Custo Reposição"].sum()
    total_custo_rep = base_rateio["$ Custo Reposição"].sum()

    canal = [
        "Digital",
        "Franquias",
        "Lojas Próprias",
        "Mercado Internacional",
        "Multimarcas",
        "Outras Vendas",
        "Total"
    ]

    valores = [
        digital_custo_rep,
        franquias_custo_rep,
        lp_custo_rep,
        mi_custo_rep,
        multimarcas_custo_rep,
        outras_custo_rep,
        total_custo_rep
    ]

    df_custo_rep_canal = pd.DataFrame({
        "Canal": canal,
        "Soma de Custo Reposição": valores
    })

    return df_custo_rep_canal

# %%
def gerar_df_receita_canal(base_rateio: pd.DataFrame) -> pd.DataFrame:

    digital_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Digital"),
        "$ Receita"
    ].sum()
    franquias_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Franquias"),
        "$ Receita"
    ].sum()
    lp_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Lojas Próprias"),
        "$ Receita"
    ].sum()
    mi_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Mercado Internacional"),
        "$ Receita"
    ].sum()
    multimarcas_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Multimarcas"),
        "$ Receita"
    ].sum()
    outras_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Outras Vendas"),
        "$ Receita"
    ].sum()
    total_receita = base_rateio.loc[base_rateio["Dados"] == "Base", "$ Receita"].sum()

    canal = [
        "Digital",
        "Franquias",
        "Lojas Próprias",
        "Mercado Internacional",
        "Multimarcas",
        "Outras Vendas",
        "Total"
    ]

    valores = [
        digital_receita,
        franquias_receita,
        lp_receita,
        mi_receita,
        multimarcas_receita,
        outras_receita,
        total_receita
    ]

    df_receita_canal = pd.DataFrame({
        "Canal": canal,
        "Soma de Receita": valores
    })

    return df_receita_canal

# %% 
def gerar_df_custo_rep_fonte_base(base_rateio: pd.DataFrame) -> pd.DataFrame:

    eng_custo_rep_base = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Fonte"] == "ENG"),
        "$ Custo Reposição"
    ].sum()
    si_custo_rep_base = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Fonte"] == "SI"),
     "$ Custo Reposição"
    ].sum()
    sn_custo_rep_base = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Fonte"] == "SN"),
        "$ Custo Reposição"
    ].sum()
    total_custo_rep_fonte_base = base_rateio.loc[base_rateio["Dados"] == "Base", "$ Custo Reposição"].sum()

    fonte = [
    "ENG",
    "SI",
    "SN",
    "Total"
    ]

    valores = [
    eng_custo_rep_base,
    si_custo_rep_base,
    sn_custo_rep_base,
    total_custo_rep_fonte_base
    ]

    df_custo_rep_fonte_base = pd.DataFrame({
    "Fonte": fonte,
    "Soma de Custo Reposição": valores
    })

    return df_custo_rep_fonte_base

def gerar_df_receita_canal_fonte(base_rateio: pd.DataFrame) -> pd.DataFrame:
    sellin_eng_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (~base_rateio["Canal_Projeção"].str.contains("Mercado Internacional", na=False)) &
        (base_rateio["Tipo Venda"] == "Sell In") &
        (base_rateio["Fonte"] == "ENG"),
        "$ Receita"
    ].sum()
    sellin_sn_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (~base_rateio["Canal_Projeção"].str.contains("Mercado Internacional", na=False)) &
        (base_rateio["Tipo Venda"] == "Sell In") &
        (base_rateio["Fonte"] == "SN"),
        "$ Receita"
    ].sum()
    sellin_si_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (~base_rateio["Canal_Projeção"].str.contains("Mercado Internacional", na=False)) &
        (base_rateio["Tipo Venda"] == "Sell In") &
        (base_rateio["Fonte"] == "SI"),
        "$ Receita"
    ].sum()
    digital_eng_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Digital") &
        (base_rateio["Fonte"] == "ENG"),
        "$ Receita"
    ].sum()
    digital_sn_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Digital") &
        (base_rateio["Fonte"] == "SN"),
        "$ Receita"
    ].sum()
    digital_si_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Digital") &
        (base_rateio["Fonte"] == "SI"),
        "$ Receita"
    ].sum()
    lp_eng_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Lojas Próprias") &
        (base_rateio["Fonte"] == "ENG"),
        "$ Receita"
    ].sum()
    lp_sn_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Lojas Próprias") &
        (base_rateio["Fonte"] == "SN"),
        "$ Receita"
    ].sum()
    lp_si_receita = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Lojas Próprias") &
        (base_rateio["Fonte"] == "SI"),
        "$ Receita"
].sum()
    total_receita_canal_fonte = (sellin_eng_receita + sellin_sn_receita + sellin_si_receita +
                            digital_eng_receita + digital_sn_receita + digital_si_receita +
                            lp_eng_receita + lp_sn_receita + lp_si_receita
    )

    canal = [
        "Sell In",
        "Sell In",
        "Sell In",
        "Digital",
        "Digital",
        "Digital",
        "Lojas Próprias",
        "Lojas Próprias",
        "Lojas Próprias",
        "Total"
    ]

    fonte = [
        "ENG",
        "SN",
        "SI",
        "ENG",
        "SN",
        "SI",
        "ENG",
        "SN",
        "SI",
        ""
    ]

    valores = [
        sellin_eng_receita,
        sellin_sn_receita,
        sellin_si_receita,
        digital_eng_receita,
        digital_sn_receita,
        digital_si_receita,
        lp_eng_receita,
        lp_sn_receita,
        lp_si_receita, 
        total_receita_canal_fonte
    ]

    df_receita_canal_fonte = pd.DataFrame({
        "Tipo Venda/Canal": canal,
        "Fonte": fonte,
        "Soma de Receita": valores
    })

    return df_receita_canal_fonte
    
# %% 
def gerar_df_var_mapeada_canal_base(base_rateio: pd.DataFrame) -> pd.DataFrame:
    
    var_mapeada_digital_base = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Digital"),
        "Variação Mapeada"
    ].sum()
    var_mapeada_franquias_base = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Franquias"),
        "Variação Mapeada"
    ].sum()
    var_mapeada_lp_base = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Lojas Próprias"),
        "Variação Mapeada"
    ].sum()
    var_mapeada_mi_base = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Mercado Internacional"),
        "Variação Mapeada"
    ].sum()
    var_mapeada_multimarcas_base = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Multimarcas"),
        "Variação Mapeada"
    ].sum()
    var_mapeada_ov_base = base_rateio.loc[
        (base_rateio["Dados"] == "Base") &
        (base_rateio["Canal_Projeção"] == "Outras Vendas"),
        "Variação Mapeada"
    ].sum()
    var_mapeada_total_base = base_rateio.loc[
        base_rateio["Dados"] == "Base",
        "Variação Mapeada"
    ].sum()

    canal = [
        "Digital",
        "Franquias",
        "Lojas Próprias",
        "Mercado Internacional",
        "Multimarcas",
        "Outras Vendas",
        "Total"
    ]

    valores = [
        var_mapeada_digital_base,
        var_mapeada_franquias_base,
        var_mapeada_lp_base,
        var_mapeada_mi_base,
        var_mapeada_multimarcas_base,
        var_mapeada_ov_base,
        var_mapeada_total_base

    ]

    df_var_mapeada_canal_base = pd.DataFrame({
        "Canal": canal,
        "Soma de Variação Mapeada": valores
    })

    return df_var_mapeada_canal_base
# %%
