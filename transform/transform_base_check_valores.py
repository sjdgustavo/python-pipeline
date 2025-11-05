import pandas as pd

# %%
def gerar_base_check_valores(base_fonte_2: pd.DataFrame, base_fonte_3: pd.DataFrame, base_ajuste_valor: pd.DataFrame) -> pd.DataFrame:
    
    # Funções auxiliares para somar valores com condições
    def somasesnotin(df, col_soma, col_cond, conds):
        mask = ~df[col_cond].isin(conds)
        return df.loc[mask, col_soma].sum()
    
    def somasestr(df, col_soma, col_cond, cond):
        return df[df[col_cond].str.contains(cond)][col_soma].sum()
    
    # Cálculo dos valores para o Base Check Valores

    receita_bruta = somasesnotin(base_fonte_2, "$ Receitas", "Canal Comercial", ["Intercompany", "Private Label"])
    impostos = -somasesnotin(base_fonte_2, "$ Impostos Total", "Canal Comercial", ["Intercompany", "Private Label"])
    abatimentos = somasestr(base_fonte_3, "Real", "Abertura_Lucro_Bruto", "03_Abatimentos_e_TMD")
    impostos_gn99 = somasestr(base_fonte_3, "Real", "Abertura_Lucro_Bruto", "03.1")
    incentivos_producao = somasestr(base_fonte_3, "Real", "Abertura_Lucro_Bruto", "04")
    receita_liquida = receita_bruta + impostos + abatimentos + incentivos_producao
    cpv_reposicao = -somasesnotin(base_fonte_2, "$ Custo Reposição", "Canal Comercial", ["Intercompany", "Private Label"])
    variacao_fabrica = somasestr(base_fonte_3, "Real", "Abertura_Lucro_Bruto", "Variação_de_Fábrica")
    custo_rep_ic = base_fonte_2.loc[base_fonte_2["Canal Comercial"] == "Intercompany", "$ Custo Reposição"].sum()
    custo_int_ic = base_fonte_2.loc[base_fonte_2["Canal Comercial"] == "Intercompany", "$ CPV Preço Interno"].sum()
    crossdocking = base_ajuste_valor.loc[base_ajuste_valor["Indicador"] == "Crossdocking", "Valor"].sum() 
    ganho_cpv = variacao_fabrica - (custo_rep_ic - custo_int_ic) - crossdocking
    provisao_obsoleto = somasestr(base_fonte_3, "Real", "Abertura_Lucro_Bruto", "07")
    incentivos_custo = somasestr(base_fonte_3, "Real", "Abertura_Lucro_Bruto", "08")
    avp_cpv = somasestr(base_fonte_3, "Real", "Abertura_Lucro_Bruto", "09")
    custo_fixo = somasestr(base_fonte_3, "Real", "Abertura_Lucro_Bruto", "Custo_Fixo")
    lucro_bruto = receita_liquida + cpv_reposicao + ganho_cpv + provisao_obsoleto + incentivos_custo + avp_cpv + custo_fixo
    margem_bruta = lucro_bruto / receita_liquida if receita_liquida else 0 

    linhas = [
        "Receita Bruta",
        "Impostos",
        "Abatimentos e TMD",
        "Impostos GN99",
        "Incentivos Fiscais Produção",
        "Receita Líquida",
        "CPV Reposição",
        "Ganho de CPV",
        "Provisão para Obsoleto",
        "Incentivos Fiscais Custo",
        "AVP CPV",
        "(-) CPV indireto (Custo Fixo)",
        "Lucro Bruto",
        "Margem Bruta"

    ]

    valores = [
        receita_bruta,
        impostos,
        abatimentos,
        impostos_gn99,
        incentivos_producao,
        receita_liquida,
        cpv_reposicao,
        ganho_cpv,
        provisao_obsoleto,
        incentivos_custo,
        avp_cpv,
        custo_fixo,
        lucro_bruto,
        margem_bruta
    ]

    base_check_valores = pd.DataFrame({
        "DRE Base": linhas,
        "Real": valores
    })

    return base_check_valores
# %%
