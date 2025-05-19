# DiagramGPT 🎨

A powerful Streamlit-based application that leverages Azure OpenAI to transform natural language descriptions into professional architecture diagrams. Perfect for software architects, developers, and technical professionals who need to quickly create and iterate on system architecture diagrams.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.0%2B-FF4B4B.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## ✨ Features

- 🤖 **AI-Powered Diagram Generation**: Convert natural language descriptions into detailed architecture diagrams
- ⚡ **Real-time Preview**: See your changes instantly as you modify the diagram code
- 🎨 **Interactive Editor**: Built-in code editor for fine-tuning diagram details
- 🔄 **Easy Iterations**: Quick generation and modification of diagrams
- 🎯 **Azure OpenAI Integration**: Leverages advanced language models for accurate diagram generation
- 📊 **Multiple Diagram Types**: Support for various architecture and system diagrams

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:

- Python 3.8 or higher installed
- An Azure OpenAI API account with active subscription
- Basic knowledge of system architecture concepts

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ashish993/diagramGPT.git
   cd diagramGPT
   ```

2. **Create and Activate Virtual Environment** (Recommended)
   ```bash
   # For macOS/Linux
   python -m venv venv
   source venv/bin/activate

   # For Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Create Streamlit Configuration Directory**
   ```bash
   mkdir -p .streamlit
   ```

2. **Set Up Azure OpenAI Credentials**
   - Copy the template configuration file:
     ```bash
     cp .streamlit/secrets.toml.template .streamlit/secrets.toml
     ```
   - Edit `.streamlit/secrets.toml` with your Azure OpenAI credentials:
     ```toml
     AZURE_OPENAI_ENDPOINT = "your-azure-endpoint"
     AZURE_OPENAI_API_KEY = "your-api-key"
     AZURE_OPENAI_DEPLOYMENT = "your-deployment-name"
     AZURE_OPENAI_MODEL_NAME = "your-model-name"
     ```

   ⚠️ **Security Note**: Never commit `secrets.toml` to version control!

## 🎮 Usage Guide

1. **Start the Application**
   ```bash
   streamlit run app.py
   ```
   The application will open in your default browser at `http://localhost:8501`

2. **Creating Your First Diagram**
   1. Enter your architecture description in the text input area
      - Example: "Create a three-tier web application with a React frontend, Python API backend, and PostgreSQL database"
   2. Click "Generate Code" to create the initial diagram code
   3. Review and modify the generated code in the editor if needed
   4. Click "Generate Diagram" to visualize your architecture

3. **Modifying Diagrams**
   - Use the interactive code editor to:
     - Adjust component positions
     - Add/remove components
     - Modify relationships
     - Change styles and colors
   - Click "Generate Diagram" after each modification to update the visualization

## 🛠️ Advanced Usage

### Custom Styling
- Modify node shapes using the `shape` attribute
- Customize colors using hex codes or predefined colors
- Adjust line styles for connections
- Add custom icons to nodes

### Complex Diagrams
- Group related components using clusters
- Create multi-level hierarchies
- Add detailed annotations
- Use different arrow types for various relationships

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues and Solutions

1. **Application Won't Start**
   - Verify Python version: `python --version`
   - Check all dependencies are installed: `pip freeze`
   - Ensure Streamlit is properly installed: `streamlit --version`

2. **Diagram Generation Fails**
   - Verify Azure OpenAI credentials in `.streamlit/secrets.toml`
   - Check internet connectivity
   - Ensure Azure OpenAI service is available

3. **Diagram Not Updating**
   - Clear browser cache
   - Restart the Streamlit server
   - Check for syntax errors in the diagram code

For additional support, please [open an issue](https://github.com/ashish993/diagramGPT/issues) on our GitHub repository.

## 📞 Support

If you encounter any problems or have suggestions, please:
1. Check the [Issues](https://github.com/ashish993/diagramGPT/issues) page
2. Submit a new issue if your problem isn't already listed
3. Provide as much detail as possible about your environment and the problem