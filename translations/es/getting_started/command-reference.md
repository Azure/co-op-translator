<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b38d8f042530a4bc872def7cb2c141cd",
  "translation_date": "2025-05-06T17:41:00+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "es"
}
-->
# Referencia de comandos  
La CLI **Co-op Translator** ofrece varias opciones para personalizar el proceso de traducción:

Comando                                      | Descripción  
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
translate -l "language_codes"                 | Traduce tu proyecto a los idiomas especificados. Ejemplo: translate -l "es fr de" traduce al español, francés y alemán. Usa translate -l "all" para traducir a todos los idiomas soportados.  
translate -l "language_codes" -u              | Actualiza las traducciones eliminando las existentes y recreándolas. Advertencia: Esto borrará todas las traducciones actuales para los idiomas especificados.  
translate -l "language_codes" -img            | Traduce solo archivos de imagen.  
translate -l "language_codes" -md             | Traduce solo archivos Markdown.  
translate -l "language_codes" -chk            | Revisa los archivos traducidos en busca de errores y reintenta la traducción si es necesario.  
translate -l "language_codes" -d              | Activa el modo debug para un registro detallado.  
translate -l "language_codes" -r "root_dir"   | Especifica el directorio raíz del proyecto.  
translate -l "language_codes" -f              | Usa el modo rápido para la traducción de imágenes (hasta 3 veces más rápido, con una ligera pérdida en calidad y alineación).  
translate -l "language_codes" -y              | Confirma automáticamente todas las solicitudes (útil para pipelines CI/CD).  
translate -l "language_codes" --help          | Muestra detalles de ayuda dentro de la CLI con los comandos disponibles.  

### Ejemplos de uso:  

  1. Comportamiento por defecto (agrega nuevas traducciones sin eliminar las existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"  

  2. Agrega solo nuevas traducciones de imágenes en coreano (sin eliminar traducciones existentes):    translate -l "ko" -img  

  3. Actualiza todas las traducciones en coreano (Advertencia: Esto elimina todas las traducciones coreanas existentes antes de volver a traducir):    translate -l "ko" -u  

  4. Actualiza solo las imágenes en coreano (Advertencia: Esto elimina todas las imágenes coreanas existentes antes de volver a traducir):    translate -l "ko" -img -u  

  5. Agrega nuevas traducciones markdown para coreano sin afectar otras traducciones:    translate -l "ko" -md  

  6. Revisa los archivos traducidos en busca de errores y reintenta la traducción si es necesario: translate -l "ko" -chk  

  7. Revisa los archivos traducidos en busca de errores y reintenta la traducción (solo markdown): translate -l "ko" -chk -md  

  8. Revisa los archivos traducidos en busca de errores y reintenta la traducción (solo imágenes): translate -l "ko" -chk -img  

  9. Usa el modo rápido para la traducción de imágenes:    translate -l "ko" -img -f  

  10. Ejemplo de modo debug: - translate -l "ko" -d: Activa el registro en modo debug.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.