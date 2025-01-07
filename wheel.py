import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class Wheel:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("mainui.glade")
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("MainWindow")
        self.buttonTopLeft = self.builder.get_object("ButtonTopLeft")

        self.window.set_decorated(False)
        self.window.set_keep_above(True)
        self.enable_transparency()

        self.window.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)

        self.window.connect("destroy", Gtk.main_quit)
        # self.window.connect("focus-out-event", self.on_focus_out)
        
        self.buttonTopLeft.connect("clicked", self.button_clicked)
        # self.window.connect("button-press-event", Gtk.main_quit)

    def enable_transparency(self):
        # Set the window as app-paintable
        self.window.set_app_paintable(True)

        # Set a transparent visual
        screen = self.window.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.window.set_visual(visual)
        else:
            print("Transparency not supported. Ensure compositor is running.")

        # Apply CSS for transparency
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(b"""
        window {
            background-color: rgba(0, 0, 0, 0); /* Fully transparent */
        }
        """)
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )


    def on_focus_out(self, widget, event):
        print("Focus lost. Destroying window.")
        widget.destroy()

    def button_clicked(self, widget, event):
        print("Button clicked!");


    def show(self):
        self.window.show_all()

    def hide(self):
        self.window.hide()

    def close(self):
        Gtk.main_quit()


if __name__ == "__main__":
    app = WheelUI()
    app.show()
    Gtk.main()

