<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:02:55+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "br"
}
-->
# Guia de Solução de Problemas do Microsoft Co-op Translator

## Visão Geral
O Microsoft Co-Op Translator é uma ferramenta poderosa para traduzir documentos Markdown de forma simples e eficiente. Este guia vai te ajudar a resolver os problemas mais comuns ao usar a ferramenta.

## Problemas Comuns e Soluções

### 1. Problema com Tag Markdown
**Problema:** O documento Markdown traduzido inclui uma tag `markdown` no topo, causando problemas de renderização.

**Solução:** Para resolver, basta apagar a tag `markdown` do topo do arquivo. Assim, o arquivo Markdown será renderizado corretamente.

**Passos:**
1. Abra o arquivo Markdown (`.md`) traduzido.
2. Localize a tag `markdown` no topo do documento.
3. Apague a tag `markdown`.
4. Salve as alterações no arquivo.
5. Reabra o arquivo para garantir que está renderizando corretamente.

### 2. Problema com URL de Imagens Embutidas
**Problema:** As URLs das imagens embutidas não correspondem ao idioma do documento, resultando em imagens erradas ou ausentes.

**Solução:** Verifique a URL das imagens embutidas e garanta que estejam no idioma correto. Todas as imagens ficam na pasta `translated_images` e cada imagem tem uma tag de idioma no nome do arquivo.

**Passos:**
1. Abra o documento Markdown traduzido.
2. Identifique as imagens embutidas e suas URLs.
3. Verifique se o idioma no nome do arquivo da imagem corresponde ao idioma do documento.
4. Atualize as URLs se necessário.
5. Salve as alterações e reabra o documento para confirmar que as imagens aparecem corretamente.

### 3. Precisão da Tradução
**Problema:** O conteúdo traduzido não está preciso ou precisa de ajustes.

**Solução:** Revise o documento traduzido e faça os ajustes necessários para melhorar a precisão e a clareza.

**Passos:**
1. Abra o documento traduzido.
2. Revise o conteúdo com atenção.
3. Faça os ajustes necessários para melhorar a tradução.
4. Salve as alterações.

## 4. Erro de Permissão Redacted ou 404

Se imagens ou textos não estão sendo traduzidos corretamente e, ao rodar em modo -d debug, você recebe erro 401, trata-se de uma falha de autenticação—ou a chave está inválida, expirada ou não vinculada à região do endpoint.

Execute o co-op translator com o [parâmetro -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) para entender melhor a causa raiz.

- **Mensagem de Erro**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Possíveis Causas**:
  - A chave de assinatura foi redigida ou está incorreta na requisição.
  - A chave de Serviços de IA ou de Assinatura pode pertencer a outro recurso Azure (como Translator ou OpenAI) em vez de um recurso **Azure AI Vision**.

 **Tipo de Recurso**
  - Acesse o [Portal Azure](https://portal.azure.com) ou [Azure AI Foundry](https://ai.azure.com) e confirme que o recurso é do tipo `Azure AI services` → `Vision`.
  - Valide as chaves e garanta que está usando a chave correta.

## 5. Erros de Configuração (Novo Tratamento de Erros)

Com o novo sistema de tradução seletiva, o Co-op Translator agora mostra mensagens de erro explícitas quando serviços obrigatórios não estão configurados.

### 5.1. Azure AI Service Não Configurado para Tradução de Imagens

**Problema:** Você solicitou tradução de imagens (flag `-img`), mas o Azure AI Service não está configurado corretamente.

**Mensagem de Erro:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Solução:**
1. **Opção 1**: Configurar Azure AI Service
   - Adicione `AZURE_AI_SERVICE_API_KEY` ao seu arquivo `.env`
   - Adicione `AZURE_AI_SERVICE_ENDPOINT` ao seu arquivo `.env`
   - Verifique se o serviço está acessível

2. **Opção 2**: Remover a solicitação de tradução de imagens
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Configuração Obrigatória Ausente

**Problema:** Configuração essencial do LLM está faltando.

**Mensagem de Erro:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Solução:**
1. Verifique se seu arquivo `.env` tem pelo menos uma das seguintes configurações de LLM:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` e `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Você precisa configurar Azure OpenAI OU OpenAI, não ambos.

### 5.3. Confusão na Tradução Seletiva

**Problema:** Nenhum arquivo foi traduzido, mesmo com o comando executado com sucesso.

**Possíveis Causas:**
- Flags de tipo de arquivo erradas (`-md`, `-img`, `-nb`)
- Nenhum arquivo correspondente no projeto
- Estrutura de diretórios incorreta

**Solução:**
1. **Use o modo debug** para ver o que está acontecendo:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Verifique os tipos de arquivo** no seu projeto:
   ```bash
   # For markdown files
   find . -name "*.md" -not -path "./translations/*"
   
   # For notebooks
   find . -name "*.ipynb" -not -path "./translations/*"
   
   # For images
   find . -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -not -path "./translations/*"
   ```

3. **Confirme as combinações de flags**:
   ```bash
   # Translate everything (default)
   translate -l "ko"
   
   # Translate specific types
   translate -l "ko" -md -img
   ```

## 6. Migração do Sistema Antigo

### 6.1. Modo Apenas Markdown Descontinuado

**Problema:** Comandos que dependiam do fallback automático para markdown não funcionam mais como antes.

**Comportamento Antigo:**
```bash
# This used to automatically switch to markdown-only mode
translate -l "ko"  # (when Azure AI Vision was not configured)
```

**Novo Comportamento:**
```bash
# This now produces an error if image translation is requested but not configured
translate -l "ko" -img
```

**Solução:**
- **Seja explícito** sobre o que deseja traduzir:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Comportamento Inesperado de Links

**Problema:** Links em arquivos traduzidos apontam para locais inesperados.

**Causa:** O processamento dinâmico de links muda conforme os tipos de arquivo selecionados.

**Solução:**
1. **Entenda o novo comportamento dos links**:
   - Incluindo `-nb`: Links de notebooks apontam para versões traduzidas
   - Excluindo `-nb`: Links de notebooks apontam para arquivos originais
   - Incluindo `-img`: Links de imagens apontam para versões traduzidas
   - Excluindo `-img`: Links de imagens apontam para arquivos originais

2. **Escolha a combinação certa** para seu caso:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action executou mas nenhum Pull Request (PR) foi criado

**Sintoma:** Os logs do workflow para `peter-evans/create-pull-request` mostram:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Causas prováveis:**
- **Nenhuma alteração detectada:** O passo de tradução não gerou diferenças (repositório já está atualizado).
- **Saídas ignoradas:** O `.gitignore` exclui arquivos que você espera commitar (ex: `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths incompatível:** Os caminhos fornecidos para a action não correspondem aos locais reais de saída.
- **Lógica/condições do workflow:** O passo de tradução saiu antes ou escreveu em diretórios inesperados.

**Como corrigir / verificar:**
1. **Confirme se as saídas existem:** Após a tradução, verifique se há arquivos novos/alterados em `translations/` e/ou `translated_images/`.
   - Se traduzir notebooks, garanta que os arquivos `.ipynb` estão realmente em `translations/<lang>/...`.
2. **Revise o `.gitignore`:** Não ignore as saídas geradas. Certifique-se de NÃO ignorar:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (se traduzir notebooks)
3. **Garanta que add-paths corresponde às saídas:** Use valor multilinha e inclua ambas as pastas se necessário:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Force um PR para depuração:** Permita commits vazios temporariamente para confirmar se está tudo certo:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Execute com debug:** Adicione `-d` ao comando de tradução para mostrar quais arquivos foram encontrados e escritos.
6. **Permissões (GITHUB_TOKEN):** Garanta que o workflow tem permissão de escrita para criar commits e PRs:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Checklist Rápido de Depuração

Ao resolver problemas de tradução:

1. **Use o modo debug**: Adicione a flag `-d` para ver logs detalhados
2. **Confira suas flags**: Certifique-se que `-md`, `-img`, `-nb` correspondem ao que você quer
3. **Verifique a configuração**: Veja se seu arquivo `.env` tem as chaves necessárias
4. **Teste incrementalmente**: Comece só com `-md`, depois adicione outros tipos
5. **Confira a estrutura dos arquivos**: Certifique-se que os arquivos de origem existem e estão acessíveis

Para mais detalhes sobre comandos e flags disponíveis, veja a [Referência de Comandos](./command-reference.md).

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.