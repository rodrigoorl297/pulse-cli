# Pulse CLI

[![CI](https://img.shields.io/badge/CI-GitHub_Actions-black)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](pyproject.toml)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

CLI empacotada (`pyproject` + entry point) para o dia a dia de engenharia: hash de arquivos, inspecao de JSON e ping HTTP.

Pensada para o contexto **edtech**, onde times precisam de utilitarios reproduziveis em vez de scripts soltos.

## What recruiters should notice

- Pacote instalavel com `pip install -e .` e comando `pulse-cli`.
- Subcomandos, testes e CI — padrao de ferramenta interna de plataforma.
- Zero dependencias de runtime.

## Install

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -e ".[dev]"
pulse-cli --help
pulse-cli json examples/sample.json
```

## Tests

```bash
pytest -q
```
