# Install the Co Op translator package

The Co-Op Translator is a command-line interface (CLI) tool designed to help you translate all the markdown files and images in your project into multiple languages. This tutorial will guide you through configuring the translator and running it for various use cases.

### Install the Co Op translator package

1. Type the following command inside your terminal to create a virtual environment named *.venv*.

    ```console
    python -m venv .venv
    ```

1. Type the following command inside your terminal to activate the virtual environment.

    for Windows

    ```console
    .venv\Scripts\activate.bat
    ```

    for Mac / Linux

    ```console
    source .venv/bin/activate
    ```

    > **Note**
    > If it worked, you should see (.venv) before the command prompt. Remember to activate the virtual environment every time you work on the project by running from the repository's root directory.

1. To install the package, type the following command inside your terminal:

    ```console
    pip install co-op-translator==0.2.0
    ```
