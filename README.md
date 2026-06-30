# LocalEats - Integração Contínua

Este repositório foi desenvolvido como parte da atividade **PBL 12** da disciplina **Qualidade de Software**, com o objetivo de demonstrar a aplicação de práticas de **Integração Contínua (CI)** utilizando GitHub Actions e testes automatizados.

## Objetivos

- Implementar uma funcionalidade simples (`calculate_total`)
- Criar testes automatizados com **Pytest**
- Configurar um pipeline de **GitHub Actions**
- Automatizar a execução dos testes a cada **push** ou **pull request**
- Demonstrar o uso de **GitHub Issues** para gerenciamento de funcionalidades e defeitos

## Tecnologias utilizadas

- Python 3.12
- Pytest
- GitHub Actions
- GitHub Issues
- Git

## Estrutura do projeto

```text
localeats-integracao-continua/
│
├── .github/
│   └── workflows/
│       └── quality.yml
│
├── tests/
│   └── test_order.py
│
├── app.py
├── requirements.txt
└── README.md
```

## Funcionalidade

A função `calculate_total` realiza o cálculo do valor total de um pedido com base no preço e na quantidade informados.

Exemplo:

```python
calculate_total(20, 3)
# Resultado: 60
```

## Testes Automatizados

Os testes foram implementados utilizando **Pytest**.

Para executá-los localmente:

```bash
python -m pytest
```

## Pipeline de Integração Contínua

O projeto utiliza **GitHub Actions** para executar automaticamente os testes sempre que ocorre um:

- Push na branch `main`
- Pull Request para a branch `main`

O workflow realiza automaticamente:

1. Checkout do repositório
2. Configuração do Python
3. Instalação das dependências
4. Execução dos testes automatizados

## Controle de Qualidade

Este projeto utiliza:

- ✅ GitHub Issues para gerenciamento de tarefas e defeitos
- ✅ Testes automatizados
- ✅ Integração Contínua (CI)
- ✅ GitHub Actions

