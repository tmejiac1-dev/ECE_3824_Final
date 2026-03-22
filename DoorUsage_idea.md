# Final Project: Door Usage

## Project Proposal

A people counting system for three doorways in the ENGR building using a cloud database.

## Project Overview

The goal of this project is to design a system that detects when people pass through a doorway and sends the data to a cloud database. The system focuses on reliable detection and data logging rather than complex sensor behavior.

---

## Data Collection

The system will collect the following data:

### 1. **Person Count**
The count will increase each time a person passes through the doorway.

### 2. **Timestamp**
The time of each event will be recorded.

**Why this data is collected:**
- Monitor foot traffic through a door using person count
- Determine busy times of the day
- Enable simple notifications based on door usage data
- Estimate building usage

---

## Hardware

### 1. **ESP32 Development Board**

ESP32 has built-in Wi-Fi and Bluetooth modules which can send data to the cloud.

### 2. **IR Beam Sensor**

Used to detect when a person passes through the door.

### 3. **Power Supply**

Provides power for ESP32 and sensors.

### 4. **Jumper Wires and Breadboard**

Used for wiring the system.

---

## Frontend

### Dashboard

**The dashboard will allow the user to:**
- View the current people count for each door
- View charts of people count over time
- Monitor busy time periods

### Possible Features

- Door usage history (daily or weekly graphs)
- Alerts when the count exceeds a threshold per hour
- Display nearby information such as food trucks, shops, and transportation

---