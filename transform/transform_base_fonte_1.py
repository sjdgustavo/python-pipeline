# %% 
import pandas as pd

# %% Função para gerar o df com a coluna "Fonte Ajustada"
def gerar_base_rateio(base_fonte_1: pd.DataFrame) -> pd.DataFrame:
    
    base_rateio = base_fonte_1.copy()

    # Invertendo o sinal das colunas
    colunas_negativas = ["$ Imposto Calculado", "$ Custo Reposição", "$ CPV Preço Interno"]
    base_rateio[colunas_negativas] = base_rateio[colunas_negativas] * -1

    # Alterando a regra de negócio da coluna Coleção
    def ajuste_colecao(row):
        if row["Artigo Estação Cod"] == "125" and row["Coleção"] == "Atual":
            if row["Tipo Transação"] == "Faturamento":
                return "Antiga"
            elif row["Tipo Transação"] == "Devolução":
                return "Atual"
        return row["Coleção"]
    
    base_rateio["Coleção"] = base_rateio.apply(ajuste_colecao, axis=1)

    base_rateio["Dados"] = "Base"

    selecionando_cols = ['Dados', 'Mês-Ano', 'Tipo Venda', 'Tipo Transação', 'Canal_Projeção', 'Loja Ponto Venda', 'Marca',
        'Coleção', 'Fonte', 'Produto Cód', 'ProdutoPiramide_Atual', 'Estação', '# Peças', '$ Receita', '$ Imposto Calculado',
        '$ Custo Reposição', '$ CPV Preço Interno']
    base_rateio = base_rateio[selecionando_cols]

    return base_rateio

             

# %%
