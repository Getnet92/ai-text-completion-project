# AI-Powered Text Completion Project

This project implements an AI-powered text completion application using Python and the Hugging Face Inference API.

## Setup

1.  **Prerequisites:**
    * Python 3.6 or higher.
    * pip (Python's package installer).

2.  **Install Dependencies:**
    ```bash
    pip install huggingface_hub
    ```

3.  **Hugging Face Access Token:**
    * You need a Hugging Face access token to use the Inference API.
    * Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) and create a new token with the "read" role.
    * Set the token as an environment variable named `HF_TOKEN`.

    * **Windows:**
        ```powershell
        $env:HF_TOKEN="your_token_here"
        ```
        (Remember to set it as a system environment variable for persistent use and restart your terminal.)
    * **Linux/macOS:**
        ```bash
        export HF_TOKEN="your_token_here"
        ```
        (Add this to your shell configuration file (e.g., `~/.bashrc`) for persistent use.)

## Usage

1.  **Run the script:**
    ```bash
    python your_script_name.py
    ```

2.  **Interact with the application:**
    * The application will prompt you to enter a text prompt.
    * The AI-generated response will be displayed.
    * Type `quit` or `exit` to end the session.

## Dependencies

* `huggingface_hub`:  For interacting with the Hugging Face Inference API.
