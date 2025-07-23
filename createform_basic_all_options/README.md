# DataZone Custom Form Creator

This repository contains a Python script for creating custom form types in Amazon DataZone with advanced annotations.

## Overview

The `create_custom_form-updated.py` script simplifies the process of creating custom form types in Amazon DataZone by providing a structured approach with sensible defaults while still allowing customization through user input. The script includes advanced DataZone annotations that match the behavior of forms created through the AWS console.

## Features

- Creates a custom form type with predefined fields
- Supports both required and optional fields
- Handles different data types (String, Integer, Boolean)
- Includes advanced DataZone annotations for enhanced functionality
- Provides interactive prompts with default values
- Displays detailed results of the form creation

## Form Structure

The script creates a form with the following fields:

| Field Name | Data Type | Required | Annotations | Description |
|------------|-----------|----------|------------|-------------|
| Name | String | Yes | `@amazon.datazone#requiredForCondition(actions:["PUBLISHING","SUBSCRIPTION"])`, `@amazon.datazone#searchable` | The name of the item, required for publishing and subscription actions, and searchable |
| Description | String | No | None | A description of the item |
| ID | Integer | Yes | None | A unique identifier |
| VIP | Boolean | No | None | A flag indicating VIP status |

## Advanced Annotations

The script uses the following DataZone-specific annotations:

- `@amazon.datazone#requiredForCondition(actions:["PUBLISHING","SUBSCRIPTION"])`: Makes the field required specifically for publishing and subscription actions
- `@amazon.datazone#searchable`: Makes the field searchable in the DataZone interface

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
python create_custom_form-updated.py
```

The script will:
1. Initialize the DataZone client
2. Prompt for your DataZone domain ID (with a default)
3. Prompt for your DataZone project ID (with a default)
4. Create the form type using the Smithy model with advanced annotations
5. Display the creation result

## Default Configuration

- Form Name: `customForm2`
- Domain ID: `your domain id`
- Project ID: `your project id`
- Region: `us-west-2`

You can override the domain and project IDs by providing your own values when prompted.

## How It Works

The script uses the AWS SDK for Python (boto3) to interact with the Amazon DataZone API. It creates a Smithy model that defines the structure of the form with advanced annotations and then calls the `create_form_type` API to register the form type in your DataZone domain.

## Smithy Model

The script generates a Smithy model that looks like this:

```
namespace <domain_id>

structure customForm2 {
    @required
    @amazon.datazone#requiredForCondition(actions:["PUBLISHING","SUBSCRIPTION"])
    @amazon.datazone#searchable
    Name: String,
    
    Description: String,
    
    @required
    ID: Integer,

    VIP: Boolean
}
```

## Error Handling

The script includes comprehensive error handling for:
- AWS client errors (with detailed error messages)
- Unexpected exceptions

## Customization

To modify the form structure, edit the `create_smithy_model()` function to change the fields, data types, required attributes, or annotations.
