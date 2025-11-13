# 🚀 Future Skills Career Advisor (GS 2025.2)

## 💡 Descrição do Projeto

Este projeto foi desenvolvido como parte da **Global Solution 2025.2 - Future at Work** da FIAP, focado em **Ciência da Computação**.

O objetivo é criar um sistema em **Python orientado a objetos** que atue como uma ferramenta inteligente de orientação de carreiras. O sistema organiza e analisa perfis profissionais, simulando uma recomendação de carreiras para o futuro, alinhada ao tema "Future Skills Lab".

O foco é conectar lógica de programação e automação ao desenvolvimento humano e profissional.

### Funcionalidades Principais

* **Modelagem de Dados:** Utiliza classes, listas e dicionários para armazenar dados sobre competências (técnicas e comportamentais) e carreiras.
* **Análise de Perfil:** Permite o cadastro do nome do usuário e o nível (0 a 10) em diversas competências.
* **Geração de Recomendação:** Com base no perfil, o sistema calcula a afinidade e gera recomendações personalizadas indicando as 3 carreiras mais adequadas.

## ✔️ Requisitos Técnicos Mínimos

O projeto atende aos seguintes requisitos técnicos:

* Código desenvolvido em **Python** e organizado em **módulos e classes**.
* Uso de **listas, tuplas e/ou dicionários** para estruturação e análise dos dados.
* Implementação de **classes, atributos e métodos** (`Perfil`, `Competencia`, `Carreira`, `Recomendador`).
* Aplicação de **funções e condicionais** para processar e gerar recomendações.
* Interface textual simples (**CLI**) para interação com o usuário (menu, cadastro, exibição de resultados).

## 📁 Estrutura de Arquivos e Classes

O sistema é dividido em módulos para garantir a organização e a aplicação da Orientação a Objetos:

| Arquivo/Classe | Propósito |
| :--- | :--- |
| `main.py` | Contém o loop principal, o menu CLI, e gerencia o fluxo de criação do perfil e a exibição das recomendações. |
| **`Competencia`** (`competencia.py`) | Modelagem de uma competência individual (nome e nível 0-10). |
| **`Perfil`** (`perfis.py`) | Representa o usuário. Armazena o nome e a lista de objetos `Competencia` do usuário. |
| **`Carreira`** (`carreira.py`) | Modelagem de uma carreira. Armazena o nome e o **dicionário** de competências necessárias. |
| **`Recomendador`** (`recomendador.py`) | Classe que armazena a base de carreiras e implementa a lógica de `recomendar(perfil)`, calculando a afinidade e ordenando os resultados. |

## ⚙️ Instruções de Execução

Para rodar o projeto em ambiente local:

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/TaysirAli/Future-Skills-Career-Advisor/
    cd GS-Python
    ```

2.  **Execute o Arquivo Principal (`main.py`):**
    ```bash
    python main.py
    ```

3.  **Utilize o Menu:** Siga as opções na interface de linha de comando (CLI) para criar um novo perfil e visualizar o *ranking* de carreiras recomendadas.
