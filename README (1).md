# 🍽️ Restaurant Name & Menu Generator using Gemini LLM

This project uses **LangChain** with **Google Gemini** to generate creative restaurant names and menu items based on a cuisine type.

---

## 📁 Project Structure

```
project-root/
├── .env                           # Stores your Google API key
├── app.py                         # Main script to run the generator
├── key.py                         # Loads API key from environment
├── requirements.txt               # Python dependencies
├── restaurant_suggestion/
│   └── restaurant.py              # Core logic using LangChain + Gemini
```

---

## ▶️ How It Works

1. User provides a cuisine (e.g., `"Mexican"`)
2. The system generates:
   - A fancy restaurant name
   - 10 creative menu items for that restaurant

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Set up your environment

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the root with this content:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Create a `key.py` file:

```python
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
```

### 3. Run the app

You can test the generator with:

```bash
python app.py
```

---

## 📦 Requirements

```
langchain
langchain-community
langchain-google-genai
python-dotenv
```

Install via:

```bash
pip install -r requirements.txt
```

---

## 🧠 Tech Used

- [LangChain](https://www.langchain.com/)
- [Google Gemini (via langchain-google-genai)](https://ai.google.dev/)
- Python 3.10+

---

## ✨ Example Output

```json
{
  "cuisine": "Indian",
  "restaurant_name": "Spice Symphony",
  "menu_items": "1. Curry Carnival\n2. Tandoori Twilight\n..."
}
```

---

## 📄 License

MIT License (or your preferred license)

---

## 🙋‍♂️ Author

Built by [Your Name]
