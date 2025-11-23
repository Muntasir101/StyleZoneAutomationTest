"""
Bug Report Generator for Test Failures
Automatically generates detailed bug reports when tests fail
"""
import os
import json
from datetime import datetime
from pathlib import Path


class BugReportGenerator:
    """Generate bug reports for failed tests"""
    
    def __init__(self, report_dir="bug_reports"):
        self.report_dir = Path(report_dir)
        self.report_dir.mkdir(exist_ok=True)
    
    def generate_report(self, test_name, failure_message, screenshot_path=None, 
                       test_steps=None, expected_result=None, actual_result=None,
                       environment_info=None, additional_info=None):
        """
        Generate a bug report for a failed test
        
        Args:
            test_name: Name of the failed test
            failure_message: Error message from the test
            screenshot_path: Path to screenshot (if available)
            test_steps: List of test steps
            expected_result: Expected result
            actual_result: Actual result
            environment_info: Environment details
            additional_info: Any additional information
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_id = f"BUG_{timestamp}"
        
        # Create report data
        report_data = {
            "report_id": report_id,
            "timestamp": datetime.now().isoformat(),
            "test_name": test_name,
            "status": "FAILED",
            "failure_message": str(failure_message),
            "screenshot": screenshot_path if screenshot_path and os.path.exists(screenshot_path) else None,
            "test_steps": test_steps or [],
            "expected_result": expected_result or "N/A",
            "actual_result": actual_result or "N/A",
            "environment": environment_info or self._get_default_environment(),
            "additional_info": additional_info or {}
        }
        
        # Generate reports in multiple formats
        self._generate_json_report(report_id, report_data)
        self._generate_markdown_report(report_id, report_data)
        self._generate_html_report(report_id, report_data)
        
        return report_id, report_data
    
    def _get_default_environment(self):
        """Get default environment information"""
        import platform
        import sys
        
        return {
            "platform": platform.platform(),
            "python_version": sys.version,
            "browser": "Chrome",
            "base_url": os.getenv("BASE_URL", "https://muntasir101.github.io/stylezone")
        }
    
    def _generate_json_report(self, report_id, report_data):
        """Generate JSON format bug report"""
        json_path = self.report_dir / f"{report_id}.json"
        # Convert Path objects to strings for JSON serialization
        serializable_data = self._make_json_serializable(report_data)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(serializable_data, f, indent=2, ensure_ascii=False)
    
    def _make_json_serializable(self, obj):
        """Convert objects to JSON-serializable format"""
        if isinstance(obj, dict):
            return {key: self._make_json_serializable(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self._make_json_serializable(item) for item in obj]
        elif hasattr(obj, '__str__') and not isinstance(obj, (str, int, float, bool, type(None))):
            return str(obj)
        return obj
    
    def _generate_markdown_report(self, report_id, report_data):
        """Generate Markdown format bug report"""
        md_path = self.report_dir / f"{report_id}.md"
        
        md_content = f"""# Bug Report: {report_data['test_name']}

**Report ID:** {report_id}  
**Date:** {report_data['timestamp']}  
**Status:** {report_data['status']}

---

## Test Information

**Test Name:** `{report_data['test_name']}`

**Failure Message:**
```
{report_data['failure_message']}
```

---

## Test Steps

"""
        if report_data['test_steps']:
            for i, step in enumerate(report_data['test_steps'], 1):
                md_content += f"{i}. {step}\n"
        else:
            md_content += "No steps provided.\n"
        
        md_content += f"""
---

## Expected vs Actual Results

**Expected Result:**
{report_data['expected_result']}

**Actual Result:**
{report_data['actual_result']}

---

## Screenshot

"""
        if report_data['screenshot']:
            screenshot_name = os.path.basename(report_data['screenshot'])
            md_content += f"![Screenshot]({report_data['screenshot']})\n\n"
            md_content += f"**Screenshot Path:** `{report_data['screenshot']}`\n\n"
        else:
            md_content += "No screenshot available.\n\n"
        
        md_content += f"""---

## Environment Information

"""
        for key, value in report_data['environment'].items():
            md_content += f"- **{key.replace('_', ' ').title()}:** {value}\n"
        
        if report_data['additional_info']:
            md_content += "\n---\n\n## Additional Information\n\n"
            for key, value in report_data['additional_info'].items():
                md_content += f"- **{key}:** {value}\n"
        
        md_content += f"""
---

## Reproduction Steps

1. Navigate to the application
2. Follow the test steps mentioned above
3. Observe the failure

---

**Generated by:** StyleZone Test Automation Framework  
**Report Location:** `{md_path}`
"""
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
    
    def _generate_html_report(self, report_id, report_data):
        """Generate HTML format bug report"""
        html_path = self.report_dir / f"{report_id}.html"
        
        screenshot_html = ""
        if report_data['screenshot'] and os.path.exists(report_data['screenshot']):
            screenshot_html = f"""
            <div class="screenshot">
                <h3>Screenshot</h3>
                <img src="{os.path.abspath(report_data['screenshot'])}" alt="Test Failure Screenshot" style="max-width: 100%; border: 1px solid #ddd; border-radius: 4px;">
                <p><strong>Screenshot Path:</strong> <code>{report_data['screenshot']}</code></p>
            </div>
            """
        
        steps_html = ""
        if report_data['test_steps']:
            steps_html = "<ol>"
            for step in report_data['test_steps']:
                steps_html += f"<li>{step}</li>"
            steps_html += "</ol>"
        else:
            steps_html = "<p>No steps provided.</p>"
        
        env_html = ""
        for key, value in report_data['environment'].items():
            env_html += f"<tr><td><strong>{key.replace('_', ' ').title()}</strong></td><td>{value}</td></tr>"
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bug Report: {report_data['test_name']}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #dc2626;
            border-bottom: 3px solid #dc2626;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #1f2937;
            margin-top: 30px;
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 5px;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: bold;
        }}
        .badge-failed {{
            background-color: #fee2e2;
            color: #991b1b;
        }}
        .info-box {{
            background-color: #f9fafb;
            border-left: 4px solid #3b82f6;
            padding: 15px;
            margin: 15px 0;
        }}
        .error-box {{
            background-color: #fef2f2;
            border-left: 4px solid #dc2626;
            padding: 15px;
            margin: 15px 0;
            font-family: 'Courier New', monospace;
            white-space: pre-wrap;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        table td {{
            padding: 10px;
            border-bottom: 1px solid #e5e7eb;
        }}
        table td:first-child {{
            width: 200px;
            font-weight: 600;
        }}
        code {{
            background-color: #f3f4f6;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        .screenshot img {{
            max-width: 100%;
            border: 1px solid #ddd;
            border-radius: 4px;
            margin: 10px 0;
        }}
        ol, ul {{
            margin: 10px 0;
            padding-left: 30px;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e5e7eb;
            color: #6b7280;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🐛 Bug Report: {report_data['test_name']}</h1>
        
        <div class="info-box">
            <p><strong>Report ID:</strong> {report_id}</p>
            <p><strong>Date:</strong> {report_data['timestamp']}</p>
            <p><strong>Status:</strong> <span class="badge badge-failed">FAILED</span></p>
        </div>
        
        <h2>Test Information</h2>
        <div class="info-box">
            <p><strong>Test Name:</strong> <code>{report_data['test_name']}</code></p>
        </div>
        
        <h2>Failure Message</h2>
        <div class="error-box">{report_data['failure_message']}</div>
        
        <h2>Test Steps</h2>
        {steps_html}
        
        <h2>Expected vs Actual Results</h2>
        <table>
            <tr>
                <td>Expected Result</td>
                <td>{report_data['expected_result']}</td>
            </tr>
            <tr>
                <td>Actual Result</td>
                <td>{report_data['actual_result']}</td>
            </tr>
        </table>
        
        {screenshot_html}
        
        <h2>Environment Information</h2>
        <table>
            {env_html}
        </table>
        
        <div class="footer">
            <p><strong>Generated by:</strong> StyleZone Test Automation Framework</p>
            <p><strong>Report Location:</strong> <code>{html_path}</code></p>
        </div>
    </div>
</body>
</html>
"""
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def get_latest_report(self):
        """Get the most recent bug report"""
        reports = list(self.report_dir.glob("BUG_*.json"))
        if not reports:
            return None
        
        latest = max(reports, key=os.path.getctime)
        with open(latest, 'r', encoding='utf-8') as f:
            return json.load(f)

