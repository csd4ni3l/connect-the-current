import arcade.gui, arcade

button_texture = arcade.gui.NinePatchTexture(64 // 4, 64 // 4, 64 // 4, 64 // 4, arcade.load_texture("assets/graphics/button.png"))
button_hovered_texture = arcade.gui.NinePatchTexture(64 // 4, 64 // 4, 64 // 4, 64 // 4, arcade.load_texture("assets/graphics/button_hovered.png"))

wire_sound_effect = arcade.Sound("assets/sound/wire.mp3")

TEXTURE_MAP = {
    ("line", "vertical", True): arcade.load_texture("assets/graphics/powered_lines/line/vertical.png"),
    ("line", "vertical", False): arcade.load_texture("assets/graphics/unpowered_lines/line/vertical.png"),
    
    ("line", "horizontal", True): arcade.load_texture("assets/graphics/powered_lines/line/horizontal.png"),
    ("line", "horizontal", False): arcade.load_texture("assets/graphics/unpowered_lines/line/horizontal.png"),

    ("corner", "left_bottom", True): arcade.load_texture("assets/graphics/powered_lines/corner/left_bottom.png"),
    ("corner", "left_bottom", False): arcade.load_texture("assets/graphics/unpowered_lines/corner/left_bottom.png"),
    
    ("corner", "left_top", True): arcade.load_texture("assets/graphics/powered_lines/corner/left_top.png"),
    ("corner", "left_top", False): arcade.load_texture("assets/graphics/unpowered_lines/corner/left_top.png"),
    
    ("corner", "right_bottom", True): arcade.load_texture("assets/graphics/powered_lines/corner/right_bottom.png"),
    ("corner", "right_bottom", False): arcade.load_texture("assets/graphics/unpowered_lines/corner/right_bottom.png"),
    
    ("corner", "right_top", True): arcade.load_texture("assets/graphics/powered_lines/corner/right_top.png"),
    ("corner", "right_top", False): arcade.load_texture("assets/graphics/unpowered_lines/corner/right_top.png"),

    ("t_junction", "left_right_bottom", True): arcade.load_texture("assets/graphics/powered_lines/t_junction/left_right_bottom.png"),
    ("t_junction", "left_right_bottom", False): arcade.load_texture("assets/graphics/unpowered_lines/t_junction/left_right_bottom.png"),
    
    ("t_junction", "left_right_top", True): arcade.load_texture("assets/graphics/powered_lines/t_junction/left_right_top.png"),
    ("t_junction", "left_right_top", False): arcade.load_texture("assets/graphics/unpowered_lines/t_junction/left_right_top.png"),
    
    ("t_junction", "top_bottom_left", True): arcade.load_texture("assets/graphics/powered_lines/t_junction/top_bottom_left.png"),
    ("t_junction", "top_bottom_left", False): arcade.load_texture("assets/graphics/unpowered_lines/t_junction/top_bottom_left.png"),
    
    ("t_junction", "top_bottom_right", True): arcade.load_texture("assets/graphics/powered_lines/t_junction/top_bottom_right.png"),
    ("t_junction", "top_bottom_right", False): arcade.load_texture("assets/graphics/unpowered_lines/t_junction/top_bottom_right.png"),

    ("cross", "cross", True): arcade.load_texture("assets/graphics/powered_lines/cross/cross.png"),
    ("cross", "cross", False): arcade.load_texture("assets/graphics/unpowered_lines/cross/cross.png"),

    ("power_source", "cross", True): arcade.load_texture("assets/graphics/power_source.png"),

    ("house", "cross", True): arcade.load_texture("assets/graphics/powered_lines/cross/cross.png"),
    ("house", "cross", False): arcade.load_texture("assets/graphics/unpowered_lines/cross/cross.png"),
}
