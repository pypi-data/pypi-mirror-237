import yaml
import webbrowser
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from galgen import UserError, CONFIG_NAME, THUMBNAILS_NAME
from logging import getLogger

logger = getLogger(__file__)

def build_action(path, force, show):
    path = Path(path)
    config_path = path / CONFIG_NAME

    if not config_path.exists():
        raise UserError(f"Config file doesn't exist: {config_path}. Have you run 'galgen init'?")

    index_path = Path(path) / 'index.html'
    environment = Environment(loader=FileSystemLoader(path))
    template = environment.get_template("index.html.j2")
    config = yaml.safe_load(config_path.read_text())

    def list_images(path):
        thumbnails_path = path / THUMBNAILS_NAME
        if not thumbnails_path.exists():
            thumbnails_path = path
            logger.warn(f"Directory '{THUMBNAILS_NAME}' doesn't exist in: {path}")
            
        def get_thumbnail_path(image_path):
            thumbnail_path = thumbnails_path / image_path.name
            if not thumbnail_path.exists():
                thumbnail_path = image_path
                logger.warn(f"There is no thumbnail for: {image_path}")
            return thumbnail_path

        images = [dict(image=f, thumb=get_thumbnail_path(f))
                  for f in sorted(path.iterdir()) if f.is_file()]

        if not images:
            raise UserError(f'At least one image expected in: {path}')

        return images

    galleries = [dict(title=gallery['title'], images=list_images(path / gallery['path']))
                for gallery in config['galleries']]

    params = dict(title=config['title'], galleries=galleries)
    
    if not force and index_path.exists():
        raise UserError('Gallery already built. Use -f to overwrite.')
    
    template.stream(**params).dump(str(index_path))
    logger.info(f'File generated: {index_path}')

    if show:
        webbrowser.open(f'file://{index_path.absolute()}')

