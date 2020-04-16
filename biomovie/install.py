
# Copyright (c) 2020 Greg Pintilie - gregdp@gmail.com
# LICENCE - please see: https://opensource.org/licenses/MIT


import sys, os, shutil

#li = sys.argv.index ( "install.py" )
#print li


if len(sys.argv) != 2 :
    print ""
    print "Please add the path where Chimera is installed, e.g.:"
    print "   python install.py /home/greg/applications/Chimera"
    print ""

    exit()


print ""

# path on Mac
opath1 = os.path.join ( sys.argv[1], "Contents" )
opath1 = os.path.join ( opath1, "Resources" )
opath1 = os.path.join ( opath1, "share" )

# path on unix
opath2 = os.path.join ( sys.argv[1], "share" )

didInstall = False

for opath in [opath1, opath2] :

    if os.path.isdir( opath ) :
        opath = os.path.join ( opath, "biomovie" )

        if os.path.isdir( opath ) :
            print " - removing previous BioMovie:", opath
            try :
                shutil.rmtree(opath)
            except :
                pass

        #print " - copying from:", os.getcwd()
        print " - copying . ->", opath

        try :
            shutil.copytree ( os.getcwd(), opath )
            didInstall = True
        except :
            print "Could not copy to:", opath
            print " 1. please check if you have write access"
            print " 2. try with sudo python install.py <path to Chimera>"
            print ""
            break

        didInstall = True

if didInstall :

    print ""
    print "Installation complete."
    print ""
    print "To use:"
    print " 1. Please restart Chimera."
    print " 2. Select Tools -> Utilities -> BioMovie"
    print ' 3. Please note that on Mac OS, you may see the message "Chimera is damaged and cannot be opened." Please see the following link for the solution: https://www.santoshsrinivas.com/disable-gatekeeper-in-macos-sierra/'
    print ' 4. More info: https://cryoem.slac.stanford.edu/ncmi/resources/software/BioMovie'
    print ""

    #wh = os.path.join ( os.getcwd(), "install.html" )
    #import webbrowser
    #webbrowser.open( 'file://' + wh, new=2)


else :
    print ""
    print 'Could not find install path from "' + sys.argv[1] + '"'
    print " - please check the path to Chimera"
    print ""
