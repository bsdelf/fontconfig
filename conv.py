#!/usr/bin/env python3

import argparse
from xml.dom import minidom

def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="file", metavar="file", nargs=1)
    args = parser.parse_args()

    confname = args.file[0]
    xmldoc = minidom.parse(confname)
    match_elems = xmldoc.getElementsByTagName("match");

    for match in match_elems:
        parent = match.parentNode;
        test_elems = match.getElementsByTagName("test")
        edit_elems = match.getElementsByTagName("edit")

        # must have only one test and at least one edit
        if (test_elems == None or edit_elems == None or
            len(test_elems) != 1 or len(edit_elems) < 1):
                continue

        test = test_elems[0];
        nstr = len(test.getElementsByTagName("string"))

        # if test on multi-string
        if nstr < 2:
            continue
        
        # build new matches, each of them only has one test string
        sepmatches = [match.cloneNode(deep=True) for i in range(nstr)]
        idx = 0
        for sepmatch in sepmatches:
            septest = sepmatch.getElementsByTagName("test")[0];
            stridx = 0
            for sepstr in septest.getElementsByTagName("string"):
                if (stridx != idx):
                    septest.removeChild(sepstr)
                stridx += 1
            parent.insertBefore(sepmatch, match)
            idx += 1
        parent.removeChild(match)

    with open(confname+".out", "w") as outfile:
        xmldoc.toprettyxml()
        xmldoc.writexml(outfile)
    

if __name__ == "__main__":
    __main__()

