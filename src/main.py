from textnode import TextNode, TextType

def main():
    textnode = TextNode('This is a text node', TextType.PLAIN_TEXT)
    print(textnode)

if __name__ == "__main__":
    main()