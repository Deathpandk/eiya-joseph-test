from cities.models import Distance

def get_distance(city_1, city_2):
    distance = Distance.objects.filter(city_1=city_1, city_2=city_2).first()
    if distance:
        return distance.distance
    distance = Distance.objects.filter(city_1=city_2, city_2=city_1).first()
    if distance:
        return distance.distance
    return None
