

# QNAP QIoT Suite Lite 

![Picture](doc/media/QIoT.jpg)

This repository contains QIoT device SDKs. We provide sample code for enable connect client devices to QNAP QIoT Suite Lite. 

## QNAP QIoT device SDKs

The QNAP QIoT device SDKs contain code that facilitate building devices and applications that connect to and are managed by QNAP QIoT Suite services.

Devices and data sources in an IoT solution can range from a simple network-connected sensor to a powerful, standalone computing device. Devices may have limited processing capability, memory, communication bandwidth, and communication protocol support. The IoT device SDKs enable you to implement client applications for a wide variety of devices.

This repository contains the following QIoT device SDK sample code:

[QNAP QIoT device SDK sample code for Node.js](nodejs/)

Each language SDK includes sample code and documentation in addition to the library code. 
The API reference documentation is coming soon.

### OS platforms and hardware compatibility

QNAP IoT device SDKs can be used with a broad range of OS platforms and devices. See OS Platforms and hardware compatibility.


### For Example

- **Arduino Yún**
![Picture](doc/media/Arduino-Yún.png)

- **Raspberry Pi**
![Picture](doc/media/Raspberrypi.png)

- **Intel® Edison**
![Picture](doc/media/Intel-edison-mini-board.png)

- **Linkit7688 (Duo)**
![Picture](doc/media/Linkit7688_(Duo).png)

## Samples

Within the repository, you can find various types of simple samples that can help you get started.
Below is a complete list of all these simple samples.
In addition to these simple samples, you can find a long list of [getting started guides](doc/set_out) that describe all the steps necessary to run the simple samples on a wide variety of devices and platforms.

- Node.js device SDK:

[Raspberry sample code](nodejs/device/raspberrypi/examples)

[Intel Edison sample code](nodejs/device/intel-edison/examples)

## Contribution, feedback and issues

If you would like to become an active contributor to this project please follow the instructions provided in the contribution guidelines.
If you encounter any bugs or have suggestions for new features, please file an issue in the [Issues](https://github.com/QNAP/qnap-iot-sdks/issues) section of the project.

## Support

If you are having issues using one of the packages or using the QNAP QIoT Suite service that go beyond simple bug fixes or help requests that would be dealt within the [issues section](https://github.com/qnap-dev/qnap-qiot-sdks/issues) of this project.

To engage QNAP support, you can create a support ticket directly from the [QNAP Helpdesk](https://helpdesk.qnap.com/).


## QIoT GitBook
To learn more about QIoT, please refer to follow link: 
https://anderson2007.gitbooks.io/qiot-suite-lite/content/


## Additional resources

In addition to the language SDKs, this repository ([qnap-qiot-sdks](https://github.com/qnap-dev/qnap-qiot-sdks)) contains the following folders:


### /doc

This folder contains the following documents that are relevant to all the language SDKs:

-  How to set up your device environment and define your device's sensor then send the data to QIoT Suite.

### /tools(Coming soon)

This folder contains tools you will find useful when you are working with QIoT container and the device SDKs.
