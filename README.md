# This application gets twitch messages in real time and prints them in push notifications

## To run
create a .env file with OAUTH="your twitch API token without the 'oauth:'"

```bash
pip3 -r requirements.txt
python3 main.py
```

## To install on your android device
### Install buildozer
```bash
git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python setup.py install
```

### Initialize buildozer in your app directory
```bash
buildozer init
```

### Plug in your device to your computer and deploy the app
```bash
buildozer android debug deploy run
```