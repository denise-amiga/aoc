def my_read_input() -> str:
    txt: str = ''
    with open('input.txt', 'r') as f:
        txt = f.read()
    return txt
