class Hill:
    def __init__(self, name, height, area, image_path="default", id=None) -> None:
        self.name = name
        self.height = height
        self.area = area
        self.image_path = image_path
        self.id = id