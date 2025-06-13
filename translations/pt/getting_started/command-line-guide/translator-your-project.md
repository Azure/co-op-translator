<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:47:01+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "pt"
}
-->
# Traduza o seu projeto usando o Co-op Translator

O **Co-op Translator** é uma ferramenta de linha de comandos (CLI) que ajuda a traduzir ficheiros markdown e imagens do seu projeto para várias línguas. Esta secção explica como usar a ferramenta, apresenta as várias opções da CLI e fornece exemplos para diferentes casos de uso.

> [!NOTE]
> Para uma lista completa de comandos e as suas descrições detalhadas, consulte a [Referência de comandos](./command-reference.md).

---

## Cenários e Comandos de Exemplo

Aqui estão alguns casos de uso comuns do **Co-op Translator**, juntamente com os comandos apropriados a executar.

### 1. Tradução Básica (Uma Só Língua)

Para traduzir todo o seu projeto (ficheiros markdown e imagens) para uma única língua, como Coreano, use o seguinte comando:

```bash
translate -l "ko"
```

Este comando irá traduzir todos os ficheiros markdown e imagens para Coreano, adicionando novas traduções sem apagar as já existentes.

> [!TIP]
>
> Quer saber quais os códigos de línguas disponíveis no **Co-op Translator**? Visite a secção [Línguas Suportadas](https://github.com/Azure/co-op-translator#supported-languages) no repositório para mais detalhes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para adicionar a tradução em Coreano aos ficheiros markdown e imagens existentes.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Tradução para Várias Línguas

Para traduzir o seu projeto para várias línguas (por exemplo, Espanhol, Francês e Alemão), use este comando:

```bash
translate -l "es fr de"
```

Este comando irá traduzir o projeto para Espanhol, Francês e Alemão, adicionando novas traduções sem sobrescrever as já existentes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, depois de puxar as últimas alterações para refletir os commits mais recentes, usei o seguinte método para traduzir os ficheiros markdown e imagens recém-adicionados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Embora geralmente seja recomendado traduzir uma língua de cada vez, em situações como esta, onde alterações específicas precisam ser adicionadas, traduzir várias línguas ao mesmo tempo pode ser mais eficiente.

### 3. Atualizar Traduções (Apaga Traduções Existentes)

Para atualizar traduções existentes (ou seja, apagar as traduções atuais e substituí-las por novas), use a opção `-u`. Isto apagará todas as traduções existentes para as línguas especificadas e fará uma nova tradução.

```bash
translate -l "ko" -u
```

Aviso: Este comando irá pedir confirmação antes de apagar as traduções existentes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para atualizar todos os ficheiros traduzidos em Espanhol. Recomendo este método quando há alterações significativas no conteúdo original em vários documentos markdown. Se houver apenas alguns ficheiros markdown traduzidos para atualizar, é mais eficiente apagar manualmente esses ficheiros específicos e depois usar o método `-a` para adicionar as traduções atualizadas.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Traduzir Apenas Imagens

Para traduzir apenas os ficheiros de imagem no seu projeto, use a opção `-img`:

```bash
translate -l "ko" -img
```

Este comando irá traduzir apenas as imagens para Coreano, sem afetar os ficheiros markdown.

### 6. Traduzir Apenas Ficheiros Markdown

Para traduzir apenas os ficheiros markdown no seu projeto, use a opção `-md`:

```bash
translate -l "ko" -md
```

### 7. Verificar Erros nos Ficheiros Traduzidos

Se quiser verificar os ficheiros traduzidos para erros e tentar a tradução novamente se necessário, use a opção `-chk`:

```bash
translate -l "ko" -chk
```

Este comando irá analisar os ficheiros markdown traduzidos e tentar traduzir novamente qualquer ficheiro com erros.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para verificar erros de tradução nos ficheiros em Coreano e tentar automaticamente a tradução novamente para quaisquer ficheiros com problemas detetados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Esta opção verifica erros de tradução. Atualmente, se a diferença no número de quebras de linha entre o ficheiro original e o traduzido for superior a seis, o ficheiro é marcado como tendo um erro de tradução. Planeio melhorar este critério para maior flexibilidade no futuro.

Por exemplo, este método é útil para detetar blocos em falta ou traduções corrompidas, e irá automaticamente tentar traduzir novamente esses ficheiros.

No entanto, se já souber quais os ficheiros problemáticos, é mais eficiente apagar manualmente esses ficheiros e usar a opção `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

Este comando executa a tradução em modo de depuração, fornecendo informação adicional de registo que pode ajudar a identificar problemas durante o processo de tradução.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, encontrei um problema onde traduções com muitos links em ficheiros markdown causavam erros de formatação, como traduções incompletas e quebras de linha ignoradas. Para diagnosticar este problema, usei a opção `-d` para ver como o processo de tradução funcionava.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Traduzir Todas as Línguas

Se quiser traduzir o projeto para todas as línguas suportadas, use a palavra-chave all.

> [!WARNING]
> Traduzir todas as línguas ao mesmo tempo pode demorar muito tempo, dependendo do tamanho do projeto. Por exemplo, traduzir o **Phi-3 CookBook** para Espanhol demorou cerca de 2 horas. Dado o volume, não é prático que uma só pessoa trate de 20 línguas. Recomenda-se dividir o trabalho entre vários colaboradores, cada um a gerir uma ou duas línguas, e atualizar as traduções gradualmente.

```bash
translate -l "all"
```

Este comando irá traduzir o projeto para todas as línguas disponíveis. Se avançar, a tradução pode demorar bastante tempo dependendo do tamanho do projeto.

> [!TIP]
>
> ### Apagar Manualmente Ficheiros Traduzidos (Opcional)
> Os ficheiros traduzidos são agora automaticamente detetados e limpos quando um ficheiro fonte é atualizado.
>
> No entanto, se quiser atualizar manualmente uma tradução — por exemplo, para refazer um ficheiro específico ou substituir o comportamento do sistema — pode usar o seguinte comando para apagar todas as versões do ficheiro em todas as pastas de línguas.
>
> ### No Windows:
> 1. **Usando o Prompt de Comando**:
>    - Abra o Prompt de Comando.
>    - Navegue até à pasta onde os ficheiros estão localizados usando o comando `cd`.
>    - Use o seguinte comando para apagar ficheiros:
>      ```
>      del /s *filename*
>      ```
>      A opção `/s` procura também nas subpastas.
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
>   - Use the `find` pelo comando adequado:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Substitua `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` para atualizar as alterações mais recentes dos ficheiros.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.