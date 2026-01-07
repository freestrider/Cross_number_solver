
across = input("input across numbers").split()
down = input("input down numbers").split()

links = []
loop = True

print("""format:
       across number shared_digit down_number shared digit
      type finish to finish""")
while loop:
    link_raw = input().split()
    if link_raw[0] == "finish":
        loop = False
        break
    link = (int(across.index(link_raw[0])),int(link_raw[1])-1,int(down.index(link_raw[2]))+len(across),int(link_raw[3])-1)
    links.append(link)

print(links)