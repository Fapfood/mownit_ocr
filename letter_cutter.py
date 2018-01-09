from pathlib import Path

from scipy import ndimage, misc

from letter_divider import divide

LABELS = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K',
          'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
          'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.',
          ',', '!', '?', 'Ą', 'ą', 'Ć', 'ć', 'Ę', 'ę', 'Ł', 'ł', 'Ń', 'ń', 'Ó', 'ó', 'Ś', 'ś', 'Ź', 'ź', 'Ż', 'ż']


def cut(name):
    img = ndimage.imread('resources/{}_pl.png'.format(name), flatten=True)

    Path('resources/{}'.format(name)).mkdir(parents=True, exist_ok=True)

    lines = divide(img)

    counter = 0
    for line in lines:
        for letter in line:
            file_name = 'resources/{}/[{}].png'.format(name, LABELS[counter])
            misc.imsave(file_name, letter)
            counter += 1

# cut('arial')
# cut('roman')
