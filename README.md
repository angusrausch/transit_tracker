# Brisbane Public Transport Dashboard

**Never miss your train or bus again.** This dashboard provides a real-time countdown for your favorite Translink stops, factoring in exactly how long it takes you to walk or cycle to the station.

## Features
* Real-time Tracking: Pulls live data from Translink.
* Personalized Buffers: Shows you exactly when you need to leave your front door.
* Multi-stop Support: Monitor trains, buses, and ferries simultaneously.

---

## Configuration

The dashboard is powered by a stops.json file. Create this file in the root directory to track your local stations.

### JSON Schema
```json
{
    "STOP_ID": {
        "name": "Custom Location Name",
        "time": 10
    }
}
```
| Key | Type | Description |
| :--- | :--- | :--- |
| STOP_ID | String | The official Translink ID (e.g., "000042" for Central Station). |
| name | String | A nickname for the stop (e.g., "Work," "Home," or "The Local"). |
| time | Integer | Minutes required to travel from your door to the platform. |

### Example stops.json

{
    "000042": {
        "name": "Central Station",
        "time": 8
    },
    "010452": {
        "name": "Cultural Centre Busway",
        "time": 5
    }
}

---

## How to find Stop IDs

Finding the correct ID is crucial for the dashboard to pull the right data:

1. Translink Website: Search for your stop on the Translink Timetable page. The Stop ID is usually a 6-digit number listed next to the station name.
2. Google Maps: Click on a transit icon (bus stop or train station). The 6-digit Stop ID is often listed in the Information sidebar.
3. Physical Stops: Most bus stop signs in Brisbane have the 6-digit ID printed at the bottom of the sign.

---

## Installation & Usage

1. Clone the repository.
2. Create your stops.json file.
3. Run the application.
    - Currently only terminal but will make a webpage

---

Note: This project is not affiliated with Translink or the Queensland Government. It uses publicly available transit data.