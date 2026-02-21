This project is meant to play with multiple agents running against of local and on-line models.
Using 
* llama3.1:8b for synthesis
* qwen2.5-coder:7b for coding
* deepseek-r1:8b for planning and debating

How to use uv
* install: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
* create the .venv folder: uv venv
* activate: .venv\Scripts\activate
* to install all packages in pyproject.toml: uv sync

Training
* [LangGraph Complete Course](https://www.youtube.com/watch?v=jGg_1h0qzaM)
* [LangChain Crash Course](https://www.youtube.com/watch?v=J7j5tCB_y4w)
