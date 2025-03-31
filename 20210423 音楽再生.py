"""
utf-8    20210423
Pyaudioで音楽再生をする

※注意
コマンドプロンプトで
「python -m pip install python-vlc」
と入れてインストールをしてからじゃないとimprot vlcがエラーになる！
"""

import vlc
p = vlc.MediaPlayer()
p.set_mrl('0test.wav')
p.play()
input()
