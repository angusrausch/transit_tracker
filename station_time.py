import time
import requests
from google.transit import gtfs_realtime_pb2
import traceback
import json

# The SEQ Trip Updates endpoint
URL = "https://gtfsrt.api.translink.com.au/api/realtime/SEQ/TripUpdates"


def get_stops(file_name: str = "stations.json"):
    with open(file_name, 'r') as file:
        contents = json.load(file)
    return { int(k): v for k, v in contents.items() }

def get_arrival_times(stops):
    feed = gtfs_realtime_pb2.FeedMessage()
    now = time.time()

    try:
        print(f"Refreshing live arrivals...")
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        feed.ParseFromString(response.content)

        arrivals = []
        
        for entity in feed.entity:
            if entity.HasField('trip_update'):
                trip = entity.trip_update.trip
                route_id = trip.route_id
                
                for stop_update in entity.trip_update.stop_time_update:
                    if int(stop_update.stop_id) in stops:
                        ts = stop_update.arrival.time or stop_update.departure.time
                        
                        if ts > now:

                            transport_type = "Train" if any(c.isalpha() for c in route_id) else "Bus"
                            
                            try:
                                stop = stops[int(stop_update.stop_id)]
                            except KeyError:
                                stop = stop_update.stop_id

                            due_to_time = int((ts - now) / 60) 
                            time_to_leave = due_to_time - stop["time"]


                            arrivals.append({
                                'type': transport_type,
                                'stop': stop['name'],
                                'route': route_id.split("-")[0],
                                'time': due_to_time,
                                'time_to_leave': time_to_leave
                            })

        # Sort arrivals and remove any that will miss
        arrivals = [x for x in arrivals if x['time_to_leave'] >= 0]
        arrivals.sort(key=lambda x: x['time_to_leave'])
        return arrivals
    except Exception as e:
        traceback.print_exc()
        exit()

def print_arrivals(arrivals):
    print(f"{'Leave In':<8} | {'Due':<12} | {'Mode':<8} | {'Route':<6} | {'Location'}")
    print("-" * 80)
    
    for item in arrivals[:20]:
        time_display = f"{item['time'] } mins" if item['time']  > 0 else "Due Now"
        
        print(f"{item['time_to_leave']:<8} | {time_display:<12} | {item['type']:<8} | {item['route']:<6} | {item['stop']}")
        
    if not arrivals:
        print("No live data found. Note: Buses without GPS tracking won't appear.")

if __name__ == "__main__":
    stops = get_stops()
    arrivals = get_arrival_times(stops)
    print_arrivals(arrivals)