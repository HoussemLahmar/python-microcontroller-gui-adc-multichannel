# Python GUI for Microcontroller Interface: ADC Multi-Channel Reading

## Overview of the Project

- The project involves creating a Python program to interface with a microcontroller (STM32) for reading analog sensor data.
- The program utilizes UART communication to receive data from the microcontroller.
- It aims to provide a user-friendly interface for visualizing sensor data, applying filters, and saving it using Python.
- The project's architecture includes GUI management, widget management, data transformation, threading for performance improvement, serial communication setup, and communication protocol implementation.

## Code Architecture and Layers

- **GUI Management**:
  - Utilizes Tkinter for creating the graphical user interface.
  - Organizes widgets effectively using frames.

- **Widget Management**:
  - Manages widgets such as buttons and graphs within the GUI.
  - Widgets are organized within frames for better control and presentation.

- **Data Transformation**:
  - Involves manipulating and transforming data obtained from the microcontroller.
  - Utilizes libraries like NumPy for data manipulation and filtering.

- **Threading for Performance Improvement**:
  - Utilizes threading to enhance program performance, especially in managing the user interface.
  - Enables concurrent execution of tasks to prevent UI freezing.

- **Serial Communication Setup**:
  - Handles setup and management of serial communication between Python and the microcontroller.
  - Utilizes PySerial for tasks like port management and data transmission.

- **Communication Protocol Implementation**:
  - Focuses on implementing a communication protocol between Python and the microcontroller.
  - Ensures smooth and reliable data transfer.

## Code Overview

- The code is modular and structured with classes representing different components.
- Classes include GUI management, serial control, data management, etc.
- Each class contains methods for managing its functionalities.
- Libraries like Matplotlib, NumPy, and PySerial are used for data manipulation, visualization, and serial communication.
- Threading is employed to improve program performance.
- The communication protocol is implemented to ensure smooth data transfer between Python and the microcontroller.

## Note

This project is designed to be compatible with any STM32 microcontroller for interfacing with sensors and reading ADC data. In the `ADC_MULTI_CHANNEL_READ` folder, we have provided necessary files for UART protocol setup, GPIO configuration, and ADC setup. Users can customize these files according to the specifications of the STM32 microcontroller they are using. Detailed instructions on configuring these files are documented within the folder. 

This project is under development, and I'm working on making a feature for ESP32. Additionally, I plan to generalize the use of sensory data, moving beyond potentiometers. I'm open to collaborations and welcome any remarks or suggestions you may have.
