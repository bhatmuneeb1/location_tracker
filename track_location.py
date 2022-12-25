import geoip2.database

# Print a banner with your name and the text "created by"
print('\n'.join(['', ' created by Muneeb Amin Bhat ', '', '=' * 30]))

# Create a reader object
reader = geoip2.database.Reader('path/to/GeoLite2-City.mmdb')

# Prompt the user to enter an IP address
ip_address = input('Enter an IP address: ')

# Look up the location of the IP address
response = reader.city(ip_address)

# Print the location information
print(f'Country: {response.country.name}')
print(f'City: {response.city.name}')
print(f'Latitude: {response.location.latitude}')
print(f'Longitude: {response.location.longitude}')

# Close the reader
reader.close()
