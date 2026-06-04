import pandas as pd
import matplotlib.pyplot as plt

caminho = "data/processed/laptop_preco.csv"

df = pd.read_csv(caminho)

print(df.head())

media = df['Preço'].mean()

indice_caro = df['Preço'].idxmax()

indice_barato = df['Preço'].idxmin()

produto_caro = df.loc[indice_caro, 'Produto']
preco_caro = df.loc[indice_caro, 'Preço']

produto_barato = df.loc[indice_barato, 'Produto']
preco_barato = df.loc[indice_barato, 'Preço']

df_barato = df[df["Preço"] < media]

numero_baratos = len(df_barato)

df_sort = df.sort_values(by=["Preço"])

top_5 = df_sort.head(5)

print(top_5)


plt.bar(top_5["Produto"], top_5["Preço"] )

plt.title("Top 5 notebook mais baratos")
plt.xlabel("Produto")
plt.ylabel("Preço")
plt.show()