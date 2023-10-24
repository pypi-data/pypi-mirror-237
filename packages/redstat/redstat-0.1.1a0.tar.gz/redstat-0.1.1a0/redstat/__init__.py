from redstat.cli import parse_args


def main():
    namespace = parse_args()
    print(namespace)
    namespace.func(namespace)


if __name__ == '__main__':
    main()
