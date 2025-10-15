<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:03:11+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "br"
}
-->
# Instale o pacote Co-op Translator

O **Co-op Translator** é uma ferramenta de linha de comando (CLI) criada para ajudar você a traduzir todos os arquivos markdown e imagens do seu projeto para vários idiomas. Este tutorial vai te guiar na configuração do tradutor e na execução dele para diferentes casos de uso.

### Crie um ambiente virtual

Você pode criar um ambiente virtual usando `pip` ou `Poetry`. Digite um dos comandos abaixo no seu terminal.

#### Usando pip

```bash
python -m venv .venv
```

#### Usando Poetry

```bash
poetry init
```

### Ative o ambiente virtual

Depois de criar o ambiente virtual, você precisa ativá-lo. Os passos variam de acordo com o seu sistema operacional. Digite o comando abaixo no seu terminal.

#### Para pip e Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Usando Poetry

1. Se você criou o ambiente com o Poetry, digite o comando abaixo no seu terminal para ativá-lo.

    ```bash
    poetry shell
    ```

### Instalando o pacote e os pacotes necessários

Depois de configurar e ativar seu ambiente virtual, o próximo passo é instalar as dependências necessárias.

### Instalação rápida

Instale o Co-Op Translator via pip

```
pip install co-op-translator
```
Ou 

Instale via poetry
```
poetry add co-op-translator
```

#### Usando pip (a partir do requirements.txt) se você clonou este repositório

> [!NOTE]
> Por favor, NÃO faça isso se você instalou o co-op translator pela instalação rápida.

1. Se você estiver usando pip, digite o comando abaixo no seu terminal. Ele vai instalar automaticamente os pacotes necessários especificados no arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Usando Poetry (a partir do pyproject.toml)

1. Se você estiver usando Poetry, digite o comando abaixo no seu terminal. Ele vai instalar automaticamente os pacotes necessários especificados no arquivo `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.