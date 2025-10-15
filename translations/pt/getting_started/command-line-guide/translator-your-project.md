<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20943a46b11c6d74814f41a817a6db4c",
  "translation_date": "2025-10-15T03:00:53+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "pt"
}
-->
# Traduz o teu projeto com o Co-op Translator

O **Co-op Translator** é uma ferramenta de linha de comandos (CLI) que te ajuda a traduzir ficheiros markdown e imagens do teu projeto para várias línguas. Nesta secção explico como usar a ferramenta, os diferentes parâmetros da CLI e dou exemplos para vários cenários de utilização.

> [!NOTE]
> Para veres a lista completa de comandos e as suas descrições detalhadas, consulta a [Referência de Comandos](./command-reference.md).

---

## Cenários de exemplo e comandos

Aqui tens alguns casos de uso comuns do **Co-op Translator**, juntamente com os comandos adequados para cada situação.

### 1. Tradução básica (Uma só língua)

Para traduzir todo o teu projeto (ficheiros markdown e imagens) para uma só língua, como coreano, usa o seguinte comando:

```bash
translate -l "ko"
```

Este comando vai traduzir todos os ficheiros markdown e imagens para coreano, adicionando novas traduções sem apagar as que já existem.

> [!TIP]
>
> Queres saber quais os códigos de línguas disponíveis no **Co-op Translator**? Consulta a secção [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) no repositório para mais detalhes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para adicionar a tradução em coreano aos ficheiros markdown e imagens já existentes.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. Traduzir para várias línguas

Para traduzir o teu projeto para várias línguas (por exemplo, espanhol, francês e alemão), usa este comando:

```bash
translate -l "es fr de"
```

Este comando vai traduzir o projeto para espanhol, francês e alemão, adicionando novas traduções sem substituir as que já existem.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, depois de fazer pull das últimas alterações para refletir os commits mais recentes, usei o seguinte método para traduzir os ficheiros markdown e imagens que foram adicionados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> Embora normalmente seja recomendado traduzir uma língua de cada vez, em situações como esta, onde há alterações específicas a adicionar, traduzir várias línguas de uma vez pode ser eficiente.

### 3. Atualizar traduções (Apaga traduções existentes)

Para atualizar traduções já existentes (ou seja, apagar as traduções atuais e substituí-las por novas), usa a opção `-u`. Isto vai apagar todas as traduções existentes para as línguas especificadas e traduzi-las novamente.

```bash
translate -l "ko" -u
```

Atenção: Este comando vai pedir confirmação antes de avançar e apagar as traduções existentes.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para atualizar todos os ficheiros traduzidos em espanhol. Recomendo este método quando há alterações significativas no conteúdo original em vários documentos markdown. Se só precisas de atualizar alguns ficheiros traduzidos, é mais eficiente apagar manualmente esses ficheiros específicos e depois usar o método `-a` para adicionar as traduções atualizadas.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. Traduzir apenas imagens

Para traduzir apenas os ficheiros de imagem do teu projeto, usa a opção `-img`:

```bash
translate -l "ko" -img
```

Este comando vai traduzir apenas as imagens para coreano, sem mexer nos ficheiros markdown.

### 6. Traduzir apenas ficheiros Markdown

Para traduzir apenas os ficheiros markdown do teu projeto, usa a opção `-md`:

```bash
translate -l "ko" -md
```

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, usei o seguinte método para verificar erros de tradução nos ficheiros em coreano e tentar automaticamente traduzir de novo os ficheiros com problemas detetados.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

Esta opção verifica erros de tradução. Atualmente, se a diferença de quebras de linha entre o ficheiro original e o traduzido for superior a seis, o ficheiro é marcado como tendo erro de tradução. Pretendo melhorar este critério para ser mais flexível no futuro.

Por exemplo, este método é útil para detetar partes em falta ou traduções corrompidas, e vai tentar traduzir automaticamente esses ficheiros.

No entanto, se já sabes quais são os ficheiros problemáticos, é mais eficiente apagá-los manualmente e usar a opção `-a` para traduzi-los novamente.

### 8. Modo de Depuração

Para ativar o registo detalhado e facilitar a resolução de problemas, usa a opção `-d`:

```bash
translate -l "ko" -d
```

Este comando executa a tradução em modo de depuração, mostrando mais informações no registo que podem ajudar a identificar problemas durante o processo de tradução.

#### Exemplo no Phi-3 CookBook

No **Phi-3 CookBook**, deparei-me com um problema em que traduções com muitos links em ficheiros markdown causavam erros de formatação, como traduções partidas e quebras de linha ignoradas. Para diagnosticar este problema, usei a opção `-d` para ver como estava a funcionar o processo de tradução.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. Traduzir para todas as línguas

Se quiseres traduzir o projeto para todas as línguas suportadas, usa a palavra-chave all.

> [!WARNING]
> Traduzir para todas as línguas de uma vez pode demorar bastante tempo, dependendo do tamanho do projeto. Por exemplo, traduzir o **Phi-3 CookBook** para espanhol demorou cerca de 2 horas. Dada a dimensão, não é prático para uma só pessoa tratar de 20 línguas. Recomenda-se dividir o trabalho entre vários colaboradores, cada um a tratar de uma ou duas línguas, e ir atualizando as traduções gradualmente.

```bash
translate -l "all"
```

Este comando vai traduzir o projeto para todas as línguas disponíveis. Se avançares, a tradução pode demorar bastante tempo, dependendo do tamanho do projeto.

> [!TIP]
>
> ### Apagar ficheiros traduzidos manualmente (Opcional)
> Os ficheiros traduzidos agora são detetados e limpos automaticamente quando um ficheiro fonte é atualizado.
>
> No entanto, se quiseres atualizar manualmente uma tradução – por exemplo, para refazer um ficheiro específico ou substituir o comportamento do sistema – podes usar o seguinte comando para apagar todas as versões do ficheiro nas pastas de línguas.
>
> ### No Windows:
> 1. **Usando o Command Prompt**:
>    - Abre o Command Prompt.
>    - Vai até à pasta onde estão os ficheiros com o comando `cd`.
>    - Usa o seguinte comando para apagar ficheiros:
>      ```
>      del /s *filename*
>      ```
>      Substitui `filename` pela parte específica do nome do ficheiro que procuras. A opção `/s` procura em subdiretórios também.
>
> 2. **Usando o PowerShell**:
>    - Abre o PowerShell.
>    - Executa este comando:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      Substitui `"C:\YourPath"` pelo caminho da pasta e `filename` pelo nome específico.
>
> ### No macOS/Linux:
> 1. **Usando o Terminal**:
>   - Abre o Terminal.
>   - Vai até ao diretório com `cd`.
>   - Usa o comando `find`:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     Substitui `filename` pelo nome específico.
>
> Confirma sempre os ficheiros antes de apagar para evitar perdas acidentais.
>
> Depois de apagares os ficheiros que precisas de substituir, basta voltares a executar o comando `translate -l` para atualizar as alterações mais recentes.

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.