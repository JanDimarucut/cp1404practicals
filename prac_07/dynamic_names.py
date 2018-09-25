from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetApps(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.records = {"Bob Smith": "45", "John Doe": "30", "Mike Brox": "27", "Peter Jackson": "33"}

    def build(self):
        self.title = "List of names"
        self.root = Builder.load_file('dynamic_names.kv')
        self.handle_buttons()
        return self.root

    def handle_buttons(self):
        for name in self.records:
            temp_button = Button(text=name, id=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.input_label.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        self.status_text = self.records[name]


DynamicWidgetApps().run()
