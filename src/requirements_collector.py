#!/usr/bin/env python3
import collections
import gzip
import json
import re
import sys
import urllib.request
from io import BytesIO
from typing import Dict, List, Iterable, NamedTuple


def download_json_gz(url: str):
	with urllib.request.urlopen(url) as response:
		gzipped_data = response.read()
	with gzip.GzipFile(fileobj=BytesIO(gzipped_data), mode='r') as gzip_file:
		return json.load(gzip_file)


def sorted_string(collection: Iterable[str]) -> Iterable[str]:
	return sorted(collection, key=lambda r: (r.lower(), r))


class ReqData(NamedTuple):
	plugin_id: str
	requirement: str


def main():
	data = download_json_gz('https://raw.githubusercontent.com/MCDReforged/PluginCatalogue/meta/everything.json.gz')
	requirements: Dict[str, List[ReqData]] = collections.defaultdict(list)

	def add(pid: str, req_: str):
		# https://peps.python.org/pep-0426/#name
		matched = re.match(r'^([A-Z0-9][A-Z0-9._-]*[A-Z0-9]|[A-Z0-9])(.*)', req_, re.IGNORECASE)
		if matched is not None:
			package, rest = matched.group(1), matched.group(2)
			if package in ['mcdreforged', 'python']:
				return
			key = package.strip().lower().replace('-', '_')
			requirements[key].append(ReqData(pid, req_))
		else:
			print('Unknown requirement line {!r} for plugin {!r}'.format(req, plugin_id), file=sys.stderr)

	for plugin_id, plugin in data['plugins'].items():
		if (release_summary := plugin['release']) is not None and (idx := release_summary['latest_version_index']) is not None:
			release = release_summary['releases'][idx]
			for req in release['meta'].get('requirements', []):
				add(plugin_id, req)

	with open('requirements_extra_config.json', 'r', encoding='utf8') as f:
		extra_config: dict = json.load(f)
		for plugin_id, reqs in extra_config['additional'].items():
			for req in reqs:
				add(plugin_id, req)
		environment_markers: Dict[str, str] = extra_config['environment_markers']
		blacklist = set(extra_config['blacklist'])

	with open('requirements_extra.txt', 'w', encoding='utf8', newline='\n') as f:
		f.write('# The requirements_extra.txt is licensed under Creative Commons Zero (CC0)\n')
		f.write('# You are free to use, modify, and distribute it without any restrictions\n')
		f.write('\n')

		for req in sorted_string(requirements.keys()):
			if req in blacklist:
				continue

			items = []
			for rd in requirements[req]:
				if rd.requirement == req:
					items.append(rd.plugin_id)
				else:
					items.append('{} ({})'.format(rd.plugin_id, rd.requirement.replace(' ', '')))
			comment = ', '.join(sorted_string(items))

			req_line = req
			if (em := environment_markers.get(req)) is not None:
				req_line += '; ' + em

			f.write(f'# {comment}\n')
			f.write(f'{req_line}\n\n')


if __name__ == '__main__':
	main()
