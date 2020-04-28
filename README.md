# Vorlesungen

Die Vorlesungen unterliegen der [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) Lizenz

## Dual Screen Output

Way better than to configure xrandr: [pympress](https://github.com/Cimbali/pympress)

Get a list of your output devices
```
$ xrandr --listmonitors
```

Configure Displays accordingly to the listed aspect ratios
```
xrandr --output eDP1 --mode 1920x1080 --output HDMI1 --mode 1280x1024
```

scale output of the selected device to show only region of interest
For details see also [PracTeX Journal](https://www.tug.org/pracjourn/2010-1/dohmen/dohmen.pdf).
```
xrandr --output HDMI1 --mode 1280x1024 --scale 0.75x0.75 --pos 0x112
```
