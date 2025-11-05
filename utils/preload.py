import arcade.gui, arcade

button_texture = arcade.gui.NinePatchTexture(64 // 4, 64 // 4, 64 // 4, 64 // 4, arcade.load_texture("assets/graphics/button.png"))
button_hovered_texture = arcade.gui.NinePatchTexture(64 // 4, 64 // 4, 64 // 4, 64 // 4, arcade.load_texture("assets/graphics/button_hovered.png"))

vertical_connected = arcade.load_texture("assets/graphics/connected_lines/vertical.png")
horizontal_connected = arcade.load_texture("assets/graphics/connected_lines/horizontal.png")

vertical_unconnected = arcade.load_texture("assets/graphics/unconnected_lines/vertical.png")
horizontal_unconnected = arcade.load_texture("assets/graphics/unconnected_lines/horizontal.png")