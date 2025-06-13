<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:33:44+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "pt"
}
-->
# Instalar o pacote Co-op translator

O **Co-op Translator** é uma ferramenta de linha de comandos (CLI) concebida para ajudar a traduzir todos os ficheiros markdown e imagens do seu projeto para múltiplos idiomas. Este tutorial irá guiá-lo na configuração do tradutor e na sua execução para vários casos de uso.

### Criar um ambiente virtual

Pode criar um ambiente virtual usando `pip` ou `Poetry`. Escreva um dos seguintes comandos no seu terminal.

#### Usando pip

```bash
python -m venv .venv
```

#### Usando Poetry

```bash
poetry init
```

### Ativar o ambiente virtual

Depois de criar o ambiente virtual, precisa de o ativar. Os passos variam consoante o sistema operativo. Escreva o seguinte comando no seu terminal.

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

1. Se criou o ambiente com o Poetry, escreva o seguinte comando no seu terminal para o ativar.

    ```bash
    poetry shell
    ```

### Instalar o pacote e as dependências necessárias

Depois de configurar e ativar o ambiente virtual, o próximo passo é instalar as dependências necessárias.

### Instalação rápida

Instale o Co-Op Translator via pip

```
pip install co-op-translator
```
Ou 

Instale via Poetry
```
poetry add co-op-translator
```

#### Usando pip (a partir do requirements.txt) se clonou este repositório

![NOTE] Por favor, NÃO faça isto se instalou o co-op translator através da instalação rápida.

1. Se estiver a usar pip, escreva o seguinte comando no seu terminal. Irá instalar automaticamente os pacotes necessários especificados no ficheiro `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Usando Poetry (a partir do pyproject.toml)

1. Se estiver a usar Poetry, escreva o seguinte comando no seu terminal. Irá instalar automaticamente os pacotes necessários especificados no ficheiro `pyproject.toml`:

    ```bash
    poetry install
    ```

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.