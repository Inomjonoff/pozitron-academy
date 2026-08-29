# 📐 Pozitron Academy — Architecture & Algorithmic Specifications

---

## 1. SuperMemo-2 (SM-2) Mathematical Algorithm

The SM-2 algorithm calculates the next review interval ($I$) and easiness factor ($EF$) based on student response quality ($q \in [0, 5]$):

$$EF' = EF + (0.1 - (5 - q) \times (0.08 + (5 - q) \times 0.02))$$
$$\text{where } EF' \ge 1.3$$

### Interval Scheduling Rules:
- If $q < 3$ (Recall failure): $n = 0, I_1 = 1 \text{ day}$.
- If $q \ge 3$ (Successful recall):
  - For $n = 1$: $I_1 = 1 \text{ day}$
  - For $n = 2$: $I_2 = 6 \text{ days}$
  - For $n > 2$: $I_n = \text{round}(I_{n-1} \times EF')$

---

## 2. Database Schema (PostgreSQL)

```sql
-- Flashcard Decks
CREATE TABLE decks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    title VARCHAR(150) NOT NULL,
    target_language VARCHAR(10) NOT NULL,
    is_public BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Flashcards
CREATE TABLE flashcards (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    deck_id UUID REFERENCES decks(id) ON DELETE CASCADE,
    front_text VARCHAR(255) NOT NULL,
    back_translation TEXT NOT NULL,
    context_sentence TEXT,
    audio_url VARCHAR(500),
    part_of_speech VARCHAR(50),
    cefr_level VARCHAR(5) DEFAULT 'B1',
    
    -- SM-2 State Fields
    repetitions INTEGER DEFAULT 0,
    interval_days INTEGER DEFAULT 1,
    easiness_factor REAL DEFAULT 2.5,
    next_review_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Review Log History
CREATE TABLE review_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    flashcard_id UUID REFERENCES flashcards(id) ON DELETE CASCADE,
    user_id UUID NOT NULL,
    rating_quality INTEGER CHECK (rating_quality BETWEEN 0 AND 5),
    scheduled_interval INTEGER NOT NULL,
    reviewed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```
