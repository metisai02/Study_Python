travel_log =
{
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

def add_new_country(Country,times,cities):
    new_country = {}
    new_country["Country"] = Country
    new_country["visited"] = times
    new_country["cities"] = cities
    travel_log.append(new_country)
    

