import sublime, sublime_plugin, sys, os
import urllib
from requests import get
from io import BytesIO
from zipfile import ZipFile
from glob import glob

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

class DownloadStuff(sublime_plugin.TextCommand):
  def run(self, edit):
    phpcs_url = 'https://github.com/benmatselby/sublime-phpcs/archive/master.zip'
    urllib.request.urlretrieve(phpcs_url, packages_path + '/Phpcs.zip')
    if os.path.isfile(packages_path + '/Phpcs1.zip'):
      zf = ZipFile(packages_path + '/Phpcs.zip')
      zf.extractall(packages_path)
      zf.close()
      os.remove(packages_path + '/Phpcs.zip')
