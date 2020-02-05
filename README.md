# TigerV - A wireless interface for controlling automotive accessories


## Shopping List:
$27 - [Pi Zero W](https://www.amazon.com/gp/product/B0748MPQT4/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)

$12 - [NodeMCU ESP8266](https://www.amazon.com/gp/product/B07HF44GBT/ref=ppx_yo_dt_b_asin_title_o02_s01?ie=UTF8&psc=1)

$20 - [SD Cards](https://www.amazon.com/gp/product/B07CP9ZQ72/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

$58 - [Pi 3B+](https://www.amazon.com/CanaKit-Raspberry-Power-Supply-Listed/dp/B07BC6WH7V/ref=sr_1_3?keywords=raspberry+pi+3b%2B&qid=1580924958&sr=8-3)

$17 - [Fuse Block](https://www.amazon.com/gp/product/B07W6KBJ8G/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1)

$27 - [Touchscreen](https://www.amazon.com/dp/B07NSCWY8Z/?coliid=II4254KWVJXQK&colid=3PB41YGHIDZTW&psc=1&ref_=lv_ov_lig_dp_it)

$11 - [Relays](https://www.amazon.com/dp/B07DN8DTRW/?coliid=I21PV3BNJNWEHF&colid=3PB41YGHIDZTW&psc=1&ref_=lv_ov_lig_dp_it)

$9  - [Connectors](https://www.amazon.com/dp/B01LCV8DXQ/?coliid=I239Y8T2FCJZ2O&colid=3PB41YGHIDZTW&ref_=lv_ov_lig_dp_it&th=1)

$11 - [Enclosure](https://www.elexp.com/061135instrument-cases-10-x7-5-x3-1.html)

  #### [Link to Amazon list](https://www.amazon.com/hz/wishlist/ls/3PB41YGHIDZTW?ref_=wl_share)
  
#### Estimated Total Cost:
$112


# Getting Started
## Installing Raspbian
#### [Download the latest version of raspbian from this link](https://www.raspberrypi.org/downloads/raspbian/)
#### [Download the latest version of BalenaEtcher from this link](https://www.balena.io/etcher/)
#### On your PC:
- Unzip your raspbian image file
- Open Balena Etcher
- Select you image file
- Insert your microSD card
- Select your microSD card
- Click flash
- Properly eject the sd card 

*Repeat this step for two SD cards*

## Server Steup
- Install the SD card into the Pi Zero W and power it on
- Complete the initial setup and connect the Pi Zero W to a wifi network
- Update your Pi zero W by opening the terminal and entering the following commands:

  ```
  sudo apt-get update
  sudo apt-get upgrade
  ```
 
- After rebooting, install the mosquitto broker using the following

  ```
  sudo apt install mosquitto
  sudo systemctl enable mosquitto
  ```
  
- After installing mosquitto mqtt broker, set up the stand alone wifi access point using the following

  ```
  sudo apt install dnsmasq hostapd
  sudo systemctl stop dnsmasq
  sudo systemctl stop hostapd
  ```
  
- Configuring a static IP

   ```
   sudo nano /etc/dhcpcd.conf
   ```
  Go to the end of the file and edit it so that it looks like the following:
  
  ```
  interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant
    ```
- Restart the service

   ```
   sudo service dhcpcd restart
   ```
   
- Configuring the DHCP server (dnsmasq)

   ```
   sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
   sudo nano /etc/dnsmasq.conf
   ```
   Type or copy the following information into the dnsmasq configuration file and save it:
   ```
   interface=wlan0      # Use the require wireless interface - usually wlan0
   dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
   ```
- Start dnsmasq (it was stopped), it will now use the updated configuration:   
   ```
   sudo systemctl start dnsmasq   
   ```
- Configuring the access point host software (hostapd)
  ```
  sudo nano /etc/hostapd/hostapd.conf
  ```
  
  To use the 5 GHz band, you can change the operations mode from hw_mode=g to hw_mode=a. Possible values for hw_mode are:

    a = IEEE 802.11a (5 GHz)
    b = IEEE 802.11b (2.4 GHz)
    g = IEEE 802.11g (2.4 GHz)
    ad = IEEE 802.11ad (60 GHz) (Not available on the Raspberry Pi)

  ```
  interface=wlan0
  driver=nl80211
  ssid=<NameOfNetwork>
  hw_mode=b
  channel=7
  wmm_enabled=0
  macaddr_acl=0
  auth_algs=1
  ignore_broadcast_ssid=0
  wpa=2
  wpa_passphrase=AardvarkBadgerHedgehog
  wpa_key_mgmt=WPA-PSK
  wpa_pairwise=TKIP
  rsn_pairwise=CCMP
   ```
   We now need to tell the system where to find this configuration file.
   ```
   sudo nano /etc/default/hostapd
   ```
   
   Find the line with #DAEMON_CONF, and replace it with this:
   ```
   DAEMON_CONF="/etc/hostapd/hostapd.conf"
   ```
- Start it up

   ```
  sudo systemctl unmask hostapd
  sudo systemctl enable hostapd
  sudo systemctl start hostapd   
   ```

## Touchscreen Setup
Plug in the touchscreen with the pin 2 lining up with pin 2 on the pi

Start the pi and go through all of the setup

Open the terminal and execute the following commands

  ```
  sudo apt-get update
  sudo apt-get upgrade
  sudo rm -rf LCD-show
  git clone https://github.com/goodtft/LCD-show.git
  chmod -R 755 LCD-show
  cd LCD-show/
  sudo ./MHS35-show
  ```
Then reboot


## Install the TigerV software

Open the terminal and execute the following commands

  ```
  git clone https://github.com/Collin-Sanders/TigerVProject.git
  ```
  
## Set the program to run on start
