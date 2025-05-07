<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "33db54f4f3ca9f0321be05374b591f2b",
  "translation_date": "2025-05-06T18:00:06+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "br"
}
-->
# Translate your project using Co-op Translator

O **Co-op Translator** é uma ferramenta de linha de comando (CLI) que ajuda você a traduzir arquivos markdown e imagens do seu projeto para vários idiomas. Esta seção explica como usar a ferramenta, apresenta as diversas opções da CLI e fornece exemplos para diferentes casos de uso.

> [!NOTE]
> Para uma lista completa de comandos e suas descrições detalhadas, consulte a [Command reference](./command-reference.md).

---

## Cenários e Comandos de Exemplo

Aqui estão alguns casos de uso comuns do **Co-op Translator**, junto com os comandos apropriados para executar.

### 1. Tradução Básica (Idioma Único)

Para traduzir todo o seu projeto (arquivos markdown e imagens) para um único idioma, como coreano, use o seguinte comando:

```bash
translate -l "ko"
```

Esse comando vai traduzir todos os arquivos markdown e imagens para o coreano, adicionando novas traduções sem apagar as já existentes.

> [!TIP]
>
> Quer ver quais códigos de idioma estão disponíveis no **Co-op Translator**? Visite a seção [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) no repositório para mais detalhes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para adicionar a tradução para coreano nos arquivos markdown e imagens existentes.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traduzindo Vários Idiomas

Para traduzir seu projeto em vários idiomas (por exemplo, espanhol, francês e alemão), use este comando:

```bash
translate -l "es fr de"
```

Esse comando traduz o projeto para espanhol, francês e alemão, adicionando novas traduções sem sobrescrever as existentes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, após puxar as últimas alterações para refletir os commits mais recentes, usei o seguinte método para traduzir os arquivos markdown e imagens recém-adicionados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Embora geralmente seja recomendado traduzir um idioma por vez, em situações como essa, onde mudanças específicas precisam ser adicionadas, traduzir vários idiomas ao mesmo tempo pode ser eficiente.

### 3. Especificando o Diretório Raiz

Por padrão, o tradutor usa o diretório de trabalho atual. Se seu projeto estiver em outro local, especifique o diretório raiz com a opção -r:

```bash
translate -l "es fr de" -r "./my_project"
```

Esse comando traduz os arquivos em `./my_project` into Spanish, French, and German.

### 4. Updating Translations (Deletes Existing Translations)

To update existing translations (i.e., delete the current translations and replace them with new ones), use the `-u` opção. Isso vai apagar todas as traduções existentes para os idiomas especificados e refazer a tradução.

```bash
translate -l "ko" -u
```

Aviso: esse comando vai pedir confirmação antes de prosseguir com a exclusão das traduções existentes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para atualizar todos os arquivos traduzidos em espanhol. Recomendo usar esse método quando houver mudanças significativas no conteúdo original em vários documentos markdown. Se forem apenas alguns arquivos traduzidos para atualizar, é mais eficiente apagar manualmente esses arquivos específicos e então usar o método `-a` para adicionar as traduções atualizadas.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 6. Traduzindo Apenas Imagens

Para traduzir somente os arquivos de imagem do seu projeto, use a opção `-img`:

```bash
translate -l "ko" -img
```

Esse comando vai traduzir apenas as imagens para o coreano, sem afetar nenhum arquivo markdown.

### 7. Traduzindo Apenas Arquivos Markdown

Para traduzir somente os arquivos markdown do seu projeto, use a opção `-md`:

```bash
translate -l "ko" -md
```

### 8. Verificando Erros em Arquivos Traduzidos

Se quiser verificar os arquivos traduzidos em busca de erros e tentar a tradução novamente, use a opção `-chk`:

```bash
translate -l "ko" -chk
```

Esse comando vai escanear os arquivos markdown traduzidos e tentar traduzir novamente qualquer arquivo que apresente erros.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para verificar erros de tradução nos arquivos em coreano e tentar automaticamente a tradução novamente para os arquivos com problemas detectados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Essa opção verifica erros de tradução. Atualmente, se a diferença na quebra de linha entre o arquivo original e o traduzido for maior que seis, o arquivo é marcado como com erro de tradução. Pretendo melhorar esse critério para permitir maior flexibilidade no futuro.

Por exemplo, esse método é útil para detectar partes faltantes ou traduções corrompidas, e vai tentar a tradução novamente para esses arquivos.

No entanto, se você já sabe quais arquivos estão problemáticos, é mais eficiente apagar manualmente esses arquivos e usar a opção `-a` option to re-translate them.

### 9. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Esse comando executa a tradução em modo debug, fornecendo informações adicionais de log que podem ajudar a identificar problemas durante o processo de tradução.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, encontrei um problema onde traduções com muitos links em arquivos markdown causavam erros de formatação, como traduções quebradas e quebras de linha ignoradas. Para diagnosticar esse problema, usei a opção `-d` para ver como o processo de tradução funcionava.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 10. Traduzindo Todos os Idiomas

Se quiser traduzir o projeto para todos os idiomas suportados, use a palavra-chave all.

> [!WARNING]
> Traduzir todos os idiomas de uma vez pode levar um tempo considerável, dependendo do tamanho do projeto. Por exemplo, traduzir o **Phi-3 CookBook** para espanhol levou cerca de 2 horas. Considerando a escala, não é prático uma única pessoa cuidar de 20 idiomas. Recomenda-se dividir o trabalho entre vários colaboradores, cada um gerenciando um ou dois idiomas, e atualizar as traduções gradualmente.

```bash
translate -l "all"
```

Esse comando vai traduzir o projeto para todos os idiomas disponíveis. Se você prosseguir, a tradução pode levar um tempo significativo dependendo do tamanho do projeto.

> [!TIP]
>
> ### Apagando arquivos que precisam ser atualizados
> Para atualizar arquivos recentemente alterados em Pull Request, o primeiro passo é apagar todas as versões existentes do arquivo específico localizadas nas diferentes pastas de tradução por idioma. Você pode fazer isso em lote usando o seguinte comando para apagar todos os arquivos com um nome específico dentro das pastas de tradução.
>
> ### No Windows:
> 1. **Usando o Prompt de Comando**:
>    - Abra o Prompt de Comando.
>    - Navegue até a pasta onde os arquivos estão usando o comando `cd`.
>    - Use o seguinte comando para apagar arquivos:
>      ```
>      del /s *filename*
>      ```
>      A opção `/s` busca também em subdiretórios.
>
> 2. **Usando o PowerShell**:
>    - Abra o PowerShell.
>    - Execute este comando:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Substitua `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` comando:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Substitua `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` comando para atualizar as alterações mais recentes dos arquivos.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.