from  chimera.extension import EMO, manager

# -----------------------------------------------------------------------------
#
class BioMovie_EMO ( EMO ):

  def name(self):
    return 'BioMovie'
  def description(self):
    return self.categoryDescriptions()['Utilities']
  def categories(self):
    return self.categoryDescriptions().keys()
  def categoryDescriptions(self):
    # since we want to use specialized descriptions for certain categories...
    return {
      'Utilities': 'Run movie script',
    }
  def icon(self):
    return None #self.path('volseg.png')
  def activate(self):
    # self.module('volumedialog').show_volume_dialog()
    d = self.module('biomovie').show_dialog()
    return None

# -----------------------------------------------------------------------------
# Register dialogs and menu entry.
#
manager.registerExtension ( BioMovie_EMO ( __file__ ) )
