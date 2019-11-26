# TigerV2 - A touchscreen interface for controlling automotive accessories


## Shopping List:
$27 - [Pi Zero](https://www.amazon.com/gp/product/B0748MPQT4/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)

$5  - [Port Expander](https://www.amazon.com/gp/product/B00I6OEWJM/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1)

$17 - [Fuse Block](https://www.amazon.com/gp/product/B07W6KBJ8G/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1)

$27 - [Touchscreen](https://www.amazon.com/dp/B07NSCWY8Z/?coliid=II4254KWVJXQK&colid=3PB41YGHIDZTW&psc=1&ref_=lv_ov_lig_dp_it)

$11 - [Relays](https://www.amazon.com/dp/B07DN8DTRW/?coliid=I21PV3BNJNWEHF&colid=3PB41YGHIDZTW&psc=1&ref_=lv_ov_lig_dp_it)

$9  - [Connectors](https://www.amazon.com/dp/B01LCV8DXQ/?coliid=I239Y8T2FCJZ2O&colid=3PB41YGHIDZTW&ref_=lv_ov_lig_dp_it&th=1)

$11 - [Enclosure](https://www.elexp.com/061135instrument-cases-10-x7-5-x3-1.html)

  #### [Link to Amazon list](https://www.amazon.com/hz/wishlist/ls/3PB41YGHIDZTW?ref_=wl_share)
  
#### Estimated Total Cost:
$112


# Getting Started
## Installing Raspbian (for mac)
#### [Download the latest version of raspbian from this link](https://www.raspberrypi.org/downloads/raspbian/)

#### On your mac:
Open up terminal and type the following commands
  ```
  diskutil list
  ```
Identify the disk (not the partition) of your SD card
  ```
  diskutil unmountDisk /dev/disk<disk# from diskutil>
  ```
cd to directory where you image file is located
  ```
  sudo dd bs=1m if=image.img of=/dev/rdisk<disk# from diskutil> conv=sync
  ```
Right click and properly eject the sd card  

## Hardware Setup
**_I recommend viewing the autocad file in the autocad folder_**

Solder all of the pins for the pi except for the following pins: 1 , 2 , 3 , 5 , 39.

For the above pins, solder wire from the bottom through the holes.

Plug in the touchscreen and proceed with the touchscreen setup.

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


## Install the TigerV2 software

Open the terminal and execute the following commands

  ```
  git clone https://github.com/Collin-Sanders/TigerV2Project.git
  ```
  
## Set the program to run on start
