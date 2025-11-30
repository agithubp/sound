def on_button_pressed_ab():
    basic.show_icon(IconNames.CONFUSED)
    music.set_volume(255)
    music.play(music.builtin_playable_sound_effect(soundExpression.soaring),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(2000)
    music.play(music.builtin_playable_sound_effect(soundExpression.hello),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)
