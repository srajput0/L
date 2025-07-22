from PIL import Image, ImageDraw

def generate_board_image(players):
    img = Image.new('RGB', (500, 100), color='white')
    draw = ImageDraw.Draw(img)
    for idx, player in enumerate(players):
        draw.text((10, 20 * idx), f"{player.name} at {player.position}", fill='black')
    path = '/tmp/ludo_board.png'
    img.save(path)
    return path
