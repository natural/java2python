from java2python.mod import basic


def setZopeInterface(iface):
    print '##### iface.bases:', iface.bases
    iface.bases[:] = ['zope.interface.Interface']
    print '#### set zope interface', iface.bases

interfacePostWalkHandlers = [
    setZopeInterface,
    ]


# override, not supplement:
interfaceHeadHandlers = [
#    basic.simpleDocString,
    ]


methodPrologueHandlers = [

    ]
