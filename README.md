# This application gets twitch messages in real time and prints them in push notifications

## To run
pip3 -r requirements.txt
python3 main.py

## To install on your android device
### Install buildozer
git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python setup.py install

### Initialize buildozer in your app directory
buildozer init

### Plug in your device to your computer and deploy the app
buildozer android debug deploy run
