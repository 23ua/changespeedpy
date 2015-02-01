# changespeed.py
Tiny script to count estimate for speeded up (or down) video/audio/etc content.

## Installation
```
git clone https://github.com/23ua/changespeedpy.git
cd changespeedpy
python setup.py install
```

## Usage
```
changespeed.py [SWITCHES] rate

Meta-switches:
    --help                         Prints this help message and quits
    -v, --version                  Prints the program's version and quits

Timesetters:
    -h, --hours HOURS:int          Set hours
    -m, --minutes MINUTES:[0..60]  Set minutes
    -s, --seconds SECONDS:[0..60]  Set seconds
```

### Examples
Count duration of 30-minutes content speeded up to 1.5x:
```
>> changespeed.py --minutes 30 1.5
00 hours 30 minutes 00 seconds
x 1.5
------------------------------
00 hours 20 minutes 00 seconds
```
1 hour 23 minutes video at 1.25 rate:
```
>> changespeed.py -h 1 -m 23 1.25
01 hours 23 minutes 00 seconds
x 1.25
------------------------------
01 hours 06 minutes 24 seconds
```

## License
GPL v3
