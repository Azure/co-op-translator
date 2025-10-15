<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "510827ad22a2031a50838919c3594828",
  "translation_date": "2025-10-15T03:00:46+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "pt"
}
-->
# Instalar o pacote Co-op Translator

O **Co-op Translator** é uma ferramenta de linha de comandos (CLI) criada para te ajudar a traduzir todos os ficheiros markdown e imagens do teu projeto para várias línguas. Este tutorial vai guiar-te na configuração do tradutor e na sua utilização em diferentes cenários.

### Criar um ambiente virtual

Podes criar um ambiente virtual usando o `pip` ou o `Poetry`. Escreve um dos seguintes comandos no teu terminal.

#### Usar pip

```bash
python -m venv .venv
```

#### Usar Poetry

```bash
poetry init
```

### Ativar o ambiente virtual

Depois de criares o ambiente virtual, precisas de o ativar. Os passos variam consoante o teu sistema operativo. Escreve o seguinte comando no terminal.

#### Para pip e Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Usar Poetry

1. Se criaste o ambiente com o Poetry, escreve o seguinte comando no terminal para o ativar.

    ```bash
    poetry shell
    ```

### Instalar o pacote e os pacotes necessários

Depois de teres o ambiente virtual pronto e ativo, o próximo passo é instalar as dependências necessárias.

### Instalação rápida

Instala o Co-Op Translator via pip

```
pip install co-op-translator
```
Ou

Instala via poetry
```
poetry add co-op-translator
```

#### Usar pip (a partir do requirements.txt) se clonaste este repositório

> [!NOTE]
> Por favor, NÃO faças isto se instalaste o co-op translator pela instalação rápida.

1. Se estiveres a usar pip, escreve o seguinte comando no terminal. Vai instalar automaticamente os pacotes necessários indicados no ficheiro `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Usar Poetry (a partir do pyproject.toml)

1. Se estiveres a usar Poetry, escreve o seguinte comando no terminal. Vai instalar automaticamente os pacotes necessários indicados no ficheiro `pyproject.toml`:

    ```bash
    poetry install
    ```

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.