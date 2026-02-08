# 🍽️ AI Restaurant Name & Menu Generator

[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.54.0-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-1C3C3C.svg?style=for-the-badge&logo=LangChain&logoColor=white)](https://langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> **Ignite your culinary creativity.** An intelligent web application that crafts unique restaurant concepts and curated menus instantly using the power of Generative AI.

---

## 📖 Table of Contents
- [✨ Features](#-features)
- [🚀 Live Demo](#-live-demo)
- [🛠️ Tech Stack](#️-tech-stack)
- [⚙️ Installation](#️-installation)
- [🔑 API Configuration](#-api-configuration)
- [🧠 How It Works](#-how-it-works)
- [📂 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)

---

## ✨ Features

| Feature | Description |
| :--- | :--- |
| 🌍 **Global Cuisines** | Choose from 7+ major culinary styles including Indian, Italian, Japanese, and Mexican. |
| 🤖 **AI-Powered Core** | Utilizes **GPT-3.5-turbo** via LangChain for context-aware, creative generation. |
| ⚡ **Instant Results** | Real-time generation with zero lag, featuring smooth loading animations. |
| 📋 **Full Menu Generation** | Doesn't just name the place—creates 10 matching, appetizing menu items. |
| 🎨 **Modern UI** | Built with Streamlit for a responsive, clean, and professional user experience. |

---

## 🚀 Live Demo

### 📹 Preview
![Restaurant Generator Demo](https://github.com/user-attachments/assets/37a359b0-30c4-4f15-92fc-aaac9c49cff8)

### 🎯 What You Get
1. **The Brand:** A catchy, thematic restaurant name.
2. **The Food:** A curated list of 10 dishes that fit the specific theme and cuisine selected.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/) (Web Framework)
- **Orchestration:** [LangChain](https://www.langchain.com/) (LLM Logic)
- **Model:** [OpenAI GPT-3.5](https://platform.openai.com/docs/models) (via OpenRouter)
- **Language:** Python 3.12+

---

## ⚙️ Installation

Follow these steps to set up the project locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/restaurant-name-generator.git](https://github.com/yourusername/restaurant-name-generator.git)
cd restaurant-name-generator
```
## 🚀 Demo

### 📹 Video Demo


https://github.com/user-attachments/assets/37a359b0-30c4-4f15-92fc-aaac9c49cff8



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
