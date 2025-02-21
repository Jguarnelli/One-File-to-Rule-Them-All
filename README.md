# 🛠 One File to Rule Them All  

A Python script to scan a project and aggregate all `.py` files into a structured JSON file.  
This helps with AI-assisted development, refactoring, and automated code analysis.  

## 📌 Features
✅ Recursively scans a project for Python files  
✅ Excludes unnecessary folders (`.git`, `venv`, `node_modules`, etc.)  
✅ Outputs a JSON file containing all Python code  

## 🚀 Installation
```bash
git clone https://github.com/jguarnelli/One-File-to-Rule-Them-All.git
cd One-File-to-Rule-Them-All
python3 aggregate_code.py --output output.json --verbose
