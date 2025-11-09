import arcade, arcade.gui

from utils.constants import CUSTOM_DIFFICULTY_SETTINGS, slider_style, button_style
from utils.preload import button_texture, button_hovered_texture

class CustomDifficulty(arcade.gui.UIView):
    def __init__(self, pypresence_client):
        super().__init__()

        self.pypresence_client = pypresence_client
        self.anchor = self.add_widget(arcade.gui.UIAnchorLayout(size_hint=(1, 1)))
        self.box = self.anchor.add(arcade.gui.UIBoxLayout(size_between=self.window.height / 10), anchor_x="center", anchor_y="top")

        self.custom_settings = {}
        self.custom_setting_labels = {}

    def set_custom_setting(self, key, value):
        value = int(value)
        self.custom_settings[key] = value
        self.custom_setting_labels[key].text = f"{next(setting_list[1] for setting_list in CUSTOM_DIFFICULTY_SETTINGS if setting_list[0] == key)}: {value}"

    def on_show_view(self):
        super().on_show_view()

        self.box.add(arcade.gui.UILabel(text="Custom Difficulty Selector", font_size=32))
        self.box.add(arcade.gui.UISpace(height=self.window.height / 20))

        for custom_setting_key, custom_setting_name, min_value, max_value in CUSTOM_DIFFICULTY_SETTINGS:
            self.custom_settings[custom_setting_key] = int((max_value - min_value) / 2)
            self.custom_setting_labels[custom_setting_key] = self.box.add(arcade.gui.UILabel(text=f"{custom_setting_name}: {int((max_value - min_value) / 2)}", font_size=28))
            
            slider = self.box.add(arcade.gui.UISlider(step=1, min_value=min_value, max_value=max_value, value=int((max_value - min_value) / 2), style=slider_style, width=self.window.width / 2, height=self.window.height / 15))
            slider._render_steps = lambda surface: None
            slider.on_change = lambda event, key=custom_setting_key: self.set_custom_setting(key, event.new_value)

        self.play_button = self.anchor.add(arcade.gui.UITextureButton(text="Play", style=button_style, texture=button_texture, texture_hovered=button_hovered_texture, width=self.window.width / 2, height=self.window.height / 10), anchor_x="center", anchor_y="bottom")
        self.play_button.on_click = lambda event: self.play()

    def play(self):
        from game.play import Game
        self.window.show_view(Game(self.pypresence_client, self.custom_settings["size"], self.custom_settings["source_count"], self.custom_settings["house_count"]))
