fragment_a = open('templates/Top.html').read()
fragment_b = open('content/index.html').read()
fragment_c = open('templates/Bottom.html').read()

home = fragment_a + fragment_b + fragment_c

print(home)