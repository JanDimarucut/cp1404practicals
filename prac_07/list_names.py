from kivy.app import App
from kivy.lang import Builder


class ListNames(App):
    def build(self):
        self.title = 'List of names'
        self.root = Builder.load_file("list_name.kv")
        return self.root

    def handle_press(self, button):
        # print("Pressed {}".format(button.text))
        self.root.ids.output_label.text = button.text


ListNames().run()
