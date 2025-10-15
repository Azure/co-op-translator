<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:03:18+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "br"
}
-->
# Traduza seu projeto usando o Co-op Translator

O **Co-op Translator** é uma ferramenta de linha de comando (CLI) que ajuda você a traduzir arquivos markdown e imagens do seu projeto para vários idiomas. Esta seção explica como usar a ferramenta, apresenta as opções disponíveis na CLI e traz exemplos para diferentes situações.

> [!NOTE]
> Para ver a lista completa de comandos e suas descrições detalhadas, consulte a [Referência de Comandos](./command-reference.md).

---

## Cenários de exemplo e comandos

Veja abaixo alguns casos de uso comuns do **Co-op Translator**, junto com os comandos adequados para cada situação.

### 1. Tradução básica (um idioma)

Para traduzir todo o seu projeto (arquivos markdown e imagens) para um único idioma, como coreano, use o seguinte comando:

```bash
translate -l "ko"
```

Esse comando vai traduzir todos os arquivos markdown e imagens para coreano, adicionando novas traduções sem apagar as já existentes.

> [!TIP]
>
> Quer saber quais códigos de idioma estão disponíveis no **Co-op Translator**? Veja a seção [Idiomas Suportados](https://github.com/Azure/co-op-translator#supported-languages) no repositório para mais detalhes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para adicionar a tradução em coreano para os arquivos markdown e imagens já existentes.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traduzindo para vários idiomas

Para traduzir seu projeto para vários idiomas (por exemplo, espanhol, francês e alemão), use este comando:

```bash
translate -l "es fr de"
```

Esse comando vai traduzir o projeto para espanhol, francês e alemão, adicionando novas traduções sem sobrescrever as já existentes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, depois de puxar as últimas alterações para refletir os commits mais recentes, usei o seguinte método para traduzir os arquivos markdown e imagens recém-adicionados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Embora normalmente seja recomendado traduzir um idioma por vez, em situações como essa, onde mudanças específicas precisam ser adicionadas, traduzir vários idiomas de uma vez pode ser eficiente.

### 3. Atualizando traduções (apaga traduções existentes)

Para atualizar traduções já existentes (ou seja, apagar as traduções atuais e substituí-las por novas), use a opção `-u`. Isso vai apagar todas as traduções existentes para os idiomas especificados e traduzi-las novamente.

```bash
translate -l "ko" -u
```

Atenção: Esse comando vai pedir confirmação antes de apagar as traduções existentes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para atualizar todos os arquivos traduzidos em espanhol. Recomendo esse método quando há mudanças significativas no conteúdo original em vários documentos markdown. Se houver apenas alguns arquivos traduzidos para atualizar, é mais eficiente apagar manualmente esses arquivos específicos e depois usar o método `-a` para adicionar as traduções atualizadas.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Traduzindo apenas imagens

Para traduzir apenas os arquivos de imagem do seu projeto, use a opção `-img`:

```bash
translate -l "ko" -img
```

Esse comando vai traduzir apenas as imagens para coreano, sem mexer nos arquivos markdown.

### 6. Traduzindo apenas arquivos Markdown

Para traduzir apenas os arquivos markdown do seu projeto, use a opção `-md`:

```bash
translate -l "ko" -md
```

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para verificar erros de tradução nos arquivos em coreano e tentar traduzir novamente automaticamente os arquivos com problemas detectados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Essa opção verifica erros de tradução. Atualmente, se a diferença de quebras de linha entre o arquivo original e o traduzido for maior que seis, o arquivo é marcado como tendo erro de tradução. Pretendo melhorar esse critério para dar mais flexibilidade no futuro.

Por exemplo, esse método é útil para detectar partes faltando ou traduções corrompidas, e vai tentar traduzir novamente esses arquivos automaticamente.

No entanto, se você já sabe quais arquivos estão com problema, é mais eficiente apagar manualmente esses arquivos e usar a opção `-a` para traduzi-los novamente.

### 8. Modo de depuração

Para ativar o registro detalhado para diagnóstico, use a opção `-d`:

```bash
translate -l "ko" -d
```

Esse comando vai executar a tradução em modo de depuração, mostrando informações extras de log que podem ajudar a identificar problemas durante o processo de tradução.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, encontrei um problema onde traduções com muitos links em arquivos markdown causavam erros de formatação, como traduções quebradas e quebras de linha ignoradas. Para investigar esse problema, usei a opção `-d` para ver como o processo de tradução estava funcionando.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Traduzindo para todos os idiomas

Se quiser traduzir o projeto para todos os idiomas suportados, use a palavra-chave all.

> [!WARNING]
> Traduzir para todos os idiomas de uma vez pode levar bastante tempo, dependendo do tamanho do projeto. Por exemplo, traduzir o **Phi-3 CookBook** para espanhol levou cerca de 2 horas. Dada a escala, não é prático para uma pessoa só cuidar de 20 idiomas. Recomenda-se dividir o trabalho entre vários colaboradores, cada um cuidando de um ou dois idiomas, e atualizar as traduções aos poucos.

```bash
translate -l "all"
```

Esse comando vai traduzir o projeto para todos os idiomas disponíveis. Se você continuar, a tradução pode levar bastante tempo dependendo do tamanho do projeto.

> [!TIP]
>
> ### Apagando arquivos traduzidos manualmente (opcional)
> Agora os arquivos traduzidos são detectados e limpos automaticamente quando um arquivo fonte é atualizado.
>
> Porém, se você quiser atualizar uma tradução manualmente – por exemplo, para refazer um arquivo específico ou substituir o comportamento padrão do sistema – pode usar o comando abaixo para apagar todas as versões do arquivo nas pastas de idiomas.
>
> ### No Windows:
> 1. **Usando o Prompt de Comando**:
>    - Abra o Prompt de Comando.
>    - Navegue até a pasta onde estão os arquivos usando o comando `cd`.
>    - Use o seguinte comando para apagar arquivos:
>      ```
>      del /s *filename*
>      ```
>      Substitua `filename` pela parte específica do nome do arquivo que você procura. A opção `/s` busca em subpastas também.
>
> 2. **Usando o PowerShell**:
>    - Abra o PowerShell.
>    - Execute este comando:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Substitua `"C:\YourPath"` pelo caminho da pasta e `filename` pelo nome específico.
>
> ### No macOS/Linux:
> 1. **Usando o Terminal**:
>   - Abra o Terminal.
>   - Navegue até o diretório com `cd`.
>   - Use o comando `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Substitua `filename` pelo nome específico.
>
> Sempre confira os arquivos antes de apagar para evitar perda acidental.
>
> Depois de apagar os arquivos que precisam ser substituídos, basta rodar novamente o comando `translate -l` para atualizar as alterações mais recentes.

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora busquemos precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.