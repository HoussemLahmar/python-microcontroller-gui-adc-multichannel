# Setting Up STM32 Microcontroller Project

In this guide, we will detail how to set up a project for an STM32 microcontroller using Keil µVision. This project will involve configuring GPIOs for sensor input, setting up ADC conversion, and implementing UART communication. The provided files are designed to be generic and adaptable to various STM32 microcontrollers.

## Overview

The purpose of this setup is to establish communication between the STM32 microcontroller and a Python-based GUI application. While the Python GUI handles data visualization and user interaction, the microcontroller's role is to manage hardware aspects such as reading sensor data, performing ADC conversions, and transmitting data via UART.

## Files Provided

The following files are provided for setting up the STM32 microcontroller project:

- `main.c`: Main application file.
- `adc_drive.c`, `adc_drive.h`: ADC driver files.
- `gp_drive.c`, `gp_drive.h`: General-purpose I/O (GPIO) driver files.
- `help_func.c`, `help_func.h`: Helper function files.
- `msg_drive.c`, `msg_drive.h`: Message driver files.

## Configuration Steps

1. **Create a New Keil Project**:
   - Open Keil µVision.
   - Click on "Project" in the menu bar.
   - Select "New µVision Project...".
   - Choose a directory and provide a name for your project.
   - Click "Save".

2. **Add Source Files**:
   - Right-click on your project in the "Project" window.
   - Select "Add New Item to Group 'Source Group 1'".
   - Choose the source files provided for your project and click "Add".
   - Repeat this step for each source file.

3. **Add Header Files**:
   - Right-click on your project in the "Project" window.
   - Select "Add Existing Files to Group 'Source Group 1'".
   - Choose the header files provided for your project and click "Add".
   - Repeat this step for each header file.

4. **Configure Target Device**:
   - Go to "Project" > "Options for Target...".
   - Select the "Target" tab.
   - Choose your target device from the drop-down menu under "Device".
   - Click "OK" to save the changes.

5. **Build the Project**:
   - Click on "Project" in the menu bar.
   - Select "Build Target" to compile your project.
   - Check the "Build Output" pane for any errors or warnings.

6. **Flash the Microcontroller**:
   - If your Keil project includes flashing capabilities, you can flash the microcontroller directly from Keil.
   - Otherwise, you can use external flashing tools provided by the microcontroller manufacturer.

These steps give you a clear path to setting up your Keil project and adding the provided files. You can then tweak GPIO settings and other configurations to match your specific STM32 microcontroller.

With this setup, you'll be able to easily implement UART communication, ADC conversion, and GPIO configuration. These are crucial for connecting sensors and sending data to your Python GUI application.
