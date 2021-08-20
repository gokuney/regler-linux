'''
This is the core application logic file
'''
from .Firebase import Firebase
from .Actions import Actions as actions


def app(window):
    db = Firebase().instance()
    Actions = actions()

    ref = db.reference("/controller")

    # Setup basic config
    baseControl = {
        "play": False,
        "pause": False,
        "volume": False,
        "next": False,
        "prev": False,
        "mute": False,
        "unmute": False
    }

    # Get button

    btn = window.get_child().get_children()[1]
    def clicked(instance):
        Actions.play()
        print("CLICKED!")
    btn.connect("clicked", clicked)


    ref.set(baseControl)

    # Monitor events

    ## Volume
    def volumeListener(event):
        Actions.volume(event.data)
    db.reference("/controller/volume").listen(volumeListener)

    ## mute
    def muteListener(event):
        Actions.mute(event.data)
    db.reference("/controller/mute").listen(muteListener)

    ## UnMute
    def unMuteListener(event):
        Actions.unmute(event.data)
    db.reference("/controller/unmute").listen(unMuteListener)

    ## Play
    def playListener(event):
        Actions.play(event.data)
    db.reference("/controller/play").listen(playListener)

    ## Pause
    def pauseListener(event):
        Actions.pause(event.data)
    db.reference("/controller/pause").listen(pauseListener)

    ## Next
    def nextListener(event):
        Actions.next(event.data)
    db.reference("/controller/next").listen(nextListener)

    ## prev
    def prevListener(event):
        Actions.prev(event.data)
    db.reference("/controller/prev").listen(prevListener)

