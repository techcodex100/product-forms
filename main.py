from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        layout = MDBoxLayout(orientation='vertical', padding=40, spacing=20)

        self.text_field = MDTextField(
            hint_text="Write anything here...",
            helper_text="Whatever you write, on pressing the button it will be printed below",
            helper_text_mode="on_focus",
        )

        self.button = MDRaisedButton(
            text="Print",
            pos_hint={"center_x": 0.5},
            on_release=self.print_text
        )

        self.label = MDLabel(
            text="output",
            halign="center",
            theme_text_color="Primary"
        )

        layout.add_widget(self.text_field)
        layout.add_widget(self.button)
        layout.add_widget(self.label)
        return layout

    def print_text(self, instance):
        self.label.text = self.text_field.text

if __name__ == "__main__":
    MainApp().run()
