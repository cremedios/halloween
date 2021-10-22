# Halloween

A tiny project to celebrate Halloween by getting the Raspberry Pi to play spooky sounds when it detects movement.

## Components

- [Raspberry Pi](https://www.raspberrypi.com/products/)
- [USB Speaker](https://www.amazon.com/dp/B088PCWXH9)
- [HC-SR501 Pir Motion IR Sensor](https://www.amazon.com/dp/B012ZZ4LPM)
- [Female to Female Breadboard Jumper Wires](https://www.amazon.com/dp/B01EV70C78)
- [USB Power source](https://www.amazon.com/dp/B0933CJWS1) 18000mAh lasts almost 48 hours

## Pir sensor connection

![pir_raspberry](https://user-images.githubusercontent.com/1027202/138522901-5a709f34-8bf6-45b2-83ea-306751c2a4e4.jpg)

## Schedule

Script is configured to exit at 9PM. Use crontab to ensure it starts up the next morning:

```
@reboot python3 /home/pi/pumpkin.py >> /home/pi/pumpkin.log 2>&1
0 8 * * * python3 /home/pi/pumpkin.py >> /home/pi/pumpkin.log 2>&1
```

## Sounds

Sounds downloaded from
- https://free-loops.com/
- https://www.partnersinrhyme.com/