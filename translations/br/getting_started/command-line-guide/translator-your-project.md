<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-05-07T14:08:22+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "br"
}
-->
# Translate your project using Co-op Translator

The **Co-op Translator** é uma ferramenta de linha de comando (CLI) que ajuda você a traduzir arquivos markdown e imagens do seu projeto para vários idiomas. Esta seção explica como usar a ferramenta, apresenta as diversas opções de CLI e fornece exemplos para diferentes casos de uso.

> [!NOTE]
> Para uma lista completa de comandos e suas descrições detalhadas, consulte a [Command reference](./command-reference.md).

---

## Cenários e Comandos Exemplares

Aqui estão alguns casos comuns de uso do **Co-op Translator**, junto com os comandos apropriados para executar.

### 1. Tradução Básica (Idioma Único)

Para traduzir todo o seu projeto (arquivos markdown e imagens) para um único idioma, como coreano, use o seguinte comando:

```bash
translate -l "ko"
```

Este comando traduzirá todos os arquivos markdown e imagens para coreano, adicionando novas traduções sem apagar as já existentes.

> [!TIP]
>
> Quer saber quais códigos de idioma estão disponíveis no **Co-op Translator**? Visite a seção [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) no repositório para mais detalhes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para adicionar a tradução em coreano para os arquivos markdown e imagens existentes.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traduzindo Múltiplos Idiomas

Para traduzir seu projeto para vários idiomas (por exemplo, espanhol, francês e alemão), use este comando:

```bash
translate -l "es fr de"
```

Este comando traduz o projeto para espanhol, francês e alemão, adicionando novas traduções sem sobrescrever as existentes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, após puxar as últimas alterações para refletir os commits mais recentes, usei o seguinte método para traduzir os arquivos markdown e imagens recém-adicionados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Embora geralmente seja recomendado traduzir um idioma por vez, em situações como esta, onde mudanças específicas precisam ser adicionadas, traduzir múltiplos idiomas ao mesmo tempo pode ser eficiente.

### 3. Atualizando Traduções (Apaga Traduções Existentes)

Para atualizar traduções existentes (ou seja, apagar as traduções atuais e substituí-las por novas), use a opção `-u`. Isso apagará todas as traduções existentes para os idiomas especificados e fará a retradução.

```bash
translate -l "ko" -u
```

Aviso: Este comando solicitará confirmação antes de apagar as traduções existentes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para atualizar todos os arquivos traduzidos em espanhol. Recomendo este método quando houver mudanças significativas no conteúdo original em vários documentos markdown. Se houver apenas alguns arquivos traduzidos para atualizar, é mais eficiente apagar manualmente esses arquivos específicos e depois usar o método `-a` para adicionar as traduções atualizadas.

### 5. Traduzindo Apenas Imagens

Para traduzir somente os arquivos de imagem do seu projeto, use a opção `-img`:

```bash
translate -l "ko" -img
```

Este comando traduzirá apenas as imagens para coreano, sem afetar os arquivos markdown.

### 6. Traduzindo Apenas Arquivos Markdown

Para traduzir somente os arquivos markdown do seu projeto, use a opção `-md`:

```bash
translate -l "ko" -md
```

### 7. Verificando Erros em Arquivos Traduzidos

Se quiser verificar arquivos traduzidos para erros e tentar a tradução novamente, se necessário, use a opção `-chk`:

```bash
translate -l "ko" -chk
```

Este comando fará uma varredura nos arquivos markdown traduzidos e tentará retraduzir qualquer arquivo com erros.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para verificar erros de tradução nos arquivos coreanos e automaticamente tentar a tradução novamente para quaisquer arquivos com problemas detectados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Esta opção verifica erros de tradução. Atualmente, se a diferença na quebra de linha entre o arquivo original e o traduzido for maior que seis, o arquivo é marcado como com erro de tradução. Planejo melhorar esse critério para maior flexibilidade no futuro.

Por exemplo, esse método é útil para detectar partes faltantes ou traduções corrompidas, e automaticamente tentará retraduzir esses arquivos.

No entanto, se você já sabe quais arquivos estão com problema, é mais eficiente apagar manualmente esses arquivos e usar a opção `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Este comando executará a tradução no modo de depuração, fornecendo informações adicionais de log que podem ajudar a identificar problemas durante o processo de tradução.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, encontrei um problema onde traduções com muitos links em arquivos markdown causavam erros de formatação, como traduções quebradas e quebras de linha ignoradas. Para diagnosticar esse problema, usei a opção `-d` para ver como o processo de tradução funciona.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Traduzindo Todos os Idiomas

Se quiser traduzir o projeto para todos os idiomas suportados, use a palavra-chave all.

> [!WARNING]
> Traduzir todos os idiomas ao mesmo tempo pode levar bastante tempo, dependendo do tamanho do projeto. Por exemplo, traduzir o **Phi-3 CookBook** para espanhol levou cerca de 2 horas. Considerando essa escala, não é prático uma pessoa gerenciar 20 idiomas sozinha. Recomenda-se dividir o trabalho entre vários colaboradores, cada um cuidando de um ou dois idiomas, e atualizar as traduções gradualmente.

```bash
translate -l "all"
```

Este comando traduzirá o projeto para todos os idiomas disponíveis. Se prosseguir, a tradução pode levar bastante tempo dependendo do tamanho do projeto.

> [!TIP]
>
> ### Apagando Manualmente Arquivos Traduzidos (Opcional)
> Arquivos traduzidos agora são detectados automaticamente e removidos quando um arquivo fonte é atualizado.
>
> Porém, se quiser atualizar uma tradução manualmente - por exemplo, refazer um arquivo específico ou substituir o comportamento do sistema - você pode usar o seguinte comando para apagar todas as versões do arquivo nas pastas de idiomas.
>
> ### No Windows:
> 1. **Usando o Prompt de Comando**:
>    - Abra o Prompt de Comando.
>    - Navegue até a pasta onde os arquivos estão usando o comando `cd`.
>    - Use o seguinte comando para apagar os arquivos:
>      ```
>      del /s *filename*
>      ```
>      A opção `/s` busca também nas subpastas.
>
> 2. **Usando PowerShell**:
>    - Abra o PowerShell.
>    - Execute este comando:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Substitua `"C:\YourPath"` pelo caminho correto.
>
> 3. Usando o comando `cd` e `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>
> 4. Use o comando `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` para atualizar as mudanças mais recentes nos arquivos.

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.