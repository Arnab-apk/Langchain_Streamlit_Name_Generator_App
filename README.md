# 🍽️ Restaurant Name Generator

An AI-powered web application that generates creative restaurant names and matching menu items based on your chosen cuisine. Built with Streamlit and LangChain.

![Restaurant Name Generator](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.54.0-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)

## ✨ Features

- 🌍 **Multiple Cuisines**: Choose from Indian, Arabian, Mexican, Italian, American, Japanese, and Chinese cuisines
- 🤖 **AI-Powered**: Uses OpenAI's GPT-3.5-turbo through OpenRouter to generate creative names and menus
- 🎨 **Beautiful UI**: Professional, responsive design with custom styling
- ⚡ **Real-time Generation**: Get instant results with loading animations
- 📋 **Complete Menu Items**: Generates 10 matching menu items for each restaurant

## 🚀 Demo

### 📹 Video Demo

https://github.com/yourusername/restaurant-name-generator/assets/demo.mp4

*Watch the app in action! The video shows the complete workflow from selecting a cuisine to generating restaurant names and menu items.*

### What the app generates:
- A unique, themed restaurant name based on your selected cuisine
- A comprehensive list of 10 menu items that match the restaurant concept

## 📋 Prerequisites

- Python 3.12 or higher
- OpenRouter API key (for OpenAI access)
- Git (for cloning the repository)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/restaurant-name-generator.git
   cd restaurant-name-generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```
   
   On macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

4. **Install required packages**
   ```bash
   pip install streamlit langchain langchain-openai langchain-core
   ```

5. **Set up your API key**
   
   - Copy `secret.py.example` to `secret.py`
   - Edit `secret.py` and add your OpenRouter API key:
   ```python
   openai_key="your-openrouter-api-key-here"
   alternate_key=""
   ```

## 🔑 Getting an API Key

1. Sign up at [OpenRouter](https://openrouter.ai/)
2. Navigate to your API Keys section
3. Create a new API key
4. Copy the key and paste it in `secret.py`

## 📦 Project Structure

```
restaurant-name-generator/
├── streamlit/
│   └── app.py              # Main Streamlit application
├── langchain_helper.py     # LangChain logic for AI generation
├── secret.py               # API keys (not tracked by git)
├── secret.py.example       # Template for API keys
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## 🎮 Usage

1. Make sure your virtual environment is activated
2. Run the Streamlit app:
   ```bash
   streamlit run streamlit/app.py
   ```
   
   Or using the full path:
   ```bash
   .\.venv\Scripts\streamlit.exe run streamlit\app.py
   ```

3. Open your browser to `http://localhost:8501`
4. Select a cuisine from the sidebar
5. Watch as AI generates a unique restaurant name and menu!

## 🧩 How It Works

1. **User Selection**: User selects a cuisine type from the sidebar
2. **AI Chain 1**: LangChain generates a creative restaurant name for the selected cuisine
3. **AI Chain 2**: Using the restaurant name, LangChain generates relevant menu items
4. **Display**: Results are beautifully formatted and displayed in the Streamlit interface

## 🎨 Technologies Used

- **Streamlit**: Web application framework
- **LangChain**: Framework for building LLM applications
- **OpenAI GPT-3.5-turbo**: Language model for text generation
- **OpenRouter**: API gateway for accessing OpenAI models
- **Python 3.12+**: Programming language

## 📝 Configuration

The app uses the following model configuration in `langchain_helper.py`:

```python
llm = ChatOpenAI(
    temperature=0.5,
    api_key=openai_key,
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-3.5-turbo"
)
```

You can adjust the `temperature` parameter (0.0-1.0) to control creativity:
- Lower values (0.0-0.3): More focused and deterministic
- Higher values (0.7-1.0): More creative and varied

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Important Notes

- **Never commit `secret.py`** to version control - it contains your API keys
- The `.gitignore` file is configured to prevent accidental commits
- Keep your OpenRouter API key secure and never share it publicly
- Monitor your API usage to avoid unexpected charges

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

Your Name - [Your GitHub Profile](https://github.com/yourusername)

## 🙏 Acknowledgments

- OpenAI for the GPT models
- OpenRouter for API access
- Streamlit for the amazing web framework
- LangChain for simplifying LLM application development

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the [Streamlit Documentation](https://docs.streamlit.io/)
- Review the [LangChain Documentation](https://python.langchain.com/)

---

⭐ If you found this project helpful, please consider giving it a star on GitHub!
