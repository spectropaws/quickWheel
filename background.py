import gi
import threading
from pynput import keyboard

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class BackgroundApp:
    def __init__(self):
        # Create the GTK window
        self.window = Gtk.Window(title="Background App")
        self.window.set_default_size(400, 300)
        self.window.connect("destroy", Gtk.main_quit)

        # Remove the window's title bar (no close, minimize, or maximize buttons)
        self.window.set_decorated(False)

        # Set the window to always stay on top
        self.window.set_keep_above(True)

        # Add a simple label
        label = Gtk.Label(label="Hello! Press and hold Alt + Shift to show me.")
        self.window.add(label)
        self.window.hide()  # Start hidden

    def show_window(self):
        """Show the window."""
        self.window.show_all()

    def hide_window(self):
        """Hide the window."""
        self.window.hide()

def key_listener(app):
    """Listen for keybindings to show/hide the UI."""
    pressed_keys = set()

    def on_key_press(key):
        """Track pressed keys."""
        pressed_keys.add(key)

        # Show the window when Alt + Shift are pressed
        if keyboard.Key.alt in pressed_keys and keyboard.Key.shift in pressed_keys:
            app.show_window()

    def on_key_release(key):
        """Track released keys."""
        pressed_keys.discard(key)

        # Hide the window when Alt + Shift are released
        if keyboard.Key.alt not in pressed_keys or keyboard.Key.shift not in pressed_keys:
            app.hide_window()

    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()

if __name__ == "__main__":
    app = BackgroundApp()

    # Run the key listener in a separate thread
    listener_thread = threading.Thread(target=key_listener, args=(app,), daemon=True)
    listener_thread.start()

    # Run the GTK main loop
    Gtk.main()
