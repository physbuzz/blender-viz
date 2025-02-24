


all:
	blender -b planets.blend -S MelonScene -a -- --cycles-device CUDA
	blender -b planets.blend -S PlanetsOnly -a -- --cycles-device CUDA
	blender -b planets.blend -E CYCLES -S PlanetsVideo -a -- --cycles-device CUDA
