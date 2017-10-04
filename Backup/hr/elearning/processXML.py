import xml.dom.minidom


def main():
    doc = xml.dom.minidom.parse("samplexml.xml")
    print doc.nodeName
    print doc.firstChild.tagName
    skills = doc.getElementsByTagName("skill")
    print "%d skills:" % skills.length
    for skill in skills:
        print skill.getAttribute("name")

    newskill = doc.createElement("skill")
    newskill.setAttribute("name","HTML")
    doc.firstChild.appendChild(newskill)
    skills = doc.getElementsByTagName("skill")
    print "%d skills:" % skills.length
    for skill in skills:
        print skill.getAttribute("name")

if __name__ == "__main__":
    main()
