class Hill:
    def __init__(
        self, name, height, area, image_path="default", route_link=None, weather_path=None, id=None
    ) -> None:
        self.name = name
        self.height = height
        self.area = area
        self.image_path = image_path
        self.route_link = route_link
        self.weather_path = weather_path
        self.id = id
