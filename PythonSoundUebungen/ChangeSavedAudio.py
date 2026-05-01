from pydub import AudioSegment

#pydub does things in milliseconds
audio = AudioSegment.from_mp3("/Users/arturwacker/Studium/TextEditProgramme(VSC)/Python_Uebungen/test.mp3")

two_half_seconds = 2.5 * 1000

first_2_5_seconds = audio[:two_half_seconds]

last_2_5_seconds = audio[-two_half_seconds:]

beginning = first_2_5_seconds + 30
end = last_2_5_seconds - 5

complete = beginning + end

complete.export("newTest.mp3", format= "mp3")

'''
How long is it?

without_the_middle.duration_seconds == 15.0
AudioSegments are immutable

# song is not modified
backwards = song.reverse()
Crossfade (again, beginning and end are not modified)

# 1.5 second crossfade
with_style = beginning.append(end, crossfade=1500)
Repeat

# repeat the clip twice
do_it_over = with_style * 2
Fade (note that you can chain operations because everything returns an AudioSegment)

# 2 sec fade in, 3 sec fade out
awesome = do_it_over.fade_in(2000).fade_out(3000)
Save the results (again whatever ffmpeg supports)

awesome.export("mashup.mp3", format="mp3")
Save the results with tags (metadata)

awesome.export("mashup.mp3", format="mp3", tags={'artist': 'Various artists', 'album': 'Best of 2011', 'comments': 'This album is awesome!'})
You can pass an optional bitrate argument to export using any syntax ffmpeg supports.

awesome.export("mashup.mp3", format="mp3", bitrate="192k")
'''
