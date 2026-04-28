# -Smart-Disaster-Project
# Smart Disaster Relief Management System

## 📌 Overview
The Smart Disaster Relief Management System is designed to streamline the process of managing relief camps and victims during disaster situations. It provides a centralized platform to track resources, register victims, and allocate support efficiently.

---

## 🚀 Features

### Relief Camp Management
- **Add Camp**: Create new relief camps with details.
- **Camp Details**:
  - Camp ID
  - Location
  - Capacity
  - Food Packets
  - Medical Kits
  - Volunteers
- **Occupied**: Tracks the number of victims currently assigned.
- **Refresh Camps**: Updates and displays the latest camp list.

### Victim Registration
- **Register Victim**: Add new victims to the system.
- **Victim Details**:
  - Victim ID
  - Name
  - Age
  - Health Condition (Normal / Critical / Injured)
  - Assigned Camp ID
- **Refresh Victims**: Updates and displays the latest victim list.
- **Search Victim**: Find victims by their ID.

---

## 🔄 Suggested Enhancements
- **Automatic Allocation**: Assign victims to camps based on available capacity and resources.
- **Resource Tracking**: Update food packets and medical kits as victims are registered.
- **Health Prioritization**: Flag critical victims for immediate medical attention.
- **Volunteer Assignment**: Distribute volunteers across camps based on occupancy.
- **Dashboard View**: Provide overall statistics (total camps, victims, resources).

---

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS, JavaScript (or React/Angular if extended)
- **Backend**: Node.js / Python / Java (depending on implementation)
- **Database**: MySQL / PostgreSQL / MongoDB
- **Hosting**: Cloud-based deployment (Azure, AWS, or GCP)

---

## 📂 Database Schema (Example)

### ReliefCamps Table
| CampID | Location | Capacity | FoodPackets | MedicalKits | Volunteers | Occupied |
|--------|----------|----------|-------------|-------------|------------|----------|

### Victims Table
| VictimID | Name | Age | HealthCondition | CampID |
|----------|------|-----|-----------------|--------|

---

##  Usage
1. **Add Relief Camp** → Enter camp details and save.
2. **Register Victim** → Enter victim details and assign to a camp.
3. **View Camps** → Monitor resources and occupancy.
4. **View Victims** → Track health conditions and camp assignments.
5. **Search Victim** → Quickly locate victims by ID.

## 📌 Future Scope
- Integration with GIS for real-time camp location mapping.
- SMS/WhatsApp notifications for victims and volunteers.
- AI-based prediction for resource needs.
- Multi-language support for accessibility.



## 📜 License
This project is licensed under the MIT License – feel free to use and modify.
