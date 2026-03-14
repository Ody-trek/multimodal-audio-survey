"""
多模态音频理解领域搜索配置
"""

SEARCH_QUERIES = [
    ("audio large language model understanding",        "cs.SD", 12),
    ("speech language model instruction following",     "cs.CL", 10),
    ("audio visual language model multimodal",          "cs.CV", 10),
    ("audio foundation model self-supervised learning", "cs.SD", 10),
    ("speech self-supervised representation learning",  "cs.CL", 10),
    ("contrastive language audio pretraining",          "cs.SD",  8),
    ("audio text alignment zero-shot classification",   "cs.SD",  8),
    ("audio event detection classification transformer","cs.SD",  8),
    ("environmental sound recognition deep learning",   "cs.SD",  8),
    ("audio visual speech recognition fusion",          "cs.CV",  8),
    ("audio visual learning self-supervised",           "cs.CV",  8),
    ("text to audio generation diffusion",              "cs.SD",  8),
    ("audio language model generation neural codec",    "cs.SD",  8),
]

SEED_PAPER_IDS = [
    "2212.04356",  # Whisper
    "2006.11477",  # wav2vec 2.0
    "2106.07447",  # HuBERT
    "2110.13900",  # WavLM
    "2212.09058",  # BEATs
    "2207.06405",  # AudioMAE
    "2211.06687",  # CLAP
    "2106.13043",  # AudioCLIP
    "2305.11834",  # Pengi
    "2311.07919",  # Qwen-Audio
    "2310.13289",  # SALMONN
    "2306.12925",  # AudioPaLM
    "2305.10790",  # LTU (Listen Think Understand)
    "2402.08846",  # WavLLM
    "2312.11514",  # Gemini
    "2104.01778",  # AST
    "2107.13222",  # HTSAT
    "2306.05284",  # EAT
    "2201.02184",  # AV-HuBERT
    "2309.05519",  # NExT-GPT
    "2209.03143",  # AudioLM
    "2301.11325",  # MusicLM
    "2209.15352",  # AudioGen
    "2301.12503",  # Make-An-Audio
    "2210.13438",  # EnCodec
    "2305.04634",  # AudioLDM 2
    "2209.15329",  # SpeechLM
    "2110.07435",  # SpeechBrain
]

SURVEY_THEMES = {
    "音频自监督基础模型":  "Self-Supervised Audio Foundation Models",
    "音频-语言对齐与理解": "Audio-Language Alignment and Understanding",
    "音频大语言模型":      "Audio Large Language Models",
    "音视频多模态融合":    "Audio-Visual Multimodal Fusion",
    "环境声音与事件检测":  "Environmental Sound and Event Detection",
    "音频生成与合成":      "Audio Generation and Synthesis",
    "语音识别与处理":      "Speech Recognition and Processing",
}

SURVEY_TITLE    = "多模态音频理解研究综述：从基础模型到音频大语言模型"
SURVEY_SUBTITLE = "Multimodal Audio Understanding: From Foundation Models to Audio LLMs"
