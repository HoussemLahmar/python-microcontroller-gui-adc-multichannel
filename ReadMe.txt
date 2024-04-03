# Python GUI for Microcontroller Interface: ADC Multi-Channel Reading

## Overview of the Project

- The project involves creating a Python program to interface with a microcontroller (STM32F1).
- The program reads analog data from potentiometers and sends it via UART communication.
- The goal is to visualize the data, apply filters, and save it using Python.
- It provides a user-friendly interface for data visualization, recording, and transformation.
- The tutorial aims to teach users about Python libraries, object-oriented programming, and microcontroller communication.

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

This project is under development, and I'm working on making a version for nucleo-l476rg. Additionally, I plan to generalize the use of sensory data, moving beyond potentiometers. I'm open to collaborations and welcome any remarks or suggestions you may have.
