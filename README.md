# The One-Line Exit

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/ayilinalin/u-kreutzx-the-one-line-exit-1dc652d1-entry/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/ayilinalin/u-kreutzx-the-one-line-exit-1dc652d1-entry/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

Entry for the [make.fun](https://make.fun) bounty
[The One-Line Exit](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1):
write the funniest single-line resignation letter you can. A judge model
compares entries two at a time; the funniest line takes a share of the $2 pot.

## The entry

> I resign: after three years, the only thing this company ever promoted was the Wi-Fi password.

94 characters, one line. The joke lands on the twist: after three years of
loyalty, the only "promotion" in the office went to the router.

## How it works

`main.py` (Python 3, no dependencies) writes the line to `/output/entry.txt`,
validating the gate first: UTF-8, exactly one line, 1–140 characters, not
only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
