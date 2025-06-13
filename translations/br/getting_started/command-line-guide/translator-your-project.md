<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:47:21+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "br"
}
-->
# Traduza seu projeto usando o Co-op Translator

O **Co-op Translator** é uma ferramenta de linha de comando (CLI) que ajuda a traduzir arquivos markdown e imagens do seu projeto para vários idiomas. Esta seção explica como usar a ferramenta, apresenta as opções da CLI e fornece exemplos para diferentes casos de uso.

> [!NOTE]
> Para uma lista completa de comandos e suas descrições detalhadas, consulte a [Referência de Comandos](./command-reference.md).

---

## Cenários e Comandos de Exemplo

Aqui estão alguns casos comuns de uso do **Co-op Translator**, junto com os comandos apropriados para executar.

### 1. Tradução Básica (Idioma Único)

Para traduzir todo o seu projeto (arquivos markdown e imagens) para um único idioma, como coreano, use o seguinte comando:

```bash
translate -l "ko"
```

Este comando traduzirá todos os arquivos markdown e imagens para o coreano, adicionando novas traduções sem excluir as existentes.

> [!TIP]
>
> Quer saber quais códigos de idiomas estão disponíveis no **Co-op Translator**? Visite a seção [Idiomas Suportados](https://github.com/Azure/co-op-translator#supported-languages) no repositório para mais detalhes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, utilizei o seguinte método para adicionar a tradução para o coreano dos arquivos markdown e imagens existentes.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traduzindo Vários Idiomas

Para traduzir seu projeto para vários idiomas (por exemplo, espanhol, francês e alemão), use este comando:

```bash
translate -l "es fr de"
```

Este comando traduzirá o projeto para espanhol, francês e alemão, adicionando novas traduções sem sobrescrever as existentes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, após puxar as últimas alterações para refletir os commits mais recentes, utilizei o seguinte método para traduzir arquivos markdown e imagens recém-adicionados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Embora geralmente seja recomendado traduzir um idioma por vez, em situações como esta, onde mudanças específicas precisam ser adicionadas, traduzir vários idiomas ao mesmo tempo pode ser eficiente.

### 3. Atualizando Traduções (Apaga Traduções Existentes)

Para atualizar traduções existentes (ou seja, apagar as traduções atuais e substituí-las por novas), use a opção `-u`. Isso apagará todas as traduções existentes para os idiomas especificados e as traduzirá novamente.

```bash
translate -l "ko" -u
```

Aviso: Este comando solicitará sua confirmação antes de prosseguir com a exclusão das traduções existentes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para atualizar todos os arquivos traduzidos em espanhol. Recomendo este método quando há mudanças significativas no conteúdo original em vários documentos markdown. Se houver apenas alguns arquivos markdown traduzidos para atualizar, é mais eficiente excluir manualmente esses arquivos específicos e depois usar o método `-a` para adicionar as traduções atualizadas.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Traduzindo Apenas Imagens

Para traduzir somente os arquivos de imagem do seu projeto, use a opção `-img`:

```bash
translate -l "ko" -img
```

Este comando traduzirá apenas as imagens para o coreano, sem afetar nenhum arquivo markdown.

### 6. Traduzindo Apenas Arquivos Markdown

Para traduzir somente os arquivos markdown do seu projeto, use a opção `-md`:

```bash
translate -l "ko" -md
```

### 7. Verificando Erros em Arquivos Traduzidos

Se quiser verificar os arquivos traduzidos em busca de erros e tentar a tradução novamente se necessário, use a opção `-chk`:

```bash
translate -l "ko" -chk
```

Este comando irá escanear os arquivos markdown traduzidos e tentar traduzir novamente qualquer arquivo com erros.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para verificar erros de tradução nos arquivos coreanos e automaticamente tentar a tradução novamente para quaisquer arquivos com problemas detectados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Esta opção verifica erros de tradução. Atualmente, se a diferença de quebras de linha entre o arquivo original e o traduzido for maior que seis, o arquivo é marcado como tendo erro de tradução. Pretendo melhorar esse critério para maior flexibilidade no futuro.

Por exemplo, esse método é útil para detectar trechos faltantes ou traduções corrompidas, e ele tentará automaticamente a tradução novamente para esses arquivos.

No entanto, se você já sabe quais arquivos estão problemáticos, é mais eficiente excluí-los manualmente e usar a opção `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Este comando executará a tradução no modo de depuração, fornecendo informações adicionais de log que podem ajudar a identificar problemas durante o processo de tradução.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, encontrei um problema em que traduções com muitos links em arquivos markdown causavam erros de formatação, como traduções quebradas e quebras de linha ignoradas. Para diagnosticar esse problema, usei a opção `-d` para ver como o processo de tradução funcionava.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Traduzindo Todos os Idiomas

Se quiser traduzir o projeto para todos os idiomas suportados, use a palavra-chave all.

> [!WARNING]
> Traduzir todos os idiomas de uma vez pode levar um tempo significativo dependendo do tamanho do projeto. Por exemplo, traduzir o **Phi-3 CookBook** para espanhol levou cerca de 2 horas. Dada a escala, não é prático para uma pessoa cuidar de 20 idiomas. Recomenda-se dividir o trabalho entre vários colaboradores, cada um gerenciando um ou dois idiomas, e atualizar as traduções gradualmente.

```bash
translate -l "all"
```

Este comando traduzirá o projeto para todos os idiomas disponíveis. Se você prosseguir, a tradução poderá levar um tempo considerável dependendo do tamanho do projeto.

> [!TIP]
>
> ### Excluindo Arquivos Traduzidos Manualmente (Opcional)
> Os arquivos traduzidos agora são detectados e limpos automaticamente quando um arquivo fonte é atualizado.
>
> No entanto, se quiser atualizar uma tradução manualmente — por exemplo, refazer um arquivo específico ou substituir o comportamento do sistema — você pode usar o seguinte comando para excluir todas as versões do arquivo em todas as pastas de idiomas.
>
> ### No Windows:
> 1. **Usando o Prompt de Comando**:
>    - Abra o Prompt de Comando.
>    - Navegue até a pasta onde os arquivos estão localizados usando o comando `cd`.
>    - Use o seguinte comando para excluir arquivos:
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
>      Substitua `"C:\YourPath"` pelo caminho da sua pasta.
>
> 3. **Usando o comando `cd` e `find`**:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>
> 4. **Usando o comando `translate -l` para atualizar as alterações mais recentes dos arquivos.**

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.