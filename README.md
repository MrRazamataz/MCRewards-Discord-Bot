# MCRewards-Discord-Bot
A Discord bot that rewards players in Minecraft for sending messages on Discord.  
Please note, this is currently not something that I host, you need to host it yourself. If enough people request a hosted version, I could look into it.  


## How to setup:
* [Download this git as a .zip](https://github.com/MrRazamataz/MCRewards-Discord-Bot/archive/refs/heads/main.zip), or clone it.
* Install the pip packages in `requirements.txt` with `pip install -r requirements.txt` or `pip3` depening on how your system is setup.
* Go to `config.json` and fill out the needed info.
* Don't change `levels.json` or `accountdata.json` from the default ones on GitHub on first use, the bot will manage those files for you. After you have some data in them, you can change the vaules or whatever, just restart the bot once you do.
* Start the bot with `main.py`.
* Your users must link their Discord account to their Minecraft account with the `mcr!link <username>` command. Eg: `mcr!link MrRazamataz`. They will be reminded to link if they haven't every time they level up, otherwise the rewards won't work. They can change their username thats saved by re-running the command.
* To add rewards (commands ran on the server), you can run the command `mcr!addreward`. Example, `mcr!addreward 2 lp user %player% parent add level2` would add the luckperms group `level2` when they reach level `2` on the bot. `%player%` is replaced with the users Minecraft username if set with `mcr!link`. Example image: https://mrrazamataz.ga/archive/python/mcrewards/example1.png .
## Other things and Info:
Idea comes from this thread on r/admincraft https://www.reddit.com/r/admincraft/comments/qh3175/plugin_for_ingame_rewards_for_being_active_in/  

You can use MEE6 levels instead of the bot levels. To do this, set `use_mee6_levels` to true in `config.json`.

The code is simple, it's not meant to be advanced. Yes, there may be better ways to code this, like not using .json to store data or not using so many global variables, but it's simple and it works well.

The bot saves the `levels.json` file to disk from RAM every 3 mins.  
Everytime a change is made to `accountdata.json` via a bot command, the changes are saved instantly.  

## Planned:
- [ ] A method to protect against spam leveling up.  (sort of; enable `use_mee6_levels` in `config.json` to use Mee6 levels instead).
- [x] An easy way for admins to add reward commands (complete).

Let me know of suggestions by creating an issue in the Github issues TAB.

## Compatibility: 
It is compatibile with every server software that offers support for rcon. Just fill out the info in `config.json`. It runs commands with the players username that is stored in `accountdata.json`.
