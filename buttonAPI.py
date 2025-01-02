import json
import os

CONFIG_FILE = "buttonConfig.json"

class ButtonConfigManager:
    def __init__(self):
        if not os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "w") as f:
                json.dump({}, f)

    def set_button_config(self, button_id, name, icon_path, command):
        """Set the configuration for a button."""
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)

        config[button_id] = {
            "name": name,
            "icon": icon_path,
            "command": command
        }

        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)

    def get_button_config(self, button_id):
        """Get the configuration for a button."""
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
        return config.get(button_id, None)


if __name__ == "__main__":
    manager = ButtonConfigManager()

    manager.set_button_config("button1", "Button One", "/path/to/icon1.png", "command1")
    manager.set_button_config("button2", "Button Two", "/path/to/icon2.png", "command2")
    manager.set_button_config("button3", "Button Three", "/path/to/icon3.png", "command3")
    manager.set_button_config("button4", "Button Four", "/path/to/icon4.png", "command4")


    print("Config for button1:", manager.get_button_config("button1"))
    print("Config for button2:", manager.get_button_config("button2"))
    print("Config for button3:", manager.get_button_config("button3"))
    print("Config for button4:", manager.get_button_config("button4"))
