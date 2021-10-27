# MCRewards-Discord-Bot
A Discord bot that rewards players in Minecraft for sending messages on Discord


## How to setup:
* Download this git as a .zip, or clone it.
* Install the pip packages in `requirements.txt` with `pip install -r requirements.txt` or `pip3` depening on how your system is setup.
* Go to `config.json` and fill out the needed info.
* Start the bot with `main.py`.
* Your users must link their Discord account to their Minecraft account with the `mcr!link <username>` command. Eg: `mcr!link MrRazamataz`. They will be reminded to link if they haven't every time they level up, otherwise the rewards won't work.

## Other things:
Idea comes from this thread on r/admincraft https://www.reddit.com/r/admincraft/comments/qh3175/plugin_for_ingame_rewards_for_being_active_in/

The code is simple, it's not meant to be advanced. Yes, there may be better ways to code this, like not using .json to store data or not using so many global variables, but it's simple and it works well.

## Planned:
[ ] A method to protect against spam leveling up.

Let me know of suggestions by creating an issue in the Github issues TAB.