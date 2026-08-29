"""
SuperMemo-2 (SM-2) Spaced Repetition Algorithm Implementation.
Calculates the next repetition interval and easiness factor (EF)
based on student response quality (grade: 0 to 5).

Grade scale:
5 - Perfect response
4 - Correct response after a hesitation
3 - Correct response recalled with serious difficulty
2 - Incorrect response; where the correct one seemed easy to recall
1 - Incorrect response; the correct one remembered
0 - Complete blackout
"""

from datetime import datetime, timedelta
from typing import Tuple

def calculate_sm2(
    quality: int,
    repetitions: int,
    previous_interval: int,
    previous_easiness_factor: float = 2.5
) -> Tuple[int, int, float, datetime]:
    """
    Returns:
        (repetitions, new_interval_in_days, new_easiness_factor, next_review_date)
    """
    if not (0 <= quality <= 5):
        raise ValueError("Quality rating must be between 0 and 5")

    # 1. Update Easiness Factor (EF)
    new_ef = previous_easiness_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    if new_ef < 1.3:
        new_ef = 1.3  # Minimum EF threshold in standard SM-2

    # 2. Update Repetitions & Interval
    if quality >= 3:
        if repetitions == 0:
            interval = 1
        elif repetitions == 1:
            interval = 6
        else:
            interval = int(round(previous_interval * new_ef))
        repetitions += 1
    else:
        # Failed recall: reset repetitions and schedule for immediate review
        repetitions = 0
        interval = 1

    next_review_date = datetime.utcnow() + timedelta(days=interval)
    return repetitions, interval, round(new_ef, 3), next_review_date

if __name__ == "__main__":
    # Test simulation
    print("Testing SM-2 Algorithm:")
    reps, interval, ef, next_date = calculate_sm2(quality=4, repetitions=0, previous_interval=0)
    print(f"Review 1 (Grade 4): Reps={reps}, Next Interval={interval}d, EF={ef}, Date={next_date.strftime('%Y-%m-%d')}")

    reps, interval, ef, next_date = calculate_sm2(quality=5, repetitions=reps, previous_interval=interval, previous_easiness_factor=ef)
    print(f"Review 2 (Grade 5): Reps={reps}, Next Interval={interval}d, EF={ef}, Date={next_date.strftime('%Y-%m-%d')}")
