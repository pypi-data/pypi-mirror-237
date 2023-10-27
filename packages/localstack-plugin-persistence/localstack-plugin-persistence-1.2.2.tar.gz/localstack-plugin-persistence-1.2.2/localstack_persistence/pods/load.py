_B='A state for %s already exists for account %s and region %s. The new state will overwrite the old one.'
_A='/'
import logging,os.path,zipfile
from collections import defaultdict
from functools import cached_property,singledispatchmethod
from typing import Any
from localstack.services.stores import AccountRegionBundle
from localstack.state import AssetDirectory,Decoder,StateVisitor,pickle
from moto.core import BackendDict
from localstack_persistence import constants
LOG=logging.getLogger(__name__)
class InjectPodVisitor(StateVisitor):
	zip:0
	def __init__(A,zip_file,decoder=None):A.zip=zip_file;A.pod=CloudPodArchive(A.zip);A.decoder=decoder or pickle.PickleDecoder()
	@singledispatchmethod
	def visit(self,state_container):LOG.warning('cannot save state container of type %s',type(state_container))
	@visit.register(AccountRegionBundle)
	def _(self,state_container):
		B=state_container;A=self;D=B.service_name
		if D not in A.pod.stores_index:return
		for(C,E,F)in A.pod.stores_index[D]:
			if B[C]and E in B[C].keys():LOG.warning(_B,D,C,E)
			with A.zip.open(F)as G:H=A.decoder.decode(G);B[C][E].__dict__.update(H.__dict__)
	@visit.register(BackendDict)
	def _(self,state_container):
		B=state_container;A=self;D=B.service_name
		if D not in A.pod.moto_backend_index:return
		for(C,E,F)in A.pod.moto_backend_index[D]:
			if B[C]and E in B[C].keys():LOG.warning(_B,D,C,E)
			with A.zip.open(F)as G:H=A.decoder.decode(G);B[C][E].__dict__.update(H.__dict__)
	@visit.register(AssetDirectory)
	def _(self,state_container):
		A=state_container;C=A.service_name+_A;D=[A for A in self.zip.infolist()if A.filename.startswith(os.path.join(constants.ASSETS_DIRECTORY,C))]
		for B in D:B.filename=B.filename.replace(f"{constants.ASSETS_DIRECTORY}{os.sep}{A.service_name}",'');self.zip.extract(B,A.path)
class CloudPodArchive:
	zip:0
	def __init__(A,zip_file):A.zip=zip_file
	@cached_property
	def services(self):'\n        Returns the list of services that have state in this cloud pod.\n        ';B=self;A=set();A.update(B.stores_index.keys());A.update(B.moto_backend_index.keys());A.update(B.asset_directories.keys());return A
	@cached_property
	def stores_index(self):
		'\n        Creates from the list of zip items an index that makes it easy to look up all account-region-store triples for a\n        given service.\n        ';D=self.zip.namelist();B=defaultdict(list)
		for C in D:
			A=C.lstrip(_A)
			if not A.startswith(constants.API_STATES_DIRECTORY):continue
			if not A.endswith(constants.LOCALSTACK_STORE_STATE_FILE):continue
			E,F,G=A.split(_A)[1:4];B[F].append((E,G,C))
		return B
	@cached_property
	def moto_backend_index(self):
		D=self.zip.namelist();B=defaultdict(list)
		for C in D:
			A=C.lstrip(_A)
			if not A.startswith(constants.API_STATES_DIRECTORY):continue
			if not A.endswith(constants.MOTO_BACKEND_STATE_FILE):continue
			E,F,G=A.split(_A)[1:4];B[F].append((E,G,C))
		return B
	@cached_property
	def asset_directories(self):
		'\n        Creates an index of service -> asset directory (path in the zip file)\n        ';D=self.zip.namelist();A={}
		for E in D:
			B=E.lstrip(_A)
			if B.startswith(constants.ASSETS_DIRECTORY):
				if(C:=B.split(_A)[1])in A:continue
				A[C]=os.path.join(constants.ASSETS_DIRECTORY,C)
		return A