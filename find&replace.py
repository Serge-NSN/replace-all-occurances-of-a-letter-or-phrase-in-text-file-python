import string


def replace_value(file, old, new):
    with open(file, 'rt') as original:
        data = original.read()
        data = data.replace(str(old), str(new))

    with open(file, 'wt') as final:
        final.write(data)

