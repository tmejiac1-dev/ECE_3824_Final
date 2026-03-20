# Final Project: DoorUsage

## Project proposal

Three doorway in ENGR building people counter system with Cloud Database

## Project Overview

The goal of this project is to design a system that detects when people pass through a doorway, counts them, and sends the data to a cloud database.The goal of this Project is to design a hardware device which detects when people pass through a doorway.

---

## Data collection

The system will collect the following data:

### 1. **Person count**
The count will increase each time a persono passes through the doorway.

### 2. **Direction of movement**
The system could determine whether a person is entering or leaving if two sensors are used.

### 3. **Timestamp**
The time of each detection will be recorded

**Why we collected the data:**
- Monitoring foot traffic through a door base on the person count
- Determine the busy times of the day
- Push notifications about nearby events based on door usage data.
- We could using the data to estimating the building usage 

---

## HardWare

### 1. **ESP 32 development board**

ESP32 have built-in Wi-Fi and bluetooth model which can send data to the cloud.

### 2. ** IR Beam Sensor(single or double per door)**

Used to detect when a person passes through the door. Double sensors allow direction detection

### 3. **Power Suppy**

Power for ESP32 and sensors.

### 4. **Jumpwires and breadboard**

Use for wiring the system.

---

## Frontend

### Dashboard

**The dashboaed will allow the user to:**
- view the current people count for each door
- see the total number of entries and exit(if two sensors are used)
- see the charts of people count over time
- monitor busy time periods of the day

### Posible futures

- door usage history(daily or weekly graphs)
- alert when the people count exceeds a threshold in hour
- If possible, display information about nearby foodtruck, shop, and public transportation for each gate.

---