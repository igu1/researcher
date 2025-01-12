# Researcher

An AI-powered research assistant tool that helps with gathering, analyzing, and synthesizing information from various sources. Built with modern Python async capabilities and integrated with powerful language models.

## Features

- Asynchronous research operations for efficient data gathering
- Integration with multiple data sources
- Smart content summarization
- Relevance scoring for search results
- Structured output format for easy integration

## Requirements

- Python 3.8 or higher
- OpenAI API key
- Internet connection for web research

## Installation

1. Clone the repository:
```bash
git clone https://github.com/igu1/research-agents.git
cd researcher
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```
- Unix/MacOS:
```bash
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -e .
```

5. Create a `.env` file in the project root and add your API keys:
```env
OPENAI_API_KEY=your_api_key_here
```

## Project Structure

```
researcher/
├── researcher/         # Main package directory
│   ├── __init__.py
│   ├── core/          # Core functionality
│   │   ├── __init__.py
│   │   └── researcher.py
│   ├── tools/         # Research tools
│   │   └── __init__.py
│   └── utils/         # Utility functions
│       └── __init__.py
├── tests/             # Test directory
│   ├── __init__.py
│   └── test_researcher.py
├── README.md
└── pyproject.toml
```

## Usage

```python
from researcher.core.researcher import Researcher

async def main():
    researcher = Researcher()
    results = await researcher.research("What are the latest developments in quantum computing?")
    summary = await researcher.summarize(results)
    print(summary)
```

## Development

- Run tests: `pytest`
- Format code: `black .`
- Sort imports: `isort .`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- **Eeza** - [GitHub](https://github.com/igu1)
