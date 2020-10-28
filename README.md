# Depecher - A Telegram client for Sailfish OS
based on tdlib.

Features:
- Send/View/Delete messages
- View photos
- View stickers
- View gift
- Uploading/Downloading photos/docs
- Receive notifications
- 2FA authorization enabled
- and more...


## Openrepos 

https://openrepos.net/content/blacksailer/depecher


## Contribute?

- Review code!
- Create issue for missing features!
- Do something really cool!


 ## Build 
 
 - Installing dependencies

Enter the sailfish os build machine (Start it from Tools/Options/Sailfish OS/Start Virtual Machine)

ssh -p 2222 -i ~/SailfishOS/vmshare/ssh/private_keys/engine/mersdk mersdk@localhost

- Enter the arch to use (use the arm)

sb2 -m sdk-install -R -t SailfishOS-3.4.0.24-armv7hl
    
- Add the tdlibjson repo

zypper ar http://repo.merproject.org/obs/home:/blacksailer:/branches:/home:/blacksailer/sailfish_latest_armv7hl/ tdlibsjon 
    
Refresh zypper repos

zypper ref  

- Install dependencies

zypper install tdlibjson tdlibjson-devel   
 
 
## Licenses

 - sticker-smiled is made for jgibbon under [![GPLv3](https://www.gnu.org/graphics/gplv3-88x31.png)](https://www.gnu.org/licenses/gpl-3.0.html)
