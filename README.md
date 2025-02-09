# Intelligent Driving System for Agricultural Vehicles

## What?
The **Intelligent Driving System for Agricultural Vehicles** is designed to enhance automation in agricultural machinery, focusing on improving precision, safety, and efficiency in farming operations. Developed in collaboration with John Deere, the system integrates embedded computing, real-time processing, and automation to assist or autonomously operate tractors in agricultural tasks.<br><br>

## How?
The system is built around an **STM32 microcontroller**, which serves as the core processing unit for collecting, analyzing, and transmitting data. Using **RTOS (Real-Time Operating System)**, tasks such as sensor data processing, motor control, and communication are managed efficiently, ensuring precise execution of operations.<br><br>

The system employs multiple input devices, including **potentiometers, a matrix keypad, and push buttons**, which act as controls for managing the tractor’s movements and functions. A **display LCD** provides real-time feedback, showing important parameters such as speed, position, and operational status.<br><br>

For data visualization, a **Raspberry Pi 4** is integrated to process and display historical and real-time data. The Raspberry Pi receives information via **serial communication** from the STM32 and utilizes **Python-based visualization tools (Matplotlib, Tkinter, Pandas, Seaborn)** to present insights on tractor performance.<br><br>

To ensure efficient hardware interaction, the **STM32 microcontroller** makes use of **UART for serial communication, GPIO for sensor interfacing, and ADC for precise analog data acquisition**. The system is programmed in **C and Python** using **STM32 IDE**, and communication with external systems is managed using **Putty and VNC Viewer** for remote monitoring and control.<br><br>

### Implementation Phases
- **Conceptualization**: Reviewing John Deere’s requirements and defining system architecture.<br>
- **Prototyping**: Developing individual modules, testing hardware components, and verifying data collection methods.<br>
- **Final Implementation**: Integrating all modules into a fully functional system with real-time data processing and control mechanisms.<br><br>

## Results
- **Increased Precision**: The system ensures accurate depth and spacing in seed planting, optimizing crop yield.<br>
- **Enhanced Safety**: Automating certain tasks reduces operator fatigue and exposure to harsh environmental conditions.<br>
- **Improved Efficiency**: The real-time monitoring and control system streamlines agricultural operations, reducing human intervention.<br>
- **Scalability**: The modular design allows for future enhancements, such as AI-based decision-making and additional sensor integration.<br><br>

This project represents a significant advancement in **agricultural automation**, showcasing how embedded systems and real-time computing can optimize farming efficiency while ensuring sustainability and safety.

