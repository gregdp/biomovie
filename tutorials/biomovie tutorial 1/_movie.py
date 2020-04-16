

# LICENCE - please see: https://opensource.org/licenses/MIT

# for development  - ignore these
#    import biomovie; import biomovie.biomovie; biomovie.biomovie.show_dialog()
#    reload(biomovie.biomovie); biomovie.biomovie.show_dialog()
#    execfile ("/Users/greg/Dropbox/_data/biomovie tutorial 1/_movie.py")


# biomovie 1 - A first movie using some simple actions :
# - showing/hiding models
# - varying transparency and threshold
# - rotating models

# Read/skim through the script, then see Instructions at the bottom to run it


from biomovie import biomovie as BM


# this is the BioMovie dialog which helps setup and run the movie
dlg = BM.get_dialog()


# this is the movie script
def bioMovieScript () :

    print "Starting movie script..."

    # First, get the models that will be used in the script
    # - these models should be already open in Chimera
    # - use GetMap(name) for maps (.mrc, .map, ...)
    # - use GetMolecule(name) for molecule objects (.pdb, ...)
    # - the name passed to the function should be the same as what is shown in
    #   the Model Panel

    wholeMap = dlg.GetMap("emd_21452_ex.mrc")
    mapForChain = {}
    for ci in ["A", "B", "C"] :
        mapForChain[ci] = dlg.GetMap("emd_21452_ex_%s.mrc" % ci)

    # list of all models for convenience
    all = [wholeMap] + mapForChain.values()

    print " - done getting models"


    # make the movie object in which we will put actions
    MOVIE = BM.Movie(dlg)

    # if movie 'preview' is slow, reduce this to speed through
    # for making the movie, use 30 as this will translate a time of
    # '1' to 1 second in the movie; i.e. 30 frames per second
    frameMul = 30


    # now the fun starts - add actions to the movie

    # the t and d are convenience variables that keep the current time in the
    # movie (t) and the amount of time that an action will take (d)
    t = 0; d = 0;

    # start by hiding all models and showing only the whole map
    # - these actions happen at the current time (t)
    MOVIE.add ( BM.Hide (t, all ) )
    MOVIE.add ( BM.Show (t, wholeMap ) )

    # because later in the movie we may set the transparency (alpha), set it
    # back to 1 here at the start
    MOVIE.add ( BM.SetAlpha (t, [wholeMap] + mapForChain.values(), 1 ) )

    # set threshold
    MOVIE.add ( BM.SetThr (t, wholeMap, 0.65 ) )

    # this sets the interpolation object back to the start state
    #MOVIE.add ( ModInterp (t, t, iMol, closedMol, closedMol ) )

    # going to the next action typically involves advancing current time (by
    # previous d); then the new d specifies how long the next action will take

    t += d; d = 6 * frameMul;
    rotAxis = [0,1,0] # rotation axis
    rotCeterPt = wholeMap.comPt # center of mass of wholeMap
    refModel = wholeMap # this model will be used as the reference
    MOVIE.add ( BM.Rotate (t, t+d, all, refModel, rotCeterPt, rotAxis, 360.0) )


    # make wholeMap dissapear and chain/protein maps appear
    # note when using transparency - since Chimera rendering does not do
    # surface ordering, it is best to set only one surface as transparent at
    # a time
    t += d; d = 1 * frameMul;
    MOVIE.add ( BM.VaryAlpha (t, t+d, wholeMap, 1.0, 0.0 ) )
    MOVIE.add ( BM.Hide (t+d, wholeMap ) )
    MOVIE.add ( BM.Show (t, mapForChain.values() ) )
    MOVIE.add ( BM.VaryThr (t, t+d, mapForChain.values(), 3.0, 0.65 ) )

    # pause for 1 second for dramatic effect, or as a place to add text in
    # post-processing, e.g. with iMovie
    t += d; d = 1 * frameMul;

    # rotate one more time
    t += d; d = 6 * frameMul;
    MOVIE.add ( BM.Rotate (t, t+d, all, wholeMap, wholeMap.comPt, [0,1,0], 360.0) )

    # once all actions have been added, roll the movie
    MOVIE.make()





if dlg == None :
    print " - did not find BioMovie dialog"
    print " - start it from Tools -> Utilities -> BioMovie"


else :
    print " - found BioMovie dialog"

    # set the name of the movie file
    dlg.movieName.set("CoV-2 movie 1")

    # set where frames for the movie will be saved
    dlg.framesPath = "/Users/greg/_data/biomovie tutorial 1/frames"

    # path to ffmpeg, to encode the movie
    #  - the one bundled with Chimera will be used by default if None is specified
    dlg.ffmpegPath = None

    # set the script function in the dialog
    dlg.scriptFun = bioMovieScript

    print " - movie script set; now press 'Go' in the BioMovie dialog"


# a list of Actions and their parameters
# Hide (time, model/s )
# - time: time
# - model/s: a single model (of type AnimatableModel) or a list of models

# Show (time, model/s )
# - time: time
# - model/s: a single model (of type AnimatableModel) or a list of models

# SetAlpha (time, model/s, alpha )
# - time: time
# - model/s: a single model (of type AnimatableModel) or a list of models
# - alpha: the transparency, a number between 0 and 1

# VaryAlpha (startTime, endTime, model/s, startAlpha, endAlpha )
# - startTime: startTime
# - endTime: endTime
# - model/s: a single model (of type AnimatableModel) or a list of models
# - startAlpha: start transparency value
# - endAlpha: end transparency value

# SetThr (time, model/s, threshold )
# - time: time
# - model/s: a single model (of type AnimatableModel) or a list of models
# - threshold: the density value at which to draw the isocontour
#   see Volume Viewer for a range of values for any given map
#   be careful with this value, just as when setting the threshold in Chimera
#   using the histogram; too low of a value will show a box around the entire
#   map and can take a long time to refresh the window

# VaryThr (startTime, endTime, model/s, startThr, endThr )
# - startTime: startTime
# - endTime: endTime
# - model/s: a single model (of type AnimatableModel) or a list of models
# - startThr: start threshold value
# - endThr: end threshold value

# Rotate (startTime, endTime, models, refModel, rotCeterPt, rotAxis, totDegrees)
# - startTime: startTime
# - endTime: endTime
# - models: a list of models (of type AnimatableModel)
# - refModel: a reference model - which model to use as a reference; its
#             transform at the start time will be applied to the rotation
#             center point
# - rotCeterPt: rotation center point; usually the center of a map/model
# - rotAxis: rotation axis
# - totDegrees: how many degrees to rotate by


# Instructions:
# 1. open all models in the tutorial folder and set colors as desired
# 2. open the BioMovie dialog from Tools -> Utilities -> BioMovie
# 3. open IDLE from Tools -> General Controls -> IDLE
# 4. in IDLE, run 'execfile ("[path to this script]")'. You should see:
#    - found BioMovie dialog
#    - movie script set; now press 'Go' in the BioMovie dialog
# 5. press the Go buton in the BioMovie dialog
#     - check 'Save' first if ready to make the the movie
#     - make sure to set the framesPath above
#     - check 'Stop' at any point to stop if needed
#     - once all frames are recorded, if 'Save' is checked, ffmpeg will then be
#       used to create the movie file in framesPath/../[movie name].mov;
#       this file will be pretty big, but it retains very good quality; to
#       reduce the file size, a program like HandBrake can then be used


# other notes:
# - the movie frames will have the same dimension as the main Chimera window
# - to set the size of the window to a standard format before making the movie:
# - open the command linefrom Tools -> General Controls -> Command Line
# - in the command line (not in IDLE), run, e.g: 'windowsize 1920 1080'
