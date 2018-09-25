from kivy.app import App
from kivy.lang import Builder


class TemperatureConverter(App):
    def build(self):
        self.title = 'Temperature Converter'
        self.root = Builder.load_file('convert_temp.kv')
        return self.root

    def calculate_celsius_to_fahrenheit(self):
        value = self.handle_error()
        fahrenheit = value * 9.0 / 5 + 32
        self.root.ids.output_label.text = "{} f".format(str(fahrenheit))

    def calculate_fahrenheit_to_celsius(self):
        value = self.handle_error()
        celsius = 5 / 9 * (value - 32)
        self.root.ids.output_label.text = "{} C".format(str(celsius))

    def handle_clear(self):
        self.root.ids.input_label.text = ''
        self.root.ids.output_label.text = ''

    def handle_increment(self, change):
        value = self.handle_error() + change
        self.root.ids.input_label.text = str(value)

    def handle_error(self):
        try:
            value = float(self.root.ids.input_label.text)
            return value
        except ValueError:
            return 0


TemperatureConverter().run()
