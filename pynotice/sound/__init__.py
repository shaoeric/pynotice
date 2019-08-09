from os.path import dirname, join, exists

sound_root = dirname(__file__)
resource_root = join(sound_root, "resource")

success_audio = join(resource_root, "success.wav")
error_audio = join(resource_root, "error.wav")
