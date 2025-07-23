# DataZone Custom Form Creator

This repository contains a Python script for creating custom form types in Amazon DataZone.

## Overview

The `create_custom_form.py` script simplifies the process of creating custom form types in Amazon DataZone by providing a structured approach with sensible defaults while still allowing customization through user input.

## Features

- Creates a custom form type with predefined fields
- Supports both required and optional fields
- Handles different data types (String, Integer, Boolean)
- Provides interactive prompts with default values
- Displays detailed results of the form creation

## Form Structure

The script creates a form with the following fields:

| Field Name | Data Type | Required | Description |
|------------|-----------|----------|-------------|
| Name | String | Yes | The name of the item |
| Description | String | No | A description of the item |
| ID | Integer | Yes | A unique identifier |
| VIP | Boolean | No | A flag indicating VIP status |

## Prerequisites

- Python 3.x
- AWS credentials configured with appropriate permissions for Amazon DataZone
- boto3 library installed

## Installation

1. Clone this repository
2. Install required dependencies:
   ```
   pip install boto3
   ```

## Usage

Run the script from the command line:

```bash
python create_custom_form.py
```

The script will:
1. Initialize the DataZone client
2. Prompt for your DataZone domain ID (with a default)
3. Prompt for your DataZone project ID (with a default)
4. Create the form type using the Smithy model
5. Display the creation result

## Default Configuration

- Domain ID: `your domain id here`
- Project ID: `your project id here`
- Region: `us-west-2`
- Form Name: `customForm`

You can override these defaults by providing your own values when prompted.

## How It Works

The script uses the AWS SDK for Python (boto3) to interact with the Amazon DataZone API. It creates a Smithy model that defines the structure of the form and then calls the `create_form_type` API to register the form type in your DataZone domain.

## Error Handling

The script includes comprehensive error handling for:
- AWS client errors (with detailed error messages)
- Unexpected exceptions

## Customization

To modify the form structure, edit the `create_smithy_model()` function to change the fields, data types, or required attributes.
