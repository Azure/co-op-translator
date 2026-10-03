# Traduzir, editar e revisar um pequeno projeto

Comece com dois arquivos Markdown curtos e um idioma de destino. Você verá onde as traduções são escritas, o que acontece quando a origem muda e como verificar o resultado.

## Resultados registrados

O exemplo foi executado em 19 de setembro de 2026 com Co-op Translator 0.21.0 e Azure OpenAI (`gpt-5-mini`). Os comandos de CLI não modificados foram invocados através do `CliRunner` do Click usando o wheel construído e as dependências Python existentes.

| Etapa | Resultado |
| --- | --- |
| Visualizar | Saída 0; nenhuma tradução por modelo solicitada |
| Tradução inicial | Saída 0; 27.36 segundos |
| Revisão inicial | Saída 0 |
| Editar README e revisar | Saída 1; tradução obsoleta detectada |
| Atualizar tradução | Saída 0; 22.17 segundos |
| Revisão após atualização | Saída 0; sem erros ou avisos |
| Guia inalterado | Bytes idênticos antes e depois da atualização do README |
| Executar novamente | Saída 0; hashes idênticos para todos os arquivos de tradução |

Estas são medidas de execuções individuais, não garantias de desempenho. O tempo de configuração está excluído; a cobrança do provedor não foi medida. Uma execução sem alterações ainda pode executar uma verificação de saúde do provedor.

Inspecione a [tradução inicial](../../assets/demo/before.txt), [tradução atualizada](../../assets/demo/after.txt), [diff completo da tradução](../../assets/demo/update.diff), [revisão obsoleta](../../assets/demo/review-stale.txt), [revisão final](../../assets/demo/review-after.txt) e [detalhes da execução](../../assets/demo/results.json). A tradução do arquivo inteiro pode alterar outras palavras, como mostra o diff capturado. Ambos os artefatos de texto mantêm o aviso gerado.

A revisão humana ainda importa: a atualização capturada usa `[사용 가이드](guide.md)을`; a partícula coreana deveria ser `[사용 가이드](guide.md)를`. Os artefatos de texto mantêm essa saída intacta em vez de apresentar uma tradução editada como saída do modelo. A revisão estrutural passa apesar desse problema de redação.

## 1. Prepare uma pequena pasta

Use Python 3.11–3.14 e o [configuração do ambiente virtual](configuration.md#local-runtime-setup). Instale a versão usada neste exemplo:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Baixe [README.txt](../../assets/demo/README.txt) e [guide.txt](../../assets/demo/guide.txt) para esta pasta, salvando-os como `README.md` e `guide.md`. Eles são documentos de projeto fictícios e pequenos; nenhuma instalação de aplicativo é necessária.

O README inclui um bloco de código e um link para `guide.md`. Sua frase final é:

```text
Notes are saved locally.
```

Mantenha apenas esses dois documentos-fonte nesta pasta. Todos os comandos seguintes são executados dentro de `translation-demo` e funcionam no Bash e no PowerShell.

## 2. Visualizar sem credenciais

```bash
translate -l "ko" -md --dry-run
```

A visualização estima o trabalho de tradução sem chamar um modelo ou gravar traduções. As estimativas de tokens não constituem uma cotação de cobrança. A primeira execução deve identificar ambos os arquivos Markdown como trabalho novo.

## 3. Escolha um provedor e traduza

Configure um provedor usando o [guia de configuração](configuration.md): Azure OpenAI, OpenAI ou Anthropic. As traduções de texto da OpenAI e da Anthropic não requerem uma conta Azure. Serviços de imagem não são necessários para este exemplo.

Se você usar um arquivo `.env` local, adicione `.env` ao `.gitignore` desta pasta. As chamadas de tradução usam sua conta do provedor e podem gerar cobranças.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Abra `translations/ko/README.md` e `translations/ko/guide.md`. Verifique a redação em coreano, o bloco de código e o link do README traduzido para o guia traduzido. A redação de saída varia conforme o modelo.

`co-op-review` verifica atualidade, estrutura e links locais. Um resultado aprovado não certifica a precisão linguística. Resolva quaisquer erros relatados antes de continuar.

Registre a linha de base bem-sucedida com o Git (configure sua identidade Git primeiro, se necessário):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Altere a origem

Em `README.md`, substitua `Notes are saved locally.` por:

```text
Notes are saved locally as Markdown files.
```

Deixe `guide.md` inalterado. Em seguida, execute:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

A revisão deve reportar a tradução do README como obsoleta e sair com falha. Este é o estado intermediário esperado. A visualização deve identificar trabalho para o README alterado.

## 5. Atualize e inspecione o diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Inspecione o diff real: a CLI padrão retraduz o arquivo alterado, de modo que o modelo também pode revisar outras redações nesse arquivo. O guia inalterado não deve ter diff. A revisão não deve mais reportar o README como obsoleto; investigue quaisquer outras constatações em vez de ignorá-las.

A preservação em nível de bloco de edições humanas em Markdown requer um provedor de estado de tradução opcional na [API Python](api.md). Isso não está habilitado por esses comandos de CLI.

## 6. Execute novamente sem alterações

Faça commit da origem e da tradução atualizadas:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Com as traduções atuais e a configuração inalterada, o tradutor pula os arquivos. O comando Git final não deve produzir diff e deve sair com sucesso.

## Próximos passos

- [Traduzir apenas um README e abrir um pull request](github-actions.md#your-first-readme-translation-pr).
- [Escolher CLI, API Python ou MCP](workflows.md).
- [Relatar um problema de tradução sem codificar](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).