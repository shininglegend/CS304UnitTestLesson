import math


def is_leap_year(year):
    """Return True if `year` is a leap year in the Gregorian calendar.

    Spec:
    - A year divisible by 4 is a leap year,
    - except a year divisible by 100 is NOT a leap year,
    - except a year divisible by 400 IS a leap year.
    - Raise ValueError for year < 1.

    Examples: 2024 -> True, 2023 -> False, 1900 -> False, 2000 -> True.
    """
    if year < 1:
        raise ValueError("year must be 1 or later")
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def late_penalty(score, hours_late):
    """Return the score after the course late penalty.

    Spec (from the syllabus: 10% per 24-hour period late):
    - hours_late <= 0: score is unchanged.
    - Each STARTED 24-hour period late deducts 10% of the original score.
      More than 0 and up to and including 24 hours late = 1 period (-10%).
      More than 24 and up to and including 48 hours = 2 periods (-20%), etc.
    - The result never goes below 0.
    - Raise ValueError if score < 0.

    Examples: (80, 0) -> 80, (80, 1) -> 72, (80, 24) -> 72, (80, 25) -> 64,
              (80, 1000) -> 0.
    """
    if score < 0:
        raise ValueError("score must not be negative")
    if hours_late <= 0:
        return score
    periods = math.ceil(hours_late / 24)
    percent_kept = max(0, 100 - 10 * periods)
    return score * percent_kept / 100


def letter_grade(score):
    """Return the letter grade for a percentage score.

    Spec:
    - 90 to 100 -> "A"
    - 80 up to (not including) 90 -> "B"
    - 70 up to (not including) 80 -> "C"
    - 60 up to (not including) 70 -> "D"
    - below 60 -> "F"
    - Raise ValueError if score < 0 or score > 100.

    Examples: 95 -> "A", 90 -> "A", 89.9 -> "B", 59.99 -> "F".
    """
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
