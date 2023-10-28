import sys
sys.path.append('../slicenet')

from slicenet.entities.cloud import Cloud
from slicenet.entities.nf import Nf
from slicenet.mgrs.nfMgr import NfMgr
from slicenet.mgrs.sliceMgr import SliceMgr
from slicenet.entities.staticslice import StaticSlice
from slicenet.entities.service import Service
from slicenet.entities.slicelet import Slicelet

class SlicenetLoader:

    def loadYAML(fname: str) -> bool:
        pass

    def doDeployment() -> bool:
        pass

    def launchExperiment() -> bool:
        pass

    def returnSlicelets() -> list(Slicelet):
        pass