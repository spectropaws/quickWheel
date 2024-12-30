import threading
from main import WheelUI
from pynput import keyboard
from gi.repository import GLib, Gtk

class App:
    def __init__(self):
        self.wheel = WheelUI()

    def show_window(self):
        """Show the window."""
        GLib.idle_add(self.wheel.show)

    def hide_window(self):
        """Hide the window."""
        GLib.idle_add(self.wheel.hide)

def key_listener(app):
    """Listen for keybindings to show/hide the UI."""
    pressed_keys = set()

    def on_key_press(key):
        """Track pressed keys."""
        pressed_keys.add(key)

        # Show the window when Alt + Shift are pressed
        if keyboard.Key.alt in pressed_keys and keyboard.Key.shift in pressed_keys:
            app.show_window()
            print("Pressed keybinding: Showing window")

    def on_key_release(key):
        """Track released keys."""
        pressed_keys.discard(key)

        # Hide the window when Alt + Shift are released
        if keyboard.Key.alt not in pressed_keys or keyboard.Key.shift not in pressed_keys:
            app.hide_window()
            print("Released keybinding: Hiding window")

    # Using the listener in a non-blocking way
    listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
    listener.start()  # Start listener without blocking

if __name__ == "__main__":
    app = App()

    # Run the key listener in a separate thread
    listener_thread = threading.Thread(target=key_listener, args=(app,))
    listener_thread.daemon = True  # Daemon thread will exit when the main program exits
    listener_thread.start()

    Gtk.main()  # Start the GTK event loop in the main thread
