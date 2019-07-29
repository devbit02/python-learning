
def handler 

def prompt_user(may_skip=False, is_final=False):
    variants = [
        "[Y]YES when successful",
        "[N]NO to exit",
        "[S]SKIP to go next script",
        "[C]CONTINUE"
    ]
    prompt = ' or '.join(variants[2:] if may_skip else variants[:2])
    answer = input("\x1b[0;32mPlease type {}:\x1b[0m ".format(prompt)).lower()
    print(answer)

prompt_user()
name = input("What is your name? ")
print("Hello, {}".format(name))