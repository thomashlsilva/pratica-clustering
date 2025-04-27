# Análise de Agrupamento Hierárquico - Estatística Multivariada

Este projeto é uma prática didática de **Clustering Hierárquico** baseada no livro **"Análise de Dados Através de Métodos de Estatística Multivariada"** da autora **Sueli Aparecida Mingoti**.

O objetivo principal é aplicar diferentes estratégias de ligação (*linkage*) e métricas de distância para entender como cada combinação influencia na formação dos agrupamentos de amostras.

---

## Sobre os Dados

A matriz `F` representa um conjunto de **8 amostras** com **4 variáveis** cada.  
Após a criação, a matriz foi **transposta** (seguindo a abordagem nxp do livro) e **normalizada** variável a variável para padronizar a escala dos dados.

---

## Metodologia Aplicada

Foi utilizada a função `scipy.cluster.hierarchy.linkage()` para gerar as ligações entre amostras, com variações nos métodos de ligação e tipos de distância:

- **Métodos de Ligação (Linkage) utilizados:**
  - **Single** (Ligação simples)
  - **Complete** (Ligação completa)
  - **Average** (Ligação média)
  - **Centroid** (Centroide)
  - **Ward** (Minimização da variância intragrupo)

- **Métricas de Distância utilizadas:**
  - **Euclidean** (Euclidiana)
  - **Cosine** (Cosseno)
  - **Correlation** (Correlação)
  - **Chebyshev**

*Obs: O código possui um trecho comentado que demonstra a intenção de utilizar a distância de Mahalanobis, mas ela não foi efetivamente usada nos resultados.*

---

## Estrutura de Pastas

- `/average/`
  - Clustering usando método de ligação média com 4 tipos de distância.
  
- `/centroid_ward/`
  - Clustering usando métodos de ligação centroide e Ward (apenas distância euclidiana).
  
- `/complete/`
  - Clustering usando método de ligação completa com 4 tipos de distância.
  
- `/single/`
  - Clustering usando método de ligação simples com 4 tipos de distância.

Cada pasta contém os dendrogramas gerados para as diferentes configurações.

---

## Conclusões (baseadas no exercício)

- Métodos de **ligação simples (single)** tendem a formar agrupamentos alongados, sendo sensíveis a outliers.
- Métodos de **ligação completa (complete)** formam grupos mais compactos e homogêneos.
- Métodos de **ligação média (average)** produzem resultados intermediários, equilibrando a formação dos grupos.
- O método de **Ward** é o mais rigoroso, minimizando a variância dentro dos clusters e favorecendo grupos de tamanhos mais semelhantes.
- O tipo de **distância** influencia diretamente na percepção de similaridade:
  - **Euclidiana** enfatiza diferenças absolutas.
  - **Coseno e Correlação** consideram a direção dos vetores (importante para dados normalizados).
  - **Chebyshev** é extremamente sensível ao maior desvio em qualquer variável.

### Aplicação Didática
Este exercício proporciona:
- A prática da construção de dendrogramas.
- A compreensão visual do impacto dos métodos de ligação e métricas de distância.
- O entendimento prático dos conceitos discutidos teoricamente no livro de Sueli Mingoti.

---

## Como Executar

Certifique-se de ter os seguintes pacotes Python instalados:

```bash
pip install -r requirements.txt
```

Execute o código principal para gerar dendrogramas personalizados.