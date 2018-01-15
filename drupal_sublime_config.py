import sublime, sublime_plugin, sys, os
import urllib
from io import BytesIO
from zipfile import ZipFile
from glob import glob

enc = sys.getdefaultencoding()

# Get Sublime packages path dynamically
packages_path = sublime.packages_path()

class DrupalSublimeConfigCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # PHPcs linter path
    mat_url = 'https://github.com/equinusocio/material-theme/archive/master.zip'
    # Download files from internet resources
    urllib.request.urlretrieve(mat_url, packages_path + '/Material Theme.zip')
    # Check if file exists
    if os.path.isfile(packages_path + '/Material Theme.zip'):
      zf = ZipFile(packages_path + '/Material Theme.zip')
      zf.extractall(packages_path)
      zf.close()
      # Remove file after finishing operations
      os.remove(packages_path + '/Material Theme.zip')
      os.rename(packages_path + '/material-theme-master', packages_path + '/Material Theme')

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

class DownloadLinters(sublime_plugin.TextCommand):
  def run(self, edit):
    # PHPcs linter path
    phpcs_url = 'https://github.com/benmatselby/sublime-phpcs/archive/master.zip'
    self._downloadInternetResources(phpcs_url, 'sublime-phpcs-master', 'Phpcs')

  def _downloadInternetResources(self, path, folderName, replacement):
    # Download files from internet resources
    urllib.request.urlretrieve(path, packages_path + '/' + replacement + '.zip')

    # Check if file exists
    if os.path.isfile(packages_path + '/' + replacement + '.zip'):
      zf = ZipFile(packages_path + '/' + replacement + '.zip')
      zf.extractall(packages_path)
      zf.close()
      # Remove file after finishing operations
      os.remove(packages_path + '/' + replacement + '.zip')
      os.rename(packages_path + '/' + folderName, packages_path + '/' + replacement)
