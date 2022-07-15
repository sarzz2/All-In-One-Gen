import os
from pydub import AudioSegment


# parameter choice for length of song
def music_gen(choice):
    path = os.path.split(os.getcwd())[0]
    pathx = os.path.split(os.getcwd())[0]
    # path += "/static/temp/"
    path += "/timathon/AIG/static/temp/"
    count = 0
    # melody
    os.system(f"melody_rnn_generate \
    --config=attention_rnn \
     --bundle_file={pathx}/attention_rnn.mag \
    --output_dir={path} \
    num_output=10 \
    num_steps=512 \
    --primer_midi={pathx}/OmensOfLove.midi")

    # drums
    # os.system(f"drums_rnn_generate \
    # --config=drum_kit \
    #  --bundle_file=drum_kit_rnn.mag \
    # --output_dir={path} \
    # num_output=12 \
    # num_steps=256 \
    # --primer_drums='[(36,)]'")

    x = os.listdir(path)
    for i in x:
        count += 1
        os.system(f"timidity {path}{i} -Ow -o {path}out{count}.wav")
        try:
            os.remove(f"{path}{i}")
        except:
            pass

    if choice == 1:
        sound3 = AudioSegment.from_wav(f"{path}out6.wav")
        sound4 = AudioSegment.from_wav(f"{path}out7.wav")
        sound5 = AudioSegment.from_wav(f"{path}out8.wav")
        combined_sounds = sound3 + sound4 + sound5
        combined_sounds.export(f"{path}final.wav", format="wav")
    elif choice == 2:
        sound1 = AudioSegment.from_wav(f"{path}out4.wav")
        sound2 = AudioSegment.from_wav(f"{path}out5.wav")
        sound3 = AudioSegment.from_wav(f"{path}out6.wav")
        sound4 = AudioSegment.from_wav(f"{path}out7.wav")
        sound5 = AudioSegment.from_wav(f"{path}out8.wav")
        combined_sounds = sound1 + sound2 + sound3 + sound4 + sound5
        combined_sounds.export(f"{path}final.wav", format="wav")
    else:
        sound1 = AudioSegment.from_wav(f"{path}out4.wav")
        sound2 = AudioSegment.from_wav(f"{path}out5.wav")
        sound3 = AudioSegment.from_wav(f"{path}out6.wav")
        sound4 = AudioSegment.from_wav(f"{path}out7.wav")
        sound5 = AudioSegment.from_wav(f"{path}out8.wav")
        sound6 = AudioSegment.from_wav(f"{path}out9.wav")
        sound7 = AudioSegment.from_wav(f"{path}out10.wav")
        combined_sounds = sound2 + sound1 + sound3 + sound4 + sound5 + sound6 + sound7
        combined_sounds.export(f"{path}final.wav", format="wav")

    for i in range(2, len(x) + 1):
        os.remove(f"{path}out{i}.wav")


