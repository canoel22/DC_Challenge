import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

#------------- carrega o banco de dados para visualização --------------------

input_file = './cars_train.csv'
dataset = pd.read_csv(input_file, encoding='UTF-16')
carros = pd.DataFrame(dataset)


#------------- printamos as estatísticas --------------------

describe_carros_df = carros.describe()
print(describe_carros_df)


#------------- printamos os gráficos --------------------

num_columns= describe_carros_df._get_numeric_data().columns
describe_carros_df.reset_index(inplace=True) 
describe_carros_df = describe_carros_df[describe_carros_df['index'] != 'count'] #remove qualquer variável do plot

for i in num_columns:
    try:
        sns.catplot(x="index", y=i, data=describe_carros_df, kind="bar", palette="ch:.25")
        plt.subplots_adjust(top=0.9)
        plt.title(f'{i}')
        plt.show()
    except:
        continue
