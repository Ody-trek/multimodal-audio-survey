"""
配置文件
========
所有敏感信息从环境变量读取，绝不硬编码。
"""

import os
from pathlib import Path

ROOT_DIR     = Path(__file__).parent
OUTPUTS_DIR  = ROOT_DIR / "outputs"
OUTPUTS_DIR.mkdir(exist_ok=True)

# ── Anthropic ──────────────────────────────────────────────
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
CLAUDE_MODEL      = "claude-opus-4-6"

# ── GitHub ─────────────────────────────────────────────────
GITHUB_REPO_URL = os.environ.get("GITHUB_REPO_URL", "")
GITHUB_TOKEN    = os.environ.get("GITHUB_TOKEN", "")
