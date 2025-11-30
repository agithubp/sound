input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showIcon(IconNames.Confused)
    music.setVolume(255)
    music.play(music.builtinPlayableSoundEffect(soundExpression.soaring), music.PlaybackMode.UntilDone)
    basic.pause(2000)
    music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.UntilDone)
    basic.clearScreen()
})
