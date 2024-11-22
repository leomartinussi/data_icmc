# Leonardo José Martinussi
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

class Modelo():
    def __init__(self):
        self.df = None
        self.names = None

    def CarregarDataset(self, path):
        """
        Carrega o conjunto de dados a partir de um arquivo CSV.

        Parâmetros:
        - path (str): Caminho para o arquivo CSV contendo o dataset.
        
        O dataset é carregado com as seguintes colunas: SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm e Species.
        """
        self.names = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
        self.df = pd.read_csv(path, names=self.names)

    def TratamentoDeDados(self):
        """
        Realiza o pré-processamento dos dados carregados.

        Sugestões para o tratamento dos dados:
            * Utilize `self.df.head()` para visualizar as primeiras linhas e entender a estrutura.
            * Verifique a presença de valores ausentes e faça o tratamento adequado.
            * Considere remover colunas ou linhas que não são úteis para o treinamento do modelo.
        
        Dicas adicionais:
            * Explore gráficos e visualizações para obter insights sobre a distribuição dos dados.
            * Certifique-se de que os dados estão limpos e prontos para serem usados no treinamento do modelo.
        """
        self.df.head(6)
        for col in self.df.columns.tolist():
            print('Número de missing na coluna {}: {}'.format(col, self.df[col].isnull().sum()))
        self.df.dropna()
        self.df.info()

        printar = input("Deseja printar imagens? (s/n)")
        if printar == 's':
            contagem = self.df['Species'].value_counts()
            contagem.plot(kind='bar')
            plt.xticks(rotation=0)
            plt.title('Tipos')
            plt.xlabel('Espécies')
            plt.ylabel('Frequência')
            plt.show()

            cores = ['red' if s == 'Iris-versicolor' else s for s in self.df['Species']]
            cores = ['blue' if s == 'Iris-setosa' else s for s in cores]
            cores = ['green' if s == 'Iris-virginica' else s for s in cores]
            plt.scatter(self.df['SepalLengthCm'],self.df['SepalWidthCm'], c = cores)
            plt.title('Sepal')
            plt.xlabel('SepalLengthCm')
            plt.ylabel('SepalWidthCm')
            plt.show()

            plt.scatter(self.df['PetalLengthCm'],self.df['PetalWidthCm'], c = cores)
            plt.title('Petal')
            plt.xlabel('PetalLengthCm')
            plt.ylabel('PetalWidthCm')
            plt.show()

            sns.pairplot(self.df, hue='Species')
            plt.show()

            sns.boxplot(x='Species', y='PetalLengthCm', data=self.df)
            plt.show()

        # remover outliers se der tempo

    def Treinamento(self):
        """
        Treina o modelo de machine learning.

        Detalhes:
            * Utilize a função `train_test_split` para dividir os dados em treinamento e teste.
            * Escolha o modelo de machine learning que queira usar. Lembrando que não precisa ser SMV e Regressão linear.
            * Experimente técnicas de validação cruzada (cross-validation) para melhorar a acurácia final.
        
        Nota: Esta função deve ser ajustada conforme o modelo escolhido.
        """
        self.label_encoder_flor = LabelEncoder()
        # self.y = self.label_encoder_flor.fit_transform(self.y)

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.df.iloc[:, :-1], self.label_encoder_flor.fit_transform(self.df.iloc[:,-1]), test_size=0.35, random_state=42)

        print("""Modelos utilizados:
              1- Random Forest
              2- SVM - kernel linear
              3- SVM - kernel rbf""")

        self.classificadorrf = RandomForestClassifier()
        self.classificadorrf.fit(self.x_train, self.y_train)

        self.classificadorkl = SVC(kernel='linear')
        self.classificadorkl.fit(self.x_train, self.y_train)

        self.classificadorkrbf = SVC(kernel='rbf')
        self.classificadorkrbf.fit(self.x_train, self.y_train)

    def Teste(self):
        """
        Avalia o desempenho do modelo treinado nos dados de teste.

        Esta função deve ser implementada para testar o modelo e calcular métricas de avaliação relevantes, 
        como acurácia, precisão, ou outras métricas apropriadas ao tipo de problema.
        """
        self.y_pred = self.classificadorrf.predict(self.x_test)
        print("Acurácia Random Forest:", accuracy_score(self.y_test, self.y_pred))

        self.y_pred = self.classificadorkl.predict(self.x_test)
        print("Acurácia kernel linear:", accuracy_score(self.y_test, self.y_pred))

        self.y_pred = self.classificadorkrbf.predict(self.x_test)
        print("Acurácia kernel rbf:", accuracy_score(self.y_test, self.y_pred))


    def Train(self):
        """
        Função principal para o fluxo de treinamento do modelo.

        Este método encapsula as etapas de carregamento de dados, pré-processamento e treinamento do modelo.
        Sua tarefa é garantir que os métodos `CarregarDataset`, `TratamentoDeDados` e `Treinamento` estejam implementados corretamente.
        
        Notas:
            * O dataset padrão é "iris.data", mas o caminho pode ser ajustado.
            * Caso esteja executando fora do Colab e enfrente problemas com o path, use a biblioteca `os` para gerenciar caminhos de arquivos.
        """
        self.CarregarDataset("iris.data")  # Carrega o dataset especificado.

        # Tratamento de dados opcional, pode ser comentado se não for necessário
        self.TratamentoDeDados()
        
        self.Treinamento()  # Executa o treinamento do modelo

# Lembre-se de instanciar as classes após definir suas funcionalidades
# Recomenda-se criar ao menos dois modelos (e.g., Regressão Linear e SVM) para comparar o desempenho.
# A biblioteca já importa LinearRegression e SVC, mas outras escolhas de modelo são permitidas.

leo = Modelo()
leo.Train()
leo.Teste()
#print(leo.df)