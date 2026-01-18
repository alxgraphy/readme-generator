"""
AI Enhancer - Uses Claude API to improve README descriptions
"""
import os
from typing import Dict


class AIEnhancer:
    """Enhances README content using Claude API"""
    
    def __init__(self):
        self.api_key = os.environ.get('ANTHROPIC_API_KEY')
        
        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable not set. "
                "Get your API key from https://console.anthropic.com/"
            )
    
    def enhance(self, readme_content: str, scan_results: Dict, tech_info: Dict) -> str:
        """Enhance README with AI-generated descriptions"""
        try:
            import anthropic
        except ImportError:
            raise ImportError(
                "anthropic package not installed. Install with: pip install anthropic"
            )
        
        client = anthropic.Anthropic(api_key=self.api_key)
        
        # Prepare context for Claude
        context = self._prepare_context(scan_results, tech_info)
        
        # Create prompt
        prompt = f"""You are a technical writer helping to improve a README file.

Here's the auto-generated README:

{readme_content}

Project context:
{context}

Please improve this README by:
1. Writing a compelling, professional project description (2-3 sentences)
2. Suggesting 3-5 realistic features based on the detected technologies
3. Making the overall tone more engaging and clear

Keep the same structure and sections, just improve the content. Do not add new sections.
Return ONLY the improved README content, no explanations."""

        # Call Claude API
        try:
            message = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Extract enhanced content
            enhanced_content = message.content[0].text
            
            return enhanced_content
        
        except Exception as e:
            print(f"Warning: AI enhancement failed: {e}")
            print("Returning original README content")
            return readme_content
    
    def _prepare_context(self, scan_results: Dict, tech_info: Dict) -> str:
        """Prepare context information for Claude"""
        context_parts = []
        
        context_parts.append(f"- Primary Language: {tech_info['primary_language']}")
        
        if tech_info['languages']:
            context_parts.append(f"- Languages: {', '.join(tech_info['languages'])}")
        
        if tech_info['frameworks']:
            context_parts.append(f"- Frameworks: {', '.join(tech_info['frameworks'])}")
        
        if tech_info['package_managers']:
            context_parts.append(f"- Package Managers: {', '.join(tech_info['package_managers'])}")
        
        context_parts.append(f"- File Count: {scan_results['file_count']}")
        context_parts.append(f"- Has Tests: {tech_info['has_tests']}")
        context_parts.append(f"- Has CI/CD: {tech_info['has_ci']}")
        
        return '\n'.join(context_parts)