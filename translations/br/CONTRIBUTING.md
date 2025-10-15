<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd4704f50c55da7d572b691484aa0b30",
  "translation_date": "2025-10-15T03:01:44+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "br"
}
-->
# Contribuindo para o Co-op Translator

Este projeto está aberto a contribuições e sugestões. A maioria das contribuições exige que você concorde com um
Acordo de Licença de Contribuidor (CLA), declarando que você tem o direito de, e realmente concede,
os direitos de uso da sua contribuição. Para mais detalhes, visite https://cla.opensource.microsoft.com.

Ao enviar um pull request, um bot de CLA irá automaticamente determinar se você precisa fornecer
um CLA e irá marcar o PR de forma apropriada (ex: status check, comentário). Basta seguir as instruções
fornecidas pelo bot. Você só precisa fazer isso uma vez para todos os repositórios que usam nosso CLA.

## Configuração do ambiente de desenvolvimento

Para configurar o ambiente de desenvolvimento deste projeto, recomendamos usar o Poetry para gerenciar as dependências. Usamos o `pyproject.toml` para gerenciar as dependências do projeto, portanto, para instalar as dependências, utilize o Poetry.

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

### Instalando o pacote e dependências necessárias

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

2. Copie alguns arquivos markdown e imagens que você deseja traduzir para o diretório de teste. Por exemplo:
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

5. Verifique os arquivos traduzidos em `test_docs/translations` e `test_docs/translated_images` para conferir:
   - Qualidade da tradução
   - Se os comentários de metadados estão corretos
   - Se a estrutura original do markdown foi preservada
   - Se os links e imagens estão funcionando corretamente

Esse teste manual ajuda a garantir que suas alterações funcionam bem em cenários reais.

### Variáveis de ambiente

1. Crie um arquivo `.env` na raiz do projeto copiando o arquivo `.env.template` fornecido.
1. Preencha as variáveis de ambiente conforme orientado.

> [!TIP]
>
> ### Opções adicionais de ambiente de desenvolvimento
>
> Além de rodar o projeto localmente, você também pode usar o GitHub Codespaces ou VS Code Dev Containers como alternativas para configurar o ambiente de desenvolvimento.
>
> #### GitHub Codespaces
>
> Você pode rodar estes exemplos virtualmente usando o GitHub Codespaces, sem necessidade de configurações adicionais.
>
> O botão irá abrir uma instância do VS Code baseada na web no seu navegador:
>
> 1. Abra o template (isso pode levar alguns minutos):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Abrir no GitHub Codespaces"></a>
>
> #### Rodando localmente com VS Code Dev Containers
>
> ⚠️ Esta opção só funciona se o seu Docker Desktop estiver com pelo menos 16 GB de RAM alocados. Se você tiver menos de 16 GB de RAM, pode tentar a opção do [GitHub Codespaces](../..) ou [configurar localmente](../..).
>
> Uma opção relacionada é o VS Code Dev Containers, que abre o projeto no seu VS Code local usando a [extensão Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Inicie o Docker Desktop (instale se ainda não tiver)
> 2. Abra o projeto:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Abrir no Dev Containers"></a>


### Estilo de código

Utilizamos o [Black](https://github.com/psf/black) como formatador de código Python para manter um estilo consistente em todo o projeto. O Black é um formatador rigoroso que reformata automaticamente o código Python para seguir o padrão do Black.

#### Configuração

A configuração do Black está especificada no nosso `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalando o Black

Você pode instalar o Black usando Poetry (recomendado) ou pip:

##### Usando Poetry

O Black é instalado automaticamente ao configurar o ambiente de desenvolvimento:
```bash
poetry install
```

##### Usando pip

Se estiver usando pip, instale o Black diretamente:
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
> Recomendamos configurar seu editor para formatar o código automaticamente com o Black ao salvar. A maioria dos editores modernos oferece suporte a isso por meio de extensões ou plugins.

## Executando o Co-op Translator

Para rodar o Co-op Translator usando Poetry no seu ambiente, siga estes passos:

1. Navegue até o diretório onde deseja realizar testes de tradução ou crie uma pasta temporária para testes.

2. Execute o comando abaixo. Substitua `-l ko` pelo código do idioma para o qual deseja traduzir. O parâmetro `-d` ativa o modo debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Certifique-se de que o ambiente Poetry está ativado (poetry shell) antes de rodar o comando.

## Contribuir com um novo idioma

Aceitamos contribuições para adicionar suporte a novos idiomas. Antes de abrir um PR, siga os passos abaixo para facilitar a revisão.

1. Adicione o idioma ao mapeamento de fontes
   - Edite `src/co_op_translator/fonts/font_language_mappings.yml`
   - Adicione uma entrada com:
     - `code`: Código de idioma no padrão ISO (ex: `vi`)
     - `name`: Nome amigável para exibição
     - `font`: Uma fonte disponível em `src/co_op_translator/fonts/` que suporte o script
     - `rtl`: `true` se for da direita para a esquerda, senão `false`

2. Inclua os arquivos de fonte necessários (se aplicável)
   - Se precisar de uma fonte nova, verifique a compatibilidade de licença para distribuição open source
   - Adicione o arquivo de fonte em `src/co_op_translator/fonts/`

3. Verificação local
   - Execute traduções em uma pequena amostra (Markdown, imagens e notebooks, conforme necessário)
   - Verifique se a saída está correta, incluindo fontes e layout RTL se aplicável

4. Atualize a documentação
   - Certifique-se de que o idioma aparece em `getting_started/supported-languages.md`
   - Não é necessário alterar o `README_languages_template.md`; ele é gerado a partir da lista de idiomas suportados

5. Abra um PR
   - Descreva o idioma adicionado e qualquer consideração sobre fonte/licença
   - Anexe capturas de tela dos resultados renderizados, se possível

Exemplo de entrada YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```


## Mantenedores

### Mensagem de commit e estratégia de merge

Para garantir consistência e clareza no histórico de commits do projeto, seguimos um formato específico de mensagem de commit **para o commit final** ao usar a estratégia **Squash and Merge**.

Quando um pull request (PR) é mesclado, os commits individuais são agrupados em um único commit. A mensagem final do commit deve seguir o formato abaixo para manter um histórico limpo e consistente.

#### Formato da mensagem de commit (para squash and merge)

Usamos o seguinte formato para mensagens de commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Especifica a categoria do commit. Usamos os seguintes tipos:
  - `Docs`: Para atualizações de documentação.
  - `Build`: Para alterações relacionadas ao sistema de build ou dependências, incluindo atualizações de arquivos de configuração, workflows de CI ou Dockerfile.
  - `Core`: Para modificações na funcionalidade principal do projeto, especialmente nos arquivos do diretório `src/co_op_translator/core`.

- **description**: Um resumo conciso da alteração.
- **PR number**: O número do pull request associado ao commit.

**Exemplos**:

- `Docs: Atualiza instruções de instalação para maior clareza (#50)`
- `Core: Melhora o tratamento da tradução de imagens (#60)`

> [!NOTE]
> Atualmente, os prefixos **`Docs`**, **`Core`** e **`Build`** são adicionados automaticamente aos títulos dos PRs com base nos labels aplicados ao código fonte modificado. Desde que o label correto seja aplicado, normalmente você não precisa atualizar o título do PR manualmente. Basta verificar se está tudo correto e se o prefixo foi gerado adequadamente.

#### Estratégia de merge

Utilizamos **Squash and Merge** como estratégia padrão para pull requests. Essa estratégia garante que as mensagens de commit sigam nosso formato, mesmo que os commits individuais não sigam.

**Motivos**:

- Histórico do projeto limpo e linear.
- Consistência nas mensagens de commit.
- Menos ruído de commits menores (ex: "fix typo").

Ao mesclar, certifique-se de que a mensagem final do commit siga o formato descrito acima.

**Exemplo de Squash and Merge**
Se um PR contém os seguintes commits:

- `fix typo`
- `update README`
- `adjust formatting`

Eles devem ser agrupados em:
`Docs: Melhora clareza e formatação da documentação (#65)`

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.