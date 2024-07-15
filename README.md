# Text-to-Speech Converter using Amazon Polly

This is a Python-based Text-to-Speech (TTS) application that leverages Amazon Polly to convert text into lifelike speech. The application provides a simple graphical user interface (GUI) built using `tkinter` and enhanced with `ttkthemes`.

## Features

- Convert text to speech using Amazon Polly.
- Select different voices for the speech synthesis.
- Simple and modern GUI.

## Prerequisites

- Python 3.x ![Python](https://img.shields.io/badge/Python-3.x-blue)
- AWS Account with Amazon Polly enabled ![AWS](https://img.shields.io/badge/AWS-Polly-orange)
- AWS CLI configured with a profile (`boto3_user`) that has access to Polly ![AWS CLI](https://img.shields.io/badge/AWS%20CLI-Configured-brightgreen)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/text-to-speech
    cd text-to-speech
    ```

2. Create a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Install the `boto3` and `ttkthemes` packages if they are not listed in `requirements.txt`:
    ```sh
    pip install boto3 ttkthemes
    ```

## Configuration

Ensure you have AWS credentials set up. The application uses the `boto3_user` profile. You can set up AWS credentials by running:
```sh
aws configure --profile boto3_user
