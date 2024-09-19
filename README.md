# Project

# Co Op Translator

_Easily automate multilingual translations for your projects powered by advanced LLM technology._

[![Python package](https://img.shields.io/pypi/v/co-op-translator)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

## Overview of Co Op Translator

**Co Op Translator** is a tool designed to automate multilingual translations for various projects using advanced Large Language Model (LLM) technology. This project aims to simplify the process of translating content into multiple languages, making it accessible and efficient for developers.

### Python Package

**Co Op Translator** Python package designed to automate multilingual translations across all files in your project. Powered by advanced Language Learning Models (LLMs), it simplifies the localization process by providing accurate and efficient translations.

Co Op Translator scans all your project files and translates all Markdown documents and even text within images found in your folders. This comprehensive approach ensures that every part of your project is accessible to a global audience.

By integrating Co Op Translator into your workflow, you can:

- **Automate Translations:** Easily translate text in your project files into multiple languages.
- **Comprehensive Coverage:** Translate all Markdown files and text within images in your project directories.
- **Advanced LLM Technology:** Utilize cutting-edge language models for high-quality translations.
- **Simplify Localization:** Streamline the process of localizing your project for international markets.
- **Easy Integration:** Seamlessly integrate with your existing project setup.

Co Op Translator empowers developers to focus on core functionalities while effortlessly managing multilingual support.

Here is an example of how Co Op Translator can be used to translate text in images and Markdown files in your project:

![Example](/imgs/ex.png)


#### Key Features:
- **Multilingual Translation**: Supports translation into multiple languages, leveraging the power of LLMs.
- **Automation**: Automates the translation process, reducing manual effort and increasing consistency.
- **Integration**: Easily integrates with existing projects, providing a seamless translation experience.

#### Getting Started:
1. **Setting Up the Development Environment**:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - For Windows:
       ```bash
       venv\Scripts\activate.bat
       ```
     - For Mac/Linux:
       ```bash
       source venv/bin/activate
       ```

2. **Installing Required Packages**:
   - Install the necessary packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Environment Variables**:
   - Create an `.env` file in the root directory by copying the provided `.env.template` file.
   - Fill in the environment variables as guided.

4. **Installing the Package**:
   - Install the package in editable mode:
     ```bash
     pip install -e .
     ```

5. **Running Tests**:
   - Ensure the virtual environment is activated and run tests:
     ```bash
     pytest tests/
     ```

#### Sample Notebooks:
- **Getting Started with notebook: basic version**
- **Getting Started with notebook: module version**

#### Repository Structure:
- **data/**: Contains data files.
- **notebooks/**: Jupyter notebooks for examples and tutorials.
- **src/co_op_translator/**: Source code for the translator.
- **tests/**: Test cases for the project.


## Getting started with Co Op Translator

### How to Use Co Op Translator

1. [Set up Azure resources before starting](./docs/set-up-azure-resources.md)
1. [Create an '.env' file in the root directory](./docs/create-env-file.md)
1. [Install the Co Op translator package](./docs/install-package.md)
1. [Use Co Op translator in your project](./docs/use-co-op-translator.md)

### Prerequisites

- Azure AI Services resource
- Azure OpenAI resource
- Python 3.10 or higher


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
