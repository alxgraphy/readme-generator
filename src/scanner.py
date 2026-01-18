"""
Project Scanner - Analyzes project structure and files
"""
from pathlib import Path
from typing import Dict, List, Set
import os


class ProjectScanner:
    """Scans a project directory and extracts metadata"""
    
    # Files/folders to ignore
    IGNORE_DIRS = {
        '__pycache__', '.git', '.github', 'node_modules', 'venv', 'env',
        '.venv', 'dist', 'build', '.next', '.nuxt', 'target', 'bin', 'obj',
        '.idea', '.vscode', '.DS_Store', 'coverage', '.pytest_cache',
        '__MACOSX', '.mypy_cache', '.tox'
    }
    
    IGNORE_FILES = {
        '.DS_Store', 'Thumbs.db', '.gitignore', '.gitattributes',
        'package-lock.json', 'yarn.lock', 'poetry.lock', 'Pipfile.lock'
    }
    
    def __init__(self, project_path: Path):
        self.project_path = Path(project_path)
        self.files: List[Path] = []
        self.directories: List[Path] = []
        self.file_extensions: Set[str] = set()
        
    def scan(self) -> Dict:
        """Scan the project and return metadata"""
        self._scan_recursive(self.project_path)
        
        return {
            'project_path': self.project_path,
            'project_name': self.project_path.name,
            'files': self.files,
            'directories': self.directories,
            'file_count': len(self.files),
            'dir_count': len(self.directories),
            'extensions': sorted(self.file_extensions),
            'file_tree': self._generate_tree(),
            'special_files': self._find_special_files()
        }
    
    def _scan_recursive(self, path: Path, depth: int = 0, max_depth: int = 10):
        """Recursively scan directories"""
        if depth > max_depth:
            return
        
        try:
            for item in path.iterdir():
                # Skip ignored items
                if item.name in self.IGNORE_DIRS or item.name in self.IGNORE_FILES:
                    continue
                
                if item.name.startswith('.') and item.name not in {'.env.example', '.editorconfig'}:
                    continue
                
                if item.is_file():
                    self.files.append(item)
                    if item.suffix:
                        self.file_extensions.add(item.suffix)
                
                elif item.is_dir():
                    self.directories.append(item)
                    self._scan_recursive(item, depth + 1, max_depth)
        
        except PermissionError:
            pass  # Skip directories we can't access
    
    def _generate_tree(self, max_files: int = 50) -> str:
        """Generate a tree structure of the project"""
        tree_lines = []
        
        # Sort files by path depth and name
        sorted_files = sorted(self.files, key=lambda p: (len(p.parts), str(p)))[:max_files]
        
        # Group by directory
        dir_structure = {}
        for file in sorted_files:
            rel_path = file.relative_to(self.project_path)
            dir_path = rel_path.parent
            if dir_path not in dir_structure:
                dir_structure[dir_path] = []
            dir_structure[dir_path].append(rel_path.name)
        
        # Build tree
        tree_lines.append(f"{self.project_path.name}/")
        
        for dir_path in sorted(dir_structure.keys()):
            if str(dir_path) != '.':
                indent = '  ' * len(dir_path.parts)
                tree_lines.append(f"{indent}├── {dir_path.name}/")
            
            indent = '  ' * (len(dir_path.parts) + (1 if str(dir_path) != '.' else 0))
            for filename in sorted(dir_structure[dir_path]):
                tree_lines.append(f"{indent}├── {filename}")
        
        if len(self.files) > max_files:
            tree_lines.append(f"  ... and {len(self.files) - max_files} more files")
        
        return '\n'.join(tree_lines)
    
    def _find_special_files(self) -> Dict[str, Path]:
        """Find important project files"""
        special_files = {}
        
        # Common important files
        important = {
            'readme': ['README.md', 'README.rst', 'README.txt', 'README'],
            'license': ['LICENSE', 'LICENSE.md', 'LICENSE.txt', 'COPYING'],
            'requirements': ['requirements.txt', 'Pipfile', 'pyproject.toml', 'setup.py'],
            'package': ['package.json', 'Cargo.toml', 'go.mod', 'pom.xml', 'build.gradle'],
            'config': ['.env.example', 'config.yml', 'config.json', 'settings.py'],
            'docker': ['Dockerfile', 'docker-compose.yml', '.dockerignore'],
            'ci': ['.github/workflows', '.gitlab-ci.yml', '.travis.yml', 'Jenkinsfile'],
            'makefile': ['Makefile', 'makefile'],
            'changelog': ['CHANGELOG.md', 'CHANGELOG.rst', 'HISTORY.md']
        }
        
        for category, filenames in important.items():
            for filename in filenames:
                file_path = self.project_path / filename
                if file_path.exists():
                    special_files[category] = file_path
                    break
        
        return special_files