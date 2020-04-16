# biomovie
Make movies in UCSF Chimera using python scripts.

To Install:

1. First, <a href="https://www.cgl.ucsf.edu/chimera/download.html">download</a> and install UCSF Chimera.
* Run it once before installing the plugin; on some platforms, e.g. MacOS, you may see a warning message on first run which you have to accept. This may prevent further issues after adding the plugin.
* On Windows, install to your home folder rather than to "Program Files". In the latter, the OS may not allow further modifications, i.e. adding this plugin.
2. <a href="https://github.com/gregdp/biomovie/tree/master/download">Download</a> latest version of the BioMovie plugin.
3. In a terminal, navigate to where the file was downloaded, then execute the following commands (replacing #_# with latest version number):
* unzip biomovie_#_#.zip 
* cd biomovie_#_#
* python install.py [path to Chimera]

e.g.:
* python install.py ~/Desktop/Chimera.app/


Note that on Windows, you may use the python bundled with Chimera itself, so the third command would be
* [path to Chimera]\bin\python install.py [path to Chimera]

To Run:
1. (Re)start Chimera*
2. Start BioMovie: Tools -> Utilities -> BioMovie
3. See [tutorial](https://github.com/gregdp/biomovie/tree/master/tutorials)
3. More details [here](https://cryoem.slac.stanford.edu/ncmi/resources/software/biomovie)

\* On Mac OS, an error message may be shown on first run after installing, see [here](https://www.santoshsrinivas.com/disable-gatekeeper-in-macos-sierra/) for solution.
