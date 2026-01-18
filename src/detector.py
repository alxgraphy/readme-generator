"""
Technology Detector - Identifies languages, frameworks, and tools
"""
from pathlib import Path
from typing import Dict, List, Set


class TechDetector:
    """Detects technologies used in a project"""
    
    # Language detection by file extension
    LANGUAGE_MAP = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.jsx': 'React',
        '.tsx': 'React',
        '.java': 'Java',
        '.c': 'C',
        '.cpp': 'C++',
        '.cs': 'C#',
        '.go': 'Go',
        '.rs': 'Rust',
        '.rb': 'Ruby',
        '.php': 'PHP',
        '.swift': 'Swift',
        '.kt': 'Kotlin',
        '.scala': 'Scala',
        '.r': 'R',
        '.m': 'Objective-C',
        '.sh': 'Shell',
        '.html': 'HTML',
        '.css': 'CSS',
        '.scss': 'SASS',
        '.vue': 'Vue',
        '.sql': 'SQL',
        '.md': 'Markdown'
    }
    
    # Framework/tool detection
    FRAMEWORK_INDICATORS = {
        'React': ['package.json', 'react'],
        'Next.js': ['next.config.js', 'next.config.ts'],
        'Vue.js': ['vue.config.js', 'nuxt.config.js'],
        'Angular': ['angular.json'],
        'Django': ['manage.py', 'settings.py'],
        'Flask': ['app.py', 'flask'],
        'FastAPI': ['main.py', 'fastapi'],
        'Express': ['express'],
        'Node.js': ['package.json'],
        'Docker': ['Dockerfile', 'docker-compose.yml'],
        'Kubernetes': ['.yaml', 'k8s'],
        'Terraform': ['.tf'],
        'Streamlit': ['streamlit'],
        'Pytest': ['pytest.ini', 'conftest.py'],
        'Jest': ['jest.config.js']
    }
    
    def __init__(self, scan_results: Dict):
        self.scan_results = scan_results
        self.files = scan_results['files']
        self.extensions = scan_results['extensions']
        self.special_files = scan_results['special_files']
        
    def detect(self) -> Dict:
        """Detect all technologies used in the project"""
        return {
            'languages': self._detect_languages(),
            'frameworks': self._detect_frameworks(),
            'package_managers': self._detect_package_managers(),
            'tools': self._detect_tools(),
            'primary_language': self._get_primary_language(),
            'has_tests': self._has_tests(),
            'has_docs': self._has_docs(),
            'has_ci': self._has_ci()
        }
    
    def _detect_languages(self) -> List[str]:
        """Detect programming languages"""
        languages = set()
        
        for ext in self.extensions:
            if ext in self.LANGUAGE_MAP:
                languages.add(self.LANGUAGE_MAP[ext])
        
        return sorted(list(languages))
    
    def _detect_frameworks(self) -> List[str]:
        """Detect frameworks and major libraries"""
        frameworks = set()
        
        # Check special files
        file_names = {f.name for f in self.files}
        
        for framework, indicators in self.FRAMEWORK_INDICATORS.items():
            for indicator in indicators:
                if any(indicator in str(f) for f in self.files):
                    frameworks.add(framework)
                    break
        
        # Check package.json for JS frameworks
        if 'package' in self.special_files:
            frameworks.update(self._parse_package_json())
        
        # Check requirements.txt for Python frameworks
        if 'requirements' in self.special_files:
            frameworks.update(self._parse_requirements())
        
        return sorted(list(frameworks))
    
    def _detect_package_managers(self) -> List[str]:
        """Detect package managers"""
        managers = []
        
        indicators = {
            'pip': ['requirements.txt', 'setup.py'],
            'poetry': ['pyproject.toml', 'poetry.lock'],
            'npm': ['package.json', 'package-lock.json'],
            'yarn': ['yarn.lock'],
            'pnpm': ['pnpm-lock.yaml'],
            'cargo': ['Cargo.toml'],
            'go mod': ['go.mod'],
            'maven': ['pom.xml'],
            'gradle': ['build.gradle']
        }
        
        file_names = {f.name for f in self.files}
        
        for manager, files in indicators.items():
            if any(f in file_names for f in files):
                managers.append(manager)
        
        return managers
    
    def _detect_tools(self) -> List[str]:
        """Detect development tools"""
        tools = []
        
        if 'docker' in self.special_files:
            tools.append('Docker')
        
        if 'ci' in self.special_files:
            tools.append('CI/CD')
        
        if any('.yaml' in str(f) or '.yml' in str(f) for f in self.files):
            if any('k8s' in str(f) or 'kubernetes' in str(f) for f in self.files):
                tools.append('Kubernetes')
        
        if 'makefile' in self.special_files:
            tools.append('Make')
        
        return tools
    
    def _get_primary_language(self) -> str:
        """Determine the primary programming language"""
        lang_counts = {}
        
        for file in self.files:
            ext = file.suffix
            if ext in self.LANGUAGE_MAP:
                lang = self.LANGUAGE_MAP[ext]
                lang_counts[lang] = lang_counts.get(lang, 0) + 1
        
        if not lang_counts:
            return 'Unknown'
        
        # Return language with most files
        return max(lang_counts.items(), key=lambda x: x[1])[0]
    
    def _has_tests(self) -> bool:
        """Check if project has tests"""
        test_indicators = ['test', 'tests', 'spec', '__tests__', 'pytest', 'jest']
        
        return any(
            indicator in str(f).lower() 
            for f in self.files 
            for indicator in test_indicators
        )
    
    def _has_docs(self) -> bool:
        """Check if project has documentation"""
        doc_indicators = ['docs', 'documentation', 'doc', 'README']
        
        return any(
            indicator in str(f) 
            for f in self.files 
            for indicator in doc_indicators
        )
    
    def _has_ci(self) -> bool:
        """Check if project has CI/CD"""
        return 'ci' in self.special_files
    
    def _parse_package_json(self) -> Set[str]:
        """Parse package.json for frameworks"""
        frameworks = set()
        try:
            import json
            package_file = self.special_files['package']
            data = json.loads(package_file.read_text())
            
            deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
            
            if 'react' in deps:
                frameworks.add('React')
            if 'next' in deps:
                frameworks.add('Next.js')
            if 'vue' in deps:
                frameworks.add('Vue.js')
            if 'express' in deps:
                frameworks.add('Express')
            if '@angular/core' in deps:
                frameworks.add('Angular')
        except:
            pass
        
        return frameworks
    
    def _parse_requirements(self) -> Set[str]:
        """Parse requirements.txt for frameworks"""
        frameworks = set()
        try:
            req_file = self.special_files['requirements']
            content = req_file.read_text().lower()
            
            if 'django' in content:
                frameworks.add('Django')
            if 'flask' in content:
                frameworks.add('Flask')
            if 'fastapi' in content:
                frameworks.add('FastAPI')
            if 'streamlit' in content:
                frameworks.add('Streamlit')
            if 'pytest' in content:
                frameworks.add('Pytest')
        except:
            pass
        
        return frameworks