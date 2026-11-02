# CS 304 – Unit Testing (Nov 2)

Setup (once):

    pip install pytest
    pytest -q          # from this folder; runs every test_*.py it finds

Folders:

- `example/` – a tiny function and its tests. Read `test_example.py` if pytest is new to you.
- `demo/` – the AI demo. `shipping.py` is the code; `SPEC.md` is what it is supposed to do.
- `swap/` – the mutation swap. `grading.py` has three functions with specs in their docstrings.
- `decompose/` – a function you can't easily test. Make it testable, then test it.
- `.github/workflows/tests.yml` – runs `pytest` on every push and pull request.

## Mutation swap rules

Round 1 – write tests (6 min)
- Your pair gets ONE function in `swap/grading.py`. Write tests for it in a new file, e.g. `swap/test_leap_year.py`.
- Test from the docstring spec. All your tests must pass against the real function.

Round 2 – plant a mutant (5 min)
- Rotate: you now attack another pair's function AND read their test file.
- Change ONE small thing in that function so it breaks the spec (flip `<` to `<=`, drop a rule, change a constant...).
- Your goal: a real bug that their tests still pass. AI is allowed.
- Run their tests. Red = your mutant was "killed". Green = it "survived" (their tests have a gap).

Pair A: `is_leap_year`   → attacks `late_penalty`
Pair B: `late_penalty`   → attacks `letter_grade`
Pair C: `letter_grade`   → attacks `is_leap_year`

## Decompose exercise

`decompose/submissions_report.py` works, but you can't unit test it: it reads a file, uses a global deadline, and prints instead of returning.

1. Extract a pure function: `final_score(score, submitted_at, deadline) -> float`.
2. Pass the deadline in instead of reading the global.
3. Have the report return its lines instead of printing them (and get rid of the `REPORT` global).
4. Write `decompose/test_submissions_report.py`. Use the late-penalty spec from `swap/grading.py`.
