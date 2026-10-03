# Traduzir, editar e rever um pequeno projeto

Comece com dois ficheiros Markdown pequenos e uma língua alvo. Verá onde as traduções são escritas, o que acontece quando a origem muda e como verificar o resultado.

## Resultados registados

O exemplo foi executado a 19 de setembro de 2026 com o Co-op Translator 0.21.0 e Azure OpenAI (`gpt-5-mini`). Os comandos CLI não modificados foram invocados através do `CliRunner` do Click, usando a wheel construída e as dependências Python existentes.

| Passo | Resultado |
| --- | --- |
| Pré-visualização | Exit 0; nenhuma tradução de modelo solicitada |
| Tradução inicial | Exit 0; 27,36 segundos |
| Revisão inicial | Exit 0 |
| Editar README e rever | Exit 1; tradução desatualizada detectada |
| Atualizar tradução | Exit 0; 22,17 segundos |
| Revisão após atualização | Exit 0; sem erros ou avisos |
| Guia inalterado | Bytes idênticos antes e depois da atualização do README |
| Executar novamente | Exit 0; hashes idênticos para todos os ficheiros de tradução |

Estas são medições de execuções individuais, não garantias de desempenho. O tempo de configuração está excluído; a faturação do fornecedor não foi medida. Uma execução sem alterações ainda pode realizar uma verificação de integridade do fornecedor.

Inspecione a [tradução inicial](../../assets/demo/before.txt), [tradução atualizada](../../assets/demo/after.txt), [diff completo da tradução](../../assets/demo/update.diff), [revisão desatualizada](../../assets/demo/review-stale.txt), [revisão final](../../assets/demo/review-after.txt), e [detalhes da execução](../../assets/demo/results.json). A tradução de ficheiro completo pode alterar outras formulações, como o diff capturado mostra. Ambos os artefactos de texto mantêm o aviso gerado.

A revisão humana continua a ser importante: a atualização capturada usa `[사용 가이드](guide.md)을`; a partícula coreana devia ser `[사용 가이드](guide.md)를`. Os artefactos de texto mantêm esta saída intacta em vez de apresentarem uma tradução editada como saída do modelo. A revisão estrutural passa apesar deste problema de formulação.

## 1. Preparar uma pasta pequena

Use Python 3.11–3.14 e a [configuração do ambiente virtual](configuration.md#local-runtime-setup). Instale a versão usada neste exemplo:

```bash
python -m pip install co-op-translator==0.21.0
mkdir translation-demo
cd translation-demo
git init
```

Descarregue [README.txt](../../assets/demo/README.txt) e [guide.txt](../../assets/demo/guide.txt) para esta pasta, guardando-os como `README.md` e `guide.md`. São pequenos documentos fictícios de projeto; não é necessária a instalação de qualquer aplicação.

O README inclui um bloco de código e um link para `guide.md`. A sua última frase é:

```text
Notes are saved locally.
```

Mantenha apenas estes dois documentos de origem nesta pasta. Todos os comandos seguintes são executados dentro de `translation-demo` e funcionam no Bash e no PowerShell.

## 2. Pré-visualizar sem credenciais

```bash
translate -l "ko" -md --dry-run
```

A pré-visualização estima o trabalho de tradução sem invocar um modelo ou escrever traduções. As estimativas de tokens não são uma cotação de faturação. A primeira execução deve identificar ambos os ficheiros Markdown como trabalho novo.

## 3. Escolher um fornecedor e traduzir

Configure um fornecedor usando o [guia de configuração](configuration.md): Azure OpenAI, OpenAI ou Anthropic. A tradução de texto com OpenAI e Anthropic não requer uma conta Azure. Serviços de imagem não são necessários para este exemplo.

Se usar um ficheiro `.env` local, adicione `.env` ao `.gitignore` desta pasta. As chamadas de tradução usam a sua conta do fornecedor e podem acarretar custos.

```bash
translate -l "ko" -md
co-op-review -l "ko"
```

Abra `translations/ko/README.md` e `translations/ko/guide.md`. Verifique a formulação coreana, o bloco de código e o link do README traduzido para o guia traduzido. A redação da saída varia consoante o modelo.

`co-op-review` verifica a atualidade, a estrutura e os links locais. Um resultado com aprovação não certifica a precisão linguística. Resolva quaisquer erros reportados antes de continuar.

Registe a baseline bem-sucedida com o Git (configure primeiro a sua identidade Git se necessário):

```bash
git add README.md guide.md translations
git commit -m "Record initial Korean translation"
```

## 4. Alterar a origem

Em `README.md`, substitua `Notes are saved locally.` por:

```text
Notes are saved locally as Markdown files.
```

Deixe `guide.md` inalterado. Depois execute:

```bash
co-op-review -l "ko"
translate -l "ko" -md --dry-run
```

A revisão deve reportar a tradução do README como desatualizada e terminar sem sucesso. Este é o estado intermédio esperado. A pré-visualização deve identificar trabalho para o README alterado.

## 5. Atualizar e inspecionar o diff

```bash
translate -l "ko" -md
git diff -- README.md translations/ko/README.md
git diff -- translations/ko/guide.md
co-op-review -l "ko"
```

Inspecione o diff real: o CLI pré-definido retraduz o ficheiro alterado, pelo que o modelo também pode rever outra formulação nesse ficheiro. O guia inalterado não deverá ter diff. A revisão não deverá voltar a reportar o README como desatualizado; investigue quaisquer outros achados em vez de os ignorar.

A preservação ao nível de blocos das edições humanas em Markdown requer um fornecedor opcional de estado de tradução na [Python API](api.md). Não está ativado por estes comandos CLI.

## 6. Executar novamente sem alterações

Faça commit da origem e da tradução atualizadas:

```bash
git add README.md translations
git commit -m "Update Korean translation after source edit"
translate -l "ko" -md
git diff --exit-code -- translations
```

Com as traduções atuais e a configuração inalterada, o tradutor ignora os ficheiros. O comando Git final não deverá produzir diff e deverá terminar com sucesso.

## Próximos passos

- [Traduzir apenas um README e abrir um pull request](github-actions.md#your-first-readme-translation-pr).
- [Escolher CLI, Python API, ou MCP](workflows.md).
- [Reportar um problema de tradução sem escrever código](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml).