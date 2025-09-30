#!/usr/bin/env python3
import datetime, random, pathlib

# Ensure folders exist
BASE = pathlib.Path("notes")
BASE.mkdir(parents=True, exist_ok=True)

# Use UTC for determinism on GitHub runners
now_utc = datetime.datetime.utcnow()
today = now_utc.date()
fname = BASE / f"{today.isoformat()}.md"

topics = [
    "Investing: note a market mover or earnings date.",
    "Crypto: log a pair to watch and target levels.",
    "BMW/Auto: part number or retrofit idea to research.",
    "SEO/Jobs: keyword cluster or meta snippet to try.",
    "Smart-home: sensor idea or automation rule.",
    "Personal: small win, training, or habit note.",
]

random.seed(int(now_utc.strftime("%Y%m%d%H")))  # slight variation each hour
topic = random.choice(topics)

header = f"# {today.isoformat()} Daily Note\n\n"
line = f"- Update @ {now_utc.strftime('%H:%M:%S')}Z — {topic}\n"

if fname.exists():
    with open(fname, "a", encoding="utf-8") as f:
        f.write(line)
else:
    with open(fname, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(line)

# Touch README so there is always a tiny change if notes didn't change
readme = pathlib.Path("README.md")
pulse = f"\nLast run (UTC): {now_utc.isoformat()}Z\n"
with open(readme, "a", encoding="utf-8") as f:
    f.write(pulse)