def oscillate(start, count):
    # Tạo ra dãy số dao động đối xứng
    for k in range(start, count):
        yield k
        yield -k

def main():
    for n in oscillate(-3, 5):
        print(n, end=' ')
    print()

if __name__ == "__main__":
    main()
