from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
# from kivy.lang import Builder

 


class MyWidget(BoxLayout):
    label_text = StringProperty("Hello, World!")

    def update_label(self):
        self.label_text = "Button Clicked!"

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == "__main__":
    MyApp().run()
