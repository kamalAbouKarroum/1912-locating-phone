import requests

def get_location(mcc, mnc, lac, cell_id, api_key):
    url = f'http://opencellid.org/cell/get?key={api_key}&mcc={mcc}&mnc={mnc}&lac={lac}&cellid={cell_id}&format=json'
    response = requests.get(url)
    data = response.json()

    if 'lat' in data and 'lon' in data:
        return data['lat'], data['lon']
    else:
        return None

if __name__ == "__main__":
    print("""
           ████       ██████      ████      ██████ 
          ██ ██       ██  ██     ██ ██     ██    ██ 
         ██  ██       ██████    ██  ██          ██
             ██           ██        ██         ██ 
             ██           ██        ██        ██
             ██           ██        ██       ██
          ████████    ██████     ███████    ████████
			  Author: Kamal Abou Karroum | 1912

	===========================================================
			Instagram : @kamal_abou_karroum
	===========================================================
""")
    api_key = "YOUR_API_KEY"
    mcc = input("Enter MCC: ")
    mnc = input("Enter MNC: ")
    lac = input("Enter LAC: ")
    cell_id = input("Enter Cell ID: ")

    location = get_location(mcc, mnc, lac, cell_id, api_key)
    if location:
        print(f"The phone is approximately located at Latitude: {location[0]}, Longitude: {location[1]}")
    else:
        print("Location not found.")
