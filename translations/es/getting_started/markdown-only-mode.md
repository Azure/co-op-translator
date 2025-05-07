<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-05-06T17:43:37+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "es"
}
-->
# Modo Solo Markdown

## Introducción
El modo solo Markdown está diseñado para traducir únicamente el contenido Markdown de tu proyecto. Este modo omite el proceso de traducción de imágenes y se enfoca exclusivamente en el contenido textual, siendo ideal para situaciones donde no se requiere traducir imágenes o no están configuradas las variables de entorno necesarias para Computer Vision.

## Cuándo Usar
- Cuando las variables de entorno relacionadas con Computer Vision no están configuradas.
- Cuando deseas traducir solo el contenido de texto sin actualizar los enlaces de imágenes.
- Cuando el usuario lo especifica explícitamente usando la opción `-md` en la línea de comandos.

## Cómo Activar
Para activar el modo solo Markdown, usa la opción `-md` en tu comando. Por ejemplo:
```
translate -l "ko" -md
```

O si las variables de entorno relacionadas con Computer Vision no están configuradas. Ejecutar `translate -l "ko"` cambiará automáticamente al modo solo Markdown.

```
translate -l "ko"
```

Este comando traduce el contenido Markdown al coreano y actualiza los enlaces de imagen a sus rutas originales, en lugar de modificarlos a rutas de imagen traducidas.

## Comportamiento
En modo solo Markdown:
- El proceso de traducción omite el paso de traducción de imágenes.
- Los enlaces de imagen en el Markdown permanecen sin cambios, apuntando a sus rutas originales.

## Ejemplos
### Antes
```markdown
![Image](../../../getting_started/translated/path/to/image.png)
```
### Después de usar el modo solo Markdown
```markdown
![Image](../../../getting_started/original/path/to/image.png)
```

## Solución de Problemas
- Asegúrate de que la opción `-md` esté correctamente especificada en el comando.
- Verifica que no haya variables de entorno de Computer Vision que interfieran con el proceso.

## Conclusión
El modo solo Markdown ofrece una forma simplificada de traducir el contenido de texto sin modificar los enlaces de imagen. Es especialmente útil cuando la traducción de imágenes no es necesaria o cuando se trabaja en entornos sin configuración de Computer Vision.

**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.