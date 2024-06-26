import pygame
import pathlib

type NestedDict = dict[str, pygame.Surface | "NestedDict"]


def load_audio() -> dict[str : pygame.mixer.Sound]:
    path = pathlib.Path(r"assets\audio")
    audio = {}
    for audio_path in path.iterdir():
        audio[audio_path.stem] = pygame.mixer.Sound(file=audio_path)
    return audio


def load_sprites() -> NestedDict:
    path = pathlib.Path(r"assets\sprites")
    sprites = {}
    for path, directories, files in path.walk():
        container = sprites
        for part in path.parts[2:]:
            container.setdefault(part, {})
            container = container[part]

        # Updates sprites dictionary with all file in directory with file name as key and pygame.Surface
        container.update(
            {
                (path / file_name)
                .stem: pygame.image.load(path / file_name)
                .convert_alpha()
                for file_name in files
            }
        )

    return sprites
