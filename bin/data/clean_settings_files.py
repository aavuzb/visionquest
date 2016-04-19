from xml.etree.ElementTree import ElementTree
import os

'''
Clean the settings file from parameters such as
<fullscreen__F_>1</fullscreen__F_>
This allows for configuration loaded to not change some of the display modes
We can use XPath to go to sub parameter such as 
Transition_time which is a child of settings_transition
'''
elementsToRemove =['fullscreen__F_','show_gui__G_',
'.//settings_transition/Transition_time',
'.//settings_transition/Settings_file']
def clean():
    currentDir = os.path.dirname(os.path.realpath(__file__))
    print(currentDir)

    for filename in os.listdir(currentDir+'\\'):
        if not filename.endswith('.xml'):
            continue
        print ('Cleaning {}'.format(filename))
        cleanFile(os.path.join(currentDir,filename))

def cleanFile(filename):
    tree = ElementTree()
    tree.parse(filename)
    parent_map = dict((c,p) for p in tree.getiterator() for c in p)
    
    root = tree.getroot()
    for element in elementsToRemove:
        elementNode = tree.find(element)
        if(elementNode is not None):
            parent_map[elementNode].remove(elementNode)
        tree.write(filename)

if __name__ == '__main__':
    clean()
    input("Done. Pressed any key to close.")