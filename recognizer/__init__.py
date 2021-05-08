import click


@click.command()
@click.option("-i", "--image", 'image', required=True, type=click.Path(exists=True))
def recognize(image):
    print(image)
