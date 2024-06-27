
import seaborn as sns
import matplotlib.pyplot as plt

def create_corr_matrix(data):
    corr = data.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

def create_distplot(data, column):
    sns.displot(data, x=column, hue="Weight_Category", kind='kde', height=6, aspect=1.5)
    plt.title(f'Distribution of {column}')
    plt.show()

def create_hist(data, x, hue):
    sns.countplot(data=data, x=x, hue=hue)
    plt.title(f'Count Plot of {x}')
    plt.xticks(rotation=45)
    plt.show()
