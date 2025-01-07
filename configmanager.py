import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ConfigManager:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("ApplicationWindow.glade")

        self.window = self.builder.get_object("MainWindow")
        self.window.connect("destroy", Gtk.main_quit)
        
        self.builder.connect_signals(self)

        self.window.show_all()

    def on_ButtonTop_clicked(self, widget):
        print("Button 1 clicked")

    def on_ButtonLeft_clicked(self, widget):
        print("Button 2 clicked")
    
    def on_ButtonRight_clicked(self, widget):
        print("Button 3 clicked")

    def on_ButtonBottom_clicked(self, widget):
        print("Button 4 clicked")


if __name__ == "__main__":
    app = ConfigManager()
    Gtk.main()
