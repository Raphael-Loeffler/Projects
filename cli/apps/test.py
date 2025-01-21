print("test")

def contains_char(s, chars):
    return any(c in s for c in chars)

# Example usage

if __name__ == "__main__":
    s = "hello world"
    chars = "aeiou"
    print("start")
    print(contains_char(s, chars))
    print("end")