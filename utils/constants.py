import arcade.color
from arcade.types import Color
from arcade.gui.widgets.buttons import UITextureButtonStyle, UIFlatButtonStyle
from arcade.gui.widgets.slider import UISliderStyle

CUSTOM_DIFFICULTY_SETTINGS = [
    ["source_count", "Source Count", 1, 20],
    ["house_count", "House Count", 1, 20],
    ["size", "Size", 3, 30]
]

ROTATIONS =  {
    "line": ["vertical", "horizontal"],
    "corner": ["right_bottom", "left_bottom", "left_top", "right_top"],
    "t_junction": ["top_bottom_right", "left_right_bottom", "top_bottom_left", "left_right_top"],
    "cross": ["cross"]
}

NEIGHBOURS = {
    "vertical": {"b", "t"},
    "horizontal": {"l", "r"},
    "left_bottom": {"l", "b"},
    "right_bottom": {"r", "b"},
    "left_top": {"l", "t"},
    "right_top": {"r", "t"},
    "top_bottom_right": {"t", "b", "r"},
    "top_bottom_left": {"t", "b", "l"},
    "left_right_bottom": {"l", "r", "b"},
    "left_right_top": {"l", "r", "t"},
    "cross": {"l", "r", "t", "b"}
}

DIRECTIONS = {"t": (0, -1, "b"), "b": (0, 1, "t"), "l": (-1, 0, "r"), "r": (1, 0, "l")}

menu_background_color = (30, 30, 47)
log_dir = 'logs'
discord_presence_id = 1435687634960777266

button_style = {'normal': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK), 'hover': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK),
                'press': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK), 'disabled': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK)}
big_button_style = {'normal': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, font_size=26), 'hover': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, font_size=26),
                'press': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, font_size=26), 'disabled': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, font_size=26)}

dropdown_style = {'normal': UIFlatButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, bg=Color(128, 128, 128)), 'hover': UIFlatButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, bg=Color(49, 154, 54)),
                  'press': UIFlatButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, bg=Color(128, 128, 128)), 'disabled': UIFlatButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, bg=Color(128, 128, 128))}

slider_default_style = UISliderStyle(bg=Color(128, 128, 128), unfilled_track=Color(128, 128, 128), filled_track=Color(49, 154, 54))
slider_hover_style = UISliderStyle(bg=Color(49, 154, 54), unfilled_track=Color(128, 128, 128), filled_track=Color(49, 154, 54))

slider_style = {'normal': slider_default_style, 'hover': slider_hover_style, 'press': slider_hover_style, 'disabled': slider_default_style}

settings = {
    "Graphics": {
        "Window Mode": {"type": "option", "options": ["Windowed", "Fullscreen", "Borderless"], "config_key": "window_mode", "default": "Windowed"},
        "Resolution": {"type": "option", "options": ["1366x768", "1440x900", "1600x900", "1920x1080", "2560x1440", "3840x2160"], "config_key": "resolution"},
        "Anti-Aliasing": {"type": "option", "options": ["None", "2x MSAA", "4x MSAA", "8x MSAA", "16x MSAA"], "config_key": "anti_aliasing", "default": "4x MSAA"},
        "VSync": {"type": "bool", "config_key": "vsync", "default": True},
        "FPS Limit": {"type": "slider", "min": 0, "max": 480, "config_key": "fps_limit", "default": 60},
    },
    "Sound": {
        "SFX": {"type": "bool", "config_key": "sfx", "default": True},
        "SFX Volume": {"type": "slider", "min": 0, "max": 100, "config_key": "sfx_volume", "default": 50},
    },
    "Miscellaneous": {
        "Discord RPC": {"type": "bool", "config_key": "discord_rpc", "default": True},
    },
    "Credits": {}
}
settings_start_category = "Graphics"
