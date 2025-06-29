<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:37:48+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "sr"
}
-->
# Инсталирање Co-op translator пакета

**Co-op Translator** је алатка за командну линију (CLI) дизајнирана да вам помогне да преведете све markdown фајлове и слике у вашем пројекту на више језика. Овај туторијал ће вас провести кроз конфигурисање преводиоца и његово покретање за различите случајеве употребе.

### Креирање виртуелног окружења

Виртуелно окружење можете направити користећи или `pip` или `Poetry`. Укуцајте једну од следећих команди у вашем терминалу.

#### Коришћење pip

```bash
python -m venv .venv
```

#### Коришћење Poetry

```bash
poetry init
```

### Активирање виртуелног окружења

Након креирања виртуелног окружења, потребно је да га активирате. Кораци се разликују у зависности од вашег оперативног система. Укуцајте следећу команду у терминалу.

#### За pip и Poetry

- Windows:

    ```bash
    .venv\Scripts\activate
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Коришћење Poetry

1. Ако сте креирали окружење помоћу Poetry, укуцајте следећу команду у терминалу да бисте га активирали.

    ```bash
    poetry shell
    ```

### Инсталирање пакета и потребних зависности

Када је ваше виртуелно окружење подешено и активирано, следећи корак је инсталација неопходних зависности.

### Брза инсталација

Инсталирајте Co-Op Translator преко pip

```
pip install co-op-translator
```  
Или

Инсталирајте преко poetry  
```
poetry add co-op-translator
```

#### Коришћење pip-а (из requirements.txt) ако сте клонирали овај репозиторијум

![NOTE] Молимо вас да ОВО НЕ РАДИТЕ ако сте инсталирали co-op translator преко брзе инсталације.

1. Ако користите pip, укуцајте следећу команду у терминалу. Она ће аутоматски инсталирати потребне пакете наведене у `requirements.txt` фајлу:

    ```bash
    pip install -r requirements.txt
    ```

#### Коришћење Poetry (из pyproject.toml)

1. Ако користите Poetry, укуцајте следећу команду у терминалу. Она ће аутоматски инсталирати потребне пакете наведене у `pyproject.toml` фајлу:

    ```bash
    poetry install
    ```

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала употребом овог превода.