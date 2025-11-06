import arcade.gui, arcade

button_texture = arcade.gui.NinePatchTexture(64 // 4, 64 // 4, 64 // 4, 64 // 4, arcade.load_texture("assets/graphics/button.png"))
button_hovered_texture = arcade.gui.NinePatchTexture(64 // 4, 64 // 4, 64 // 4, 64 // 4, arcade.load_texture("assets/graphics/button_hovered.png"))

vertical_powered = arcade.load_texture("assets/graphics/powered_lines/line/vertical.png")
horizontal_powered = arcade.load_texture("assets/graphics/powered_lines/line/horizontal.png")
left_bottom_powered = arcade.load_texture("assets/graphics/powered_lines/corner/left_bottom.png")
left_top_powered = arcade.load_texture("assets/graphics/powered_lines/corner/left_top.png")
right_bottom_powered = arcade.load_texture("assets/graphics/powered_lines/corner/right_bottom.png")
right_top_powered = arcade.load_texture("assets/graphics/powered_lines/corner/right_top.png")

vertical_unpowered = arcade.load_texture("assets/graphics/unpowered_lines/line/vertical.png")
horizontal_unpowered = arcade.load_texture("assets/graphics/unpowered_lines/line/horizontal.png")
left_bottom_unpowered = arcade.load_texture("assets/graphics/unpowered_lines/corner/left_bottom.png")
left_top_unpowered = arcade.load_texture("assets/graphics/unpowered_lines/corner/left_top.png")
right_bottom_unpowered = arcade.load_texture("assets/graphics/unpowered_lines/corner/right_bottom.png")
right_top_unpowered = arcade.load_texture("assets/graphics/unpowered_lines/corner/right_top.png")

power_source = arcade.load_texture("assets/graphics/power_source.png")
