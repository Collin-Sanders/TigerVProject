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
