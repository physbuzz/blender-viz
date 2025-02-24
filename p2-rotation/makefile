

lowres:
	blender -b rotation.blend -E CYCLES -s 1 -e 359 -j 6 -P set_lowres.py -o "//out/lowres_" -a -- --cycles-device CUDA
	ffmpeg -y -framerate 20 -pattern_type glob -i "out/lowres_*.png" -vf "scale=256:256,split[s0][s1];[s0]palettegen=max_colors=256[p];[s1][p]paletteuse=dither=bayer:bayer_scale=3" output-small.gif

highres:
	blender -b rotation.blend -E CYCLES -s 1 -e 359 -o "//out/highres_" -a -- --cycles-device CUDA
	ffmpeg -y -framerate 60 -i "out/highres_%04d.png" -c:v libx264 -pix_fmt yuv420p -crf 18 output-highres.mp4
