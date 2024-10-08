# Install the Co-op translator package

The **Co-op Translator** is a command-line interface (CLI) tool designed to help you translate all the markdown files and images in your project into multiple languages. This tutorial will guide you through configuring the translator and running it for various use cases.

### Create a virtual environment

You can create a virtual environment using either `pip` or `Poetry`. Type one of the following commands inside your terminal.

#### Using pip

```bash
python -m venv .venv
```

#### Using Poetry

```bash
poetry init
```

### Activate the virtual environment

After creating the virtual environment, you'll need to activate it. The steps differ based on your operating system. Type the following command inside your terminal.

#### For both pip and Poetry

- Windows:

    ```bash
    venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source venv/bin/activate
    ```

#### Using Poetry

1. If you created the environment with Poetry, type the following command inside your terminal to activate it.

    ```bash
    poetry shell
    ```

### Installing the Package and required Packages

Once your virtual environment is set up and activated, the next step is to install the necessary dependencies.

#### Using Poetry (from pyproject.toml)

1. If you're using Poetry, type the following command inside your terminal. It will automatically install the required packages specified in the `pyproject.toml` file:

    ```bash
    poetry install
    ```
