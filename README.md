<div align="center">

# 🎓 Pozitron Academy — Language Learning & Spaced Repetition Platform

<p align="center">
  <b>Open, Community-Driven Language Acquisition Ecosystem with SuperMemo-2 (SM-2) Spaced Repetition & Interactive Book Reader</b>
</p>

[![Live Demo](https://img.shields.io/badge/Live_Portfolio-naimjon.vercel.app-8A2BE2?style=for-the-badge&logo=vercel&logoColor=white)](https://naimjon.vercel.app/#projects)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![aiogram 3.x](https://img.shields.io/badge/aiogram-3.x-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://aiogram.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Project Overview

**Pozitron Academy** is built to solve the primary reason language learners fail: *rapid vocabulary attrition due to lack of structured review loops*.

By pairing the scientifically verified **SuperMemo-2 (SM-2)** algorithm with an **Interactive Book Reader** and **Telegram Bot Companion**, learners retain 95%+ of studied vocabulary with minimal daily time investment.

---

## 🌟 Core Pillars

```text
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│   SuperMemo-2 Engine    │     │  Interactive Reader     │     │   Telegram Study Bot    │
│  - Adaptive Intervals   │ ──► │  - 1-Click Translation  │ ──► │  - Daily Review Alerts  │
│  - Memory Decay Curves  │     │  - Instant Card Create  │     │  - Flashcard Quizzes    │
│  - Quality Rating (0-5) │     │  - CEFR Level Filter    │     │  - Streaks & XP Ranks   │
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
```

---

## 🛠️ Tech Stack & Key Components

- **Backend Core**: Python 3.11+, FastAPI (REST API & Webhooks)
- **Telegram Ecosystem**: `aiogram 3.x` with inline query keyboards & state machines (FSM)
- **Algorithm Engine**: Pure Python implementation of SuperMemo-2 (`backend/sm2.py`)
- **Database**: PostgreSQL with SQLAlchemy 2.0 (Async) + Redis for session cache
- **Audio / Speech**: Text-to-Speech (TTS) integration for natural native pronunciation

---

## 📂 Project Structure

```
pozitron-academy/
├── backend/
│   ├── sm2.py                  # Tested SuperMemo-2 algorithm implementation
│   ├── bot.py                  # aiogram 3.x Telegram bot entrypoint
│   └── app/                    # FastAPI application
│       ├── routers/            # Decks, Cards, Reviews, Auth
│       ├── models/             # SQLAlchemy database models
│       └── schemas/            # Pydantic schemas
├── ARCHITECTURE.md             # In-depth algorithmic & database architecture
├── PROMPTS.md                  # Language tutoring & exercise generation prompts
├── ROADMAP.md                  # Development phases & milestones
└── README.md                   # Project overview
```

---

## 🚀 Quick Start Guide

### 1. Test the SM-2 Algorithm Engine

```bash
# Clone the repository
git clone https://github.com/Inomjonoff/pozitron-academy.git
cd pozitron-academy

# Run the SM-2 algorithm test simulation
python backend/sm2.py
```

### 2. Configure Environment Variables

```bash
cp .env.example .env
# Edit .env with your TELEGRAM_BOT_TOKEN and DATABASE_URL
```

---

## 📖 Documentation

- 🧠 **[ARCHITECTURE.md](ARCHITECTURE.md)** — SM-2 mathematical formulas, database ERD, and bot state machines.
- 🤖 **[PROMPTS.md](PROMPTS.md)** — Prompts for automated CEFR vocabulary extraction and conversational language tutoring.
- 🗺️ **[ROADMAP.md](ROADMAP.md)** — Step-by-step roadmap from MVP to multi-platform release.

---

## 👨‍💻 Author

**Naimjon Inomjonov**  
*Python Backend & AI Automation Developer*  
- 🌐 **Portfolio**: [naimjon.vercel.app](https://naimjon.vercel.app)
- 🐙 **GitHub**: [@Inomjonoff](https://github.com/Inomjonoff)
- 💬 **Telegram**: [@Naimjon_Inomjonov](https://t.me/Naimjon_Inomjonov)
- 📧 **Email**: [naiminomjonov@gmail.com](mailto:naiminomjonov@gmail.com)

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
