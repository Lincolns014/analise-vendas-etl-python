# 📊 Análise de Vendas - Tech (Pipeline ETL com Python)

## 📌 Descrição

Projeto de análise de dados que simula um cenário real de uma empresa de tecnologia, utilizando um pipeline ETL completo para ingestão, tratamento, transformação e geração de insights.

## 🎯 Objetivo

Identificar padrões de vendas, desempenho das lojas e comportamento ao longo do tempo para apoiar a tomada de decisão.

## ⚙️ Pipeline ETL

* Extração de dados (CSV e Excel)
* Tratamento e limpeza de dados
* Criação de métricas (faturamento, região, tipo de venda)
* Geração de análises e visualizações

## 🛠️ Tecnologias

* Python
* Pandas
* NumPy
* Matplotlib

## 📊 Resultados

### 🏆 Ranking de lojas

Arquivo gerado automaticamente com o faturamento por loja.

### 📈 Evolução de vendas

Gráfico mostrando comportamento mensal das vendas.

## 🧠 Insights

* Salvador e Rio de Janeiro lideram o faturamento
* Distribuição equilibrada entre lojas
* Picos de vendas em outubro
* Sazonalidade identificada em fevereiro e novembro

## 🚀 Como executar

```bash
pip install -r requirements.txt
python src/analise.py
```

## 📁 Outputs gerados

* ranking_lojas.csv
* faturamento_lojas.png
* vendas_mes.png

## 📌 Próximos passos

* Integração com banco de dados (SQL)
* Criação de dashboard no Power BI
* Automatização do pipeline (agendamento)
