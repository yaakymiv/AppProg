# AppProg

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-project.git
    cd your-project
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    - **Windows:**
      ```bash
      .\venv\Scripts\activate
      ```
    - **MacOS:**
      ```bash
      source venv/bin/activate
      ```

3. Download dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python main.py
    ```

## API Endpoint

The Flask application exposes an API endpoint:

- `/api/v1/hello-world-{variant_number}`: Returns a JSON response with a "Hello World" message specific to your variant number.
