<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:35:46+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "es"
}
-->
# Modo Solo Markdown

## Introducción
El modo solo Markdown está diseñado para traducir únicamente el contenido Markdown de tu proyecto. Este modo omite el proceso de traducción de imágenes y se centra exclusivamente en el contenido textual, lo que lo hace ideal para situaciones donde no se requiere traducir imágenes o no se han configurado las variables de entorno necesarias para Computer Vision.

## Cuándo usarlo
- Cuando no están configuradas las variables de entorno relacionadas con Computer Vision.
- Cuando quieres traducir solo el contenido de texto sin actualizar los enlaces de imágenes.
- Cuando el usuario lo especifica explícitamente usando la opción de línea de comandos `-md`.

## Cómo habilitarlo
Para activar el modo solo Markdown, usa la opción `-md` en tu comando. Por ejemplo:
```
translate -l "ko" -md
```

O si las variables de entorno relacionadas con Computer Vision no están configuradas. Ejecutar `translate -l "ko"` cambiará automáticamente al modo solo Markdown.

```
translate -l "ko"
```

Este comando traduce el contenido Markdown al coreano y actualiza los enlaces de imágenes a sus rutas originales, en lugar de modificarlos a rutas de imágenes traducidas.

## Comportamiento
En modo solo Markdown:
- El proceso de traducción omite el paso de traducción de imágenes.
- Los enlaces de imágenes en Markdown permanecen sin cambios, apuntando a sus rutas originales.

## Ejemplos
### Antes
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.es.png)
```
### Después de usar modo solo Markdown
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.es.png)
```

## Solución de problemas
- Asegúrate de que la opción `-md` esté especificada correctamente en el comando.
- Verifica que ninguna variable de entorno de Computer Vision interfiera con el proceso.

## Conclusión
El modo solo Markdown ofrece una forma simplificada de traducir el contenido de texto sin modificar los enlaces de imágenes. Es especialmente útil cuando la traducción de imágenes no es necesaria o cuando se trabaja en entornos sin configuración de Computer Vision.

**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por un humano. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.