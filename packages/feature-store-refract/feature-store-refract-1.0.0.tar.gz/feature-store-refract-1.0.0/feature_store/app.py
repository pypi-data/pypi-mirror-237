import os


def main():
    frequency = os.getenv("frequency")

    print("Inside feature store recipe code", frequency)

    return "OK"


if __name__ == "__main__":
    main()
