from kivy.app import App
from kivy.lang import Builder


class GradeDecider(App):
    def build(self):
        self.title = "Grade Decider"
        self.root = Builder.load_file('grade_decider.kv')
        return self.root

    def handle_grades(self, value):
        print("calculate pressed")
        # value = self.handle_errors()

        if 100 >= value >= 90:
            self.root.ids.output_label.text = "High Distinction"

        elif 90 > value >= 75:
            self.root.ids.output_label.text = "Distinction"

        elif 75 > value >= 65:
            self.root.ids.output_label.text = "Credit"

        else:
            self.root.ids.output_label.text = "N/A"


    # def handle_errors(self):
    #     try:
    #         value = self.root.ids.input_label.text
    #         return value
    #
    #     except ValueError:
    #         return "Invalid input, enter a number between 0 and 100"

    def handle_clear(self):
        self.root.ids.input_label.text = ''
        self.root.ids.output_label.text = ''


GradeDecider().run()