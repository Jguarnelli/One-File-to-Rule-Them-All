# 💍 One File to Rule Them All 🔥

A Python script to **scan a project** and **aggregate all `.py` files** into a **structured JSON file**.  
This helps with **AI-assisted development**, **refactoring**, and **automated code analysis**.

---

## 📌 Features
- ✅ **Recursive scan** of your project for Python files  
- ✅ **Exclusion of unnecessary folders** (`.git`, `venv`, `node_modules`, etc.)  
- ✅ **Structured JSON output** containing all Python code  

---

## 🏁 Getting Started

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/jguarnelli/One-File-to-Rule-Them-All.git
   cd One-File-to-Rule-Them-All
   ```
2. **Run the script**:
   ```bash
   python3 aggregate_code.py --output output.json --verbose
   ```
   This command will generate a `output.json` file containing all `.py` file content.

### Example Output
```json
{
  "src/main.py": "def main():\n    print('Hello World')\n",
  "utils/helper.py": "class Helper:\n    pass\n"
}
```
> Each key represents a file path, and the value is the **entire file content**.

---

## 🔧 Use Cases

1. **AI-Assisted Development**  
   Provide a single JSON file to AI tools like GitHub Copilot or ChatGPT.  
   This allows them to understand your entire codebase at once, improving suggestions and refactoring insights.

2. **Refactoring & Clean Code**  
   Identify duplicate functions, spot unused code, or unify naming conventions across all `.py` files in one go.

3. **Automated Code Analysis**  
   Integrate the JSON into tools that look for security flaws, coding standard violations, or performance bottlenecks.

4. **Documentation & Testing**  
   Generate docstrings or test suites automatically by parsing the aggregated JSON for function/class definitions.

---

## 👥 Authors
- **[Jeremy](https://github.com/JeremyVigny)** – Creator & Maintainer  
- **[Josselin](https://github.com/jguarnelli)** – Co-Maintainer & Contributor  

---

## 🤝 Contributing

Contributions are welcome! Feel free to open **issues** for bugs or **pull requests** with new features.  
For details, check out our [CONTRIBUTING.md](CONTRIBUTING.md) (coming soon).

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🌐 Community & Support

- **Issues**: Use [GitHub Issues](../../issues) to report bugs or request features.  
- **Contact**: Reach out via the GitHub profiles mentioned above.

---

**⭐ Star the repo if you find it helpful! Happy coding.**
