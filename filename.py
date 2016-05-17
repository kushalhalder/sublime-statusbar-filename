import sublime, sublime_plugin, os
  
class FileNameInStatusBar(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        filename = os.path.split(view.file_name())
        # get `show_full_path` settings
        settings = sublime.load_settings('Preferences.sublime-settings')
        
        if filename is None:
            view.erase_status('_filename')
        else:
            if settings.get('show_full_path') is True:
                view.set_status('_filename', "File Path: " + filename[0] + "/" + filename[1])
            else:
                view.set_status('_filename', "File: " + filename[1])