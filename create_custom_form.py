#!/usr/bin/env python3
"""
DataZone Custom Form Creator

This script creates a custom form type in Amazon DataZone with specified fields.
The form includes required and optional fields of different data types.
"""

import boto3
import json
from botocore.exceptions import ClientError

# Default values
DEFAULT_DOMAIN_ID = "your domain id here"
DEFAULT_PROJECT_ID = "your project id here"
DEFAULT_REGION = "us-west-2"
FORM_NAME = "customForm"


def create_smithy_model(domain_id):
    """
    Creates a Smithy model for the form with the correct namespace.
    
    Args:
        domain_id (str): The DataZone domain ID to use as namespace
        
    Returns:
        str: The Smithy model definition
    """
    return f"""namespace {domain_id}

structure {FORM_NAME} {{
    @required
    Name: String,
    
    Description: String,
    
    @required
    ID: Integer,

    VIP: Boolean
}}"""


def create_form_type(client, domain_id, project_id):
    """
    Creates a custom form type in DataZone.
    
    Args:
        client: The boto3 DataZone client
        domain_id (str): The ID of the DataZone domain
        project_id (str): The ID of the project that owns this form type
        
    Returns:
        dict: Response containing details of the created form type
    """
    # Generate the Smithy model
    smithy_model = create_smithy_model(domain_id)
    
    # Create the form type
    return client.create_form_type(
        domainIdentifier=domain_id,
        name=FORM_NAME,
        model={"smithy": smithy_model},
        owningProjectIdentifier=project_id,
        status="ENABLED"
    )


def get_user_input(prompt, default_value):
    """
    Gets user input with a default value.
    
    Args:
        prompt (str): The prompt to display to the user
        default_value (str): The default value to use if no input is provided
        
    Returns:
        str: The user input or default value
    """
    user_input = input(f"{prompt} [{default_value}]: ")
    return user_input.strip() if user_input.strip() else default_value


def display_result(result):
    """
    Displays the result of the form type creation.
    
    Args:
        result (dict): The response from the create_form_type API call
    """
    print("\nForm type created successfully!")
    print(f"Name: {result.get('name')}")
    print(f"Domain ID: {result.get('domainId')}")
    print(f"Project ID: {result.get('owningProjectId')}")
    print(f"Revision: {result.get('revision')}")
    
    print("\nFull response:")
    print(json.dumps(result, indent=2))


def main():
    """
    Main function to execute the form type creation process.
    """
    try:
        # Initialize the DataZone client
        dzclient = boto3.client('datazone', region_name=DEFAULT_REGION)
        print(f"DataZone client initialized successfully in region {DEFAULT_REGION}.")
        
        # Get user inputs with defaults
        domain_id = get_user_input("Enter your DataZone domain ID", DEFAULT_DOMAIN_ID)
        project_id = get_user_input("Enter your DataZone project ID", DEFAULT_PROJECT_ID)
        
        # Create the form type
        print(f"\nCreating form type '{FORM_NAME}' in domain '{domain_id}'...")
        result = create_form_type(dzclient, domain_id, project_id)
        
        # Display the result
        display_result(result)
        
        return result
        
    except ClientError as e:
        error_message = e.response.get('Error', {}).get('Message', str(e))
        print(f"Error creating form type: {error_message}")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None


if __name__ == "__main__":
    main()
