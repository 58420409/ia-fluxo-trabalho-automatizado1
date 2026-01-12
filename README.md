[![Python CI - Testes Automatizados](https://github.com/58420409/ia-fluxo-trabalho-automatizado1/actions/workflows/python-tests.yml/badge.svg)](https://github.com/58420409/ia-fluxo-trabalho-automatizado1/actions/workflows/python-tests.yml)

# IA na prática: Acelerando o desenvolvimento e garantindo a qualidade com um fluxo de trabalho automatizado por IA

## 📌 Contexto e Desafio do Projeto

Este projeto foi desenvolvido como trabalho acadêmico com o objetivo de analisar e demonstrar, de forma prática, como ferramentas de Inteligência Artificial podem ser utilizadas para equilibrar **velocidade de entrega** e **qualidade de software** em equipes de desenvolvimento.

O cenário simulado representa uma empresa que desenvolve uma ferramenta de colaboração online e enfrenta dificuldades no seu fluxo de trabalho de engenharia de software.

### 🔍 Problema Identificado

A equipe de desenvolvimento enfrenta um dilema recorrente:

- Quando prioriza **velocidade**, a cobertura de testes diminui e a quantidade de bugs aumenta;
- Quando prioriza **qualidade**, com testes e revisões detalhadas, os prazos do roadmap não são cumpridos.

Esse problema se intensificou no último trimestre, após uma campanha de marketing que prometeu novas funcionalidades em curto prazo, aumentando a pressão sobre a equipe técnica.

### 👥 Perfil da Equipe

- Desenvolvedores de nível **júnior e pleno**;
- Conhecimento técnico adequado, porém com resistência à escrita de testes automatizados;
- Processo de **code review manual lento**, tornando-se um gargalo.

### ⚠️ Principais Gargalos do Fluxo Atual

1. **Desenvolvimento Lento**  
   Muito tempo gasto com código repetitivo para criação de componentes, APIs e estruturas básicas.

2. **Baixa Cobertura de Testes**  
   Testes unitários são escritos de forma inconsistente, pois são vistos como um atraso no desenvolvimento.

3. **Ciclo de Feedback Tardio**  
   Bugs são identificados apenas em fases avançadas (QA manual ou produção).

4. **Inconsistência no Código**  
   Soluções diferentes para problemas semelhantes, aumentando a complexidade da base de código.

---

## 🤖 O Papel da Inteligência Artificial no Desenvolvimento de Software

A Inteligência Artificial tem se tornado uma aliada estratégica no desenvolvimento moderno de software, atuando principalmente em três frentes:

### 🧠 Geração de Código

Ferramentas como o **GitHub Copilot** auxiliam desenvolvedores na criação de funções, componentes e estruturas básicas, reduzindo o tempo gasto com código repetitivo e acelerando o desenvolvimento.

### 🧪 Geração de Testes Automatizados

A IA pode sugerir e gerar testes unitários de forma assistida, incentivando boas práticas de qualidade e aumentando a cobertura de testes sem impactar negativamente a produtividade da equipe.

### 🔁 Integração Contínua (CI/CD)

Com o uso do **GitHub Actions**, é possível automatizar a execução de testes a cada alteração no código, garantindo feedback rápido e reduzindo o risco de bugs em produção.

---

## 🧩 Solução Proposta

A solução apresentada neste projeto combina duas ferramentas principais:

- **GitHub Copilot**: utilizado para acelerar o desenvolvimento de funcionalidades e a geração de testes automatizados.
- **GitHub Actions**: utilizado para criar um pipeline de Integração Contínua (CI), responsável por executar automaticamente os testes a cada push no repositório.

Essa combinação permite aumentar a velocidade de entrega sem comprometer a qualidade do software.

---

## 🤖 Uso do GitHub Copilot na Prática

O GitHub Copilot foi utilizado como assistente de desenvolvimento para gerar a função principal de negócio responsável pelo cálculo do valor final de pedidos com desconto, bem como seus testes unitários.

Durante a implementação, foram utilizados prompts em linguagem natural para solicitar ao Copilot a criação dos testes automatizados. Esses prompts estão documentados diretamente no código-fonte por meio de comentários, conforme solicitado no desafio.

---

## 🏢 Caso Real de Uso de IA no Desenvolvimento

Segundo a documentação oficial do GitHub, equipes que utilizam o **GitHub Copilot** relataram aumento significativo na velocidade de desenvolvimento, especialmente em tarefas repetitivas, além de maior consistência no código.

O **GitHub Actions** é amplamente utilizado por projetos open source e empresas para automatizar pipelines de testes e deploy, reduzindo erros humanos e aumentando a confiabilidade do software entregue.

Além disso, Martin Fowler, em seu artigo *Test Coverage*, destaca que a qualidade do software não deve ser medida apenas pela quantidade de testes, mas pela relevância e efetividade deles, reforçando a importância da automação no processo de desenvolvimento.

---

## 🛠️ Tecnologias Utilizadas

- Python
- GitHub Copilot
- GitHub Actions
- Pytest
- GitHub

---

## 📂 Estrutura do Repositório

```text
├── app/                 # Código-fonte da aplicação
│   └── pedidos.py
├── tests/               # Testes automatizados
│   └── test_pedidos.py
├── .github/workflows/   # Workflow do GitHub Actions
│   └── python-tests.yml
├── README.md            # Documentação do projeto
