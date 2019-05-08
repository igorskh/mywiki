# Convert HTML to PNG in Python with virtual browser and virtual display
*Tags: #ubuntu #python * 

## Description
It is an example how to save a leaflet map generated with [Folium](https://github.com/python-visualization/folium) as a png image.

## Tools
[folium](https://github.com/python-visualization/folium)
[selenium](https://www.seleniumhq.org/)
[pyvirtualdisplay](https://pypi.org/project/PyVirtualDisplay/)

## Install Ubuntu packages
If you use a Ubuntu server and there is no graphical interface, gecko driver and Firefox need to be installed:
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar xvfz geckodriver-v0.24.0-linux64.tar.gz
sudo cp geckodriver /bin/geckodriver
```

For the virtual display:
```
sudo apt install xvfb xephyr
```

Without using a virtual display, you will get an error in the `geckodriver.log` file such as:
```
Error: no DISPLAY environment variable specified
```

## Install python packages
```
pip install folium
pip install selenium
pip install pyvirtualdisplay
```

## Python code
```
from pyvirtualdisplay import Display 
from selenium import webdriver
import folium
import time

m = folium.Map(
    location=[45.5236, -122.6750],
    tiles='Stamen Toner',
    zoom_start=13,
    max_zoom=16
)

fn = 'map.html' #path to the html file

# can be defined to fit all points on the map
#m.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])
m.save(fn)

delay = 2
tmpurl = 'file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=fn)
m.save(fn)
browser.get(tmpurl)
#Give the map tiles some time to load
time.sleep(delay)
browser.save_screenshot(fn + ".png")
```
