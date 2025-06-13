<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4ed48f23ec418b31e90a02fe629fcde",
  "translation_date": "2025-06-12T12:08:56+00:00",
  "source_file": "getting_started/supported-languages.md",
  "language_code": "pt"
}
-->
# Idiomas suportados

A tabela abaixo lista os idiomas atualmente suportados pelo **Co-op Translator**. Ela inclui os códigos dos idiomas, os nomes e quaisquer problemas conhecidos associados a cada idioma. Se você quiser adicionar suporte para um novo idioma, adicione o código correspondente, o nome e a fonte apropriada no arquivo `font_language_mappings.yml` localizado em `src/co_op_translator/fonts/` e envie um pull request após testar.

| Código do Idioma | Nome do Idioma       | Fonte                             | Suporte RTL | Problemas Conhecidos |
|------------------|----------------------|----------------------------------|-------------|----------------------|
| en               | English              | NotoSans-Medium.ttf              | Não         | Não                  |
| fr               | French               | NotoSans-Medium.ttf              | Não         | Não                  |
| es               | Spanish              | NotoSans-Medium.ttf              | Não         | Não                  |
| de               | German               | NotoSans-Medium.ttf              | Não         | Não                  |
| ru               | Russian              | NotoSans-Medium.ttf              | Não         | Não                  |
| ar               | Arabic               | NotoSansArabic-Medium.ttf        | Sim         | Não                  |
| fa               | Persian (Farsi)      | NotoSansArabic-Medium.ttf        | Não         | Não                  |
| ur               | Urdu                 | NotoSansArabic-Medium.ttf        | Não         | Não                  |
| zh               | Chinese (Simplified) | NotoSansCJK-Medium.ttc           | Não         | Não                  |
| mo               | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc    | Não         | Não                  |
| hk               | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc| Não         | Não                  |
| tw               | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc   | Não         | Não                  |
| ja               | Japanese             | NotoSansCJK-Medium.ttc           | Não         | Não                  |
| ko               | Korean               | NotoSansCJK-Medium.ttc           | Não         | Não                  |
| hi               | Hindi                | NotoSansDevanagari-Medium.ttf    | Não         | Não                  |
| bn               | Bengali              | NotoSansBengali-Medium.ttf       | Não         | Não                  |
| mr               | Marathi              | NotoSansDevanagari-Medium.ttf    | Não         | Não                  |
| ne               | Nepali               | NotoSansDevanagari-Medium.ttf    | Não         | Não                  |
| pa               | Punjabi (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf      | Não         | Não                  |
| pt               | Portuguese (Portugal)| NotoSans-Medium.ttf              | Não         | Não                  |
| br               | Portuguese (Brazil)  | NotoSans-Medium.ttf              | Não         | Não                  |
| it               | Italian              | NotoSans-Medium.ttf              | Não         | Não                  |
| pl               | Polish               | NotoSans-Medium.ttf              | Não         | Não                  |
| tr               | Turkish              | NotoSans-Medium.ttf              | Não         | Não                  |
| el               | Greek                | NotoSans-Medium.ttf              | Não         | Não                  |
| th               | Thai                 | NotoSansThai-Medium.ttf          | Não         | Não                  |
| sv               | Swedish              | NotoSans-Medium.ttf              | Não         | Não                  |
| da               | Danish               | NotoSans-Medium.ttf              | Não         | Não                  |
| no               | Norwegian            | NotoSans-Medium.ttf              | Não         | Não                  |
| fi               | Finnish              | NotoSans-Medium.ttf              | Não         | Não                  |
| nl               | Dutch                | NotoSans-Medium.ttf              | Não         | Não                  |
| he               | Hebrew               | NotoSansHebrew-Medium.ttf        | Não         | Não                  |
| vi               | Vietnamese           | NotoSans-Medium.ttf              | Não         | Não                  |
| id               | Indonesian           | NotoSans-Medium.ttf              | Não         | Não                  |
| ms               | Malay                | NotoSans-Medium.ttf              | Não         | Não                  |
| tl               | Tagalog (Filipino)   | NotoSans-Medium.ttf              | Não         | Não                  |
| sw               | Swahili              | NotoSans-Medium.ttf              | Não         | Não                  |
| hu               | Hungarian            | NotoSans-Medium.ttf              | Não         | Não                  |
| cs               | Czech                | NotoSans-Medium.ttf              | Não         | Não                  |
| sk               | Slovak               | NotoSans-Medium.ttf              | Não         | Não                  |
| ro               | Romanian             | NotoSans-Medium.ttf              | Não         | Não                  |
| bg               | Bulgarian            | NotoSans-Medium.ttf              | Não         | Não                  |
| sr               | Serbian (Cyrillic)   | NotoSans-Medium.ttf              | Não         | Não                  |
| hr               | Croatian             | NotoSans-Medium.ttf              | Não         | Não                  |
| sl               | Slovenian            | NotoSans-Medium.ttf              | Não         | Não                  |
| uk               | Ukrainian            | NotoSans-Medium.ttf              | Não         | Não                  |
| my               | Burmese (Myanmar)    | NotoSans-Medium.ttf              | Não         | Não                  |

## Adicionando um novo idioma

Para adicionar suporte a um novo idioma:

1. Acesse [src/co_op_translator/fonts/font_language_mappings.yml](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/fonts/font_language_mappings.yml).
2. Adicione o código do idioma, o nome e o nome do arquivo de fonte apropriado. Certifique-se de incluir o atributo `rtl` se o idioma for da direita para a esquerda.
3. Se precisar usar uma nova fonte, verifique se ela é livre para uso em projetos open-source, conferindo a licença e os termos de direitos autorais. Após a verificação, adicione o arquivo da fonte no diretório `src/co_op_translator/fonts/`.
4. Teste suas alterações localmente para garantir que o novo idioma seja suportado corretamente.
5. Envie um Pull Request com suas alterações e indique a adição do novo idioma na descrição do PR.

Exemplo:

```yaml
new_lang:
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.