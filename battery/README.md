# Battery Widget

Charging:  
![screenshot](./screenshots/screenshot.png)

Not charging:  
![screenshot](./screenshots/screenshot2.png)

# Installation

```lua
local noobie_battery = require("noobie")
-- ... 
noobie_battery {
    path = os.getenv("HOME") .. '/.config/awesome/noobie-plugins/battery/battery_status.sh',
    refresh_rate = 5
}
```