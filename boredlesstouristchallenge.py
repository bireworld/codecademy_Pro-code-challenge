destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt" ]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_destination_index(destination):
  #for destination in destinations:
  destination_index = destinations.index(destination)
  return destination_index

print(get_destination_index("São Paulo, Brazil"))  
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index 
test_destination_index = get_traveler_location(test_traveler) 
print(test_destination_index)

attractions = [[], [], [], [], []]
print(attractions)
def add_attraction(destination,attraction):
  destination_index = get_destination_index(destination)
  if destination in destinations:
  #print(destination_index)
    try:
      destination_index = get_destination_index(destination)
    except ValueError:
      return "ValueError caught"
    #print("ValueError caught")
  attractions_for_destination = attractions[destination_index]
  #print(attractions_for_destination)

  attractions_for_destination = attractions_for_destination.append(attraction)
  return attractions_for_destination
  #print(attractions_for_destination)
add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
print (attractions)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    #print("length of attractions_in_city: " + str(len(attractions_in_city)))
    attractions_with_interest = []
    for possible_attraction in range(len(attractions_in_city)):
        attraction = attractions_in_city[possible_attraction]
        attraction_tags = attractions_in_city[possible_attraction][1]
        #print("Stored in attraction_tags at index " +str(possible_attraction)+": " + str(attraction_tags))
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(attraction[0])
    return attractions_with_interest
la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination,traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + " " + traveler_destination
  for attraction in traveler_attractions:
    interests_string += " " + attraction + " "
  return interests_string
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
  



    
