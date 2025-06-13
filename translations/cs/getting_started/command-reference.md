<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-06-12T11:32:42+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "cs"
}
-->
# Command reference
The **Co-op Translator** CLI ofrece varias opciones para personalizar el proceso de traducción:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduce tu proyecto a los idiomas especificados. Ejemplo: translate -l "es fr de" traduce a español, francés y alemán. Usa translate -l "all" para traducir a todos los idiomas soportados.
translate -l "language_codes" -u              | Actualiza las traducciones eliminando las existentes y recreándolas. Warning: Esto eliminará todas las traducciones actuales para los idiomas especificados.
translate -l "language_codes" -img            | Traduce solo archivos de imagen.
translate -l "language_codes" -md             | Traduce solo archivos Markdown.
translate -l "language_codes" -chk            | Revisa los archivos traducidos en busca de errores y reintenta la traducción si es necesario.
translate -l "language_codes" -d              | Activa el modo debug para registros detallados.
translate -l "language_codes" -r "root_dir"   | Especifica el directorio raíz del proyecto.
translate -l "language_codes" -f              | Usa modo rápido para la traducción de imágenes (hasta 3x más rápido, con una ligera pérdida en calidad y alineación).
translate -l "language_codes" -y              | Confirma automáticamente todas las solicitudes (útil para pipelines CI/CD).
translate -l "language_codes" --help          | Detalles de ayuda dentro del CLI mostrando los comandos disponibles.

### Usage examples:

  1. Comportamiento por defecto (agrega nuevas traducciones sin eliminar las existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Agrega solo nuevas traducciones de imágenes en coreano (no se eliminan traducciones existentes):    translate -l "ko" -img

  3. Actualiza todas las traducciones en coreano (Warning: Esto elimina todas las traducciones coreanas existentes antes de traducir de nuevo):    translate -l "ko" -u

  4. Actualiza solo imágenes coreanas (Warning: Esto elimina todas las imágenes coreanas existentes antes de traducir de nuevo):    translate -l "ko" -img -u

  5. Agrega nuevas traducciones markdown para coreano sin afectar otras traducciones:    translate -l "ko" -md

  6. Revisa archivos traducidos en busca de errores y reintenta traducciones si es necesario: translate -l "ko" -chk

  7. Revisa archivos traducidos en busca de errores y reintenta traducciones (solo markdown): translate -l "ko" -chk -md

  8. Revisa archivos traducidos en busca de errores y reintenta traducciones (solo imágenes): translate -l "ko" -chk -img

  9. Usa modo rápido para la traducción de imágenes:    translate -l "ko" -img -f

  10. Ejemplo de modo debug: - translate -l "ko" -d: Activa registros de depuración.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.