# Contribuir mejoras de idioma

Tu conocimiento del idioma puede ayudar a mejorar Co-op Translator. Empieza con un ejemplo, una corrección sugerida y una explicación usando el [formulario de comentarios de traducción](https://github.com/Azure/co-op-translator/issues/new?template=translation_feedback.yml). No necesitas escribir código ni pagar por una ejecución del modelo.

## De un informe a una mejora compartida

1. Un colaborador proporciona un extracto de la fuente, su traducción y el contexto.
2. Un revisor de idioma verifica el significado, la naturalidad y si la sugerencia depende de una localidad o curso específico.
3. Un mantenedor decide si la corrección debe estar en el curso fuente, en una instrucción de idioma compartida, en la configuración de terminología o en el código de traducción.
4. Para una regla compartida, un mantenedor compara las salidas antes y después del cambio en el ejemplo reportado y en ejemplos no relacionados. Los colaboradores pueden revisar estas salidas sin ejecutar la herramienta por sí mismos.
5. El PR resultante enlaza el informe y acredita a las personas que aportaron ejemplos y la revisión. El despliegue o la regeneración en los repositorios consumidores es un paso aparte.

Un informe no cambia automáticamente los prompts ni regenera las traducciones del curso. Las correcciones específicas de un curso deben permanecer vinculadas al repositorio del curso. No asumas que una edición manual sobrevivirá a una retraducción posterior; confirma el comportamiento para ese flujo de trabajo.

## Ejemplo existente: enlaces Markdown en japonés

El [archivo de instrucciones en japonés](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/templates/language/ja.md) indica al modelo que traduzca el texto del enlace mientras preserva la sintaxis Markdown y el destino del enlace. Por ejemplo, un enlace escrito como `[text](URL)` no debe convertirse en `「text」（URL）`.

Este es un ejemplo concreto de una regla de idioma respaldada por una ilustración de salida correcta e incorrecta. No es evidencia de que las instrucciones del prompt por sí solas garanticen Markdown correcto.

El [generador de prompts Markdown](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/utils/markdown/prompts.py) carga `templates/language/<language_code>.md` usando un código de idioma en minúsculas y recortado. Si no existe el archivo, usa las instrucciones comunes. Esto describe la ruta del prompt Markdown; no supongas que cada imagen u otra ruta de traducción use las mismas instrucciones.

Las [pruebas de prompts](https://github.com/Azure/co-op-translator/blob/main/tests/co_op_translator/utils/markdown/test_prompts.py) comprueban que las instrucciones en japonés estén incluidas. Eso verifica el ensamblaje del prompt, no la calidad de la traducción.

## ¿Qué debe incluir una regla de idioma?

Propón una corrección precisa y repetible con un ejemplo de origen, el comportamiento esperado y un contraejemplo donde la regla no deba aplicarse. Conserva el significado, los marcadores de posición, el código, las URL y la estructura del documento. Evita convertir la preferencia de estilo de una persona o la terminología de un curso en una regla universal.

La [implementación del glosario](https://github.com/Azure/co-op-translator/blob/main/src/co_op_translator/glossary.py) actual protege términos contra la traducción. No es un diccionario de terminología de origen a destino. Discute el nuevo comportamiento de terminología antes de prometerlo a los colaboradores.

## Ejemplo comunitario: un informe sobre nombre de producto en japonés

En el [informe #527](https://github.com/Azure/co-op-translator/issues/527), @hyoshioka0128 identificó una traducción al japonés que cambió el nombre del producto `Co-op Translator` a `Co-op 翻訳`. El informe incluía un enlace al documento afectado y una captura de pantalla, lo que facilitó localizar el problema.

El colaborador también enlazó un [PR de curso relacionado](https://github.com/microsoft/AZD-for-beginners/pull/109). En la discusión del issue, el mantenedor reconoció el informe y propuso investigar por qué cambió el nombre, incluyendo la protección de terminología, el comportamiento del glosario y la ruta de traducción.

Esto muestra cómo un pequeño informe puede respaldar la investigación más allá de una corrección de redacción individual. No es un resultado verificado de antes/después ni evidencia de que las instrucciones japonesas de enlaces Markdown arriba hayan solucionado este problema del nombre del producto.

Puedes contribuir de la misma manera: comparte el texto original, la traducción actual, la corrección sugerida y por qué importa. Añade un enlace al documento o una captura de pantalla cuando sea útil. No necesitas diagnosticar la causa ni escribir un prompt antes de reportarlo.

## Validación antes de adoptar una regla

Usa las mismas muestras de origen, revisión del traductor, proveedor/modelo y ajustes de generación para las ejecuciones de referencia y candidatas, cambiando solo la instrucción propuesta. Registra el cambio real del prompt y las salidas; repite ejemplos cuando sea necesario para distinguir un efecto consistente de la variabilidad de las salidas. Incluye la falla reportada, contextos contrastantes y ejemplos que ya se traducen correctamente.

| Muestra | Fuente/contexto | Salida base | Salida candidata | Evaluación del revisor |
| --- | --- | --- | --- | --- |
| Falla reportada | Por recopilar | No ejecutado | No ejecutado | Pendiente |
| Contraejemplo | Por recopilar | No ejecutado | No ejecutado | Pendiente |
| Ejemplo no afectado | Por recopilar | No ejecutado | No ejecutado | Pendiente |

Comprueba los invariantes estructurales por separado de los juicios lingüísticos. Una prueba exitosa de carga del prompt no es una evaluación de calidad, y una única frase exacta esperada no es la única traducción válida. Si faltan contexto, ejecuciones del modelo o revisión lingüística, deja la propuesta pendiente en lugar de afirmar que el problema está solucionado.