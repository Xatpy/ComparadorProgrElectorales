
if __name__ == "__main__":
    contador = 0
    for line in open('htmlCiudadanos.txt'):
        if 'class="header"' in line:
            contador += 1
            if contador == 1:
                continue
            firstIndex = line.find(">")
            lastIndex = line.rfind("<")
            print line[firstIndex + 1 : lastIndex]