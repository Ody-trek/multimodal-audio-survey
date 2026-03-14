# 多模态音频理解研究综述自动生成系统

> 自动收集 arXiv 论文 → Claude Batches API 批量分析 → 生成 Markdown 综述 → 推送 GitHub

## 快速开始

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."
export GITHUB_REPO_URL="https://github.com/Ody-trek/audio-survey-results.git"
export GITHUB_TOKEN="ghp_..."
python main.py
```

## 覆盖方向

| 主题 | 代表工作 |
|------|---------|
| 音频自监督基础模型 | wav2vec 2.0, HuBERT, WavLM, BEATs |
| 音频-语言对齐与理解 | CLAP, AudioCLIP, Pengi |
| 音频大语言模型 | Qwen-Audio, SALMONN, AudioPaLM, LTU |
| 音视频多模态融合 | AV-HuBERT, NExT-GPT |
| 环境声音与事件检测 | AST, HTSAT, EAT |
| 音频生成与合成 | AudioLM, MusicLM, AudioLDM 2 |
| 语音识别与处理 | Whisper, SpeechLM |
