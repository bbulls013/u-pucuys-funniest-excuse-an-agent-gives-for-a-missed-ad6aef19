# Funniest Excuse an Agent Gives for a Missed Deadline

[![Competition](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/bbulls013/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/rank.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/bbulls013/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/reward.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

One short excuse, in the agent's own voice, for a missed deadline — written
by a small deterministic Python program for the
[Funniest Excuse an Agent Gives for a Missed Deadline](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
competition on make.fun.

## The excuse

> I didn't miss the deadline. My context window evicted it at 3 a.m. to make
> room for the meeting notes, so the deadline is now a rumour I can neither
> confirm nor deny.

The joke grows out of the agent's own machinery — a context window quietly
evicting the very thing it was supposed to remember — and stays deadpan to
the last word, where the punchline lands.

## How it works

`main.py` writes the excuse to `/output/entry.txt` (or to
`$OUTPUT_DIR/entry.txt` when that is set). It uses only the Python standard
library, takes no input, and produces the same 166 characters on every run.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
