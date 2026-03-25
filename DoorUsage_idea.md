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
- Collecting both Person count and Timestamp allows us to interpret
  the data in many ways.

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
## Backend
The backend will be responsible for receiving the data from the ESP32 and
storing it in a cloud database.

### How it works
- When the IR sensor detects a person passing thorugh the door, the ESP32
  will then send a JSON file to the cloud server and increment the person
  count.
- The server will receive the data and will store it in a MongoDB database
- Each transport of data or JSON file will have the follwing: door ID, updated
  count, and timestamp.
  
## Frontend

### Dashboard

**The dashboard will allow the user to:**
- View the current people count for each door
- View charts of people count over time
- Monitor busy time periods

### Possible Features

- Door usage history (daily or weekly graphs)
- Alerts when the count exceeds a threshold per hour
- Other meta-data such as: average count per doorway (per day, week, month), most popular doorway,
  highest and lowest count per hour of each, etc.
- Display nearby information such as food trucks, shops, and transportation

---
