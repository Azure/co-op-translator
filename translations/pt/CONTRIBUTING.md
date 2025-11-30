<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T10:50:58+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pt"
}
-->
# Contribuir para o Co-op Translator

Este projeto aceita contribuições e sugestões. A maioria das contribuições requer que concorde com um Acordo de Licença de Contribuidor (CLA) declarando que tem o direito e efetivamente concede-nos os direitos para usar a sua contribuição. Para mais detalhes, visite https://cla.opensource.microsoft.com.

Quando submeter um pull request, um bot de CLA determinará automaticamente se precisa fornecer um CLA e decorará o PR adequadamente (por exemplo, verificação de estado, comentário). Basta seguir as instruções fornecidas pelo bot. Só precisará fazer isto uma vez para todos os repositórios que usam o nosso CLA.

## Configuração do ambiente de desenvolvimento

Para configurar o ambiente de desenvolvimento deste projeto, recomendamos usar o Poetry para gerir dependências. Usamos o `pyproject.toml` para gerir as dependências do projeto, pelo que deve usar o Poetry para instalar as dependências.

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

### Instalar o pacote e as dependências necessárias

#### Usando Poetry (a partir do pyproject.toml)

```bash
poetry install
```

### Testes manuais

Antes de submeter um PR, é importante testar a funcionalidade de tradução com documentação real:

1. Crie um diretório de teste na raiz do projeto:
    ```bash
    mkdir test_docs
    ```

2. Copie alguma documentação em markdown e imagens que queira traduzir para o diretório de teste. Por exemplo:
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

5. Verifique os ficheiros traduzidos em `test_docs/translations` e `test_docs/translated_images` para confirmar:
   - A qualidade da tradução
   - Os comentários de metadados estão corretos
   - A estrutura original do markdown está preservada
   - Os links e imagens funcionam corretamente

Este teste manual ajuda a garantir que as suas alterações funcionam bem em cenários reais.

### Variáveis de ambiente

1. Crie um ficheiro `.env` na raiz do projeto copiando o ficheiro `.env.template` fornecido.
1. Preencha as variáveis de ambiente conforme indicado.

> [!TIP]
>
> ### Opções adicionais para o ambiente de desenvolvimento
>
> Para além de executar o projeto localmente, pode também usar GitHub Codespaces ou VS Code Dev Containers como alternativa para configurar o ambiente de desenvolvimento.
>
> #### GitHub Codespaces
>
> Pode executar estes exemplos virtualmente usando GitHub Codespaces, sem necessidade de configurações adicionais.
>
> O botão abrirá uma instância do VS Code baseada na web no seu navegador:
>
> 1. Abra o template (isto pode demorar alguns minutos):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Executar localmente usando VS Code Dev Containers
>
> ⚠️ Esta opção só funciona se o seu Docker Desktop tiver pelo menos 16 GB de RAM alocados. Se tiver menos de 16 GB, pode tentar a opção [GitHub Codespaces](../..) ou [configurar localmente](../..).
>
> Uma opção relacionada é usar VS Code Dev Containers, que abrirá o projeto no seu VS Code local usando a [extensão Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Inicie o Docker Desktop (instale-o se ainda não estiver instalado)
> 2. Abra o projeto:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Estilo de Código

Usamos o [Black](https://github.com/psf/black) como formatador de código Python para manter um estilo consistente em todo o projeto. O Black é um formatador de código inflexível que reformata automaticamente o código Python para conformar ao estilo Black.

#### Configuração

A configuração do Black está especificada no nosso `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalar o Black

Pode instalar o Black usando Poetry (recomendado) ou pip:

##### Usando Poetry

O Black é instalado automaticamente quando configura o ambiente de desenvolvimento:
```bash
poetry install
```

##### Usando pip

Se usar pip, pode instalar o Black diretamente:
```bash
pip install black
```

#### Usar o Black

##### Com Poetry

1. Formate todos os ficheiros Python do projeto:
    ```bash
    poetry run black .
    ```

2. Formate um ficheiro ou diretório específico:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Com pip

1. Formate todos os ficheiros Python do projeto:
    ```bash
    black .
    ```

2. Formate um ficheiro ou diretório específico:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Recomendamos configurar o seu editor para formatar automaticamente o código com Black ao guardar. A maioria dos editores modernos suporta isto através de extensões ou plugins.

## Executar o Co-op Translator

Para executar o Co-op Translator usando Poetry no seu ambiente, siga estes passos:

1. Navegue até ao diretório onde pretende realizar os testes de tradução ou crie uma pasta temporária para esse efeito.

2. Execute o seguinte comando. Substitua `-l ko` pelo código da língua para a qual deseja traduzir. A flag `-d` indica modo de depuração.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Certifique-se de que o ambiente Poetry está ativado (poetry shell) antes de executar o comando.

## Contribuir com uma nova língua

Aceitamos contribuições que adicionem suporte a novas línguas. Antes de abrir um PR, por favor complete os passos abaixo para garantir uma revisão tranquila.

1. Adicione a língua ao mapeamento de fontes
   - Edite `src/co_op_translator/fonts/font_language_mappings.yml`
   - Adicione uma entrada com:
     - `code`: código da língua tipo ISO (ex.: `vi`)
     - `name`: nome amigável para exibição
     - `font`: uma fonte incluída em `src/co_op_translator/fonts/` que suporte o alfabeto
     - `rtl`: `true` se for da direita para a esquerda, caso contrário `false`

2. Inclua os ficheiros de fonte necessários (se aplicável)
   - Se for necessária uma nova fonte, verifique a compatibilidade da licença para distribuição open source
   - Adicione o ficheiro da fonte em `src/co_op_translator/fonts/`

3. Verificação local
   - Execute traduções para uma pequena amostra (Markdown, imagens e notebooks conforme apropriado)
   - Verifique se a saída é renderizada corretamente, incluindo fontes e qualquer layout RTL se aplicável

4. Atualize a documentação
   - Assegure que a língua aparece em `getting_started/supported-languages.md`
   - Não é necessário alterar `getting_started/README_languages_template.md`; este é gerado a partir da lista suportada

5. Abra um PR
   - Descreva a língua adicionada e quaisquer considerações sobre fontes/licenciamento
   - Anexe capturas de ecrã da saída renderizada, se possível

Exemplo de entrada YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Testar a nova língua

Pode testar a nova língua executando o seguinte comando:

```bash
# Criar e ativar um ambiente virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instalar o pacote de desenvolvimento
pip install -e .
# Executar a tradução
translate -l "new_lang"
```

## Mantenedores

### Mensagem de commit e estratégia de merge

Para garantir consistência e clareza no histórico de commits do nosso projeto, seguimos um formato específico para a mensagem de commit **na mensagem final** quando usamos a estratégia **Squash and Merge**.

Quando um pull request (PR) é mergeado, os commits individuais são combinados num único commit. A mensagem final deve seguir o formato abaixo para manter um histórico limpo e consistente.

#### Formato da mensagem de commit (para squash and merge)

Usamos o seguinte formato para mensagens de commit:

```bash
<type>: <description> (#<número do PR>)
```

- **type**: Especifica a categoria do commit. Usamos os seguintes tipos:
  - `Docs`: Para atualizações de documentação.
  - `Build`: Para alterações relacionadas com o sistema de build ou dependências, incluindo atualizações a ficheiros de configuração, workflows CI, ou Dockerfile.
  - `Core`: Para modificações na funcionalidade ou características principais do projeto, especialmente aquelas envolvendo ficheiros na pasta `src/co_op_translator/core`.

- **description**: Um resumo conciso da alteração.
- **PR number**: O número do pull request associado ao commit.

**Exemplos**:

- `Docs: Atualizar instruções de instalação para maior clareza (#50)`
- `Core: Melhorar o tratamento da tradução de imagens (#60)`

> [!NOTE]
> Atualmente, os prefixos **`Docs`**, **`Core`** e **`Build`** são adicionados automaticamente aos títulos dos PRs com base nas etiquetas aplicadas ao código fonte modificado. Desde que a etiqueta correta seja aplicada, normalmente não precisa de atualizar manualmente o título do PR. Só precisa de verificar se está tudo correto e se o prefixo foi gerado adequadamente.

#### Estratégia de merge

Usamos **Squash and Merge** como estratégia padrão para pull requests. Esta estratégia assegura que as mensagens de commit seguem o nosso formato, mesmo que os commits individuais não o façam.

**Razões**:

- Um histórico limpo e linear do projeto.
- Consistência nas mensagens de commit.
- Redução de ruído causado por commits menores (ex.: "corrigir erro de digitação").

Ao fazer merge, assegure que a mensagem final do commit segue o formato descrito acima.

**Exemplo de Squash and Merge**
Se um PR contiver os seguintes commits:

- `corrigir erro de digitação`
- `atualizar README`
- `ajustar formatação`

Devem ser combinados em:
`Docs: Melhorar clareza e formatação da documentação (#65)`

### Processo de lançamento

Esta secção descreve a forma mais simples para os mantenedores publicarem uma nova versão do Co-op Translator.

#### 1. Atualizar a versão no `pyproject.toml`

1. Decida o próximo número de versão (seguimos versionamento semântico: `MAJOR.MINOR.PATCH`).
2. Edite o `pyproject.toml` e atualize o campo `version` em `[tool.poetry]`.
3. Abra um pull request dedicado que apenas altere a versão (e quaisquer ficheiros de bloqueio/metadados atualizados automaticamente, se existirem).
4. Após revisão, use **Squash and Merge** e assegure que a mensagem final do commit segue o formato descrito acima.

#### 2. Criar um Release no GitHub

1. Vá à página do repositório no GitHub e abra **Releases** → **Draft a new release**.
2. Crie uma nova tag (por exemplo, `v0.13.0`) a partir da branch `main`.
3. Defina o título do release com a mesma versão (por exemplo, `v0.13.0`).
4. Clique em **Generate release notes** para preencher automaticamente o changelog.
5. Opcionalmente, edite o texto (por exemplo, para destacar novas línguas suportadas ou alterações importantes).
6. Publique o release.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->