<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a6cddf5e9648ef0bba0de7eb07e74cf1",
  "translation_date": "2025-10-15T02:10:18+00:00",
  "source_file": "getting_started/command-reference.md",
  "language_code": "es"
}
-->
# Referencia de comandos

La CLI de **Co-op Translator** ofrece varias opciones para personalizar el proceso de traducción:

Comando                                       | Descripción
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduce tu proyecto a los idiomas especificados. Ejemplo: translate -l "es fr de" traduce a español, francés y alemán. Usa translate -l "all" para traducir a todos los idiomas soportados.
translate -l "language_codes" -u              | Actualiza las traducciones eliminando las existentes y recreándolas. Advertencia: Esto eliminará todas las traducciones actuales para los idiomas especificados.
translate -l "language_codes" -img            | Traduce solo archivos de imagen.
translate -l "language_codes" -md             | Traduce solo archivos Markdown.
translate -l "language_codes" -nb             | Traduce solo archivos de cuadernos Jupyter (.ipynb).
translate -l "language_codes" --fix           | Retraduce archivos con puntuaciones de confianza bajas según los resultados de evaluaciones previas.
translate -l "language_codes" -d              | Activa el modo de depuración para obtener registros detallados.
translate -l "language_codes" --save-logs, -s | Guarda los registros de nivel DEBUG en archivos bajo <root_dir>/logs/ (la consola sigue controlada por -d)
translate -l "language_codes" -r "root_dir"   | Especifica el directorio raíz del proyecto
translate -l "language_codes" -f              | Usa el modo rápido para la traducción de imágenes (hasta 3 veces más rápido, con una ligera pérdida de calidad y alineación).
translate -l "language_codes" -y              | Confirma automáticamente todos los avisos (útil para pipelines CI/CD)
translate -l "language_codes" --help          | Muestra detalles de ayuda en la CLI con los comandos disponibles
evaluate -l "language_code"                  | Evalúa la calidad de la traducción para un idioma específico y proporciona puntuaciones de confianza
evaluate -l "language_code" -c 0.8           | Evalúa traducciones con un umbral de confianza personalizado
evaluate -l "language_code" -f               | Modo de evaluación rápida (solo basado en reglas, sin LLM)
evaluate -l "language_code" -D               | Modo de evaluación profunda (solo basado en LLM, más exhaustivo pero más lento)
evaluate -l "language_code" --save-logs, -s  | Guarda los registros de nivel DEBUG en archivos bajo <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocesa archivos Markdown traducidos para actualizar enlaces a cuadernos (.ipynb). Prefiere cuadernos traducidos cuando están disponibles; de lo contrario, puede usar los originales.
migrate-links -l "language_codes" -r          | Especifica el directorio raíz del proyecto (por defecto: directorio actual).
migrate-links -l "language_codes" --dry-run   | Muestra qué archivos cambiarían sin escribir los cambios.
migrate-links -l "language_codes" --no-fallback-to-original | No reescribe enlaces a cuadernos originales cuando faltan los traducidos (solo actualiza si existe la traducción).
migrate-links -l "language_codes" -d          | Activa el modo de depuración para obtener registros detallados.
migrate-links -l "language_codes" --save-logs, -s | Guarda los registros de nivel DEBUG en archivos bajo <root_dir>/logs/
migrate-links -l "all" -y                      | Procesa todos los idiomas y confirma automáticamente el aviso.

## Ejemplos de uso

  1. Comportamiento por defecto (agrega nuevas traducciones sin eliminar las existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Agrega solo nuevas traducciones de imágenes en coreano (no se eliminan traducciones existentes):    translate -l "ko" -img

  3. Actualiza todas las traducciones en coreano (Advertencia: Esto elimina todas las traducciones existentes en coreano antes de retraducir):    translate -l "ko" -u

  4. Actualiza solo imágenes en coreano (Advertencia: Esto elimina todas las imágenes existentes en coreano antes de retraducir):    translate -l "ko" -img -u

  5. Agrega nuevas traducciones Markdown para coreano sin afectar otras traducciones:    translate -l "ko" -md

  6. Corrige traducciones con baja confianza según resultados de evaluaciones previas: translate -l "ko" --fix

  7. Corrige traducciones con baja confianza solo para archivos específicos (markdown): translate -l "ko" --fix -md

  8. Corrige traducciones con baja confianza solo para archivos específicos (imágenes): translate -l "ko" --fix -img

  9. Usa el modo rápido para la traducción de imágenes:    translate -l "ko" -img -f

  10. Corrige traducciones con baja confianza con un umbral personalizado: translate -l "ko" --fix -c 0.8

  11. Ejemplo de modo depuración: - translate -l "ko" -d: Activa el registro de depuración.
  12. Guarda los registros en archivos: translate -l "ko" -s
  13. DEBUG en consola y archivos: translate -l "ko" -d -s

  14. Migra enlaces de cuadernos para traducciones en coreano (actualiza enlaces a cuadernos traducidos cuando estén disponibles):    migrate-links -l "ko"

  15. Migra enlaces en modo dry-run (sin escribir archivos):    migrate-links -l "ko" --dry-run

  16. Solo actualiza enlaces cuando existen cuadernos traducidos (no usa los originales):    migrate-links -l "ko" --no-fallback-to-original

  17. Procesa todos los idiomas con aviso de confirmación:    migrate-links -l "all"

  18. Procesa todos los idiomas y confirma automáticamente:    migrate-links -l "all" -y
  19. Guarda los registros en archivos para migrate-links:    migrate-links -l "ko ja" -s

### Ejemplos de evaluación

> [!WARNING]  
> **Funcionalidad Beta**: La funcionalidad de evaluación está actualmente en beta. Esta función fue lanzada para evaluar documentos traducidos, y los métodos de evaluación y su implementación detallada aún están en desarrollo y pueden cambiar.

  1. Evalúa traducciones en coreano: evaluate -l "ko"

  2. Evalúa con un umbral de confianza personalizado: evaluate -l "ko" -c 0.8

  3. Evaluación rápida (solo basada en reglas): evaluate -l "ko" -f

  4. Evaluación profunda (solo basada en LLM): evaluate -l "ko" -D

---

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de cualquier malentendido o interpretación incorrecta que surja del uso de esta traducción.