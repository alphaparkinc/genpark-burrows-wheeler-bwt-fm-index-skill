from client import BurrowsWheelerTransform

def main():
    print("=== Burrows-Wheeler Transform & Inverse ===")
    bwt = BurrowsWheelerTransform()
    text = "banana"

    res = bwt.transform(text)
    print("BWT String:", res["bwt_string"])
    assert res["bwt_string"] == "annb$aa"

    recovered = bwt.inverse_transform(res["bwt_string"])
    print("Recovered Text:", recovered)
    assert recovered == text

    print("Burrows-Wheeler Transform verified successfully!")

if __name__ == "__main__":
    main()
