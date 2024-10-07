# Ordenação de Notas Fiscais Eletrônicas (NFC-e) utilizando MergeSort

## Objetivo

Este projeto demonstra como coletar, processar e ordenar dados de notas fiscais eletrônicas (NFC-e) extraídos de páginas HTML. Utilizando o algoritmo *MergeSort*, os dados são organizados de acordo com critérios específicos, como CNPJ ou data de emissão.

## Funcionamento

O sistema é composto por três módulos principais:

1. **NFCE.py**: Faz o parsing do HTML da NFC-e para extrair informações como chave de acesso, emissor, itens, resumo e dados gerais. Esses dados são convertidos em formato JSON.
2. **request.py**: Faz requisições HTTP para URLs de NFC-e, processa a resposta HTML com a classe `NFCE` e salva os dados JSON em um arquivo de texto.
3. **mergesort.py**: Implementa o algoritmo *MergeSort* para ordenar os dados das NFC-e, utilizando como critério informações específicas como CNPJ ou data de emissão.

### Diagrama de Funcionamento

```plaintext
+----------------+       +---------------+         +---------------------+
|    request.py   |----->|    NFCE.py     |------->|    mergesort.py      |
| Faz requisição  |       | Faz parsing do|        | Ordena os dados da   |
| HTTP e salva    |       | HTML da NFC-e |        | NFC-e                |
| dados JSON      |       | para JSON     |        |                     |
+----------------+       +---------------+         +---------------------+
```

## Documentação

### **NFCE.py**

A classe `NFCE` é responsável por fazer o parsing de um documento NFC-e em HTML e converter os dados para formato JSON.

#### Métodos:

- **`chave_de_acesso()`**: Extrai a chave de acesso da NFC-e.
- **`emissor()`**: Coleta informações do emissor como nome, CNPJ e endereço.
- **`tabela_itens()`**: Extrai os itens da nota fiscal, incluindo quantidade, valor unitário e valor total.
- **`resumo()`**: Coleta o resumo da nota, como o valor total.
- **`informacoes_gerais_da_nota()`**: Extrai informações gerais da nota, como número e data de emissão.
- **`json_data()`**: Gera e retorna os dados extraídos no formato JSON.

### **request.py**

Faz requisições HTTP para URLs de NFC-e, utiliza a classe `NFCE` para extrair e processar os dados e os salva em um arquivo de texto.

### **mergesort.py**

Implementa o algoritmo *MergeSort* para ordenar os dados das NFC-e.

#### Classes:

- **`File`**: Classe para manipulação de arquivos, com métodos para ler, deletar, obter intervalos de linhas e deletar o arquivo.
- **`MSE`**: Classe para implementar a ordenação dos dados com base no algoritmo *MergeSort*. Ela utiliza uma função de filtragem (`filter`) para determinar o critério de comparação (ex.: CNPJ ou data de emissão).

#### Métodos principais:

- **`mergeSort()`**: Realiza a ordenação recursiva do arquivo.
- **`merge()`**: Mescla dois arquivos ordenados.
- **`sort()`**: Inicia o processo de ordenação e retorna o nome do arquivo ordenado.

### **test_mse.py**

Este arquivo contém funções auxiliares para extrair dados JSON e realizar testes de ordenação com base em diferentes critérios, como:

- **`data_emissao()`**: Extrai a data de emissão da NFC-e.
- **`valor_total()`**: Extrai o valor total da NFC-e.
- **`cnpj()`**: Extrai o CNPJ do emissor.

Os dados são ordenados de acordo com o critério especificado e o resultado é salvo e exibido em formato JSON.

## Como Executar o Projeto

1. Crie um arquivo `urls.txt` com as URLs das NFC-e que deseja processar.
2. Execute o script `request.py` para baixar os dados das NFC-e e salvá-los em um arquivo de texto.
3. Execute o script `test_mse.py` para ordenar os dados das NFC-e e exibir o resultado ordenado.
4. O arquivo de resultado será gerado com os dados ordenados e poderá ser utilizado para outras análises.

## Requisitos

- Python 3.x
- Bibliotecas necessárias:
  - `requests`
  - `BeautifulSoup` (a partir do pacote `bs4`)
  - `lxml`
