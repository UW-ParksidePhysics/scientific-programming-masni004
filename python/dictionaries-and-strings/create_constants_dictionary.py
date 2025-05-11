def parse_constants_file(filename):
    constants = {}
    with open(filename, 'r') as f:
        next(f)
        next(f)

        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            name = ' '.join(parts[:-2])
            value_str, dimension = parts[-2], parts[-1]

            try:
                value = float(value_str)
            except ValueError:
                continue

            constants[name] = {
                'value': value,
                'dimension': dimension
            }

    return constants


if __name__ == '__main__':
    constants = parse_constants_file('constants.txt')

    for name, info in constants.items():
        print(f"{name:25s} → {info['value']:>12.6g}   [{info['dimension']}]")

    g_const = constants['gravitational constant']['value']
    print(f"\nGravitational constant = {g_const:.6g} m^3/kg/s^2")