<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "758ca1c5ae0d32c52d2dd59132dcfbf0",
  "translation_date": "2025-11-30T10:54:14+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "br"
}
-->
# Contribuindo para o Co-op Translator

Este projeto aceita contribuições e sugestões. A maioria das contribuições exige que você concorde com um Acordo de Licença de Contribuidor (CLA) declarando que você tem o direito e realmente concede a nós os direitos para usar sua contribuição. Para mais detalhes, visite https://cla.opensource.microsoft.com.

Quando você enviar um pull request, um bot de CLA determinará automaticamente se você precisa fornecer um CLA e marcará o PR adequadamente (por exemplo, verificação de status, comentário). Basta seguir as instruções fornecidas pelo bot. Você precisará fazer isso apenas uma vez para todos os repositórios que usam nosso CLA.

## Configuração do ambiente de desenvolvimento

Para configurar o ambiente de desenvolvimento deste projeto, recomendamos usar o Poetry para gerenciar dependências. Usamos o `pyproject.toml` para gerenciar as dependências do projeto, portanto, para instalar as dependências, você deve usar o Poetry.

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

### Instalando o pacote e pacotes necessários

#### Usando Poetry (a partir do pyproject.toml)

```bash
poetry install
```

### Teste manual

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

5. Verifique os arquivos traduzidos em `test_docs/translations` e `test_docs/translated_images` para confirmar:
   - A qualidade da tradução
   - Os comentários de metadados estão corretos
   - A estrutura original do markdown foi preservada
   - Os links e imagens funcionam corretamente

Esse teste manual ajuda a garantir que suas alterações funcionem bem em cenários reais.

### Variáveis de ambiente

1. Crie um arquivo `.env` na raiz do projeto copiando o arquivo `.env.template` fornecido.
1. Preencha as variáveis de ambiente conforme indicado.

> [!TIP]
>
> ### Opções adicionais para ambiente de desenvolvimento
>
> Além de executar o projeto localmente, você também pode usar GitHub Codespaces ou VS Code Dev Containers como uma alternativa para configurar o ambiente de desenvolvimento.
>
> #### GitHub Codespaces
>
> Você pode executar estes exemplos virtualmente usando GitHub Codespaces, sem necessidade de configurações adicionais.
>
> O botão abrirá uma instância do VS Code baseada na web no seu navegador:
>
> 1. Abra o template (isso pode levar alguns minutos):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### Executando localmente usando VS Code Dev Containers
>
> ⚠️ Esta opção só funcionará se seu Docker Desktop estiver alocado com pelo menos 16 GB de RAM. Se você tiver menos de 16 GB, pode tentar a opção [GitHub Codespaces](../..) ou [configurar localmente](../..).
>
> Uma opção relacionada é o VS Code Dev Containers, que abrirá o projeto no seu VS Code local usando a [extensão Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Inicie o Docker Desktop (instale se ainda não estiver instalado)
> 2. Abra o projeto:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Estilo de código

Usamos o [Black](https://github.com/psf/black) como formatador de código Python para manter um estilo consistente em todo o projeto. Black é um formatador de código rigoroso que reformata automaticamente o código Python para seguir o estilo Black.

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

1. Formate todos os arquivos Python do projeto:
    ```bash
    poetry run black .
    ```

2. Formate um arquivo ou diretório específico:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Com pip

1. Formate todos os arquivos Python do projeto:
    ```bash
    black .
    ```

2. Formate um arquivo ou diretório específico:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Recomendamos configurar seu editor para formatar automaticamente o código com Black ao salvar. A maioria dos editores modernos suporta isso via extensões ou plugins.

## Executando o Co-op Translator

Para executar o Co-op Translator usando Poetry no seu ambiente, siga estes passos:

1. Navegue até o diretório onde deseja realizar os testes de tradução ou crie uma pasta temporária para testes.

2. Execute o comando abaixo. Substitua `-l ko` pelo código do idioma para o qual deseja traduzir. A flag `-d` indica modo de depuração.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Certifique-se de que seu ambiente Poetry está ativado (poetry shell) antes de executar o comando.

## Contribuir com um novo idioma

Aceitamos contribuições que adicionem suporte a novos idiomas. Antes de abrir um PR, complete os passos abaixo para garantir uma revisão tranquila.

1. Adicione o idioma ao mapeamento de fontes
   - Edite `src/co_op_translator/fonts/font_language_mappings.yml`
   - Adicione uma entrada com:
     - `code`: código do idioma no estilo ISO (ex: `vi`)
     - `name`: nome amigável para exibição
     - `font`: uma fonte incluída em `src/co_op_translator/fonts/` que suporte o script
     - `rtl`: `true` se for da direita para a esquerda, caso contrário `false`

2. Inclua os arquivos de fonte necessários (se precisar)
   - Se uma nova fonte for necessária, verifique a compatibilidade da licença para distribuição open source
   - Adicione o arquivo da fonte em `src/co_op_translator/fonts/`

3. Verificação local
   - Execute traduções para uma pequena amostra (Markdown, imagens e notebooks conforme apropriado)
   - Verifique se a saída é renderizada corretamente, incluindo fontes e qualquer layout RTL se aplicável

4. Atualize a documentação
   - Certifique-se de que o idioma aparece em `getting_started/supported-languages.md`
   - Não é necessário alterar `getting_started/README_languages_template.md`; ele é gerado a partir da lista de idiomas suportados

5. Abra um PR
   - Descreva o idioma adicionado e quaisquer considerações sobre fontes/licenciamento
   - Anexe capturas de tela das saídas renderizadas, se possível

Exemplo de entrada YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Teste o novo idioma

Você pode testar o novo idioma executando o seguinte comando:

```bash
# Crie e ative um ambiente virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instale o pacote de desenvolvimento
pip install -e .
# Execute a tradução
translate -l "new_lang"
```

## Mantenedores

### Mensagem de commit e estratégia de merge

Para garantir consistência e clareza no histórico de commits do projeto, seguimos um formato específico para a mensagem de commit **na mensagem final** ao usar a estratégia **Squash and Merge**.

Quando um pull request (PR) é mesclado, os commits individuais são combinados em um único commit. A mensagem final deve seguir o formato abaixo para manter um histórico limpo e consistente.

#### Formato da mensagem de commit (para squash and merge)

Usamos o seguinte formato para mensagens de commit:

```bash
<type>: <description> (#<Número do PR>)
```

- **type**: Especifica a categoria do commit. Usamos os seguintes tipos:
  - `Docs`: Para atualizações de documentação.
  - `Build`: Para mudanças relacionadas ao sistema de build ou dependências, incluindo atualizações em arquivos de configuração, workflows de CI ou Dockerfile.
  - `Core`: Para modificações na funcionalidade ou recursos centrais do projeto, especialmente arquivos em `src/co_op_translator/core`.

- **description**: Um resumo conciso da mudança.
- **PR number**: O número do pull request associado ao commit.

**Exemplos**:

- `Docs: Atualizar instruções de instalação para maior clareza (#50)`
- `Core: Melhorar tratamento da tradução de imagens (#60)`

> [!NOTE]
> Atualmente, os prefixos **`Docs`**, **`Core`** e **`Build`** são adicionados automaticamente aos títulos dos PRs com base nos rótulos aplicados ao código fonte modificado. Enquanto o rótulo correto estiver aplicado, normalmente não é necessário atualizar manualmente o título do PR. Basta verificar se está tudo correto e o prefixo foi gerado adequadamente.

#### Estratégia de merge

Usamos **Squash and Merge** como estratégia padrão para pull requests. Essa estratégia garante que as mensagens de commit sigam nosso formato, mesmo que os commits individuais não o façam.

**Razões**:

- Histórico do projeto limpo e linear.
- Consistência nas mensagens de commit.
- Redução de ruído por commits menores (ex: "corrigir erro de digitação").

Ao mesclar, certifique-se de que a mensagem final do commit siga o formato descrito acima.

**Exemplo de Squash and Merge**
Se um PR contém os seguintes commits:

- `corrigir erro de digitação`
- `atualizar README`
- `ajustar formatação`

Eles devem ser combinados em:
`Docs: Melhorar clareza e formatação da documentação (#65)`

### Processo de release

Esta seção descreve a forma mais simples para mantenedores publicarem uma nova versão do Co-op Translator.

#### 1. Atualizar a versão no `pyproject.toml`

1. Decida o próximo número de versão (seguimos versionamento semântico: `MAJOR.MINOR.PATCH`).
2. Edite o `pyproject.toml` e atualize o campo `version` sob `[tool.poetry]`.
3. Abra um pull request dedicado que altere apenas a versão (e quaisquer arquivos de lock/metadados atualizados automaticamente, se houver).
4. Após revisão, use **Squash and Merge** e garanta que a mensagem final do commit siga o formato descrito acima.

#### 2. Criar um Release no GitHub

1. Vá para a página do repositório no GitHub e abra **Releases** → **Draft a new release**.
2. Crie uma nova tag (por exemplo, `v0.13.0`) a partir do branch `main`.
3. Defina o título do release com a mesma versão (por exemplo, `v0.13.0`).
4. Clique em **Generate release notes** para preencher automaticamente o changelog.
5. Opcionalmente, edite o texto (por exemplo, para destacar novos idiomas suportados ou mudanças importantes).
6. Publique o release.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->