# Chicago Weather Summary

This script fetches the current multi-day weather forecast for Chicago, Illinois from the National Weather Service API. The API gives the day of the week for each forecasted day, but no calendar dates. The script adds calendar dates to each relevant section of the data. Finally, it calls Anthropic's Claude API to summarize the data in fewer than 100 words, in plain text.

## Why I Built This
This is my first project connecting a public API to an LLM while learning Python.

## Setup
1. Install the libraries:
    ```bash
    pip3 install -r requirements.txt
    ```
2. Get an API key from console.anthropic.com and set it as the `ANTHROPIC_API_KEY` environment variable.

Note: requires Python 3 and an Anthropic account with some API credit.

## Usage
```bash
python3 weather_summary.py
```

## Example Output
```
Today (10/23) is mostly sunny with highs in the lower 70s inland and upper 60s near the lake, followed by a mostly clear to partly cloudy night with lows in the lower 50s. Saturday (10/24) is mostly cloudy with highs around 70. Sunday (10/25) is partly cloudy with lower 70s. Monday (10/26) and Tuesday (10/27) stay mostly cloudy, with highs in the upper 60s and mid 60s. Wednesday (10/28) and Thursday (10/29) turn partly cloudy with upper 60s highs. Nights remain in the lower 50s throughout.
```