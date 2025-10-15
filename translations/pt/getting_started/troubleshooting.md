<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6e626bef5ed78a1cc55b0dbf44f01d47",
  "translation_date": "2025-10-15T03:00:26+00:00",
  "source_file": "getting_started/troubleshooting.md",
  "language_code": "pt"
}
-->
# Guia de Resolução de Problemas do Microsoft Co-op Translator

## Visão Geral
O Microsoft Co-Op Translator é uma ferramenta poderosa para traduzir documentos Markdown de forma simples e eficiente. Este guia vai ajudá-lo a resolver os problemas mais comuns encontrados ao utilizar a ferramenta.

## Problemas Comuns e Soluções

### 1. Problema com a Tag Markdown
**Problema:** O documento Markdown traduzido inclui uma tag `markdown` no topo, causando problemas de visualização.

**Solução:** Para resolver, basta eliminar a tag `markdown` no topo do ficheiro. Assim, o ficheiro Markdown será apresentado corretamente.

**Passos:**
1. Abra o ficheiro Markdown (`.md`) traduzido.
2. Localize a tag `markdown` no topo do documento.
3. Apague a tag `markdown`.
4. Guarde as alterações no ficheiro.
5. Reabra o ficheiro para garantir que é apresentado corretamente.

### 2. Problema com URLs de Imagens Incorporadas
**Problema:** Os URLs das imagens incorporadas não correspondem ao idioma do documento, resultando em imagens incorretas ou ausentes.

**Solução:** Verifique o URL das imagens incorporadas e confirme que correspondem ao idioma do documento. Todas as imagens estão na pasta `translated_images` e cada imagem tem uma etiqueta de idioma no nome do ficheiro.

**Passos:**
1. Abra o documento Markdown traduzido.
2. Identifique as imagens incorporadas e os seus URLs.
3. Confirme que a etiqueta de idioma no nome do ficheiro da imagem corresponde ao idioma do documento.
4. Atualize os URLs se necessário.
5. Guarde as alterações e reabra o documento para confirmar que as imagens aparecem corretamente.

### 3. Precisão da Tradução
**Problema:** O conteúdo traduzido não está correto ou precisa de mais edição.

**Solução:** Reveja o documento traduzido e faça as edições necessárias para melhorar a precisão e a clareza.

**Passos:**
1. Abra o documento traduzido.
2. Reveja cuidadosamente o conteúdo.
3. Faça as edições necessárias para melhorar a tradução.
4. Guarde as alterações.

## 4. Erro de Permissão Redacted ou 404

Se as imagens ou o texto não estão a ser traduzidos para o idioma correto e, ao executar em modo -d debug, aparece um erro 401, trata-se de uma falha clássica de autenticação — a chave é inválida, expirou ou não está associada à região do endpoint.

Execute o co-op translator com o [parâmetro -d debug](https://github.com/Azure/co-op-translator/blob/main/getting_started/command-reference.md) para obter mais detalhes sobre a causa do problema.

- **Mensagem de Erro**: `Access denied due to invalid subscription key or wrong API endpoint.`
- **Possíveis Causas**:
  - A chave de subscrição foi removida ou está incorreta no pedido.
  - A chave de Serviços de IA ou de Subscrição pode pertencer a outro recurso Azure (como Translator ou OpenAI) em vez de um recurso **Azure AI Vision**.

 **Tipo de Recurso**
  - Aceda ao [Portal Azure](https://portal.azure.com) ou ao [Azure AI Foundry](https://ai.azure.com) e confirme que o recurso é do tipo `Azure AI services` → `Vision`.
  - Valide as chaves e certifique-se de que está a usar a chave correta.

## 5. Erros de Configuração (Novo Sistema de Gestão de Erros)

Com o novo sistema de tradução seletiva, o Co-op Translator agora apresenta mensagens de erro explícitas quando os serviços necessários não estão configurados.

### 5.1. Azure AI Service Não Configurado para Tradução de Imagens

**Problema:** Solicitou tradução de imagens (flag `-img`), mas o Azure AI Service não está devidamente configurado.

**Mensagem de Erro:**
```
Error: Image translation requested but Azure AI Service is not configured.
Please add AZURE_AI_SERVICE_API_KEY and AZURE_AI_SERVICE_ENDPOINT to your .env file.
Check Azure AI Service availability and configuration.
```

**Solução:**
1. **Opção 1**: Configurar o Azure AI Service
   - Adicione `AZURE_AI_SERVICE_API_KEY` ao seu ficheiro `.env`
   - Adicione `AZURE_AI_SERVICE_ENDPOINT` ao seu ficheiro `.env`
   - Verifique se o serviço está acessível

2. **Opção 2**: Remover o pedido de tradução de imagens
   ```bash
   # Instead of: translate -l "ko" -img
   # Use: translate -l "ko" -md
   ```

### 5.2. Configuração Essencial em Falta

**Problema:** Falta a configuração essencial do LLM.

**Mensagem de Erro:**
```
Error: No language model configuration found.
Please configure either Azure OpenAI or OpenAI in your .env file.
```

**Solução:**
1. Confirme que o seu ficheiro `.env` tem pelo menos uma das seguintes configurações LLM:
   - **Azure OpenAI**: `AZURE_OPENAI_API_KEY` e `AZURE_OPENAI_ENDPOINT`
   - **OpenAI**: `OPENAI_API_KEY`
   
   Precisa de ter Azure OpenAI OU OpenAI configurado, não ambos.

### 5.3. Confusão com Tradução Seletiva

**Problema:** Nenhum ficheiro foi traduzido, mesmo que o comando tenha sido executado com sucesso.

**Possíveis Causas:**
- Flags de tipo de ficheiro erradas (`-md`, `-img`, `-nb`)
- Não existem ficheiros correspondentes no projeto
- Estrutura de diretórios incorreta

**Solução:**
1. **Use o modo debug** para ver o que está a acontecer:
   ```bash
   translate -l "ko" -md -d
   ```

2. **Verifique os tipos de ficheiro** no seu projeto:
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

### 6.1. Modo Só-Markdown Descontinuado

**Problema:** Comandos que dependiam do modo automático só-markdown já não funcionam como antes.

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
- **Seja explícito** sobre o que pretende traduzir:
  ```bash
  translate -l "ko" -md        # Only markdown
  translate -l "ko" -md -img   # Markdown and images
  translate -l "ko"            # Everything (if all services configured)
  ```

### 6.2. Comportamento Inesperado de Links

**Problema:** Os links nos ficheiros traduzidos apontam para locais inesperados.

**Causa:** O processamento dinâmico de links muda consoante os tipos de ficheiro selecionados.

**Solução:**
1. **Compreenda o novo comportamento dos links**:
   - Inclui `-nb`: Os links dos notebooks apontam para as versões traduzidas
   - Exclui `-nb`: Os links dos notebooks apontam para os ficheiros originais
   - Inclui `-img`: Os links das imagens apontam para as versões traduzidas
   - Exclui `-img`: Os links das imagens apontam para os ficheiros originais

2. **Escolha a combinação certa** para o seu caso:
   ```bash
   # All internal links point to translated versions
   translate -l "ko" -md -img -nb
   
   # Only markdown translated, other links point to originals
   translate -l "ko" -md
   ```

## 7. GitHub Action executou mas não foi criado Pull Request (PR)

**Sintoma:** Os registos do workflow para `peter-evans/create-pull-request` mostram:

> Branch 'update-translations' is not ahead of base 'main' and will not be created

**Causas prováveis:**
- **Sem alterações detetadas:** O passo de tradução não produziu diferenças (o repositório já está atualizado).
- **Saídas ignoradas:** O `.gitignore` exclui ficheiros que espera que sejam commitados (ex: `*.ipynb`, `translations/`, `translated_images/`).
- **add-paths não corresponde:** Os caminhos fornecidos à ação não correspondem aos locais reais de saída.
- **Lógica/condições do workflow:** O passo de tradução terminou cedo ou escreveu para diretórios inesperados.

**Como corrigir / verificar:**
1. **Confirme que existem saídas:** Após a tradução, verifique se existem ficheiros novos/alterados em `translations/` e/ou `translated_images/`.
   - Se traduzir notebooks, confirme que os ficheiros `.ipynb` são realmente escritos em `translations/<lang>/...`.
2. **Reveja o `.gitignore`:** Não ignore as saídas geradas. Certifique-se de que NÃO está a ignorar:
   - `translations/`
   - `translated_images/`
   - `*.ipynb` (se traduzir notebooks)
3. **Confirme que add-paths corresponde às saídas:** Use um valor multilinha e inclua ambas as pastas se aplicável:
   ```yaml
   with:
     add-paths: |
       translations/
       translated_images/
   ```
4. **Forçar um PR para debugging:** Permita commits vazios temporariamente para confirmar que a ligação está correta:
   ```yaml
   with:
     commit-empty: true
   ```
5. **Execute com debug:** Adicione `-d` ao comando de tradução para ver que ficheiros foram detetados e escritos.
6. **Permissões (GITHUB_TOKEN):** Confirme que o workflow tem permissões de escrita para criar commits e PRs:
   ```yaml
   permissions:
     contents: write
     pull-requests: write
   ```


## Lista Rápida de Verificação para Debug

Ao resolver problemas de tradução:

1. **Use o modo debug**: Adicione o parâmetro `-d` para ver registos detalhados
2. **Verifique as flags**: Confirme que `-md`, `-img`, `-nb` correspondem ao que pretende
3. **Verifique a configuração**: Confirme que o seu ficheiro `.env` tem as chaves necessárias
4. **Teste de forma incremental**: Comece só com `-md`, depois adicione outros tipos
5. **Verifique a estrutura dos ficheiros**: Confirme que os ficheiros de origem existem e são acessíveis

Para mais informações sobre comandos e flags disponíveis, consulte a [Referência de Comandos](./command-reference.md).

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua nativa, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.