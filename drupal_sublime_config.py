import sublime, sublime_plugin, os, inspect

# Get Sublime packages path dynamically
parent_path = os.path.abspath(os.path.dirname(__file__))

class DrupalSublimeConfigCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # Copying drupal compatible config to Sublime user settings
    # Ref: https://www.drupal.org/docs/develop/development-tools/configuring-sublime-text
    with open(os.path.dirname(os.path.abspath(inspect.stack()[0][1])) + "/DrupalCompatible.sublime-settings", 'r') as f:
      with open(os.path.dirname(parent_path) + "/User/Preferences.sublime-settings", "w") as f1:
        for line in f:
          f1.write(line)
