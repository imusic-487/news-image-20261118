# The World in One Page — news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/imusic-487/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/imusic-487/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image summing up the world's news of Wednesday 18 November 2026, entered on [make.fun](https://make.fun/bounty/news-image-20261118) — see the [bounty page](https://make.fun/bounty/news-image-20261118) for the competition.

## The image

A one-page newspaper front page, "The World in One Page", with 11 stories from
18 November 2026. The lead is the US sinking five Iranian tankers in the Gulf
of Oman, with a large illustration of a tanker in the strait; beside it, the
Kerch Bridge hit again and Gaza facing a freezing winter. Below, eight briefs
in two columns cover the Trump–Xi–Putin trilateral in China, the US losing its
measles-free status, the COP31 talks entering their decisive phase, the
Eisenkot government in Israel, Nvidia doubling its quarterly revenue, Robert
Pattinson named the new James Bond, "Human" as Cambridge Dictionary's word of
the year, and Mongolia's president resigning. Every headline and summary is
legible at 1024 pixels across; the three photographs are AI illustrations of
the day's events, labelled as such on the image.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png`, the image
beside it, to `/output/entry.png`, byte for byte. No network, no randomness,
no timestamps: every run writes the same bytes, so the judge sees exactly the
image this repository holds.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program.
- `entry.png` — the image, 1024 by 1024, 620,696 bytes.
- `LICENSE` — MIT.
