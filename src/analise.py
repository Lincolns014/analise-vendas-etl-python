import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# =========================
# 📥 CARREGAMENTO DOS DADOS
# =========================
def carregar_dados():
    df_vendas = pd.read_csv("data/vendas_tech.csv", low_memory=False)
    df_gerentes = pd.read_excel("data/gerentes_lojas.xlsx")
    return df_vendas, df_gerentes


# =========================
# 🧹 LIMPEZA E TRATAMENTO
# =========================
def tratar_dados(df_vendas, df_gerentes):

    df = df_vendas.copy()

    # remover coluna desnecessária
    if "Data_Base" in df.columns:
        df = df.drop(columns=["Data_Base"])

    # tratar valores nulos
    df["Loja"] = df["Loja"].fillna("Online")

    # converter datas
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce")

    # padronizar texto
    df["Loja"] = df["Loja"].str.strip().str.title()
    df_gerentes["Loja"] = df_gerentes["Loja"].str.strip().str.title()

    # remover linhas com data inválida
    df = df.dropna(subset=["Data"])

    # remover duplicados
    df = df.drop_duplicates(subset=["ID_Pedido"])

    return df, df_gerentes


# =========================
# 📊 FEATURE ENGINEERING
# =========================
def criar_features(df):

    # faturamento
    df["Faturamento"] = df["Qtd"] * df["Preco_Unitario"]

    # tipo de venda
    df["Forma_de_Venda"] = np.where(df["Loja"] == "Online", "Online", "Presencial")

    # regiões
    dic_regioes = {
        "São Paulo": "Sudeste",
        "Belo Horizonte": "Sudeste",
        "Rio De Janeiro": "Sudeste",
        "Salvador": "Nordeste",
        "Recife": "Nordeste",
        "Curitiba": "Sul",
        "Porto Alegre": "Sul",
        "Online": "Online"
    }

    df["Região"] = df["Loja"].map(dic_regioes)

    return df


# =========================
# 📈 ANÁLISES + OUTPUTS
# =========================
def gerar_analises(df):

    # garantir pasta de saída
    os.makedirs("outputs", exist_ok=True)

    # ordenar dados
    df = df.sort_values(by=["Data", "Faturamento"]).reset_index(drop=True)

    # ranking de lojas
    ranking_lojas = (
        df.groupby("Loja")["Faturamento"]
        .sum()
        .sort_values(ascending=False)
    )

    ranking_lojas.to_csv("outputs/ranking_lojas.csv")

    # vendas por mês
    df["Mes"] = df["Data"].dt.month
    vendas_mes = df.groupby("Mes")["Faturamento"].sum()

    # =========================
    # 📊 GRÁFICO 1: LOJAS
    # =========================
    plt.figure()
    ranking_lojas.plot(kind="bar")
    plt.title("Faturamento por Loja")
    plt.xlabel("Loja")
    plt.ylabel("Faturamento")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/faturamento_lojas.png")
    plt.close()

    # =========================
    # 📈 GRÁFICO 2: MÊS
    # =========================
    plt.figure()
    vendas_mes.plot()
    plt.title("Evolução de Vendas por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Faturamento")
    plt.tight_layout()
    plt.savefig("outputs/vendas_mes.png")
    plt.close()

    return df, ranking_lojas, vendas_mes


# =========================
# 🚀 EXECUÇÃO PRINCIPAL
# =========================
def main():

    print("📥 Carregando dados...")
    df_vendas, df_gerentes = carregar_dados()

    print("🧹 Tratando dados...")
    df, df_gerentes = tratar_dados(df_vendas, df_gerentes)

    print("⚙️ Criando features...")
    df = criar_features(df)

    print("📊 Gerando análises...")
    df, ranking_lojas, vendas_mes = gerar_analises(df)

    print("\n🏆 Top 5 lojas por faturamento:")
    print(ranking_lojas.head())

    print("\n📈 Vendas por mês:")
    print(vendas_mes)

    print("\n📁 Arquivos gerados em /outputs")
    print("✅ Processo finalizado!")


if __name__ == "__main__":
    main()