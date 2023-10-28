# KeaML Deployments

This is a Python library that serves as an SDK for deploying models in KeaML. It provides a simple way to initialize a client and deploy machine learning models.

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Key](#api-key)

## Installation

You can install the latest version of KeaML SDK from PyPI:

```bash
pip install keaml
```

## Getting Started

Before you can use KeaML SDK, you'll need to initialize the client with an API key.

### API Key

To get your API key, visit [KEAML Settings](https://app.keaml.com/settings) and generate a new API key.

## Usage

Here's a simple example to get you started:

```python
import keaml

# Initialize the client with your API key
kea_client = keaml.init(api_key="your_api_key_here")

# Deploy a machine learning model
kea_client.deploy(model_object, model_name, framework_name)
```

### Methods

#### `init(api_key: str) -> KeaMLSDKClient`

Initializes the KeaML SDK client.

- **Parameters:**
  - `api_key` (str): Your KEAML API key.

- **Returns:**
  - An instance of `KeaMLSDKClient`.

#### `KeaMLSDKClient.deploy(model: Any, name: str, framework: str) -> None`

Deploys a machine learning model.

- **Parameters:**
  - `model` (Any): The machine learning model object.
  - `name` (str): The name of the model.
  - `framework` (str): The framework used for the model (e.g., "tensorflow", "pytorch").

- **Returns:**
  - None

