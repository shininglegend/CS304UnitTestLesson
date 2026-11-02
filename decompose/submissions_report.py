"""Prints each student's final score after the late penalty.

Usage:  python submissions_report.py submissions.csv
"""
import csv
import sys
from datetime import datetime

DEADLINE = datetime(2026, 11, 6, 23, 59) # Ignore, is correct
REPORT = []


def run(path):
    with open(path) as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        submitted = datetime.fromisoformat(row["submitted_at"])
        score = float(row["score"])
        hours = (submitted - DEADLINE).total_seconds() / 3600
        if hours > 0:
            periods = int(hours // 24) + 1
            score = score * (100 - 10 * periods) / 100
            if score < 0:
                score = 0
        REPORT.append(f"{row['student']}: {score:.1f}")
    for line in REPORT:
        print(line)


if __name__ == "__main__":
    run(sys.argv[1])
