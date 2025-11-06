import arcade.gui, arcade

button_texture = arcade.gui.NinePatchTexture(64 // 4, 64 // 4, 64 // 4, 64 // 4, arcade.load_texture("assets/graphics/button.png"))
button_hovered_texture = arcade.gui.NinePatchTexture(64 // 4, 64 // 4, 64 // 4, 64 // 4, arcade.load_texture("assets/graphics/button_hovered.png"))

vertical_connected = arcade.load_texture("assets/graphics/connected_lines/line/vertical.png")
horizontal_connected = arcade.load_texture("assets/graphics/connected_lines/line/horizontal.png")
left_bottom_connected = arcade.load_texture("assets/graphics/connected_lines/corner/left_bottom.png")
left_top_connected = arcade.load_texture("assets/graphics/connected_lines/corner/left_top.png")
right_bottom_connected = arcade.load_texture("assets/graphics/connected_lines/corner/right_bottom.png")
right_top_connected = arcade.load_texture("assets/graphics/connected_lines/corner/right_top.png")

vertical_unconnected = arcade.load_texture("assets/graphics/unconnected_lines/line/vertical.png")
horizontal_unconnected = arcade.load_texture("assets/graphics/unconnected_lines/line/horizontal.png")
left_bottom_unconnected = arcade.load_texture("assets/graphics/unconnected_lines/corner/left_bottom.png")
left_top_unconnected = arcade.load_texture("assets/graphics/unconnected_lines/corner/left_top.png")
right_bottom_unconnected = arcade.load_texture("assets/graphics/unconnected_lines/corner/right_bottom.png")
right_top_unconnected = arcade.load_texture("assets/graphics/unconnected_lines/corner/right_top.png")