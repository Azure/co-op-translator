<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:32:43+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pt"
}
-->
# Contribuindo para o Co-op Translator

Este projeto aceita contribuições e sugestões. A maioria das contribuições exige que você concorde com um Acordo de Licença de Contribuidor (CLA) declarando que você tem o direito e realmente concede a nós os direitos de usar sua contribuição. Para mais detalhes, visite https://cla.opensource.microsoft.com.

Ao enviar um pull request, um bot de CLA determinará automaticamente se você precisa fornecer um CLA e adicionará as marcações apropriadas no PR (por exemplo, verificação de status, comentário). Basta seguir as instruções fornecidas pelo bot. Você só precisará fazer isso uma vez para todos os repositórios que usam nosso CLA.

## Configuração do ambiente de desenvolvimento

Para configurar o ambiente de desenvolvimento deste projeto, recomendamos usar Poetry para gerenciar dependências. Usamos `pyproject.toml` para gerenciar as dependências do projeto, portanto, para instalar as dependências, você deve usar Poetry.

### Criar um ambiente virtual

#### Usando pip

```bash
python -m venv .venv
```

#### Usando Poetry

```bash
poetry init
```

### Ativar o ambiente virtual

#### Para pip e Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Usando Poetry

```bash
poetry shell
```

### Instalando o pacote e os pacotes necessários

#### Usando Poetry (a partir do pyproject.toml)

```bash
poetry install
```

### Testes manuais

Antes de enviar um PR, é importante testar a funcionalidade de tradução com documentação real:

1. Crie um diretório de teste na raiz do projeto:
    ```bash
    mkdir test_docs
    ```

2. Copie alguma documentação em markdown e imagens que deseja traduzir para o diretório de teste. Por exemplo:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Instale o pacote localmente:
    ```bash
    pip install -e .
    ```

4. Execute o Co-op Translator nos seus documentos de teste:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Verifique os arquivos traduzidos em `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template`.
1. Preencha as variáveis de ambiente conforme orientado.

> [!TIP]
>
> ### Opções adicionais para o ambiente de desenvolvimento
>
> Além de executar o projeto localmente, você também pode usar GitHub Codespaces ou VS Code Dev Containers para uma configuração alternativa do ambiente de desenvolvimento.
>
> #### GitHub Codespaces
>
> Você pode executar esses exemplos virtualmente usando GitHub Codespaces, sem necessidade de configurações adicionais.
>
> O botão abrirá uma instância do VS Code baseada na web no seu navegador:
>
> 1. Abra o template (isso pode levar alguns minutos):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Executando localmente usando VS Code Dev Containers
>
> ⚠️ Esta opção funcionará somente se seu Docker Desktop estiver configurado com pelo menos 16 GB de RAM. Se você tiver menos de 16 GB, pode tentar a opção [GitHub Codespaces](../..) ou [configurar localmente](../..).
>
> Uma opção relacionada é usar VS Code Dev Containers, que abrirá o projeto no seu VS Code local utilizando a [extensão Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Inicie o Docker Desktop (instale se ainda não estiver instalado)
> 2. Abra o projeto:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Estilo de Código

Usamos [Black](https://github.com/psf/black) como formatador de código Python para manter um estilo consistente em todo o projeto. Black é um formatador de código rigoroso que reformata automaticamente o código Python para se adequar ao estilo Black.

#### Configuração

A configuração do Black está especificada em nosso `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalando o Black

Você pode instalar o Black usando Poetry (recomendado) ou pip:

##### Usando Poetry

O Black é instalado automaticamente quando você configura o ambiente de desenvolvimento:
```bash
poetry install
```

##### Usando pip

Se estiver usando pip, você pode instalar o Black diretamente:
```bash
pip install black
```

#### Usando o Black

##### Com Poetry

1. Formate todos os arquivos Python no projeto:
    ```bash
    poetry run black .
    ```

2. Formate um arquivo ou diretório específico:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Com pip

1. Formate todos os arquivos Python no projeto:
    ```bash
    black .
    ```

2. Formate um arquivo ou diretório específico:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Recomendamos configurar seu editor para formatar o código automaticamente com Black ao salvar. A maioria dos editores modernos suporta isso via extensões ou plugins.

## Executando o Co-op Translator

Para executar o Co-op Translator usando Poetry no seu ambiente, siga estes passos:

1. Navegue até o diretório onde deseja realizar os testes de tradução ou crie uma pasta temporária para esse fim.

2. Execute o comando abaixo. A flag `-l ko` with the language code you wish to translate into. The `-d` indica o modo debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Certifique-se de que seu ambiente Poetry esteja ativado (poetry shell) antes de rodar o comando.

## Mantenedores

### Mensagem de commit e estratégia de Merge

Para garantir consistência e clareza no histórico de commits do projeto, seguimos um formato específico para a mensagem de commit **no commit final** quando usamos a estratégia **Squash and Merge**.

Quando um pull request (PR) é mesclado, os commits individuais serão agrupados em um único commit. A mensagem final desse commit deve seguir o formato abaixo para manter um histórico limpo e consistente.

#### Formato da mensagem de commit (para squash and merge)

Usamos o seguinte formato para mensagens de commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Especifica a categoria do commit. Usamos os seguintes tipos:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Atualizar instruções de instalação para maior clareza (#50)`
- `Core: Melhorar o tratamento da tradução de imagens (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `corrigir erro de digitação`
- `atualizar README`
- `ajustar formatação`

They should be squashed into:
`Docs: Melhorar clareza e formatação da documentação (#65)`

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.