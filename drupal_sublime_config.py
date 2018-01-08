import sublime, sublime_plugin, sys
enc = sys.getdefaultencoding()

# Get Sublime packages path dynamically
packages_path = sublime.packages_path()

class DrupalSublimeConfigCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # Copying drupal compatible config to Sublime user settings
    # Ref: https://www.drupal.org/docs/develop/development-tools/configuring-sublime-text
    with open((packages_path) + "/DrupalSublimeConfig/DrupalCompatible.sublime-settings", 'r') as f:
      with open((packages_path) + "/User/Preferences.sublime-settings", "w") as f1:
        for line in f:
          f1.write(line)

class FcSampleTestStepsTemplate(sublime_plugin.TextCommand):
  def run(self, edit):
    with open((packages_path) + "/DrupalSublimeConfig/SampleTestStepsTemplate.txt", 'r', encoding=enc) as f:
      content = f.read()
      self.view.insert(edit, 0, content)
