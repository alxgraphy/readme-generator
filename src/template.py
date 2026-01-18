"""
Template Generator - Creates README content from scan data
"""
from typing import Dict


class TemplateGenerator:
    """Generates README content from project analysis"""
    
    def __init__(self, project_name: str, scan_results: Dict, tech_info: Dict):
        self.project_name = project_name
        self.scan_results = scan_results
        self.tech_info = tech_info
    
    def generate(self) -> str:
        """Generate complete README content with maximum pizazz"""
        sections = [
            self._generate_header(),
            self._generate_badges(),
            self._generate_description(),
            self._generate_demo_section(),
            self._generate_features(),
            self._generate_tech_stack(),
            self._generate_quick_start(),
            self._generate_installation(),
            self._generate_usage(),
            self._generate_project_structure(),
            self._generate_roadmap(),
            self._generate_contributing(),
            self._generate_license(),
            self._generate_acknowledgments(),
            self._generate_footer()
        ]
        
        return '\n\n'.join(filter(None, sections))
    
    def _generate_header(self) -> str:
        """Generate fancy header with ASCII art"""
        # Simple ASCII art for project name
        return f"""<div align="center">

# 🚀 {self.project_name}

<p align="center">
  <strong>✨ Auto-generated README - Customize me! ✨</strong>
</p>

</div>"""
    
    def _generate_badges(self) -> str:
        """Generate GitHub badges"""
        project_slug = self.project_name.lower().replace(' ', '-')
        
        badges = []
        
        # Language badges
        if self.tech_info['primary_language']:
            lang = self.tech_info['primary_language']
            color = self._get_language_color(lang)
            badges.append(f"![{lang}](https://img.shields.io/badge/{lang}-{color}?style=for-the-badge&logo={lang.lower()}&logoColor=white)")
        
        # License badge
        if 'license' in self.scan_results['special_files']:
            badges.append(f"![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)")
        
        # Stars and forks (placeholder)
        badges.append(f"![GitHub stars](https://img.shields.io/github/stars/yourusername/{project_slug}?style=for-the-badge)")
        badges.append(f"![GitHub forks](https://img.shields.io/github/forks/yourusername/{project_slug}?style=for-the-badge)")
        
        # Issues badge
        badges.append(f"![GitHub issues](https://img.shields.io/github/issues/yourusername/{project_slug}?style=for-the-badge)")
        
        # Build status (if CI detected)
        if self.tech_info['has_ci']:
            badges.append(f"![Build](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)")
        
        # Code coverage (if tests detected)
        if self.tech_info['has_tests']:
            badges.append(f"![Coverage](https://img.shields.io/badge/coverage-85%25-green?style=for-the-badge)")
        
        return f"""<div align="center">

{' '.join(badges[:4])}

{' '.join(badges[4:]) if len(badges) > 4 else ''}

</div>"""
    
    def _generate_description(self) -> str:
        """Generate project description with emojis"""
        primary_lang = self.tech_info['primary_language']
        frameworks = self.tech_info['frameworks']
        
        description = f"A powerful {primary_lang} project"
        
        if frameworks:
            description += f" built with **{', '.join(frameworks[:3])}**"
        
        description += ". 🎯"
        
        return f"""## 📖 About

{description}

> ⚠️ **Note:** This README was auto-generated using [README Generator](https://github.com/alxgraphy/readme-generator). 
> Please customize it with your project's actual description, screenshots, and details!

### ✨ Highlights

{self._generate_highlights()}"""
    
    def _generate_highlights(self) -> str:
        """Generate highlight bullets"""
        highlights = []
        
        if self.tech_info['has_tests']:
            highlights.append("🧪 **Test Coverage** - Comprehensive test suite included")
        
        if self.tech_info['has_ci']:
            highlights.append("🔄 **CI/CD** - Automated testing and deployment")
        
        if 'Docker' in self.tech_info['tools']:
            highlights.append("🐳 **Containerized** - Docker support for easy deployment")
        
        if self.tech_info['has_docs']:
            highlights.append("📚 **Well Documented** - Clear documentation and examples")
        
        if len(self.tech_info['languages']) > 1:
            highlights.append(f"🌐 **Multi-language** - Uses {len(self.tech_info['languages'])} programming languages")
        
        if not highlights:
            highlights = [
                "⚡ **Fast & Efficient** - Optimized for performance",
                "🎨 **Modern Stack** - Built with latest technologies",
                "🔧 **Customizable** - Easy to extend and modify"
            ]
        
        return '\n'.join(f"- {h}" for h in highlights)
    
    def _generate_demo_section(self) -> str:
        """Generate demo/screenshots section"""
        return """## 🎬 Demo

<div align="center">

### 📸 Screenshots

<table>
  <tr>
    <td><img src="screenshots/demo1.png" alt="Screenshot 1" width="400"/></td>
    <td><img src="screenshots/demo2.png" alt="Screenshot 2" width="400"/></td>
  </tr>
  <tr>
    <td align="center"><em>Main Interface</em></td>
    <td align="center"><em>Feature Showcase</em></td>
  </tr>
</table>

> 🎥 **[Live Demo](#)** | 📹 **[Video Tutorial](#)**

</div>

---"""
    
    def _generate_features(self) -> str:
        """Generate features section with emojis"""
        features = []
        
        if self.tech_info['has_tests']:
            features.append("✅ Comprehensive test coverage with automated testing")
        
        if self.tech_info['has_ci']:
            features.append("🔄 Continuous Integration and Deployment pipeline")
        
        if self.tech_info['has_docs']:
            features.append("📚 Well-documented codebase with inline comments")
        
        if 'Docker' in self.tech_info['tools']:
            features.append("🐳 Docker containerization for easy deployment")
        
        if 'Kubernetes' in self.tech_info['tools']:
            features.append("☸️ Kubernetes orchestration support")
        
        # Add generic features if none detected
        if len(features) < 3:
            features.extend([
                "🚀 High performance and scalability",
                "🔒 Secure by design with best practices",
                "🎨 Clean and maintainable code architecture",
                "⚡ Fast development with hot reload",
                "🌍 Cross-platform compatibility"
            ])
        
        features = features[:6]  # Limit to 6 features
        
        features_grid = self._create_features_grid(features)
        
        return f"""## ✨ Features

{features_grid}"""
    
    def _create_features_grid(self, features: list) -> str:
        """Create a grid layout for features"""
        grid = "<table>\n<tr>\n"
        
        for i, feature in enumerate(features):
            if i > 0 and i % 2 == 0:
                grid += "</tr>\n<tr>\n"
            
            emoji = feature.split()[0]
            text = ' '.join(feature.split()[1:])
            
            grid += f"<td width=\"50%\">\n\n**{emoji} {text.split(' - ')[0]}**\n\n"
            if ' - ' in text:
                grid += f"<br/>{text.split(' - ')[1]}\n\n"
            grid += "</td>\n"
        
        # Fill empty cells if odd number
        if len(features) % 2 != 0:
            grid += "<td></td>\n"
        
        grid += "</tr>\n</table>"
        return grid
    
    def _generate_tech_stack(self) -> str:
        """Generate technology stack section with icons"""
        lines = ["## 🛠️ Tech Stack"]
        
        if self.tech_info['languages']:
            lines.append("\n### Languages")
            lang_badges = []
            for lang in self.tech_info['languages']:
                color = self._get_language_color(lang)
                lang_badges.append(f"![{lang}](https://img.shields.io/badge/{lang}-{color}?style=flat-square&logo={lang.lower()}&logoColor=white)")
            lines.append(' '.join(lang_badges))
        
        if self.tech_info['frameworks']:
            lines.append("\n### Frameworks & Libraries")
            fw_badges = []
            for fw in self.tech_info['frameworks']:
                color = self._get_framework_color(fw)
                fw_badges.append(f"![{fw}](https://img.shields.io/badge/{fw}-{color}?style=flat-square&logo={fw.lower().replace('.', '').replace(' ', '')}&logoColor=white)")
            lines.append(' '.join(fw_badges))
        
        if self.tech_info['tools']:
            lines.append("\n### Tools & Platforms")
            tool_badges = []
            for tool in self.tech_info['tools']:
                color = "2496ED"
                tool_badges.append(f"![{tool}](https://img.shields.io/badge/{tool}-{color}?style=flat-square&logo={tool.lower()}&logoColor=white)")
            lines.append(' '.join(tool_badges))
        
        return '\n'.join(lines) if len(lines) > 1 else ""
    
    def _generate_quick_start(self) -> str:
        """Generate quick start section"""
        managers = self.tech_info['package_managers']
        primary_lang = self.tech_info['primary_language']
        
        quick_commands = []
        
        # Clone
        quick_commands.append("# Clone the repository")
        quick_commands.append("git clone https://github.com/yourusername/{}.git".format(
            self.project_name.lower().replace(' ', '-')
        ))
        quick_commands.append("")
        
        # Install
        if 'npm' in managers:
            quick_commands.append("# Install dependencies")
            quick_commands.append("npm install")
            quick_commands.append("")
            quick_commands.append("# Run the project")
            quick_commands.append("npm start")
        elif 'pip' in managers:
            quick_commands.append("# Install dependencies")
            quick_commands.append("pip install -r requirements.txt")
            quick_commands.append("")
            quick_commands.append("# Run the project")
            quick_commands.append("python main.py")
        else:
            quick_commands.append("# Follow installation instructions below")
        
        return f"""## ⚡ Quick Start

```bash
{chr(10).join(quick_commands)}
```"""
    
    def _generate_installation(self) -> str:
        """Generate detailed installation instructions"""
        managers = self.tech_info['package_managers']
        primary_lang = self.tech_info['primary_language']
        
        lines = ["## 📦 Installation"]
        
        lines.append("\n### Prerequisites")
        
        # Prerequisites based on tech
        prereqs = []
        if 'Node.js' in self.tech_info['frameworks'] or 'npm' in managers:
            prereqs.append("- Node.js 16.x or higher")
        if primary_lang == 'Python':
            prereqs.append("- Python 3.8 or higher")
        if 'Docker' in self.tech_info['tools']:
            prereqs.append("- Docker and Docker Compose")
        if 'go mod' in managers:
            prereqs.append("- Go 1.20 or higher")
        
        if not prereqs:
            prereqs = [f"- {primary_lang} (latest stable version)"]
        
        lines.append('\n'.join(prereqs))
        
        # Installation steps
        lines.append("\n### Step-by-Step Guide")
        
        lines.append("\n**1️⃣ Clone the repository**")
        lines.append("```bash")
        lines.append("git clone https://github.com/yourusername/{}.git".format(
            self.project_name.lower().replace(' ', '-')
        ))
        lines.append("cd {}".format(self.project_name.lower().replace(' ', '-')))
        lines.append("```")
        
        # Installation based on detected package managers
        if 'pip' in managers:
            lines.append("\n**2️⃣ Create virtual environment (recommended)**")
            lines.append("```bash")
            lines.append("python -m venv venv")
            lines.append("source venv/bin/activate  # On Windows: venv\\Scripts\\activate")
            lines.append("```")
            
            lines.append("\n**3️⃣ Install dependencies**")
            lines.append("```bash")
            lines.append("pip install -r requirements.txt")
            lines.append("```")
        
        elif 'poetry' in managers:
            lines.append("\n**2️⃣ Install dependencies with Poetry**")
            lines.append("```bash")
            lines.append("poetry install")
            lines.append("```")
        
        elif 'npm' in managers:
            lines.append("\n**2️⃣ Install dependencies**")
            lines.append("```bash")
            lines.append("npm install")
            lines.append("# or")
            lines.append("yarn install")
            lines.append("```")
        
        elif 'cargo' in managers:
            lines.append("\n**2️⃣ Build the project**")
            lines.append("```bash")
            lines.append("cargo build --release")
            lines.append("```")
        
        elif 'go mod' in managers:
            lines.append("\n**2️⃣ Download dependencies**")
            lines.append("```bash")
            lines.append("go mod download")
            lines.append("```")
        
        # Environment setup
        lines.append("\n**4️⃣ Set up environment variables**")
        lines.append("```bash")
        lines.append("cp .env.example .env")
        lines.append("# Edit .env with your configuration")
        lines.append("```")
        
        return '\n'.join(lines)
    
    def _generate_usage(self) -> str:
        """Generate usage instructions"""
        primary_lang = self.tech_info['primary_language']
        frameworks = self.tech_info['frameworks']
        
        lines = ["## 🚀 Usage"]
        
        lines.append("\n### Basic Usage")
        
        # Generate usage based on detected tech
        if 'Django' in frameworks:
            lines.append("```bash")
            lines.append("# Run migrations")
            lines.append("python manage.py migrate")
            lines.append("")
            lines.append("# Create superuser")
            lines.append("python manage.py createsuperuser")
            lines.append("")
            lines.append("# Run development server")
            lines.append("python manage.py runserver")
            lines.append("```")
            lines.append("\nVisit `http://localhost:8000` in your browser")
        
        elif 'Flask' in frameworks or 'FastAPI' in frameworks:
            lines.append("```bash")
            lines.append("# Run the application")
            lines.append("python app.py")
            lines.append("# or")
            lines.append("uvicorn main:app --reload  # For FastAPI")
            lines.append("```")
            lines.append("\nAPI will be available at `http://localhost:8000`")
        
        elif 'Streamlit' in frameworks:
            lines.append("```bash")
            lines.append("streamlit run app.py")
            lines.append("```")
            lines.append("\nApp will open in your browser automatically")
        
        elif 'React' in frameworks or 'Next.js' in frameworks:
            lines.append("```bash")
            lines.append("# Development mode")
            lines.append("npm run dev")
            lines.append("")
            lines.append("# Build for production")
            lines.append("npm run build")
            lines.append("")
            lines.append("# Start production server")
            lines.append("npm start")
            lines.append("```")
            lines.append("\nOpen `http://localhost:3000`")
        
        else:
            lines.append("```bash")
            lines.append("# Run the application")
            if primary_lang == 'Python':
                lines.append("python main.py")
            elif primary_lang == 'Go':
                lines.append("go run main.go")
            elif primary_lang == 'Rust':
                lines.append("cargo run")
            elif primary_lang == 'Node.js' or primary_lang == 'JavaScript':
                lines.append("npm start")
            else:
                lines.append("# See documentation for usage instructions")
            lines.append("```")
        
        # Add examples section
        lines.append("\n### Examples")
        lines.append("\n```bash")
        lines.append("# Example 1: Basic usage")
        lines.append("# Add your example here")
        lines.append("")
        lines.append("# Example 2: Advanced usage")
        lines.append("# Add your example here")
        lines.append("```")
        
        return '\n'.join(lines)
    
    def _generate_project_structure(self) -> str:
        """Generate project structure section"""
        tree = self.scan_results['file_tree']
        
        return f"""## 📁 Project Structure

```
{tree}
```

### Key Directories

{self._explain_structure()}"""
    
    def _explain_structure(self) -> str:
        """Explain project structure"""
        explanations = []
        
        # Common patterns
        if any('src' in str(d) for d in self.scan_results['directories']):
            explanations.append("- **`src/`** - Source code and main application logic")
        
        if any('test' in str(d).lower() for d in self.scan_results['directories']):
            explanations.append("- **`tests/`** - Test files and test utilities")
        
        if any('doc' in str(d).lower() for d in self.scan_results['directories']):
            explanations.append("- **`docs/`** - Documentation files")
        
        if any('config' in str(d).lower() for d in self.scan_results['directories']):
            explanations.append("- **`config/`** - Configuration files")
        
        if not explanations:
            explanations = ["- See code structure above for file organization"]
        
        return '\n'.join(explanations)
    
    def _generate_roadmap(self) -> str:
        """Generate roadmap section"""
        return """## 🗺️ Roadmap

- [x] Initial release
- [ ] Add feature X
- [ ] Improve performance
- [ ] Add more documentation
- [ ] Add integration tests
- [ ] Release v2.0

See the [open issues](https://github.com/yourusername/project/issues) for a full list of proposed features."""
    
    def _generate_contributing(self) -> str:
        """Generate contributing section"""
        return """## 🤝 Contributing

Contributions make the open source community amazing! Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork** the Project
2. **Create** your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the Branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines

- Write clear, commented code
- Follow the existing code style
- Add tests for new features
- Update documentation as needed

### Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing."""
    
    def _generate_license(self) -> str:
        """Generate license section"""
        if 'license' in self.scan_results['special_files']:
            return """## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information."""
        else:
            return """## 📄 License

This project is unlicensed. Please add a LICENSE file to specify terms of use.

Recommended licenses:
- [MIT License](https://opensource.org/licenses/MIT) - Permissive
- [GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html) - Copyleft
- [Apache 2.0](https://opensource.org/licenses/Apache-2.0) - Permissive with patent grant"""
    
    def _generate_acknowledgments(self) -> str:
        """Generate acknowledgments section"""
        return """## 🙏 Acknowledgments

- Thanks to all contributors
- Inspired by awesome open source projects
- Built with amazing tools and frameworks"""
    
    def _generate_footer(self) -> str:
        """Generate footer"""
        return """---

<div align="center">

**⭐ Star this repo if you find it helpful! ⭐**

Made with ❤️ by [Your Name](https://github.com/yourusername)

**[⬆ Back to Top](#-project-name)**

*Auto-generated using [README Generator](https://github.com/alxgraphy/readme-generator)*

</div>"""
    
    def _get_language_color(self, language: str) -> str:
        """Get color code for language badge"""
        colors = {
            'Python': '3776AB',
            'JavaScript': 'F7DF1E',
            'TypeScript': '3178C6',
            'Java': 'ED8B00',
            'Go': '00ADD8',
            'Rust': 'CE412B',
            'C++': '00599C',
            'C#': '239120',
            'Ruby': 'CC342D',
            'PHP': '777BB4',
            'Swift': 'FA7343',
            'Kotlin': '7F52FF',
            'HTML': 'E34F26',
            'CSS': '1572B6'
        }
        return colors.get(language, '555555')
    
    def _get_framework_color(self, framework: str) -> str:
        """Get color code for framework badge"""
        colors = {
            'React': '61DAFB',
            'Next.js': '000000',
            'Vue.js': '4FC08D',
            'Django': '092E20',
            'Flask': '000000',
            'FastAPI': '009688',
            'Express': '000000',
            'Streamlit': 'FF4B4B',
            'Docker': '2496ED'
        }
        return colors.get(framework, '6366F1')