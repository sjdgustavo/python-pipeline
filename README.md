# 🧮 Python Pipeline — Rateio Automatizado de Dados Financeiros

## 📘 Descrição  
Este projeto tem como objetivo **automatizar o processo de rateio de valores** entre categorias e canais de vendas, gerando **novas colunas calculadas** em planilhas Excel.  

O fluxo foi desenvolvido em **Python** para substituir um processo anteriormente feito em **Excel**, que demandava tempo elevado e trabalhava com pouca performance.  
Com o novo pipeline, o cálculo é feito em segundos e de forma totalmente automatizada.  

---

## ⚙️ Estrutura do Projeto  

```bash
python-pipeline/
├── data/                  # Pasta de entrada (arquivos .xlsx do usuário)
│   ├── 042025/            # Mês de referência
│   ├── 052025/
├── export/                # Pasta de saída (arquivos processados)
│   ├── 042025/
│   ├── 052025/
├── load/                  # Etapa de ingestão de dados
│   ├── load_base_fonte_1.py
│   ├── load_base_fonte_2.py
│   ├── load_base_fonte_3.py
│   ├── load_base_ajuste_valor.py
├── transform/             # Etapa de transformação e rateio
│   ├── transform_base_check_valores.py
│   ├── transform_base_fonte_1.py
│   ├── transform_colunas_base_rateio.py
│   ├── transform_dfs_auxiliares_rateio.py
│   ├── transform_dfs_rateios.py
├── config.py              # Configurações de caminhos e parâmetros
├── main.py                # Script principal que orquestra o fluxo
└── README.md
