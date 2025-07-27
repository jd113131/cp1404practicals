"""Convert miles to kilometers using a GUI"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERTION_FACTOR = 1.609

class MilesToKmApp(App):
    distance_in_km = StringProperty()

    """MilesToKmApp is a kivy GUI for converting miles to kilometers"""
    def build(self):
        """build kivy app from kv file"""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.distance_in_km = ""
        return self.root

    def update_distance(self, distance_in_miles, increment_value):
        try:
            new_distance_miles = (int(distance_in_miles) + increment_value)
        except ValueError:
            new_distance_miles = increment_value
        self.root.ids.distance_miles.text = str(new_distance_miles)

    def convert(self, distance_in_miles):
        try:
            self.distance_in_km = str(float(distance_in_miles) * CONVERTION_FACTOR)
        except ValueError:
            self.distance_in_km = "0.0"

MilesToKmApp().run()
