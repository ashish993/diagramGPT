# Diagram Generator

A Streamlit-based application that generates architecture diagrams using natural language processing and Azure OpenAI.

## Features
- Convert natural language descriptions into architecture diagrams
- Interactive code editor for diagram customization
- Azure OpenAI integration for intelligent diagram generation

## Prerequisites
- Python 3.8 or higher
- Azure OpenAI API access

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.streamlit/secrets.toml` file with your Azure OpenAI credentials:
```toml
AZURE_OPENAI_ENDPOINT = "your-azure-endpoint"
AZURE_OPENAI_API_KEY = "your-api-key"
AZURE_OPENAI_DEPLOYMENT = "your-deployment-name"
AZURE_OPENAI_MODEL_NAME = "your-model-name"
```

⚠️ Never commit the `secrets.toml` file to version control!

## Running the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## Usage
1. Enter your architecture description in the text area
2. Click "Generate Code" to create the diagram
3. The generated diagram code can be modified in the editor
4. Click "Generate Diagram" to update the visualization

## License
MIT