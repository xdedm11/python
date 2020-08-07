from basis import*
if __name__ == '__main__':
    for tag in soup.find_all(True):
        print(tag.name)
    print(soup.find_all('p', 'course'))

    print(soup.find_all(id='link1'))
    print(soup.find_all(id='link'))
    print(soup.find_all(string='Basic Python'))