# Voltage and Current Logger

## Dependencies

__Python 2.7__

Download [python 2.7](https://www.python.org/downloads/). Make sure to install pip as well.

__Pyserial__

To automate the communication between the arduino and the computer you need to install pyserial. Most system can install it by writing the following command in either the terminal or the command prompt:

	> pip install pyserial

Another alternativ can be found [here](https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector/installing-python-and-pyserial).

__Arduino IDE__

Install [Arduino IDE](https://www.arduino.cc/en/Main/Software).

# Hardware

This chapter will describe the hardware necessary for the realtime voltage and current logger to work properly.

## Current measurements

To measure the current we used a current transformer as described in the figure below (thanks to Isabelle Florent for the figure). By using a magnetic core with with a coil, it was possible to measure the output voltage. 

![](doc/figures/current/main.png)

To make the output voltage from the current transformer match the input voltage range of the ADC better, it is possible to use an amplifier. A simple [inverting amplifier](https://en.wikipedia.org/wiki/Operational_amplifier_applications#Inverting_amplifier) was used. Remeber that the amplifier inverts the signal, so that the signal needs to be multiplied by -1. The figure below describe the setup of the amplifier.

![](doc/figures/amplifier/main.png)

If you measure AC current it is important to change the scope of the input voltage, as described in the section "Change Input Scope" below.

## Measure voltage

We used a transformer to lineary decrease the AC voltage on the grid to a value applicable for measurments. After the transformer, the voltage ranged between -6 and 6 volts. After the transformer we used a voltage devidor to decrease the maximum voltage down to 5 V. The circuit is described in the figure below.

![](doc/figures/transformer/main.png)

The circuit in the next chapter was used to change the scope from [-5 V, 5 V] to [0, 5 V].

## Change Input Scope

The Arduino's [ADC](https://en.wikipedia.org/wiki/Analog-to-digital_converter) can only read positive values, from 0 to 5 V. As the AC voltage and current has both positive and negative values it is necasarry to change the refrence. The circuit below can be used.

![](doc/figures/referance-changer/main.png)

To find the new output voltage we can use the node voltage method. With an input voltage between -5 V to 5 V the corresponding output voltage would be 0 to 4.5 V.