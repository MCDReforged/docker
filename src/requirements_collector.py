#!/usr/bin/env python3
import collections
import gzip
import json
import re
import sys
import urllib.request
from io import BytesIO
from typing import Dict, List, Iterable


def download_json_gz(url: str):
	with urllib.request.urlopen(url) as response:
		gzipped_data = response.read()
	with gzip.GzipFile(fileobj=BytesIO(gzipped_data), mode='r') as gzip_file:
		return json.load(gzip_file)


def sorted_string(collection: Iterable[str]) -> Iterable[str]:
	return sorted(collection, key=lambda r: (r.lower(), r))


def main():
	data = download_json_gz('https://raw.githubusercontent.com/MCDReforged/PluginCatalogue/meta/everything.json.gz')
	requirements: Dict[str, List[str]] = collections.defaultdict(list)

	def add(pid: str, req_: str):
		req_ = req_.strip().lower().replace('-', '_')
		if req_ != 'mcdreforged':
			requirements[req_].append(pid)

	for plugin_id, plugin in data['plugins'].items():
		for req in plugin['meta']['requirements']:
			matched = re.match(r'^([A-Z0-9][A-Z0-9._-]*[A-Z0-9]|[A-Z0-9])', req, re.IGNORECASE)
			if matched is not None:
				# https://peps.python.org/pep-0426/#name
				add(plugin_id, matched.group(1))
			else:
				print('Unknown requirement line {!r} for plugin {!r}'.format(req, plugin_id), file=sys.stderr)

	with open('requirements_additional.json', 'r', encoding='utf8') as f:
		for plugin_id, reqs in json.load(f).items():
			for req in reqs:
				add(plugin_id, req)

	with open('requirements_extra.txt', 'w', encoding='utf8') as f:
		for req in sorted_string(requirements.keys()):
			plugins = ', '.join(sorted_string(requirements[req]))
			f.write(f'# {plugins}\n')
			f.write(f'{req}\n\n')


if __name__ == '__main__':
	main()
