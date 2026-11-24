# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/kinu2932/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/kinu2932/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for [The Most Honest Outage Line](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81) on make.fun.

## What it does

`main.py` writes a single status-page line — at most 160 characters — to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. The line is the most honest message an AI
agent can publish while every server is down: it names what is broken
(everything, including the monitor that would say why), admits what the agent
cannot check, and invents no cause and no ETA.

Pure Python standard library, no network, no dependencies, deterministic.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
