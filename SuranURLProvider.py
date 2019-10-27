#!/usr/bin/env python

import datetime
import re
from xml.dom.minidom import parse, parseString
import urllib2

from autopkglib import Processor, ProcessorError

__all__ = ["SuranURLProvider"]

FILE_INDEX_URL = 'http://download.cdmplus.com/cdm%s/catalog.txt'
#FILE_DOWNLOAD_URL = 'http://download.cdmplus.com/cdm%s/%s/cdm%s.pkg'
FILE_DOWNLOAD_URL = 'http://download.cdmplus.com/cdm%s/current/cdm%s.pkg'

class SuranURLProvider(Processor):
	'''Provides URL to the latest file.'''

	input_variables = {
		'CDM_MAJOR_VERSION': {
			'required': True,
			'description': 'Numerical ID of Major CDM version number (e.g. 92)',
			}
	}
	output_variables = {
		'url': {
			'description': 'URL to the latest download'
		},
		'cdm_version': {
			'description': 'Version number of the latest download'
		},
		'cdm_build': {
			'description': 'Build number of the latest download'
		}
	}

	description = __doc__

	def get_suran_file_url(self, major_version):
		#catalogurl = FILE_INDEX_URL % major_version

		#try:
		#	f = urllib2.urlopen(catalogurl)
		#	rss = f.read()
		#	f.close()
		#except BaseException as e:
		#	raise ProcessorError('Could not retrieve catalog %s' % catalogurl)

		#line = rss.split('\n', 1)[0]
		#version = line.split('\t')[0]
		#build = line.split('\t')[4]

		#line = rss.split('\n', 1)[0]
		version = 102
		build = 102

		#return FILE_DOWNLOAD_URL % (major_version, build, major_version), version, build
		return FILE_DOWNLOAD_URL % (major_version, major_version), version, build

	def main(self):
		major_version  = self.env.get('CDM_MAJOR_VERSION')

		url, version, build = self.get_suran_file_url(major_version)
		self.env['url'] = url
		self.env['cdm_version'] = version
		self.env['cdm_build'] = build
		self.output('File URL %s' % self.env['url'])

if __name__ == '__main__':
	processor = SuranURLProvider()
	processor.execute_shell()
