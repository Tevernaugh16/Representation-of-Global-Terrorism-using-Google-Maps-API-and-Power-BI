import gmplot
import sqlite3

# Connect to the database
conn = sqlite3.connect('terrorDB.sqlite')

#Set the cursor
c = conn.cursor()

# Execute the database query. I am fetching business locations in a particular zip.
c.execute("SELECT latitude, longitude, country_txt, city, provstate, attacktype, year FROM TerrorAll WHERE year = '1994';")

# Fetch all the data returned by the database query as a list
lat_long = c.fetchall()


# Initialize two empty lists to hold the latitude and longitude values
latitude = []
longitude = []
country = []
city = []
state = []
attack = []
date = []

# Transform the the fetched latitude and longitude data into two separate lists
for i in range(len(lat_long)):
	latitude.append(lat_long[i][0])
	longitude.append(lat_long[i][1])
	country.append(lat_long[i][2])
	city.append(lat_long[i][3])
	state.append(lat_long[i][4])
	attack.append(lat_long[i][5])
	date.append(lat_long[i][6])

#function for drawing points on a map
def points():

    gmap = gmplot.GoogleMapPlotter("31.7917", "-7.0926",3.1)

    n = 0
    for i in latitude:
        if "Assassination" in attack[n]:
            gmap.marker(latitude[n], longitude[n],'y', title = attack[n] +': ' + date[n] +'. '+ city[n] + ', '+ country[n])
            n+=1

        elif "Hostage Taking (Kidnapping)" in attack[n] or "Hostage Taking (Barricade Incident)" in attack[n]:
            gmap.marker(latitude[n], longitude[n],'b', title = attack[n] +': ' + date[n] +'. '+ city[n] + ', '+ country[n])
            n+=1

        elif "Bombing/Explosion" in attack[n]:
            gmap.marker(latitude[n], longitude[n],'g', title = attack[n] +': ' + date[n] +'. '+ city[n] + ', '+ country[n])
            n+=1

        elif "Facility/Infrastructure Attack" in attack[n]:
            gmap.marker(latitude[n], longitude[n],'r', title = attack[n] +': ' + date[n] +'. '+ city[n] + ', '+ country[n])
            n+=1

        elif "Armed Assault" in attack[n]:
            gmap.marker(latitude[n], longitude[n],'m', title = attack[n] +': ' + date[n] +'. '+ city[n] + ', '+ country[n])
            n+=1

        elif "Hijacking" in attack[n]:
            gmap.marker(latitude[n], longitude[n],'k', title = attack[n] +': ' + date[n] +'. '+ city[n] + ', '+ country[n])
            n+=1

        elif "Unarmed Assault" in attack[n]:
            gmap.marker(latitude[n], longitude[n],'c', title = attack[n] +': ' + date[n] +'. '+ city[n] + ', '+ country[n])
            n+=1

        elif "Unknown" in attack[n]:
            gmap.marker(latitude[n], longitude[n],'w', title = attack[n] +': ' + date[n] +'. '+ city[n] + ', '+ country[n])
            n+=1

        gmap.draw('map.html')
    return;

#function for drawing heatmap
def heatMap():
		# Initialize the map to the first location in the list
		gmap = gmplot.GoogleMapPlotter("31.7917", "-7.0926",3.1)

		# Draw the points on the map.
		gmap.heatmap(latitude, longitude)

		# Write the map in an HTML file
		gmap.draw('map2.html')
		return;


points()
heatMap()