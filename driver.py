import os
import glob
import delegator
import json
import click
from os.path import expanduser

@click.command()
@click.option(
    '--dirname',
    type=click.Path(
        exists=True,
        resolve_path=True))
@click.option(
    '--ext', default=".wav")

# manage my library of podcasts
def main(dirname,ext):
    print("main")
    model =  expanduser("~\\Documents\\GitHub\\DeepSpeech\\deepspeech-0.7.3-models.pbmm")
    scorer =  expanduser("~\\Documents\\GitHub\\DeepSpeech\\deepspeech-0.7.3-models.scorer")
    pattern = dirname + "/"+ "*" + ext
    print("pattern" + pattern)
    audiorate = "16000"
    
    print(pattern)
    for filename in glob.glob(pattern):
        print(filename)

        if ext != 'wav':
            wavefile = filename + ".wav"

            convert_command = " " . join([        
                "ffmpeg",
                "-i",
                "'{}'".format(filename),
                "-ar",
                audiorate,
                "'{}'".format(wavefile),
            ])
        else:
            wavefile = filename
            
        if not os.path.isfile(wavefile):
            print(convert_command)
            r = delegator.run(convert_command)
            print(r.out)
        else:
            print("ready:" + wavefile)
            
        command = " " . join([
            "C:\Python38\Scripts\deepspeech.exe",
            "--model",
            model,
            "--scorer",
            scorer,
            "--audio",
            "\"{}\"".format(wavefile),
            
#            "--extended",
            "--json",
#            "--candidate_transcripts 3",
        ])
        print(command)
        r = delegator.run(command)
        print(r)
        print(r.__dict__)
        print(dir(r))
        print(r.err)
        
        with open(filename + ".json", "w") as fo:
            print(r.out)
            fo.write(r.out)
        
        
# first loop over the files
# convert them to wave

# record things in 16000hz in the future
#Warning: original sample rate (44100) is different than 16000h.z Resampling might produce erratic speech recognition.

#PS C:\Users\jmike\Documents\GitHub\DeepSpeech>
#   deepspeech --model .\deepspeech-0.7.3-models.pbmm --audio C:\Users\jmike\Downloads\podcast\test.wav
#   deepspeech --model C:\Users\jmike\Documents\GitHub\DeepSpeech\deepspeech-0.7.3-models.pbmm --audio 'C:\Users\jmike\Documents\podcast\s3\433-0830\2021-08-30 07.51.12.wav' --extended --json --candidate_transcripts 3

# deepspeech --model ~/Documents/GitHub/DeepSpeech/deepspeech-0.7.3-models.pbmm --audio ./ --extended --json

# write the text to a file
# summarize the text

# create index of what words occur when? timestamp them.

if __name__ == '__main__':
    print("main")
    main()
