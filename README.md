# lancache-prefill-discord-log
LanCache Prefill log parsing for Discord.
It only supports one log file at the moment, so if you have multiple log files, you need to run multiple instances of the script.
In my setup i have this script running in the same folder as the prefill. So i have one script for each prefill instance.

## Usage
1. Clone this repo to your prefill folder.
2. Install the Python requirements: `pip install -r requirements.txt`
3. Change the following stuff in `lancache-log-parser.py`.
   1. LogChannel: The full Discord Webhook URL: "https://discord.com/api/webhooks/XXXXXXXXXXX/XXXXXXXXXXX
   2. LogLocation: The full path to the log file: fx: "/home/prefill/SteamPrefill-2.2.2-linux-x64/app.log"
   3. UserTagging can be set to True, if you want a notification when a download has completed.
      1. Find your Discord User ID: https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID- (like: <@XXXXXXXXXXX>)

## Enable Auto-Start using systemd
1. Copy the `lancache-log-parser.service` file to `/etc/systemd/system/`
2. Change the `ExecStart` to match your setup.
3. Change user and group to match your setup.
4. Enable the service: `systemctl enable lancache-log-parser.service`
5. Start the service: `systemctl start lancache-log-parser.service`
6. Check the status: `systemctl status lancache-log-parser.service`