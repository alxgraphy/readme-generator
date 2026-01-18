<div align="center">

# 🚀 README Generator

<p align="center">
  <strong>Automatically generate professional README.md files for your projects in seconds</strong>
</p>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/CLI-Tool-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/alxgraphy/readme-maker?style=for-the-badge)

</div>

---

## 📖 About

Stop wasting time writing boilerplate documentation. README Generator scans your project, detects technologies, and creates a comprehensive, well-formatted README with badges, structure trees, and installation instructions automatically.

**Perfect for:**
- 📦 Quick project setup
- 🎯 Portfolio projects that need professional docs
- ⚡ Open source repositories
- 🚀 Rapid prototyping

---

## ✨ Features

<table>
<tr>
<td width="50%">

**🔍 Smart Detection**

Automatically identifies languages, frameworks, and tools in your project

</td>
<td width="50%">

**📊 Project Analysis**

Scans file structure and generates visual directory tree

</td>
</tr>
<tr>
<td width="50%">

**🤖 AI Enhancement**

Optional Claude API integration for polished descriptions

</td>
<td width="50%">

**⚡ Lightning Fast**

Generates professional READMEs in seconds

</td>
</tr>
<tr>
<td width="50%">

**🎨 Maximum Pizazz**

Beautiful badges, emojis, and formatted sections

</td>
<td width="50%">

**💻 CLI Interface**

Simple command-line tool, no GUI needed

</td>
</tr>
</table>

---

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/alxgraphy/readme-generator.git
cd readme-generator

# Install dependencies
pip install -r requirements.txt

# Generate a README for any project
python3 cli.py generate --path /path/to/your/project
```

**That's it!** Your README.md will be generated instantly.

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step-by-Step Guide

**1️⃣ Clone the repository**
```bash
git clone https://github.com/alxgraphy/readme-generator.git
cd readme-generator
```

**2️⃣ Create virtual environment (recommended)**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

**4️⃣ Verify installation**
```bash
python3 cli.py --help
```

---

## 🚀 Usage

### Basic Usage

**Generate README for current directory:**
```bash
python3 cli.py generate
```

**Specify a project path:**
```bash
python3 cli.py generate --path ./my-project
```

**Custom output file:**
```bash
python3 cli.py generate --output DOCUMENTATION.md
```

**Set custom title:**
```bash
python3 cli.py generate --title "My Awesome Project"
```

**Overwrite existing README without prompt:**
```bash
python3 cli.py generate --overwrite
```

**Verbose output:**
```bash
python3 cli.py generate --verbose
```

### AI Enhancement (Optional)

For even better descriptions, use Claude AI:

**1. Get API key from:** https://console.anthropic.com/

**2. Set environment variable:**
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

**3. Generate with AI enhancement:**
```bash
python3 cli.py generate --ai-enhance
```

### Examples

**Python project:**
```bash
python3 cli.py generate --path ~/projects/flask-app --ai-enhance
```

**JavaScript project:**
```bash
python3 cli.py generate --path ~/projects/react-app --title "React Dashboard"
```

**Generate for multiple projects:**
```bash
for dir in ~/projects/*/; do
  python3 cli.py generate --path "$dir"
done
```

---

## 🛠️ Supported Technologies

### Languages
Python • JavaScript • TypeScript • Java • Go • Rust • C++ • C# • Ruby • PHP • Swift • Kotlin • HTML • CSS

### Frameworks
React • Next.js • Vue.js • Angular • Django • Flask • FastAPI • Express • Streamlit • Node.js

### Tools
Docker • Kubernetes • CI/CD • Make • npm • pip • poetry • cargo • go mod • maven • gradle

**Don't see your tech?** The tool is extensible - add detection in `src/detector.py`

---

## 📁 Project Structure

```
readme-generator/
├── src/
│   ├── scanner.py       # Project file scanner
│   ├── detector.py      # Technology detection
│   ├── template.py      # README template generation
│   └── enhancer.py      # AI enhancement (optional)
├── cli.py               # Main CLI entry point
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

### Key Components

- **`scanner.py`** - Recursively scans project files and directories
- **`detector.py`** - Identifies languages, frameworks, and tools
- **`template.py`** - Generates formatted README content with badges
- **`enhancer.py`** - Uses Claude API for improved descriptions
- **`cli.py`** - Command-line interface using Click framework

---

## 🎬 Output Examples

The generated README includes:

✅ Project title and badges  
✅ Description and highlights  
✅ Demo/screenshots section (with placeholders)  
✅ Feature grid with emojis  
✅ Tech stack with colored badges  
✅ Installation instructions  
✅ Usage examples  
✅ Project structure tree  
✅ Contributing guidelines  
✅ License information  

---

## 🗺️ Roadmap

- [x] Core README generation
- [x] Language/framework detection
- [x] AI enhancement with Claude
- [x] Fancy badges and formatting
- [ ] Web UI version
- [ ] GitHub integration (auto-update on push)
- [ ] Custom templates
- [ ] Batch processing
- [ ] Plugin system for custom detectors

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add tests for new features
- Update documentation
- Keep commits atomic and descriptive

---

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.

---

## 🙏 Acknowledgments

- Built with [Click](https://click.palletsprojects.com/) for CLI
- AI enhancement powered by [Claude API](https://www.anthropic.com/)
- Badges from [Shields.io](https://shields.io/)
- Inspired by the need for better documentation

---

<div align="center">

**⭐ Star this repo if you find it useful! ⭐**

**Made with ❤️ in Toronto, Canada 🇨🇦**

**By [Alexander Wondwossen](https://github.com/alxgraphy)**

[⬆ Back to Top](#-readme-generator)

</div>
