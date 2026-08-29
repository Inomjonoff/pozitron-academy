# 🗺️ Pozitron Academy — Development Roadmap

---

## 🚀 Phase 1: Algorithm & Foundations `[COMPLETED]`
- [x] SuperMemo-2 pure Python calculation engine (`backend/sm2.py`).
- [x] Mathematical verification and unit test cases.
- [x] AI prompt library for CEFR vocabulary extraction and tutoring (`PROMPTS.md`).
- [x] Database schema & system architecture specifications (`ARCHITECTURE.md`).

---

## 📱 Phase 2: Telegram Bot MVP `[CURRENT FOCUS]`
- [ ] Initialize `aiogram 3.x` bot with inline card review keyboard.
- [ ] Flashcard study loop: Display Front → Show Answer → Rate Quality (0-5) → Schedule next SM-2 date.
- [ ] Daily reminder scheduler (`APScheduler` / Celery) sending cards due today.
- [ ] User streaks, XP points, and weekly leaderboards.

---

## 📖 Phase 3: Interactive Web Book Reader
- [ ] Web-based e-book reader (EPUB/PDF/Text) with 1-click word lookup.
- [ ] Automatic card creation from reading context with translation and audio.
- [ ] CEFR difficulty vocabulary highlighter (e.g. highlights C1 words in purple).

---

## 🌐 Phase 4: Community & Multi-Language Scaling
- [ ] Public deck repository for community sharing.
- [ ] Web Progressive Web App (PWA) with offline sync.
- [ ] Multi-language pairs support (English, German, Russian, Uzbek, Arabic).
